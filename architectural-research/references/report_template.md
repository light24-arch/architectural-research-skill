# Report Template Reference

Use this reference when generating the final .docx report via python-docx. The goal is a professional, consistent document suitable for architectural practice.

## Page Setup

```
Page size: A4 (21.0 cm × 29.7 cm)
Margins: 2.54 cm all sides (Word default)
Orientation: portrait (landscape only for extra-wide tables or diagrams)
```

## Typography

| Element | Font | Size | Bold | Color |
|---------|------|------|------|-------|
| Report title (cover) | 微软雅黑 / Calibri | 22 pt | Bold | #1a478a (dark blue) |
| Subtitle (cover) | 微软雅黑 / Calibri | 16 pt | Normal | #336699 |
| Heading 1 | 微软雅黑 / Calibri | 16 pt | Bold | #1a478a |
| Heading 2 | 微软雅黑 / Calibri | 13 pt | Bold | #2c5f8a |
| Heading 3 | 微软雅黑 / Calibri | 11 pt | Bold | #333333 |
| Body text | 微软雅黑 / Calibri | 10.5 pt | Normal | #333333 |
| Table header | 微软雅黑 / Calibri | 10 pt | Bold | #ffffff (on #1a478a bg) |
| Table cell | 微软雅黑 / Calibri | 10 pt | Normal | #333333 |
| Caption | 微软雅黑 / Calibri | 9 pt | Normal | #666666 |
| Footer / page number | 微软雅黑 / Calibri | 9 pt | Normal | #999999 |

## Heading Hierarchy

```
Heading 1: # 0. / 1. / 2. ...  followed by Chinese title
Heading 2: ## 1.1 / 2.3 ...  subsection
Heading 3: ### unnumbered, for detail topics within subsections
```

Spacing before Heading 1: 24 pt; before Heading 2: 18 pt; before Heading 3: 12 pt.
Spacing after all headings: 6 pt.

## Body Text

```
Line spacing: 1.5 lines
First line indent: none (use paragraph spacing instead)
Paragraph spacing after: 6 pt
Alignment: justified (两端对齐) for body; left for lists
```

## Tables

Use python-docx `Light Grid Accent 1` style as the base, then customize:

```python
# Header row
header_bg = RGBColor(0x1a, 0x47, 0x8a)  # dark blue background
header_font_color = RGBColor(0xff, 0xff, 0xff)  # white text
header_font_size = Pt(10)
header_font_bold = True

# Data rows
cell_font_size = Pt(10)
cell_font_color = RGBColor(0x33, 0x33, 0x33)
# Alternate row shading: white / #f0f4f8 (very light blue)

# Borders
table_border_color = RGBColor(0x99, 0x99, 0x99)
table_border_width = Pt(0.5)
```

- Table alignment: centered on page
- Column widths: auto-fit to content; set explicit widths for columns with similar data
- All numeric data: right-aligned; text: left-aligned
- Caption below table, format: `表 X: <description>` in 9pt, #666666

## Images & Diagrams

- Embed inline after the paragraph that first references them
- Caption below image, format: `图 X: <description>` in 9pt, #666666
- Maximum width: 15 cm (to fit within margins)
- SVGs: embed directly (python-docx supports EMF/WMF; convert SVG to PNG for embedding)
- Mermaid diagrams: render to PNG/SVG via mermaid-cli or an online service, then embed
- Resolution: 150 dpi minimum for raster images

## Page Breaks

Insert page breaks before:
- Each major section (Heading 1)
- The title page
- The table of contents (if generated)

Do NOT insert page breaks before subsections (Heading 2/3).

## Numbered & Bulleted Lists

```
Numbered items (1. / 2. / 3. ...) for sequential steps, strategies, or conclusions.
Bulleted items (- ) for non-ordered lists like features, observations, or components.
Indent: 0.63 cm (Word default)
```

## Data Reliability Conventions

Use **professional footnotes** at the bottom of each table or end of each section, rather than
inline warning symbols. The reader should see the data first, reliability context second.

| Situation | Footnote Format |
|-----------|-----------------|
| Inferred/assumed data | `注：以上数据基于同类型项目经验推断，需结合项目实际情况确认。` |
| Missing data | `注：[具体条目] 待任务书补充后更新。` |
| Standards-derived values | `注：上表数值依据 [规范名称] 通用要求计算，实际以规划条件为准。` |
| Qualitative judgment | `注：本段分析基于通用建筑设计知识，建议结合实地调研深化。` |
| Climate from built-in DB (nearby city) | `注：气候数据基于 [参考城市] 多年平均值推演，需结合实测微调。` |
| Climate from zone inference | `注：自然环境数据基于同气候区均值推演，需结合实测微调。` |
| Traffic from city-type inference | `注：交通分析基于城市类型推断，建议结合实地调研核实。` |

**Guidelines:**
- Place footnotes in 8.5pt, #888888, at the end of the relevant section or directly below the table.
- Use `注：` prefix consistently — it's professional and unambiguous in Chinese architectural documents.
- Never interrupt the flow of the report with inline warning symbols.
- If a section has multiple data reliability levels, use a single consolidated footnote covering all of them.

## Technical Notes for python-docx

When generating .docx via python-docx:
- Set the default document font to 微软雅黑 (10.5pt, 1.5× line spacing) via the Normal style.
- For CJK fallback, set the `w:eastAsia` font attribute on the Normal style's run properties.
- Tables: use `Light Grid Accent 1` style; manually bold the header row text; fill data rows
  with `cell.text = str(val)`. Dark blue header background (#1a478a) with white text.
- Images: embed with `doc.add_picture(path, width=Cm(15))`. Always wrap in try/except.
- Page breaks: insert before each Heading 1 (major section).