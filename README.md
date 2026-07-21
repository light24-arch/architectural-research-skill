# architectural-research v2.0

面向建筑学学生、建筑师及设计团队的 **建筑前期研究助手**（Claude Code Skill）。
输入任务书，输出一份结构化 HTML 建筑研究册——从"信息理解"到"设计策略"的完整推导链。

> **极简。编辑感。建筑学。**

---

## 快速开始

1. 在 Claude Code 中安装此 Skill
2. 提供设计任务书（`.docx` / `.pdf`），例如：`"E:\建筑\毕设\20251121海上度假酒店设计任务书.docx"`
3. Skill 自动生成单文件 HTML 研究册，浏览器直接打开，Ctrl+P 导出 A4 PDF

## 核心流程

```
设计任务书 (.docx / .pdf)
        ↓
  研究分析代理（AI）
        ↓
  结构化 HTML 研究册
        ↓
  5–8 条设计策略
```

不是资料整理，而是**设计推导引擎**。每个章节回答一个推动设计向前的问题。

## 报告结构（9 模块）

| # | 模块 | 核心内容 |
|---|------|---------|
| 01 | 项目概况 | 核心指标大字报、硬性约束清单、信息状态声明（已识别 / 推断 / 待补充） |
| 02 | 背景分析 | 区域语境、建筑类型背景、项目定位逻辑 |
| 03 | 场地与环境 | 气候 KPI → 设计策略推导、自然灾害风险评估 |
| 04 | 人群与文化 | 四类用户画像卡片、地域文化 → 空间转译链 |
| 05 | 设计挑战 | 5 个核心矛盾，每张卡片带问题标签（可点击跳转至 M06 对应机会） |
| 06 | 设计机会 | Challenge → Opportunity 链，带锚点 ID 供 M05 跳转 |
| 07 | 策略探索 | 6 条策略 × 8 要素（设计问题 → 依据 → 概念 → 空间动作 → 参考案例） |
| 08 | 案例对标 | 6 个经验证案例，含可点击 URL |
| 09 | 结论与建议 | 核心发现、风险评估、下一步行动清单 |

## 视觉系统

**黑白 Editorial** — 纯黑白色调，无装饰色块，无渐变。

```css
:root {
  --color-text: #111;
  --color-bg: #fff;
  --color-border: #e5e5e5;
  --color-card: #f9f9f9;
}
```

- 固定左侧目录栏（180px），IntersectionObserver 追踪当前阅读位置
- 圆角系统（6px / 10px / 16px）
- 中文字体排版：行高 1.8、无 letter-spacing、不使用 ch 单位
- 虚线分隔、卡片组件库
- 窄屏适配：≤860px 目录折叠为汉堡菜单
- A4 打印样式（每模块前分页）
- **不在 HTML 中展示 Mermaid 推导图或 AI 推理过程**——只呈现建筑研究结果

## 主要功能

- **单文件 HTML** — 浏览器直接打开，无需服务器
- **Ctrl+P 导出 PDF** — A4 优化打印样式表
- **挑战 → 机会跳转链接** — 点击挑战卡片底部链接直接跳转到对应设计机会
- **案例 URL 验证** — 仅引用 ArchDaily / Dezeen / Architizer / 谷德 / ArchiPosition 五个站点
- **可替换图片** — `<img>` 标签 + SVG 占位符，修改 `src` 即可替换
- **键盘导航** — ↑↓ Home End
- **双语搜索** — 每个模块中英文双源搜索

## 案例搜索优先级

进行建筑案例搜索时，**优先搜索以下五个站点**：

| 优先级 | 站点 | 定位 |
|--------|------|------|
| 1 | ArchDaily | 全球最大建筑数据库 |
| 2 | Dezeen | 精选高质量项目 + 设计策略访谈 |
| 3 | Architizer | 获奖项目，可筛选类型与气候区 |
| 4 | 谷德设计网 | 中文最佳，亚洲项目深度覆盖 |
| 5 | ArchiPosition | 中国青年建筑师 + 新兴实践 |

URL 必须来自上述五站之一或事务所官方页面。禁止引用聚合站（Pinterest、Reddit、Wikipedia）。

## 文件结构

```
architectural-research/
├── SKILL.md                            # Skill 核心定义 & HTML 渲染规则（11 节）
├── README.md                           # 本文件
├── assets/
│   └── research-book-template.html     # HTML 骨架 & 完整组件库
├── references/
│   ├── html-output-guide.md            # 视觉与技术规范
│   ├── report_template.md              # .docx 格式规范（保留）
│   └── climate_data.md                 # 内置气候参考数据库
└── evals/
    └── evals.json                      # 评估用例
```

## 示例输出

测试案例：**仙本那海上度假酒店**（马来西亚沙巴州仙本那东侧岛礁）

- 100 间模块化客房，≤3 层
- 对标 GB/T 51350-2019 近零能耗建筑标准
- 参照马来巴瑶族高脚屋文化与珊瑚石肌理
- 建于海面之上，不与陆地接壤

## 环境依赖

- Claude Code（Skill 支持）
- Python：`python-docx`（提取 .docx 任务书）、`markitdown`（提取 .pdf）
- 网络：案例搜索、气候数据 API

## 设计方法论

基于建筑设计推导链：项目理解 → 背景分析 → 场地研究 → 人群文化 → 功能推演 → 问题提炼 → 设计机会 → 策略探索 → 案例对标 → 结论。

视觉系统受瑞士 Editorial 设计传统启发，为建筑研究报告场景适配。

---

# architectural-research v2.0

A Claude Code skill for architectural pre-design research. Takes a design brief, outputs a structured HTML research book — tracing the full design derivation chain from understanding to strategy.

> **Minimal, Editorial, Architectural.**

## Quick Start

1. Install the skill in Claude Code
2. Provide a design brief (`.docx` / `.pdf`), e.g.: `"E:\建筑\毕设\20251121海上度假酒店设计任务书.docx"`
3. The skill auto-generates a single-file HTML research book — open in any browser, Ctrl+P to A4 PDF

## Core Workflow

```
Design Brief (.docx / .pdf)
        ↓
  Research Analysis Agent (AI)
        ↓
  Structured HTML Research Book
        ↓
  5–8 Design Strategies
```

Not a data dump — a **design derivation engine**. Every section answers a question that pushes the design forward.

## Report Structure (9 Modules)

| # | Module | Content |
|---|--------|---------|
| 01 | Project Overview | KPI hero row, hard constraints table, info status cards (known / inferred / missing) |
| 02 | Context Analysis | Regional context, building type history, project positioning rationale |
| 03 | Site & Environment | Climate KPIs → design strategy cards, natural disaster risk assessment table |
| 04 | User & Culture | 4 persona cards, vernacular culture → spatial translation chains |
| 05 | Design Challenges | 5 core contradictions with problem tags (click to jump to M06 opportunities) |
| 06 | Design Opportunities | Challenge → Opportunity chains with anchor IDs for M05 cross-navigation |
| 07 | Strategy Exploration | 6 strategies × 8 elements (Design Question → Evidence → Concept → Spatial Operation → Reference Cases) |
| 08 | Reference Cases | 6 verified precedent cases with clickable URLs |
| 09 | Conclusion | Key findings, risk assessment, next-step action plan |

## Design System

**Black & white editorial** — pure black-on-white, no accent colors, no gradients.

```css
:root {
  --color-text: #111;
  --color-bg: #fff;
  --color-border: #e5e5e5;
  --color-card: #f9f9f9;
}
```

- Fixed left sidebar TOC (180px) with IntersectionObserver active tracking
- Rounded corner system (`6px` / `10px` / `16px`)
- CJK typography: `line-height: 1.8`, no `letter-spacing`, no `ch` units
- Dashed dividers, card-based component library
- Responsive: sidebar collapses to hamburger at ≤860px
- A4 print stylesheet with page breaks before each module
- **No Mermaid diagrams or AI reasoning displayed** — architectural results only

## Key Features

- **Single-file HTML** — opens in any browser, no server needed
- **Ctrl+P to PDF** — A4-optimized print stylesheet
- **Challenge → Opportunity jump links** — click card links to navigate between M05 and M06
- **Verified case URLs** — ArchDaily / Dezeen / Architizer / 谷德 / ArchiPosition only
- **Replaceable images** — `<img>` tags with SVG placeholders, edit `src` to replace
- **Keyboard navigation** — ↑↓ Home End
- **Bilingual search** — Chinese + English sources for every module

## Case Search Priority

When searching for architectural precedents, **search these five sites first**:

| Priority | Site | Strengths |
|----------|------|-----------|
| 1 | ArchDaily | Largest global architecture database |
| 2 | Dezeen | Curated projects, design strategy interviews |
| 3 | Architizer | Award-winning projects, filter by typology/climate |
| 4 | 谷德设计网 | Best Chinese-language source, Asian projects in depth |
| 5 | ArchiPosition | Emerging Chinese architects & practices |

URLs must come from one of these five sites or an official firm page. Never cite aggregator sites (Pinterest, Reddit, Wikipedia).

## File Structure

```
architectural-research/
├── SKILL.md                            # Core skill definition & 11-section HTML rendering spec
├── README.md                           # This file
├── assets/
│   └── research-book-template.html     # HTML skeleton with full component library
├── references/
│   ├── html-output-guide.md            # Visual & technical specification
│   ├── report_template.md              # .docx formatting spec (legacy, retained)
│   └── climate_data.md                 # Built-in climate reference database
└── evals/
    └── evals.json                      # Evaluation cases
```

## Example Output

Test case: **Semporna Maritime Resort Hotel** (East reef, Semporna, Sabah, Malaysia)

- 100 modular guest rooms, ≤3 floors
- Near-zero energy target (GB/T 51350-2019)
- Bajau vernacular culture reference (stilt houses, coral stone texture)
- Built on sea surface, not connected to land

## Requirements

- Claude Code with skill support
- Python: `python-docx` (for .docx extraction), `markitdown` (for .pdf)
- Internet access for web search (case studies, climate data)

## Credits

Built on the architectural design derivation chain: Project Understanding → Context → Site → User & Culture → Challenges → Opportunities → Strategy Exploration → Reference Cases → Conclusion.

Design system inspired by Swiss editorial traditions, adapted for the architectural research book format.
