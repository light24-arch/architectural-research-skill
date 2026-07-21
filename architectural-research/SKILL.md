---
name: architectural-research
description: >-
  Conduct architectural pre-design research and generate a structured report in .docx format.
  Use this skill whenever a user mentions architectural pre-design research, building site analysis,
  architectural feasibility study, or provides an architectural design brief/task document (.docx or .pdf).
  Also trigger when the user asks to "analyze a site," "research before design," "prepare a site study,"
  or mentions terms like FAR/floor area ratio, building setback, site planning, zoning analysis,
  or precedent studies in an architectural context. If a design brief file is attached or mentioned,
  always use this skill.
---

# Architectural Research Agent

面向建筑学生、建筑师及设计团队的**建筑前期研究助手**。

从项目任务书中辅助完成"信息理解 → 问题发现 → 设计机会 → 空间策略"的建筑设计推导过程。
不是整理资料，而是推导设计方向。

The core methodology is a **design derivation chain**, not a data dump:

```
项目理解 → 场地研究 → 人群与文化 → 体量与功能推演 → 问题提炼 → 设计机会 → 策略探索 → 空间概念
```

Every section answers a question that pushes the design forward. The final output is a structured
research book (.docx or .html) that traces this logic, culminating in 5–8 actionable design strategies
for the designer to evaluate.

## Quick Reference

| Task | Approach |
|------|----------|
| Extract brief data | `.docx` via python-docx; `.pdf` via `markitdown` (fallback: `pypdf`) |
| Project understanding check | Before research: list identified / inferred / missing info from brief |
| Infer project location | Derive approximate address (city/district/area) directly from the brief |
| Surrounding POIs & roads | Overpass API → web search → city-type inference (3-tier fallback) |
| Climate data | Open-Meteo API → built-in city DB (`references/climate_data.md`) → zone inference |
| Wind rose | Generate SVG via bundled `scripts/wind_rose.py`; draw manually if only text data |
| Case studies | Web search bilingual; cite only verified URLs; never fabricate links |
| Design strategy generation | Cross problem sources × spatial strategy types → 5–8 actionable strategies |
| Image collection | Search and download relevant photos, maps, diagrams per image strategy |
| Final report | python-docx (.docx) or HTML (.html), following report structure below |

---

## Information Search Strategy

**Priority order:** User-provided local files → Built-in reference DB → Web search → API data.

Architectural research spans both Chinese and English sources. Always use bilingual search,
especially in these modules. If the user provided local reference files in the Before You Begin
step, load and search those first — they may eliminate the need for web search in some modules.

| Module | Chinese Sources | English Sources |
|--------|----------------|-----------------|
| 02.1 Location & Context | 当地自然资源和规划局网站、百度百科城市条目 | Wikipedia city/country pages, UN-Habitat reports |
| 02.2 Cultural Context | 知网/百度学术地域建筑论文、地方志、建筑遗产名录 | Google Scholar, JSTOR vernacular architecture |
| 03. Culture & History | 地方文史资料、非物质文化遗产名录、民俗志 | UNESCO intangible heritage, academic ethnography |
| 07. Precedent Studies | 谷德设计网(gooood.cn)、 ArchiPosition(archiposition.com) | ArchDaily(archdaily.com), Dezeen(dezeen.com), Architizer(architizer.com) |

### Case Search Priority (CRITICAL)

When searching for architectural precedent cases, **always search these five sites first**, in order of priority:

| Priority | Site | URL | Strengths |
|----------|------|-----|-----------|
| 1 | **ArchDaily** | archdaily.com | Largest global architecture database; project facts, drawings, photos |
| 2 | **Dezeen** | dezeen.com | High-quality curated projects; design strategy interviews |
| 3 | **Architizer** | architizer.com | Award-winning projects; strong filtering by typology/climate |
| 4 | **谷德设计网** | gooood.cn | Best Chinese-language source; Asian projects in depth |
| 5 | **ArchiPosition** | archiposition.com | Young Chinese architects; emerging practice strategies |

Use site-specific search queries:
- English: `site:archdaily.com [building type] [location]`
- English: `site:dezeen.com [architect name] [project type]`
- Chinese: `site:gooood.cn [建筑类型] [关键词]`

**Fallback**: If none of the five sites return relevant results, expand to general web search with bilingual queries.
**Rule**: URLs in the final report MUST come from one of these five sites or a verified official firm page. Never cite aggregator/listicle sites (e.g., Pinterest, Reddit, Wikipedia).

**Search technique:** For each topic, run at least one Chinese query and one English query.
Chinese queries should use specific project/location names and architectural terminology.
English queries should pair the project type with terms like "precedent," "case study,"
"design strategy," or "best practice."

The bilingual approach consistently surfaces more relevant results than either language
alone, especially for projects in non-English-speaking regions.

---

## Source Integrity Rules (CRITICAL)

**NEVER fabricate URLs or source references.** This is the single most important quality
rule. All links, project names, architect names, and source citations must come from
actual web search results or verified built-in knowledge.

### The Verification Rule

Before including any source link in the report, ask yourself: "Did a web search
actually return this exact URL?" If the answer is NO, do NOT include it. Instead:

| Situation | Correct Action |
|-----------|---------------|
| Search returned the URL | Include it: `来源：https://www.archdaily.com/...` |
| Search found the project but URL is unclear | Describe how to find it: `来源：ArchDaily 搜索 "Project Name"` |
| Search found similar projects but not this one | Use a descriptive reference: `来源：谷德设计网相关案例检索` |
| You know about the project from training data | **DO NOT cite it as a link.** Cite as: `参考：[Project Name] — 公开建筑媒体报道` |

### Fabrication Prevention Checklist

For EVERY report, verify the following before finalizing:

- [ ] Every URL in the report was returned by a web search during this session
- [ ] Every project name in precedent studies was confirmed by search results
- [ ] Every architect name is correctly paired with the project (search-verified)
- [ ] Every "来源" note is either a real URL or an honest description of how to find it
- [ ] No URLs were generated from memory or training data

**Why this matters:** Fabricated links in an architectural research report undermine
credibility and waste the user's time chasing nonexistent sources. Honest descriptions
of where to find information are always better than fake precision.

---

## Image Collection Strategy

Reports must be richly illustrated. Download relevant images from the web and embed them
directly in the .docx report. Treat images as first-class research content — they convey
site conditions, architectural strategies, climate data, and design intent faster than text.

### Image Targets by Module

| Module | Images to Collect | Typical Count |
|--------|------------------|---------------|
| 01. Project Understanding | — (text + tables only) | 0 |
| 02. Site & Context | City/district location map, aerial/satellite view of site area, surrounding landmark photos, street view captures, regional architectural examples | 4–8 |
| 02.2 Climate & Environment | Wind rose SVG (generated), climate charts if available, site terrain/topography if relevant | 2–4 |
| 03. Culture & Users | Local cultural heritage photos, historical images, vernacular architecture details, user scenario illustrations | 2–5 |
| 04. Program & Massing | — (tables + diagrams only) | 0 |
| 05. Design Challenges | — (text only) | 0 |
| 06. Precedent Studies | **Most image-rich section:** exterior photo, interior photo, and key diagram/plan/section per case study (2–3 images per project, 6–15 total) | 6–15 |
| 07. Strategy Exploration | Strategy concept diagrams (optional) | 0–5 |
| 08. Next Steps | — (text only) | 0 |

### Image Search Technique

1. **Search alongside text research** — when you search for climate data, also search for
   `[city name] climate chart wind rose`; when you find a precedent project, immediately grab its images.
2. **Use image-dedicated sources** — ArchDaily, gooood.cn, Dezeen all have high-quality
   project photos; Wikipedia Commons for maps and diagrams; Bing/Google image search for
   specific subjects (e.g., "Semporna aerial view Bajau stilt village").
3. **Verify relevance** — every image must be clearly related to the project. Skip generic
   stock photos. Prefer images that show specific architectural features, site conditions,
   or design strategies mentioned in the text.
4. **Caption every image** — format: `图 X: <description>。来源：<URL>` in 9pt below the image.

### Download & Embed with python-docx

```python
import urllib.request
from docx.shared import Cm

def safe_download(url, path, timeout=15):
    """Download image with error handling; returns True on success."""
    try:
        urllib.request.urlretrieve(url, path)
        return True
    except Exception:
        return False

if safe_download(image_url, 'temp_image.jpg'):
    doc.add_picture('temp_image.jpg', width=Cm(15))
else:
    # Generate placeholder — never stall the report
    doc.add_paragraph(f'[占位：此处应补充图片 — {caption}]')
```
- Always wrap image downloads in try/except; skip failed images rather than stalling
- **If download fails:** generate a text placeholder `[占位：此处应补充 XX 图片]` at the
  image location. The report MUST continue. Do not retry the same URL more than once.
- Maximum image width: 15 cm (fits within A4 margins)
- Supported formats: JPG, PNG; SVG must be converted to PNG before embedding
- Resize to reasonable dimensions; avoid embedding multi-megabyte originals
- Every image must have a caption immediately below (or the placeholder text)

### Copyright Note

This is for the user's personal design research and academic use. Images sourced from
publicly accessible architecture media and embedded with attribution and source links are
appropriate use. Do not embed images from paywalled or clearly restricted sources.

---

## Workflow — One-Time Initialization

When the skill is triggered and a task brief is provided, do NOT ask multiple questions
or run Step 0 separately. Instead, **read the brief, think silently, and output a single
initialization summary**. The user confirms once, then all research proceeds uninterrupted.

### Output format (single message, no follow-up questions):

```
## 项目理解初始化

### 项目概况
- 项目类型：[从任务书提取]
- 建设规模：[用地面积 / GFA / FAR 等指标]
- 核心功能：[主要功能组成]
- 特殊约束：[保护要素 / 限高 / 退线等]

### AI 推断（需用户确认）
- [推断 1：基于建筑类型推断的 XXX]
- [推断 2：基于项目位置推断的 XXX]

### 待补充信息
- [缺失项 1] — 影响 [哪个模块] 的分析深度
- [缺失项 2] — 影响 [哪个模块] 的分析深度

### 推荐研究深度
- 深度模块：01 / 02 / 06 / 07（标准）
- 轻量模块：04 / 05（精简）
- 策略数量：建议 5–8 个

### 输出格式
默认 HTML（浏览器查看）/ 可选 .docx（Word 文档）

---

📎 如有本地参考文件（案例 / 笔记 / 规范 / 照片），请将路径发给我——我会优先引用。

回复 1 → 按上述默认配置执行
回复 2 → 我需要补充/调整（请注明调整内容）
```

### After user confirms:

- If user replies **1**: Proceed immediately to research (Step 1–5). Do not ask any more
  questions.
- If user replies **2** with supplements: Update the initialization summary, then proceed.
- If user provides **local files**: Read them and adjust module depth accordingly
  (e.g., if user provides a full case study document → Module 06 becomes lighter,
  since user already has curated precedent material).

### User Knowledge Base (RAG Layer)

When the user provides local reference files in response to the initialization prompt,
they serve as a **pre-loaded knowledge base** with highest retrieval priority.

**Rules for user-provided files:**
1. **Always load first.** Before any web search, read the user's local files.
2. **Cite with priority.** Format: `来源：用户提供 — [文件名]`.
3. **Supplement, don't replace.** User files fill gaps; web search covers the rest.
4. **Flag coverage.** In the report introduction, note which sections were primarily sourced
   from user-provided materials.

**Supported file types:** `.pdf` / `.docx` / `.pptx` / `.jpg/.png` / `.txt/.md`

---

## Step 1 — Site, Location & Context (Macro → Meso)

### 1.1 Location & Policy (Macro)

- Identify the site's position in the city/district hierarchy (CBD, suburb, new district, etc.).
- Summarize accessibility: distance to nearest metro stations, major arterials, bus hubs.
- **Policy lookup is user-driven.** Before researching planning policies, ask the user:
  should this project consult local planning regulations and industry policies? Small-scale
  projects (e.g., renovation, single building) may reasonably skip this step; large-scale
  projects (e.g., new district, complex, public building) should include it. If the user
  requests policy research, search online for relevant planning policies, industrial development
  guidance, or urban design guidelines that apply to this district. Cite specific documents
  and always provide source URLs.
- Provide the likely URL of the local natural resources and planning bureau website as a
  reference regardless, so the user can manually verify the latest planning documents.

**Tooling — OSM/Overpass (tiered fallback):**
- **Tier 1:** Query Overpass API for `highway=primary`, `highway=secondary`, `railway=subway`,
  `amenity=bus_station` within 1–2 km radius. Run `python scripts/osm_query.py --lat <lat> --lon <lon>`.
- **Tier 2 (API fails):** Describe based on city type — no web search for roads (unreliable).
  CBD (dense transit, walkable), new district (metro-oriented, wide roads), suburb (car-dependent),
  rural (limited transit). Always mark as: "注：交通分析基于城市类型推断，建议结合实地调研核实。"

### 1.2 Cultural Context & Architectural Typology (Meso)

- Research the local architectural vernacular using **bilingual queries**: search in the
  local language for regional architecture terms (e.g., "江南水乡建筑空间原型" + "Jiangnan
  water town spatial typology"). Cover traditional spatial patterns (courtyard, skywell,
  arcade, etc.), indigenous materials, and climate-adaptive strategies.
- Find 2–3 outstanding local/regional architectural projects that successfully respond to
  similar context, and describe the specific design moves they employed.

### 1.3 Site Conditions (Meso → Micro)

Analyze the immediate site and its surroundings:

- **Site geometry:** area, shape, elevation difference, slope aspect.
- **Protected elements:** heritage buildings, structures, protected trees on or adjacent to the site.
- **Neighboring buildings:** function, height, massing, style, materials, texture, and their
  distance/orientation relative to the site.

If the Overpass data supports it, generate a simple site context map using folium and embed
it as an image in the report.

### 1.4 Traffic & Circulation (Micro)

Map the relationship between site access points and surrounding roads:

- Vehicle, pedestrian, and non-motorized circulation flows.
- Identify potential conflict points (e.g., service vehicle crossing pedestrian paths).
- If metro/subway is nearby, mark the pedestrian arrival direction and proposed connections.

**Required output:** A Mermaid flowchart showing circulation flows and conflict points.
To embed in the .docx, render the Mermaid diagram to PNG/SVG via an online service
(e.g., mermaid.ink) or describe it as a structured text diagram if rendering is unavailable.

---

## Step 2 — Climate & Environment (Hard Constraints)

Climate data has a three-tier path.

### Tier 1: Built-in City Database (preferred — read first)

**Always check `references/climate_data.md` first.** Read that file and look up the
project city by name. If the exact city is present, use its row directly. If a nearby
city with similar latitude and climate zone is present, use it and note:
"注：气候数据基于[参考城市]多年平均值推演，需结合实测微调。"

The reference covers: all Chinese provincial capitals and major cities, plus key
international destinations (Semporna, Kuala Lumpur, Bangkok, Singapore, Malé, Tokyo, Dubai, Sydney).

**For most routine projects, stop here.** The built-in DB is fast, reliable, and avoids
network dependencies. Only proceed to Tier 2 if:
- The city is NOT in the database, OR
- The project has strong passive-design or zero-carbon requirements that need granular data

### Tier 2: Open-Meteo API (on-demand, for missing cities or deep climate analysis)

Call the Open-Meteo Archive API for the project coordinates:
```
https://archive-api.open-meteo.com/v1/archive?latitude=X&longitude=Y
&start_date=2014-01-01&end_date=2023-12-31
&monthly=temperature_2m_mean,temperature_2m_max,temperature_2m_min,
precipitation_sum,relative_humidity_2m_mean,
wind_speed_10m_mean,wind_direction_10m_dominant,
sunshine_duration,shortwave_radiation_sum
```
Fetch 10 years of data, aggregate to monthly averages. Include `sunshine_duration` (hours)
and `shortwave_radiation_sum` (MJ/m²) for solar analysis. If the API is unreachable
(timeout after 15s, network error), fall back to Tier 3 without retrying.

### Tier 3: Climate Zone Inference (last resort)

If both the built-in DB and API fail, infer from the building climate zone:
- Determine zone from latitude + Köppen classification
- Use the zone-level design strategy summary at the bottom of `references/climate_data.md`
- Describe qualitative climate characteristics (e.g., "热带雨林气候，全年高温高湿")
- Mark as: "注：自然环境数据基于同气候区均值推演，需结合实测微调。"

### Wind Rose

If wind direction data is available (from API or the built-in table), generate an SVG wind rose
using `python scripts/wind_rose.py`. If only text wind data is available, draw the SVG manually
or describe the wind pattern in a structured text diagram.

### Design Implications

From the climate data (whatever tier), derive design implications:
- Optimal building orientation for natural ventilation and solar gain
- Seasonal shading requirements
- Drainage and waterproofing considerations based on precipitation patterns
- Noise sources (major roads, railways, flight paths) and suggested mitigation

Always cite the data source tier in the report so the user knows the reliability level.

---

## Step 3 — Program & Massing Analysis (→ Module 04)

From the brief's metrics, compute the buildable envelope, then layer in the functional program.
This is the quantitative backbone of the report — it locks down the numbers before any strategy
or concept work begins.

1. **Maximum buildable volume:** site_area × FAR
2. **Maximum building footprint:** site_area × building_density
3. **Height constraint:** min(regulated height limit, aviation/other limits)
4. **Typical floor count range:** height_limit ÷ typical floor height (3.6–4.5m for commercial, 2.8–3.3m for residential)
5. **Setback analysis:** apply front/side/rear setback requirements to determine the buildable envelope
6. **Area balance table:** GFA breakdown by function, with underground parking estimation

Present this as a structured table in the report. If any input metric is missing, note the
assumption used and mark the result as preliminary.

---

## Step 4 — Culture, History & Users (Soft Context)

### 4.1 Cultural & Historical Narrative

Search in **both Chinese and English** for the site's and surrounding area's:
- Historical evolution and significant events (local gazetteers, Wikipedia, UNESCO records)
- Local customs, folklore, or intangible heritage (非物质文化遗产 + UNESCO ICH)
- Industrial heritage or notable community memory
- Cultural symbols that could inform the design concept

This section provides narrative inspiration, not rigid constraints. Surface compelling stories
that could become a design driver.

### 4.2 User Profiles & Behavior

Identify the likely user groups and their behavior patterns:
- Primary users (residents, office workers, visitors — depends on building type)
- Secondary users (service staff, delivery, maintenance)
- Special needs groups (elderly, children, disabled)

**Survey generation:** If the project would benefit from primary user research, generate a
structured questionnaire (mostly multiple-choice, 10–15 questions) targeted at the identified
user groups. Output it as a table in the report appendix.

**Data limitation:** If census or demographic data is not available for the specific area,
base user profiles on the building type's established design knowledge, and clearly label
this as: "注：本段用户画像基于通用建筑设计知识推断，建议结合实地调研深化。"

---

## Step 5 — Precedent Studies (Strategy Extraction)

Present each case study with both text and images — a good case analysis shows, not just tells.
Include representative project photos, diagrams, or plans to illustrate key strategies alongside
the written analysis. This is for the user's personal design research, so using publicly available
images from architecture media is appropriate.

### Global/National Benchmarks (3–5 projects)
Search in **both Chinese and English** for internationally recognized projects of the same
building type. Use ArchDaily (cn/en), gooood.cn, ArchGo, Dezeen, Architizer, and Divisare.
Run parallel queries:

- Chinese: `[建筑类型] 案例 设计策略 [地点/气候区]`
- English: `[building type] precedent design strategy [location/climate]`

For each project, capture:

- Project name, location, architect, year, GFA
- **Source link:** Provide the URL returned by the web search. If the exact URL is unclear
  from search results, write a descriptive reference instead (e.g., "ArchDaily 搜索 'Project Name'").
  **Never fabricate a URL.** Follow the Source Integrity Rules above.
- Key design concept (1 sentence)
- 2–3 specific strategies worth borrowing (spatial organization, material innovation,
  environmental response, structural logic)
- Embed 2–3 representative images (exterior, interior, key diagram/plan) with captions
- 1 limitation or critique

### Local/Regional Precedents (2–3 projects)
Search for projects of the same type in the same city or climate zone. Use bilingual queries
with the city/climate-zone name in both languages (e.g., "Hangzhou library architecture" +
"杭州 图书馆 建筑案例"). Focus on how each project addresses local climate, cultural norms,
and market conditions specifically. Always include source links for every project.

### Comparative Matrix

Generate a structured comparison table in the report:

| Project | Location | GFA | Key Strategy | Material | Climate Response | Relevance to This Brief | Source |
|---------|----------|-----|-------------|----------|------------------|------------------------|--------|
| ... | ... | ... | ... | ... | ... | ... | [link] |

For each source link in the matrix, follow the Source Integrity Rules: use only URLs
returned by actual web searches. If a URL is unclear, write "搜索 '[project name]' on ArchDaily" etc.

---

## Output: The Research Book

Write the final report as `<Project-Name>_前期研究报告.html` (default) or `.docx` (on request).
The report is not a data dump — it is a **design derivation book** that traces
the logic from understanding to strategy.

### Report Structure (9-Module Design Derivation Chain)

```
# [项目名称] — 建筑前期研究报告

## 01 项目概况 Project Overview
   任务书核心指标提取 / 硬性约束清单（表格：维度+内容）/ 信息状态声明
   （已识别 / AI推断需确认 / 待补充，用3张卡片并列）
   重点：一页之内建立项目认知基线，读者不需要翻任务书。

## 02 背景分析 Context Analysis
   区域语境（城市定位 / 产业特点 / 相关发展规划）/ 建筑类型背景
   （如任务书要求的模块化建筑缘起与发展）/ 为什么这个项目在此地有价值
   重点：从宏观视野解释项目定位，不孤立地看建筑。

## 03 场地与环境 Site & Environment
   3.1 气候数据大字报（KPI Row：年均温 / 湿度 / 日照 / 降雨，4列）
   3.2 气候 → 设计策略推导（3张卡片：高温→通风 / 强日照→遮阳+产能 / 强风盐雾→耐候）
   3.3 自然灾害风险评估（5列表格：灾害类型 / 风险等级 / 影响 / 设计应对）
   重点：每项环境数据必须转译为设计动作。表格、卡片、KPI 都是"论据"。

## 04 人群与文化 User & Culture
   4.1 人群画像（4列卡片：人群名 → 核心行为 → 空间需求 → 设计回应）
   4.2 地域文化 → 空间转译链（文化原型 → 空间特征 → 现代转译，3列Chain组件）
   4.3 生活方式 → 空间需求映射表
   重点：文化用"聚落+架空+连桥"等空间组织表达，不用符号化装饰。

## 05 设计挑战 Design Challenges
   5个核心矛盾，每个一张Challenge Card（左边框线+问题描述+问题标签）。
   标签分类：场地问题 / 气候问题 / 文化问题 / 能源问题 / 技术问题 / 空间问题。
   每张卡片底部附"→ 查看对应的设计机会"链接（跳转到Module 06对应锚点）。
   重点：此时只定义问题，不给出答案。每个挑战以"核心问题：xxx？"收尾。

## 06 设计机会 Design Opportunities
   5个机会，对应Module 05的5个挑战。每个机会用Chain组件（← → 连接）：
   从Challenge 0X → 机会简述 → 机会展开说明。
   每个机会链有独立锚点ID（#opp-01 ~ #opp-05），供Module 05跳转。
   重点：问题是给定的，机会是主动发现的。每个机会可指向一条或多条后续策略。

## 07 策略探索 Strategy Exploration
   6条设计策略，每条一个Strategy Card（8要素完整结构）：
   Strategy Name → Design Question → Evidence(Site/Culture/User) →
   Opportunity → Concept → Spatial Operation（必须转译为具体空间动作）→
   Reference Cases（说明学什么）→ Applicability。
   末尾附策略生成矩阵（5×5覆盖关系表：问题来源 × 空间策略类型）。
   重点：每条策略的空间动作必须具体（如"架空底层""连桥街道系统"），
   禁止只有抽象概念没有空间回应。

## 08 案例对标 Reference Cases
   6个案例，包含：图片网格（3列，可替换img标签）+ 对比表
   （案例名/年份地点/建筑师/关键策略/本项目启示/已验证URL）。
   末尾附4条关键启示（2×2卡片网格）。
   重点：URL必须通过web search验证后填入，未验证的不填。
   每个案例说明"学习什么"和"对本策略的启发"。

## 09 结论与建议 Conclusion
   5条核心发现（编号列表）/ 硬性vs弹性约束表 / 风险评估表（5行）/
   3步行动建议（3列卡片：01策略筛选 → 02场地深化 → 03概念方案）。
   重点：不是重复前文，是提炼可操作的下一步。
```

### Output Format

Default output is **.html**. User can request .docx if needed.

- **.html (default, recommended)**: Single-file interactive research book — black & white
  editorial design, fixed left sidebar TOC (180px), rounded corners, smooth scroll,
  Challenge→Opportunity jump links, printed to A4 PDF via Ctrl+P.
  Opens in any browser, no server needed. Best for presentation, sharing, and team review.
  (Full HTML generating rules: see "HTML Rendering Specification" below.)
- **.docx (on request)**: Traditional Word document — python-docx with embedded images,
  following `references/report_template.md` formatting spec. Best for academic submission
  where .docx is required.

### HTML Rendering Specification

This section is the **complete rendering rulebook** for generating the HTML research book.
Read it before writing any HTML output. The canonical reference implementation is at
`assets/research-book-template.html` (to be sync'd with the v2 design system).

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

**CRITICAL: Do NOT display AI reasoning chains, Mermaid diagrams, or internal analysis flow in the HTML.**
The research book shows architectural results, not AI thinking process.

| Component | CSS Class | Use When | Example Module |
|-----------|-----------|----------|----------------|
| KPI Row | `.rb-kpi-row` (flex, gap, card bg) | 3–4 key metrics in a horizontal row | M01 (rooms/FAR/module size), M03 (temp/humidity/sunlight/rain) |
| Card Grid | `.rb-card-grid` (3-col grid) | Comparing equal-weight items side by side | M01 (info status ×3), M03 (climate→strategy ×3), M04 (persona ×4), M09 (next steps ×3) |
| Card (accent top) | `.rb-card-accent` (card + border-top) | Cards with a black top-border accent | M03 (climate design strategies) |
| Table | `.rb-table` | Structured comparison data, >3 rows | M01 (constraints), M03 (disaster risks), M04 (lifestyle→space), M08 (case matrix), M09 (risks) |
| Chain | `.rb-chain` (flex row + `.rb-chain-arrow`) | Sequential "A → B → C" reasoning | M04 (culture→space translation), M06 (challenge→opportunity chains) |
| Strategy Card | `.rb-strategy-card` (left border + card bg) | Each design strategy | M07 (6 strategies × 8 elements each) |
| Challenge Card | `.rb-strategy-card` with `background: var(--color-bg); border-left-width: 1px` | Each design challenge | M05 (5 challenges with problem tags) |
| Image Grid | `.rb-img-grid` (3-col grid) | Case photos, site photos | M08 (3 case images) |
| Divider | `.rb-divider` (dashed border-top) | Visual separation without new heading | Between M06 opportunity chains |

**Images**: Use `<img class="rb-img" src="...">` with inline SVG data URI placeholders (grey rect + label text).
Users replace by editing the `src` attribute. Do NOT use `<div>` as image placeholder.

**Problem Tags**: In M05, each challenge card has pill-shaped `<span>` tags (`border-radius: 99px; border: 1px solid var(--color-border); font-size: 11px`) for visual categorization: 场地问题 / 气候问题 / 文化问题 / 能源问题 / 技术问题 / 空间问题.

#### 6. Case Links & URLs

**CRITICAL**: URLs must be verified via web search before inclusion.
- Stage 1: AI identifies case name + architect + year + strategic value (no URL).
- Stage 2: Web search for official/authoritative pages (ArchDaily, Dezeen, firm website, UN-Habitat, etc.).
- Stage 3: Only `verified=true` URLs are rendered as clickable `<a href="..." target="_blank" rel="noopener">` links in the HTML.
- Each case link cell in the table shows: `[官网 →]` or `[ArchDaily →]` or `[UN-Habitat →]` etc.
- If no verified URL found: leave link cell blank or mark as `[待验证]`.

#### 7. Challenge → Opportunity Jump Links

- Each challenge card in M05 ends with: `<a href="#opp-NN" class="rb-challenge-link">→ 查看对应的设计机会</a>`
- Each opportunity chain in M06 has a unique ID: `id="opp-01"` through `id="opp-05"`
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
- Case URLs have been web-search verified (note verification date).
- The report can be printed to A4 PDF via Ctrl+P (browser print).

#### 11. Strategy Card Internal Structure (M07)

Each strategy card MUST contain these 8 sections, in this order, using `.rb-h3` for sub-headings and `.rb-body-sm` for content:

1. **Design Question** — Why this strategy is needed. The specific problem it addresses.
2. **Evidence** — Design basis, citing Site / Culture / User evidence from earlier modules.
3. **Opportunity** — What new possibility architecture can create.
4. **Concept** — The design concept in 1–2 sentences.
5. **Spatial Operation** — MUST be translated into concrete spatial actions (e.g., "架空底层" "连桥街道系统" "半室外冷巷" "BIPV屋面一体化"). This is the most important section — no abstract concepts without spatial response.
6. **Reference Cases** — Name specific projects and explain what to learn from each. Never just list names.
7. **Applicability** — What project types this strategy suits.
8. **Strategy number** — Labeled as STRATEGY 01/06 through 06/06 at the top of each card.


## Design Strategy Template (Module 07)

Each of the 5–8 design strategies MUST follow this 8-element structure.
This is the core deliverable of the entire research — where analysis becomes design action.

### Strategy Generation Logic

Follow this 5-step chain for each strategy:

```
Step 1: 事实发现 What exists?     → from Modules 01–04 analysis
Step 2: 问题判断 What challenges?  → from Module 05
Step 3: 设计机会 What opportunities? → cross with strategy matrix
Step 4: 策略生成 How architecture responds? → spatial concept
Step 5: 空间转译 How it becomes space? → spatial operations
```

### Strategy Generation Matrix

Cross **problem sources** × **spatial strategy types** to generate strategies.
This prevents empty conceptual language — every strategy is anchored to a specific problem.

**Problem Sources (问题来源):**
- 场地问题 (site constraints)
- 人群问题 (user needs)
- 文化问题 (cultural context)
- 环境问题 (climate/ecology)

**Spatial Strategy Types (空间策略类型):**

| 类型 | 空间动作 |
|------|---------|
| 开放型 | 架空 / 边界开放 / 公共庭院 |
| 聚落型 | 小体量组合 / 庭院组织 / 节点连接 |
| 生态型 | 绿色廊道 / 景观融合 / 生态缓冲 |
| 体验型 | 空间序列 / 仪式感 / 游览路径 |
| 未来型 | 灵活空间 / 智慧系统 / 新产业融合 |

### Individual Strategy Template

```
### 策略 N：【策略名称】（4–8 字，清晰传达核心主张）

> 示例：开放共融型城市节点 / 庭院渗透式教学聚落 / 漂浮模块化生态岛

**1. 核心问题 Problem（2–3 句）**
从 Module 05 的"问题 → 机会"分析中提取，说明当前场地或项目面临的具体挑战。
- 第一句：陈述现状或矛盾（引用具体数据或场地条件）
- 第二句：说明如果不解决这个问题，对项目的影响是什么
- 示例："基地东侧紧邻城市快速路（噪声 > 70dB），西侧与滨河绿地被围墙完全隔离。
  若不处理这两侧界面，建筑将同时面临噪声干扰和景观资源浪费。"

**2. 设计机会 Opportunity（2–3 句）**
从限制条件中看到积极的设计可能，说明建筑介入后能创造什么新的空间价值。
- 示例："噪声界面恰好是城市人流最密集的方向——将底层向城市打开，
  建筑不仅可以屏蔽上层噪声，还能把过路人群转化为底层商业和文化空间的自然客流。"

**3. 设计依据 Evidence（3 条，每条 1–2 句）**
- 场地依据：来自 Module 02 的具体分析结论（地形 / 景观 / 交通 / 城市关系）
- 文化/人群依据：来自 Module 03 的具体分析结论（地域文化 / 建筑传统 / 用户行为 / 社会需求）
- 技术/气候依据：来自 Module 02.2 或 Module 04 的具体数据（体量指标 / 气候数据 / 日照 / 风向）

**4. 设计概念 Concept（1–2 句）**
选择一个明确的概念方向，并说明为什么适合本项目。概念不等于策略——概念是"做什么"，策略是"怎么做"。
- 社会类：开放共融 / 社区共享 / 多元共生 / 场所记忆 / 过渡空间
- 生态类：生态融合 / 绿色廊道 / 自然共生 / 气候应答 / 海绵系统
- 空间类：庭院聚落 / 空间渗透 / 场所营造 / 轴线组织 / 层叠序列
- 技术类：被动式环境控制（通风/遮阳/辐射制冷）/ 高性能表皮 / 模块化装配 / 光伏集成
- 未来类：灵活可变 / 智慧建筑 / 新产业融合 / 共享经济空间

**5. 空间动作 Spatial Operation（选择 3–5 个，从概念到空间的翻译）**
这些必须是与策略直接相关的具体空间操作，不是泛泛的"优化空间"：
底层架空 / 边界打开 / 渗透式界面 / 半室外过渡 / 庭院系统 / 空间序列 / 中轴组织 /
对景关系 / 体量错动 / 屋顶利用 / 下沉空间 / 双层表皮 / 拔风天井 / 退台花园 /
模块组合 / 架空连廊 / 视线通廊 / 灰空间节点

**6. 参考案例 Reference（1–2 个）**
来自 Module 06 的案例（或额外搜索），每个注明：
- 案例名称 + 地点
- 学习了什么（具体的策略或构造方式，不是"可以参考它的设计理念"）
- 本项目的适用性（直接迁移 / 需要调整 / 仅作思路参考）
- 示例："MVRV 深圳万科云城 — 学习其底层架空+商业街坊串联策略，本项目可直接迁移该逻辑。"

**7. 适用条件 Applicability（1–2 句）**
- 该项目类型的匹配度（文旅 / 公共建筑 / 城市更新 / 教育 / 办公 / 居住）
- 适用规模范围（建筑面积 / 用地面积）
- 任何前置条件（如：需要有城市界面、需要有高差、需要有一定密度）

**8. 策略价值 Value（1–2 句）**
- 这个策略解决的核心矛盾是什么？
- 如果不采用这个策略，项目的设计品质会缺失什么？
- 与 Module 05 的"设计机会"形成闭环呼应。
```

### Cross-Strategy Coherence Check

生成全部 5–8 个策略后，做一次交叉检查：
- [ ] 5–8 个策略是否覆盖了 Module 05 提炼的主要问题？（不遗漏）
- [ ] 每个策略是否用到了 Module 06 中至少一个案例的启示？（不脱离研究）
- [ ] 策略之间是否有明显的差异化？（空间动作不重复）
- [ ] 是否存在互斥策略？（如有，标注为"A/B 方案"，供设计师选择）
- [ ] 每个策略的空间动作是否可被设计人员直接作为下一步深化方向？

### Strategy Quality Checklist

Before finalizing each strategy, verify:
- [ ] Anchored to a specific finding from Modules 01–05 (not generic)
- [ ] Includes at least 3 concrete spatial operations (not just abstract concept)
- [ ] References at least one evidence source + one precedent case
- [ ] Distinguishable from other strategies (not the same idea rephrased)
- [ ] Actionable — a designer reading it knows what to explore next
- [ ] Self-contained — can be read and understood without referring to other strategies

---

## Adaptive Depth Control

The skill adapts research depth through two mechanisms working together:

### Mechanism A: Term Extraction + Search (automatic)
Step 0's Adaptive Research Focus extracts distinctive terms from the brief and runs targeted
web searches to find related precedents, strategies, and references. Based on what the
searches actually return, module depth is adjusted accordingly. If a term yields rich
architectural material, that module gets deeper treatment; if sparse, lighter.

### Mechanism B: User Confirmation (manual)
After keyword detection, present the proposed module depth to the user (as Before You Begin
specifies). The user can override any module's depth.

### Mechanism C: Phase-Based Default (fallback)
If no keywords are detected and the user doesn't specify, fall back to phase-based defaults:
- **Concept stage:** Modules 01, 02, 03, 07 at standard; 04, 05 at light; 06 at standard
- **Feasibility study:** All modules at standard; 06 at deep
- **Pre-construction:** Modules 01, 02, 04 at deep; rest at standard

### Graceful Degradation
In all cases, if an API call fails or web search returns nothing useful, degrade gracefully.
Note the limitation in the report and provide a manual alternative. Never stall waiting for
an external service.

---

## Bundled Scripts

- `scripts/osm_query.py` — Query Overpass API for POIs and road network around given coordinates.
  Usage: `python scripts/osm_query.py --lat <lat> --lon <lon> [--radius 1500]`
  Output: JSON with `pois`, `roads`, `railways` arrays.

- `scripts/wind_rose.py` — Generate SVG wind rose from wind frequency/direction/speed data.
  Usage: `python scripts/wind_rose.py --input wind_data.json --output wind_rose.svg`
  Input format: `[{direction: "N", speed_range: "2-4", frequency: 0.12}, ...]`

- `scripts/climate_fetch.py` — Fetch climate data from Open-Meteo API.
  Usage: `python scripts/climate_fetch.py --lat <lat> --lon <lon> --years 10`
  Output: JSON with monthly temperature, humidity, precipitation, wind.