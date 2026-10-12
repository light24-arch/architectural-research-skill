# HTML 交付规范（唯一当前版本）

按 SKILL.md 先完成用户选择的主文档；交付后用户需要 HTML 演示时再加载本指南。
HTML 演示复用主文档结论与证据；不作为默认主文档，不因选择演示重新展开调研。

任务范围由 [SKILL.md](../SKILL.md) 决定；章节、数量和策略八要素由 [report-structure.md](report-structure.md) 决定；证据由 [evidence-quality.md](evidence-quality.md) 决定。此文件只负责渲染。


This section is the **complete rendering rulebook** for generating the HTML research book.
Read it before writing any HTML output. The canonical reference implementation is at
`assets/research-book-template.html` (neutral nine-module skeleton; not a completed research report).

#### 1. Design System (Black & White Editorial)

```css
:root{
  --color-text: #111;
  --color-bg: #fff;
  --color-border: #e5e5e5;
  --color-card: #f9f9f9;
  --color-text-secondary: #555;
  --color-text-helper: #888;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
}
```

Principles:
- **No accent color blocks, no gradients, no decorative graphics.** Pure black-on-white.
- **No `margin-left: -xxx` or `position: absolute` as primary layout.** Use Flexbox / CSS Grid.
- Table header row: black background (#111) + white text (NOT blue).
- Cards: light grey `#f9f9f9` background, `border-radius: var(--radius-md)`, no colored borders.
- Strategy Cards: left border `2px solid var(--color-text)` (black, not colored).
- Dashed dividers (`border-top: 1px dashed var(--color-border)`) for visual lightness.

#### 2. Typography

- Body: `font-size: 15px; line-height: 1.8;` (relaxed reading rhythm)
- **No `letter-spacing` on Chinese text.** CJK characters have built-in spacing.
- **No `ch` units.** Use fixed max-width (e.g., `max-width: 700px`) for content columns.
- H1: `font-weight: 300; font-size: clamp(24px, 3.5vw, 40px);`
- H2: `font-weight: 400; font-size: clamp(18px, 2vw, 24px);`
- KPI number: `font-weight: 300; font-size: clamp(36px, 5vw, 64px);`
- Meta labels: `font-family: JetBrains Mono; font-size: 11px; color: var(--color-text-helper);`
- Font stack: `"Inter", "Noto Sans SC", system-ui, sans-serif`
- **Overflow defense** on body: `overflow-x: hidden` + all titles get `overflow-wrap: break-word; max-width: 100%;`

#### 3. Layout & Sidebar

- Body: `max-width: 1000px; margin: 0 auto; padding: 0;`
- **Fixed left sidebar TOC**: `<nav id="toc-sidebar">` with `position: fixed; width: 180px;` positioned at `left: max(0px, calc((100vw - 1000px) / 2))` to align with body edge. Contains cover + 01–09 module links.
- **Content area**: `<main id="content">` with `margin-left: 180px; max-width: 700px; padding: var(--sp-8) var(--sp-7);`
- TOC active state tracked via `IntersectionObserver` (rootMargin: `-15% 0px -75% 0px`).
- Responsive (≤860px): sidebar collapses to hamburger toggle (`#btn-toc-toggle`), content margin-left → 0.
- Print: sidebar hidden (`display: none`), content margin-left → 0, page breaks before each module.

#### 4. Cover

- White background, black text, centered layout.
- Min-height: 70vh, flexbox vertical centering.
- Structure: Meta label (mono font, 11px, "ARCHITECTURAL RESEARCH BOOK") → Project title (H1, weight 300) → Subtitle (lead, max-width ~440px) → Date line (mono, 11px, "YYYY.MM.DD · Author · HTML Research Book").
- Bottom border: `1px solid var(--color-border)` separating cover from content.
- **No colored background. No decorative elements.**

#### 5. Component Library & Module Mapping

Do not display private AI reasoning or internal analysis logs. Architectural circulation, site and design diagrams are research results and may be included with evidence captions.

| Component | CSS Class | Use When | Example Module |
|-----------|-----------|----------|----------------|
| KPI Row | `.rb-kpi-row` (flex, gap, card bg) | 3–4 key metrics in a horizontal row | M01 (rooms/FAR/module size), M03 (temp/humidity/sunlight/rain) |
| Card Grid | `.rb-card-grid` (3-col grid) | Comparing equal-weight items side by side | M01 (info status ×3), M03 (climate→strategy ×3), M04 (persona ×4), M09 (next steps ×3) |
| Card (accent top) | `.rb-card-accent` (card + border-top) | Cards with a black top-border accent | M03 (climate design strategies) |
| Table | `.rb-table` | Structured comparison data, >3 rows | M01 (constraints), M03 (disaster risks), M04 (lifestyle→space), M08 (case matrix), M09 (risks) |
| Chain | `.rb-chain` (flex row + `.rb-chain-arrow`) | Sequential "A → B → C" reasoning | M04 (culture→space translation), M06 (challenge→opportunity chains) |
| Strategy Card | `.rb-strategy-card` (left border + card bg) | Each design strategy | M07 (按实际数量生成策略卡，内容遵循 report-structure.md 的八要素) |
| Challenge Card | `.rb-strategy-card` with `background: var(--color-bg); border-left-width: 1px` | Each design challenge | M05 (实际挑战数量，附问题标签) |
| Image Grid | `.rb-img-grid` (3-col grid) | Case photos, site photos | M08 (3 case images) |
| Divider | `.rb-divider` (dashed border-top) | Visual separation without new heading | Between M06 opportunity chains |

**Images**: Use actual attributed research images when available. Otherwise use `<img class="rb-img" src="...">` with explicitly labeled inline SVG placeholders (grey rect + 占位图 text).
Replace placeholders with researched assets before delivery where possible; unresolved placeholders remain labeled. Do NOT use `<div>` as image placeholder.

**Problem Tags**: In M05, each challenge card has pill-shaped `<span>` tags (`border-radius: 99px; border: 1px solid var(--color-border); font-size: 11px`) for visual categorization: 场地问题 / 气候问题 / 文化问题 / 能源问题 / 技术问题 / 空间问题.

#### 6. Sources and evidence

Follow `evidence-quality.md`: a searchable URL is not proof of the linked claim.
Use readable source IDs near claims and captions; provide title, URL, locator,
verification status and access date in the source list. Render discovered source links
even when access is limited, but label them 待核实 and exclude them as decisive evidence.
Only call sources 已核验 when their content was read and supports the associated claim.
Placeholders must be labeled 占位图（未获取真实图片）; do not assign them real photo credits.

#### 7. Challenge → Opportunity Jump Links

- Each challenge card in M05 ends with: `<a href="#opp-NN" class="rb-challenge-link">→ 查看对应的设计机会</a>`
- Each opportunity chain in M06 has a unique ID: `id="opp-01"` through the actual opportunity count
- CSS for `.rb-challenge-link`: `font-size: 12px; color: var(--color-text-helper); text-decoration: none; border-bottom: 1px dashed var(--color-border);`
- Hover state: `color: var(--color-text); border-bottom-color: var(--color-text);`

#### 8. Print Stylesheet

```css
@media print{
  @page{ size: A4; margin: 2cm; }
  body{ max-width: none; }
  #toc-sidebar{ display: none; }
  #content{ margin-left: 0; max-width: none; padding: 0; }
  .module{ break-before: page; border-bottom: none; }
  .rb-cover{ break-after: page; min-height: 80vh; }
  .rb-img-grid, .rb-table-wrap, .rb-strategy-card, .rb-chain{ break-inside: avoid; }
  #btn-top, #btn-toc-toggle{ display: none; }
}
```

#### 9. JavaScript Interactions

- `IntersectionObserver` for sidebar TOC active state tracking (rootMargin: `-15% 0px -75% 0px`).
- Keyboard navigation: ↑/↓ (previous/next module), Home (cover), End (last module).
- Back-to-top floating button (`#btn-top`, appears after 600px scroll, bottom-right fixed).
- Sidebar link smooth scroll (prevent default, `scrollIntoView({behavior:'smooth', block:'start'})`).
- Mobile hamburger toggle for sidebar (≤860px breakpoint, `#btn-toc-toggle`).

#### 10. File Naming & Delivery

Save as `<Project-Name>_前期研究报告.html`. Inform the user the file is ready and can be opened in any browser.
Mention that:
- Images are SVG placeholders and can be replaced by editing the `src` attribute of `<img>` tags.
- State actual source verification status and date; do not claim all links were verified if some remain pending.
- The report can be printed to A4 PDF via Ctrl+P (browser print).


模板是起始骨架，未实现的组件、返回顶部和键盘交互按本指南及任务需要补充；完成后验证实际行为，不因模板名而宣称功能齐备。
