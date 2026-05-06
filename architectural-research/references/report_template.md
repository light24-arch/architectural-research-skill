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

## Data Flag Conventions

| Symbol | Meaning |
|--------|---------|
| `⚠` | Inferred/assumed data — not from original brief |
| `待补充` | Missing data — requires user to provide |
| `基于规范推断` | Value derived from general standards, not project-specific |
| `基于通用设计知识推断` | Qualitative judgment, not hard data |

Use these flags consistently so the user immediately knows the reliability of each data point.

## Technical Notes for python-docx

```python
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

# Set default font for the entire document
style = doc.styles['Normal']
style.font.name = '微软雅黑'
style.font.size = Pt(10.5)
style.paragraph_format.line_spacing = 1.5

# For CJK font fallback
rPr = style.element.get_or_add_rPr()
rFonts = OxmlElement('w:rFonts')
rFonts.set(qn('w:eastAsia'), '微软雅黑')
rPr.append(rFonts)

# Add a table with custom header formatting
def add_styled_table(doc, headers, rows):
    table = doc.add_table(rows=1+len(rows), cols=len(headers))
    table.style = 'Light Grid Accent 1'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Style header row
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            for run in p.runs:
                run.bold = True
    # Fill data
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            table.rows[r+1].cells[c].text = str(val)
    return table
```