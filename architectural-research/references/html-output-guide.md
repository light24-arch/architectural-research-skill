# HTML Research Book — Visual & Technical Spec

> 基于 guizang-ppt-skill 的 Swiss 模板体系（Carbon 2x Grid / Inter + Noto Sans SC /
> 极轻字重 / 直角纯色 / hairline 分隔），适配 A4 纵向滚动研究报告。

---

## 1. Design Tokens

### Color System

```css
:root{
  /* Primary */
  --paper: #fafaf8;           /* 主底色 */
  --ink: #0a0a0a;             /* 文字主色 */
  --accent: #9BBFE7;          /* 海蓝高亮（区别于 PPT 的 IKB #002FA7） */
  --accent-rgb: 155, 191, 231;
  --accent-on: #ffffff;       /* accent 上的反色文字 */

  /* Grey scale */
  --grey-1: #f0f0ee;          /* 浅灰底 */
  --grey-2: #d4d4d2;          /* 中灰分割线 */
  --grey-3: #737373;          /* 暗灰辅助文字 */

  /* Text roles */
  --text-primary: #0a0a0a;
  --text-secondary: #525252;
  --text-helper: #737373;
  --text-placeholder: #a3a3a3;
  --text-on-color: #ffffff;
  --border-subtle: #e0e0e0;
  --border-strong: #a3a3a3;
}
```

### Typography

```css
  /* Font stack — inherited from Swiss template */
  --sans: "Inter", "Helvetica Neue", "Helvetica", "Arial", system-ui, sans-serif;
  --sans-zh: "PingFang SC", "Noto Sans SC", "Microsoft YaHei UI", "微软雅黑", sans-serif;
  --mono: "JetBrains Mono", "SF Mono", "Consolas", monospace;
```

| Role | Class | Font | Weight | Size | Use |
|------|-------|------|--------|------|-----|
| Cover title | `.rb-cover-title` | sans + sans-zh | 200 | `min(8vw, 12vh)` | 封面项目名 |
| Module heading | `.rb-h1` | sans + sans-zh | 200 | `min(5vw, 9vh)` | 01–08 模块标题 |
| Sub-heading | `.rb-h2` | sans + sans-zh | 300 | `min(2.4vw, 5vh)` | 模块内小节标题 |
| Lead | `.rb-lead` | sans + sans-zh | 400 | `max(16px, 1.1vw)` | 模块导语 |
| Body | `.rb-body` | sans + sans-zh | 400 | `max(15px, .95vw)` | 正文段落 |
| Body small | `.rb-body-sm` | sans + sans-zh | 400 | `max(13px, .82vw)` | 表格内文字 / 脚注 |
| Meta / labels | `.rb-meta` | mono | 500 | `max(12px, .72vw)` | 日期 / 数据来源 / 图示编号 |
| KPI number | `.rb-kpi` | sans | 200 | `min(6vw, 10vh)` | 数据大字报数字 |
| Caption | `.rb-cap` | sans + sans-zh | 400 | `max(12px, .72vw)` | 图注 / 表注，颜色 `var(--text-helper)` |

### Spacing (Carbon 2x Grid)

```css
  --sp-3: 8px;   --sp-4: 12px;  --sp-5: 16px;  --sp-6: 24px;
  --sp-7: 32px;  --sp-8: 40px;  --sp-9: 48px;  --sp-10: 64px;
  --sp-11: 80px; --sp-12: 96px; --sp-13: 160px;
```

### Motion (Carbon)

```css
  --ease-prod: cubic-bezier(.2,0,.38,.9);
  --ease-exp: cubic-bezier(.4,.14,.3,1);
  --dur-fast: .11s;  --dur-mod: .24s;  --dur-slow: .4s;
```

---

## 2. Page Layout

### Base Structure

```
┌────────────────────────────────────────────┐
│  Cover (full-width accent bg, project name) │
├──────┬─────────────────────────────────────┤
│ TOC  │  01 项目理解                         │
│ side │  ─────────────────────────────────   │
│ bar  │  02 场地与环境研究                    │
│      │  ─────────────────────────────────   │
│ 240px│  03 城市、人群与文化研究               │
│      │  ...                                │
│      │                                      │
│      │  [content area: 700px max-width]     │
│      │                                      │
│      │  08 下一步建议                        │
└──────┴─────────────────────────────────────┘
```

### CSS

```css
body{
  max-width: 1000px;           /* TOC(240px) + content(~700px) + padding */
  margin: 0 auto;
  font-family: var(--sans), var(--sans-zh);
  color: var(--ink);
  background: var(--paper);
  scroll-behavior: smooth;
}

/* Sidebar TOC */
#toc{
  position: fixed; left: max(0px, calc((100vw - 1000px) / 2));
  top: 0; width: 240px; height: 100vh;
  padding: var(--sp-7) var(--sp-5);
  overflow-y: auto;
  border-right: 1px solid var(--border-subtle);
  background: var(--paper);
  z-index: 100;
}
#toc a{
  display: block; padding: 6px 0;
  font-size: 13px; color: var(--text-secondary);
  text-decoration: none; border-left: 2px solid transparent;
  padding-left: var(--sp-4);
  transition: color var(--dur-fast), border-color var(--dur-fast);
}
#toc a.active, #toc a:hover{
  color: var(--accent);
  border-left-color: var(--accent);
}

/* Main content */
#content{
  margin-left: 240px;
  padding: var(--sp-8) var(--sp-7);
}
.module{
  padding: var(--sp-8) 0 var(--sp-10);
  border-bottom: 1px solid var(--border-subtle);
}
.module:last-child{ border-bottom: none; }
```

### Responsive

On screens narrower than 900px, the TOC collapses to a hamburger toggle (top-left corner).
The `#content` margin-left becomes 0.

---

## 3. Component Library

### 3.1 Cover (Module 00)

Full-width accent background (#9BBFE7), centered project name in ExtraLight 200.
Optional: ASCII dot-matrix canvas from Swiss template (copy `ascii-bg` canvas + IIFE).

```html
<header class="rb-cover" style="background:var(--accent);color:var(--accent-on);
  min-height:60vh;display:flex;flex-direction:column;justify-content:center;align-items:center;
  text-align:center;padding:var(--sp-10)">
  <div class="rb-meta" style="opacity:.72;letter-spacing:.18em">ARCHITECTURAL RESEARCH BOOK</div>
  <h1 class="rb-cover-title">[项目名称]</h1>
  <div class="rb-lead" style="max-width:48ch;margin-top:var(--sp-6);opacity:.86">[副标题/任务书来源]</div>
  <div class="rb-meta" style="margin-top:var(--sp-7);opacity:.62">[日期] · [作者] · [格式：HTML Research Book]</div>
</header>
```

### 3.2 Module Header

Each of the 08 modules opens with a consistent heading block:

```html
<section class="module" id="module-01">
  <header class="rb-module-head">
    <div class="rb-meta" style="color:var(--accent);letter-spacing:.16em;margin-bottom:var(--sp-4)">
      01 / 08
    </div>
    <h2 class="rb-h1">项目理解 <span style="font-weight:300;opacity:.56">Project Understanding</span></h2>
    <p class="rb-lead" style="max-width:52ch;margin-top:var(--sp-4)">[模块导语 — 2-3 句，说明本章要回答什么问题]</p>
  </header>
  <!-- module content -->
</section>
```

### 3.3 KPI Data Hero (for Module 01 key metrics)

From Swiss template S06 KPI Tower, adapted for horizontal inline:

```html
<div class="rb-kpi-row" style="display:flex;gap:var(--sp-8);padding:var(--sp-7) 0;
  border-top:1px solid var(--border-subtle);border-bottom:1px solid var(--border-subtle)">
  <div class="rb-kpi-item">
    <div class="rb-kpi">78,300</div>
    <div class="rb-meta">用地面积 (㎡)</div>
  </div>
  <div class="rb-kpi-item">
    <div class="rb-kpi">1.2</div>
    <div class="rb-meta">容积率 FAR</div>
  </div>
  <!-- ... N more -->
</div>
```

### 3.4 Image Grid (for Modules 02, 06)

From Swiss S15/S16, 3-column grid:

```html
<div class="rb-img-grid" style="display:grid;grid-template-columns:repeat(3,1fr);
  gap:var(--sp-5);margin:var(--sp-6) 0">
  <figure>
    <img src="02-site-aerial.jpg" loading="lazy"
         style="width:100%;aspect-ratio:16/10;object-fit:cover" alt="">
    <figcaption class="rb-cap">图 2.1: 场地区位航拍。来源：Google Earth</figcaption>
  </figure>
  <!-- ... N more -->
</div>
```

### 3.5 Comparative Table (for Modules 04, 06, 07)

```html
<table class="rb-table" style="width:100%;border-collapse:collapse;margin:var(--sp-6) 0">
  <thead>
    <tr style="background:var(--accent);color:var(--accent-on)">
      <th style="padding:var(--sp-4);text-align:left;font-weight:500">项目</th>
      <th>GFA</th><th>关键策略</th><th>来源</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid var(--border-subtle)">
      <td style="padding:var(--sp-4)">Shebara Resort</td>
      <td>—</td><td>100%离网光伏</td>
      <td><a href="...">ArchDaily</a></td>
    </tr>
    <tr style="background:var(--grey-1);border-bottom:1px solid var(--border-subtle)">
      <td style="padding:var(--sp-4)">...</td>
      <td>...</td><td>...</td><td>...</td>
    </tr>
  </tbody>
</table>
```

### 3.6 Strategy Card (for Module 07)

Each strategy rendered as an accent-bordered card:

```html
<div class="rb-strategy-card" style="border-left:3px solid var(--accent);
  padding:var(--sp-5) var(--sp-6);margin-bottom:var(--sp-6);background:var(--grey-1)">
  <div class="rb-meta" style="color:var(--accent)">策略 01 / 08</div>
  <h3 class="rb-h2" style="margin-top:var(--sp-3)">【策略名称】</h3>
  <div style="margin-top:var(--sp-4);display:grid;gap:var(--sp-4)">
    <!-- 8 elements rendered in structured sub-sections -->
  </div>
</div>
```

### 3.7 Design Challenge (for Module 05)

Problem → Opportunity → Strategy arrow format:

```html
<div class="rb-challenge-chain" style="display:flex;align-items:center;gap:var(--sp-5);
  padding:var(--sp-6) 0">
  <div style="flex:1;padding:var(--sp-5);background:var(--grey-1)">
    <div class="rb-meta">问题</div>
    <div class="rb-body-sm" style="margin-top:var(--sp-3)">基地与城市联系弱</div>
  </div>
  <div style="font-size:24px;color:var(--accent)">→</div>
  <div style="flex:1;padding:var(--sp-5);background:var(--grey-1)">
    <div class="rb-meta">机会</div>
    <div class="rb-body-sm" style="margin-top:var(--sp-3)">创造城市公共接口</div>
  </div>
  <div style="font-size:24px;color:var(--accent)">→</div>
  <div style="flex:1;padding:var(--sp-5);background:var(--grey-1)">
    <div class="rb-meta">策略方向</div>
    <div class="rb-body-sm" style="margin-top:var(--sp-3)">开放式底层空间</div>
  </div>
</div>
```

### 3.8 Mermaid Diagram

```html
<pre class="mermaid" style="background:var(--grey-1);padding:var(--sp-5);
  margin:var(--sp-6) 0;border:1px solid var(--border-subtle)">
graph TD
  A[项目理解] --> B[场地研究]
  B --> C[人群文化]
  C --> D[功能推演]
  D --> E[问题提炼]
  E --> F[案例启示]
  F --> G[策略探索]
</pre>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
```

---

## 4. Print Stylesheet

```css
@media print{
  @page{ size: A4; margin: 0; }
  body{ max-width: 210mm; }
  *{ -webkit-print-color-adjust: exact; print-color-adjust: exact; forced-color-adjust: none; }
  #toc{ display: none; }
  #content{ margin-left: 0; padding: 2cm; }
  .module{ break-before: page; border-bottom: none; padding: 0; }
  .rb-cover{ break-after: page; min-height: 297mm; }
  .rb-img-grid{ break-inside: avoid; }
  .rb-table{ break-inside: avoid; }
  .rb-strategy-card{ break-inside: avoid; }
  #btn-top{ display: none; }
}
```

---

## 5. Interaction & Navigation

### Sidebar TOC

- Fixed left sidebar, scrollable independently
- Active section detection via `IntersectionObserver` — highlights current module in TOC
- Click TOC item → `scrollIntoView({behavior:'smooth'})`
- TOC items numbered 01–08 + cover

### Keyboard

| Key | Action |
|-----|--------|
| ↑ | Scroll to previous module top |
| ↓ | Scroll to next module top |
| Home | Scroll to cover |
| End | Scroll to module 08 bottom |

### Back to Top

Floating button (bottom-right, fixed) — appears after scrolling past 01.
Scrolls to cover with smooth animation.

### Image Lightbox

Click any image in `.rb-img-grid` → opens full-resolution version in centered modal.
Close with × button, click outside, or Escape key.

---

## 6. Edit Mode

Reuse `contentEditable` pattern from resume-builder and guizang-ppt-skill:
- Toggle button (bottom-right, fixed): ✎ 编辑 / ✓ 保存
- `.page` becomes `contentEditable`, structural elements (headers, dates) protected
- Save → download modified HTML
- Cleanup garbage tags before export

---

## 7. Data Footnotes

Inherited from SKILL.md Data Reliability Conventions:
```html
<footer class="rb-footnote" style="font-size:max(11px,.68vw);color:var(--text-helper);
  margin-top:var(--sp-6);padding-top:var(--sp-4);border-top:1px solid var(--border-subtle)">
  注：气候数据基于斗湖气象站多年平均值推演，需结合实测微调。
</footer>
```

---

## 8. File Structure

```
architectural-research/
├── SKILL.md
├── assets/
│   └── research-book-template.html    ← Single-file HTML skeleton (to build)
└── references/
    ├── html-output-guide.md           ← This file
    ├── report_template.md
    ├── climate_data.md
    └── interview-guide.md
```

`research-book-template.html` will be a complete, runnable template with all CSS +
placeholder content, following the specs in this guide. Generate it by composing the
components above into a valid HTML document.
