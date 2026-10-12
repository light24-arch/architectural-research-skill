# 建筑调研技能：文件维护地图

此文件只供维护者查看目录职责，执行入口为 SKILL.md；不另设研究规则。

```text
architectural-research/
├── SKILL.md                         入口：范围、流程、按需加载与交付
├── README.md                        维护地图（本文件）
├── references/
│   ├── task-modes.md                模式完成标准
│   ├── project-types.md             三类项目的侧重点、深度与转译
│   ├── evidence-quality.md          证据与引用标准
│   ├── research-methods.md          按问题读取的研究方法
│   ├── research-maintenance.md      定位纠正、筛选与入库的跨笔记同步
│   ├── precedent-matching.md        案例匹配、迁移与深读程度
│   ├── design-directions.md         备选设计方向、重点问题与分析计划
│   ├── climate_data.md              待核实气候线索
│   ├── report-structure.md          九模块、动态数量、策略八要素
│   ├── markdown-output-guide.md     Markdown 组织与渲染
│   ├── html-output-guide.md         HTML 样式与交互
│   ├── report_template.md           Word 格式（保留旧名）
│   └── feishu-output-guide.md       飞书渲染与可用连接导入
├── scripts/
│   └── check_library.py             案例数、已有编号与本地链接的只读检查
└── assets/
    └── research-book-template.html 新完整 HTML 报告的占位骨架
```

## 修改时只更新对应规则的维护位置

| 要修改什么 | 修改文件 | 同步检查 |
|---|---|---|
| 触发、范围、输出选择、加载关系 | SKILL.md | 参考入口和格式选择 |
| 各模式完成条件 | task-modes.md | 不扩大其他模式 |
| 三类项目侧重点、阶段深度与交叉用途 | project-types.md | 主文件入口、研究方法、案例、方向和报告位置 |
| 来源、事实/推断、冲突 | evidence-quality.md | 其他文件只引用，不复制规则 |
| 场地/气候/指标等具体方法 | research-methods.md | 图像、计算、工具边界 |
| 定位纠正、用户筛选、候选转正式 | research-maintenance.md | 当前文件、影响范围、数量与状态 |
| 案例匹配和详细研究 | precedent-matching.md | 匹配维度、迁移与实际深读程度 |
| Markdown库机械检查 | scripts/check_library.py | 只读、排除配置、链接及已有编号；不做研究判断 |
| 从调研到备选方向及后续分析 | design-directions.md | 主文件入口、07/09 位置及档案关联 |
| 报告编号、数量、策略结构 | report-structure.md | HTML 骨架标题和目录 |
| 某格式样式与交互 | 对应输出指南 | 只影响该格式；HTML 同步模板 |
| 气候数据 | climate_data.md | 逐项来源、统计期与状态 |

## 模板维护

assets 只放会复制到成果中的文件，references 放指令和方法；模板不作为已核验案例。
模板中的九个标题/目录来自 report-structure.md；不将策略数量或示例数据写死。
用模板生成成果前替换项目、日期、章节和来源占位；缺口按证据标准注明。
引用路径变更时检查调用与文内链接；没有实际脚本就不创建空 scripts 目录或保留虚假调用命令。
不在模板和格式指南复制完整策略要素，避免两处改动不同步。

本次撤回误加的围护结构指南与触发，保留此前一致性、证据质量和气候/计算边界改进。

连续指令的对象定位规则维护在 SKILL.md；经典大师、近年同类型、其他专项的检索偏好维护在 precedent-matching.md。
研究方法和输出指南只引用检索顺序，不重复定义数量、时期和经典判定标准。

项目类型确认、主文档选择和主文档交付后的 HTML 询问流程维护在 SKILL.md。
课程设计、实际项目、竞赛作品的具体侧重点唯一维护在 project-types.md；其他文件只接入，不复制整套要求。
项目类型与研究任务模式分别记录；任务书校正类型初步排序，交叉用途组合有关要求。
主文档由用户选择 Obsidian、飞书文档或 DOCX，没有默认形式；HTML 演示是主文档交付后的可选阶段。
Obsidian 的详细关联形式只在用户选择该形式时使用，其分区、文件粒度、字段及附件组织仍待讨论。

2026-10-12维护补充：从真实定位更正、筛选后文件变化与蒙西入库提炼通用方法，未把苏州地名、项目编号或9案总数写成全局规则。
语义场景输入维护在evals/evals.json；它们不是已经执行通过的独立agent评测。
