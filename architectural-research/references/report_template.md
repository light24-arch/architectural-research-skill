# Report Template Reference

用户选择 DOCX 主文档时加载。先生成、检验并交付 DOCX，再按 SKILL.md 询问 HTML 演示需求。

规则来源：任务范围遵循 [SKILL.md](../SKILL.md)；章节、数量和策略结构遵循 [report-structure.md](report-structure.md)；证据遵循 [evidence-quality.md](evidence-quality.md)。排版不改变研究范围。
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
Heading 1: # 01–09 + report-structure.md 的章节名（仅新完整报告）；其他模式沿用任务结构
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
- SVGs: convert to PNG before embedding with python-docx
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

使用 evidence-quality.md 的事实、推断、待核实状态。正文/表格内用来源编号与必要状态文字；
表下注以 8.5pt 补充方法、假设与限制。混合状态逐行/字段标注，不能用章节末的一条通用免责声明替代。
规范数值注明文件版本、条款、地区与适用对象；来源未核验时不能称法定约束。
气候库无元数据仅作线索；代理城市标推断；气候区仅作定性推断。

## Technical Notes for python-docx

When generating .docx via python-docx:
- Set the default document font to 微软雅黑 (10.5pt, 1.5× line spacing) via the Normal style.
- For CJK fallback, set the `w:eastAsia` font attribute on the Normal style's run properties.
- Tables: use `Light Grid Accent 1` style; manually bold the header row text; fill data rows
  with `cell.text = str(val)`. Dark blue header background (#1a478a) with white text.
- Images: embed with `doc.add_picture(path, width=Cm(15))`. Always wrap in try/except.
- Page breaks: insert before each Heading 1 (major section).
