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

# Architectural Pre-Design Research

Produce a structured _Architectural Pre-Design Research Report_ (.docx) from a design brief (.docx/.pdf).
The core methodology is **macro → meso → micro**, layer by layer: understand the city-scale role first,
then the neighborhood context, then the site's internal characteristics.

## Quick Reference

| Task | Approach |
|------|----------|
| Extract brief data | `.docx` via python-docx; `.pdf` via `markitdown` (fallback: `pypdf`) |
| Infer project location | Derive approximate address (city/district/area) directly from the brief |
| Surrounding POIs & roads | Overpass API → web search → city-type inference (3-tier fallback) |
| Climate data | Open-Meteo API → built-in city DB (`references/climate_data.md`) → zone inference |
| Wind rose | Generate SVG via bundled `scripts/wind_rose.py`; draw manually if only text data |
| Case studies | Web search bilingual; cite only verified URLs; never fabricate links |
| Image collection | Search and download relevant photos, maps, diagrams for modules 1/2/4/5 per image strategy |
| Final report | python-docx with embedded images, following `references/report_template.md` |

---

## Information Search Strategy

Architectural research spans both Chinese and English sources. Always use bilingual search,
especially in these modules:

| Module | Chinese Sources | English Sources |
|--------|----------------|-----------------|
| 1.1 Location & Policy | 当地自然资源和规划局网站、百度百科城市条目 | Wikipedia city/country pages, UN-Habitat reports |
| 1.2 Cultural Context | 知网/百度学术地域建筑论文、地方志、建筑遗产名录 | Google Scholar, JSTOR vernacular architecture |
| 4.1 History & Culture | 地方文史资料、非物质文化遗产名录、民俗志 | UNESCO intangible heritage, academic ethnography |
| 5. Precedent Studies | 谷德设计网(gooood.cn)、ArchDaily CN、建筑学院(archcollege.com)、搜建筑(soujianzhu.cn) | ArchDaily, Dezeen, Architizer, Divisare, World-Architects |

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
| 0. Project Overview | — (text + tables only) | 0 |
| 1. Site & Context | City/district location map, aerial/satellite view of site area, surrounding landmark photos, street view captures, regional architectural examples | 4–8 |
| 2. Climate & Environment | Wind rose SVG (generated), climate charts if available, site terrain/topography if relevant | 2–4 |
| 3. Zoning & Massing | — (tables + diagrams only) | 0 |
| 4. Culture & Users | Local cultural heritage photos, historical images, vernacular architecture details, user scenario illustrations | 2–5 |
| 5. Precedent Studies | **Most image-rich section:** exterior photo, interior photo, and key diagram/plan/section per case study (2–3 images per project, 6–15 total) | 6–15 |
| 6. Conclusions | Conceptual site strategy diagram (optional) | 0–1 |

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
    except Exception as e:
        print(f"Image download failed: {url} — {e}")
        return False

if safe_download(image_url, 'temp_image.jpg'):
    doc.add_picture('temp_image.jpg', width=Cm(15))
```
- Always wrap image downloads in try/except; skip failed images rather than stalling
- Maximum image width: 15 cm (fits within A4 margins)
- Supported formats: JPG, PNG; SVG must be converted to PNG before embedding
- Resize to reasonable dimensions; avoid embedding multi-megabyte originals
- Every image must have a caption immediately below

### Copyright Note

This is for the user's personal design research and academic use. Images sourced from
publicly accessible architecture media and embedded with attribution and source links are
appropriate use. Do not embed images from paywalled or clearly restricted sources.

---

## Before You Begin

Before starting any research, ask the user two questions in one short message:

1. **Module scope:** "Before I start, do you want all 6 modules at standard depth, or should I
   focus on specific ones? (e.g., skip policy if it's a small project, or go deep on culture.)"
2. **Policy research:** For projects with regulatory complexity, ask whether to include
   planning policy research.

If the user doesn't specify, default to the concept-stage profile (Modules 0/1/2/5 at standard;
3/4 at light). Then proceed to Step 0.

---

## Step 0 — Parse the Brief

Before any research, extract every quantitative and qualitative requirement from the brief:

- Project name, location (full address), building type
- Site area, floor area ratio (FAR), building density, height limit, green space ratio
- Functional program (room types, areas, adjacency requirements)
- Parking requirements, setback distances
- Any special constraints (protected trees, heritage buildings, noise zones)

Infer the project's approximate location directly from the brief — the goal is to identify the
general project address (city, district, area), not precise coordinates. If the brief's address
is vague, derive a reasonable location from project name, mentioned landmarks, or administrative
region; ask the user for clarification only if the location is genuinely ambiguous.

If any critical metric is missing from the brief (FAR, site area, height limit), flag it in the report
as "待补充" (to be supplemented) and state why the analysis for that dimension is limited.

### Adaptive Research Focus

After extracting the basic metrics, determine what makes this specific project unique
by extracting terms directly from the brief and searching for related knowledge online.
Do NOT rely on a fixed keyword list — every project has its own vocabulary.

#### Step A: Extract Distinctive Terms

Read the brief and pull out **5–10 terms, phrases, or requirements** that distinguish
this project from a generic one. Focus on:

- Repeated technical terms (e.g., a brief about Semporna repeatedly mentions "巴瑶族")
- Unique site conditions (e.g., "潟湖", "历史街区核心保护区", "山坡台地")
- Explicit design mandates (e.g., "产展销一体", "近零能耗", "BIM协同设计")
- Named cultural/geographic references (e.g., "苏州园林", "良渚文化")
- Unusual functional requirements (e.g., "生产与博物馆功能区分割", "漂浮模块")

These are the project's own words — not category labels.

#### Step B: Search with Those Terms

For each distinctive term, run targeted bilingual web searches that combine the term
with the project's building type and location. The goal is to find: relevant precedents,
applicable design strategies, regulatory frameworks, and scholarly references.

Example: If the brief says "巴瑶族高脚屋", search "Bajau stilt house construction
technique" and "巴瑶族 水上村落 建筑". If it says "近零能耗", search "near-zero
energy resort tropical climate precedent". If it says "城中村有机更新", search
"urban village organic renewal hillside adaptive reuse".

**The search findings drive the emphasis.** If searches for a term yield rich
architectural material, that area gets deep treatment. If searches return sparse
results, scale back and note the limitation in the report.

#### Step C: Present the Adjusted Plan

After searching, tell the user concisely what emerged and how it reshapes the plan:
> "从任务书提取到核心方向：巴瑶族文化转译、近零能耗海上建筑、模块化体系。
> 搜索后：巴瑶族建筑有详实民族志文献和影像（Module 4→深度），
> 近零能耗海上度假村有成熟先例（Module 3→标准），
> 模块化海上酒店案例偏少（Module 5→以全球海上度假村案例替代）。是否调整？"

The user then confirms or overrides before full research begins.

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
- **Tier 2 (API fails):** Use web search for "[city name] [district] 交通 地铁 公交 道路"
  and "[city name] [district] transportation metro road network" to gather accessibility info.
- **Tier 3 (no structured data):** Describe based on city type: CBD (dense transit, walkable),
  new district (metro-oriented, wide roads), suburb (car-dependent), rural (limited transit).
  Always mark Tier 3 data as: "基于城市类型推断，建议人工核实".

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

Climate data has a three-tier degradation path. Always try Tier 1 first.

### Tier 1: Open-Meteo API (preferred)

Call the Open-Meteo Archive API for the project coordinates (replace lat/lon/dates):
```
https://archive-api.open-meteo.com/v1/archive?latitude=X&longitude=Y
&start_date=2014-01-01&end_date=2023-12-31
&monthly=temperature_2m_mean,temperature_2m_max,temperature_2m_min,
precipitation_sum,relative_humidity_2m_mean,
wind_speed_10m_mean,wind_direction_10m_dominant,
sunshine_duration,shortwave_radiation_sum
```
Fetch 10 years of data, aggregate to monthly averages. Include `sunshine_duration` (hours)
and `shortwave_radiation_sum` (MJ/m²) for solar analysis. This is the most accurate source.

### Tier 2: Built-in City Database (fallback)

If the API is unreachable (network error, timeout after 15s, SSL failure), immediately
switch to the built-in climate reference at `references/climate_data.md`. Read that file
and look up the project city by name. If the exact city is present, use its row directly.
If a nearby city with similar latitude and climate zone is present, use it and note:
"气候数据基于[参考城市]多年平均值推断".

The reference covers: all Chinese provincial capitals and major cities, plus key
international destinations (Semporna, Kuala Lumpur, Bangkok, Singapore, Malé, Tokyo, Dubai, Sydney).

### Tier 3: Climate Zone Inference (last resort)

If the city is not in the database, infer from the building climate zone:
- Determine zone from latitude + Köppen classification
- Use the zone-level design strategy summary at the bottom of `references/climate_data.md`
- Describe qualitative climate characteristics (e.g., "热带雨林气候，全年高温高湿")
- Mark all data as: "基于气候分区推断，建议人工核实具体气象数据"

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

## Step 3 — Zoning & Massing (Volume Control)

This is a deterministic calculation. From the brief's metrics, compute:

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
this as "基于通用设计知识推断" (inferred from general design knowledge).

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

## Output: The Report

Write the final report as a `.docx` file named `<Project-Name>_前期调研报告.docx`.

### Report Structure (Required Sections)

```
# [项目名称] 建筑前期调研报告
## 0. 项目概况 (Project Overview)
   - 提取自任务书的核心指标表
## 1. 场地区位与周边分析 (Site & Context)
   - 1.1 区位与交通可达性
   - 1.2 地域文脉与建筑风貌
   - 1.3 场地现状与周边建筑
   - 1.4 交通流线分析
## 2. 气候与环境分析 (Climate & Environment)
   - 2.1 温湿度与降水
   - 2.2 日照与风向 (含风玫瑰图)
   - 2.3 噪音分析与设计策略
## 3. 法规与体量推演 (Zoning & Massing)
   - 3.1 规划指标解读
   - 3.2 最大可建体量计算
   - 3.3 面积平衡表
## 4. 人文与人群需求 (Culture & Users)
   - 4.1 历史文脉叙事
   - 4.2 使用者画像与行为模式
   - 4.3 调研问卷 (附录)
## 5. 案例对标研究 (Precedent Studies)
   - 5.1 国内外典型案例
   - 5.2 周边同类项目
   - 5.3 案例对比评估矩阵
## 6. 综合结论与设计建议 (Conclusions & Recommendations)
```

### Formatting Rules

Read `references/report_template.md` for the complete formatting specification before
generating the report. That file defines precise font sizes, colors, heading hierarchy,
table styling, image handling, page setup, and data flag conventions. Follow it exactly.

Key principles (detailed spec in the reference file):
- Use python-docx for all document creation.
- Title page with project name (22pt bold dark blue) + subtitle (16pt).
- Heading 1 (16pt bold), Heading 2 (13pt bold), Heading 3 (11pt bold).
- Body text 10.5pt, 1.5× line spacing, justified alignment.
- Tables: dark blue header row with white text, alternating row shading.
- Images: embed inline with numbered captions; max 15cm width.
- Data flags: ⚠ (inferred), 待补充 (missing), 基于规范推断 (standards-based).
- Page size: A4, margins 2.54cm all sides.

---

## Section 6 Requirements — Design Recommendations

Section 6 (综合结论与设计建议) is the most actionable part of the report. Do NOT treat it
as a lightweight summary. It must be as detailed as the research sections and directly
grounded in the findings from Modules 1–5.

### 6.1 Core Conclusions (5–8 items)

Each conclusion must:
- State a finding from the research, not a generic platitude
- Reference specific data or precedents from earlier sections
- Be 2–4 sentences long, explaining WHY this matters for design

Bad: "注重可持续发展"
Good: "基于仙本那年均日照7.5h/天的数据（Section 2.2），光伏系统可满足80%以上能耗需求。参考Soneva Secret的90%清洁能源先例（Section 5.1），建议将浮式光伏阵列与储能系统作为酒店能源策略的核心，而非仅作为补充。"

### 6.2 Design Strategies (10–15 items)

This is the core deliverable. Each strategy must:
- Be numbered and have a clear title
- Include 2–4 sentences explaining the rationale (WHY) and implementation approach (HOW)
- Reference specific precedents, climate data, or site conditions from earlier sections
- Be actionable — a designer reading this should know what to do next
- Prioritize strategies that respond to the project's unique constraints (keywords from Step 0)

Format each strategy as:
```
N. 【策略标题】
为什么要这样做（1-2句基于调研数据的理由）。
具体怎么做（1-2句实施建议）。参考：[案例/数据来源]。
```

### 6.3 Risk Assessment

Table format, but each risk entry should include specific mitigation steps, not generic advice.

### 6.4 Next Steps

Actionable, sequenced, with clear ownership (what the designer does vs. what requires consultants).

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
- **Concept stage:** Modules 0, 1, 2, 5 at standard; 3, 4 at light
- **Feasibility study:** All modules at standard
- **Pre-construction:** Modules 0, 1, 3 at deep; rest at standard

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