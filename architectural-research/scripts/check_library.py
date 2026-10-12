"""Read-only checks for a flat Markdown precedent library; standard library only."""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

DEFAULT_EXCLUDES = {
    '00_案例库索引.md', '01_案例比较矩阵.md',
    '02_苏州课程设计转译.md', '03_研究口径与来源目录.md',
}

def fields(text):
    if not text.startswith('---\n'):
        return {}
    end = text.find('\n---', 4)
    if end < 0:
        return {}
    result = {}
    for line in text[4:end].splitlines():
        if ':' in line and not line.startswith((' ', '#')):
            key, value = line.split(':', 1)
            result[key.strip()] = value.strip().strip('\"\x27')
    return result

def without_fences(text):
    return re.sub(r'(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[^\n]*$', '', text)

def check(library, project, excludes):
    library, project = library.resolve(), project.resolve()
    if not library.is_dir() or not project.is_dir():
        raise ValueError('Library and project-root must be existing directories.')
    library_files = sorted(library.glob('*.md'))
    files = sorted(set(library_files + list(project.glob('*.md'))))
    documents = {p: p.read_text(encoding='utf-8-sig') for p in files}
    cases, candidates, errors, warnings = [], [], [], []
    used = {}
    for p in library_files:
        meta = fields(documents[p])
        if p.name in excludes:
            continue
        if meta.get('正式入库', '').lower() == 'false' or meta.get('status') in {'候选', '待用户选择', '待选'}:
            candidates.append(p.name)
            continue
        cases.append(p.name)
        case_id = meta.get('案例编号')
        if case_id:
            if case_id in used:
                errors.append({'kind': 'duplicate_id', 'id': case_id, 'files': [used[case_id], p.name]})
            else:
                used[case_id] = p.name
        else:
            warnings.append({'kind': 'id_not_declared', 'file': p.name})
    for p, text in documents.items():
        meta = fields(text)
        declared = meta.get('案例总数')
        if p.parent == library and declared is not None:
            try:
                count = int(declared)
            except ValueError:
                errors.append({'kind': 'invalid_count', 'file': p.name, 'declared': declared})
            else:
                if count != len(cases):
                    errors.append({'kind': 'count_mismatch', 'file': p.name, 'declared': count, 'actual': len(cases)})
        body = without_fences(text)
        for match in re.finditer(r'\]\((<[^>]+>|[^)\n]+)\)', body):
            target = match.group(1)
            if target.startswith('<'):
                target = target[1:-1]
            else:
                target = re.split(r'\s+[\"\x27]', target, maxsplit=1)[0]
            target = unquote(target.split('#', 1)[0])
            if not target or re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I):
                continue
            if not (p.parent / target).exists():
                errors.append({'kind': 'missing_link', 'file': p.name, 'target': target})
        for match in re.finditer(r'\[\[([^\]]+)\]\]', body):
            target = match.group(1).split('|', 1)[0].split('#', 1)[0]
            if not target:
                continue
            if not any(q.stem == target or q.relative_to(project).with_suffix('').as_posix() == target
                       for q in files if q.is_relative_to(project)):
                warnings.append({'kind': 'wiki_unresolved_in_scanned_scope', 'file': p.name, 'target': target})
    return {'case_count': len(cases), 'case_files': cases, 'candidate_files': candidates,
            'errors': errors, 'warnings': warnings, 'passed': not errors,
            'scope': 'Top-level library/project Markdown, basic inline local links and declared count/IDs; no source or drawing validation.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--library', required=True, type=Path)
    parser.add_argument('--project-root', type=Path)
    parser.add_argument('--exclude', action='append', default=[], help='Additional navigation/non-case filename, repeatable.')
    args = parser.parse_args()
    try:
        result = check(args.library, args.project_root or args.library.parent,
                       DEFAULT_EXCLUDES | set(args.exclude))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
