# architectural-research v2.0

Claude Code skill for architectural pre-design research. Takes a design brief, outputs a structured HTML research book — tracing the full design derivation chain from understanding to strategy.

> **Minimal, Editorial, Architectural.**

## Quick Start

1. Install the skill in Claude Code
2. Provide a design brief (`.docx` / `.pdf`): `"E:\建筑\毕设\20251121海上度假酒店设计任务书.docx"`
3. The skill auto-generates a single-file HTML research book

## What It Does

```
Design Brief (.docx/.pdf)
        ↓
  Research Analysis Agent
        ↓
  Structured HTML Research Book
        ↓
  5–8 Design Strategies
```

Not a data dump — a **design derivation engine**. Every section answers a question that pushes the design forward.

## Report Structure (9 Modules)

| # | Module | Content |
|---|--------|---------|
| 01 | Project Overview | Key metrics, hard constraints, info status (known / inferred / missing) |
| 02 | Context Analysis | Regional context, building type background, project rationale |
| 03 | Site & Environment | Climate KPIs → design strategy mapping, natural disaster risk assessment |
| 04 | User & Culture | Persona cards, vernacular culture → spatial translation chains |
| 05 | Design Challenges | 5 core contradictions with problem tags (jump to M06 opportunities) |
| 06 | Design Opportunities | Challenge → Opportunity → Direction chains with anchor IDs |
| 07 | Strategy Exploration | 6 strategies × 8 elements (Question → Evidence → Concept → Spatial Operation → Cases) |
| 08 | Reference Cases | 6 verified precedent cases with clickable URLs |
| 09 | Conclusion | Key findings, risk assessment, next-step action plan |

## Design System

**Black & white editorial** — pure black-on-white, no accent colors, no gradients.

```
:root {
  --color-text: #111;
  --color-bg: #fff;
  --color-border: #e5e5e5;
  --color-card: #f9f9f9;
}
```

- Fixed left sidebar TOC (180px) with IntersectionObserver active tracking
- Rounded corners (`6px` / `10px` / `16px`)
- CJK typography: `line-height: 1.8`, no `letter-spacing`, no `ch` units
- Dashed dividers, card-based component library
- Responsive: sidebar collapses to hamburger at ≤860px
- A4 print stylesheet with page breaks before each module
- No Mermaid / AI reasoning diagrams displayed — architectural results only

## Key Features

- **Single-file HTML** — opens in any browser, no server needed
- **Ctrl+P to PDF** — A4-optimized print stylesheet
- **Challenge → Opportunity jump links** — click tags to navigate between modules
- **Verified case URLs** — ArchDaily / Dezeen / Architizer / 谷德 / ArchiPosition only
- **Replaceable images** — `<img>` tags with SVG placeholders, edit `src` to replace
- **Keyboard navigation** — ↑↓ Home End
- **Bilingual search** — Chinese + English sources for every module

## File Structure

```
architectural-research/
├── SKILL.md                            # Main skill definition & rendering rules
├── assets/
│   └── research-book-template.html     # HTML skeleton with full component library
├── references/
│   ├── html-output-guide.md            # Visual & technical spec
│   ├── report_template.md              # .docx formatting spec (legacy)
│   └── climate_data.md                 # Built-in climate reference DB
└── evals/
    └── evals.json                      # Skill evaluation cases
```

## Example Output

Test case: **仙本那海上度假酒店** (Semporna Maritime Resort Hotel, Malaysia)
- 100 modular guest rooms, ≤3 floors
- Near-zero energy target (GB/T 51350-2019)
- Bajau vernacular culture reference
- Built on reef, not connected to land

## Requirements

- Claude Code with skill support
- Python: `python-docx` (for .docx brief extraction), `markitdown` (for .pdf)
- Internet access for web search (case studies, climate data)

## Credits

Built on architectural research methodology: 项目理解 → 场地研究 → 人群文化 → 功能推演 → 问题提炼 → 设计机会 → 策略探索 → 案例对标 → 结论.

Design system inspired by Swiss editorial traditions, adapted for architectural research book format.
