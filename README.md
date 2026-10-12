# architectural-research

面向建筑学学生、建筑师及设计团队的建筑前期研究 skill。围绕任务书、场地资料和已有案例，建立“证据—问题—设计机会—空间动作”的研究关系。

支持完整前期调研、专题研究、案例库建设和已有研究补充。按用户目标确定范围；主文档形式由用户选择，HTML演示按需另行制作。

## 开始使用

技能包位于[`architectural-research/`](architectural-research/)，执行入口是[`SKILL.md`](architectural-research/SKILL.md)。将整个技能目录放入所用工具支持的技能目录，再提供研究要求、任务书及已有资料。

示例请求：

- “这是课程设计任务书，研究两个候选场地的周边条件与痛点，输出Markdown。”
- “参考已有案例找类似社区更新项目；先给候选信息，我再决定是否入库。”
- “详细研究这个菜场案例，并加入现有案例库。”
- “场地位置更正了，请修改受影响的结论、来源和设计方向。”
- “我筛选了案例库，结合最新调研完善保留案例的关联。”

新研究先确认课程设计、实际项目或竞赛用途。已明确的用途、范围和格式沿用，不重复初始化。

## 工作范围

| 范围 | 主要成果 |
| --- | --- |
| 完整前期调研 | 与任务书匹配的研究、问题、备选方向、空间策略及验证计划 |
| 专题研究 | 围绕指定场地、交通、人群、文化或环境问题的证据与空间启示 |
| 案例库 | 有来源、匹配依据、空间动作和迁移限制的单案、索引及比较 |
| 研究补充 | 在原结构中增量修改，修正受影响结论并同步相关链接 |

完整研究可使用九模块组织；专题、单案例和局部修改不强制套用整套模板或固定案例数量。

## 更新后的研究方法

- **先核准对象：** 地图地标、街巷及邻接关系优先于相似简称；定位与正式红线、产权及当前用途分开。
- **更正传播到结论：** 错误前提影响资源、人群、问题、方向和路线时，修订相应内容，保留有效研究。
- **维护真实案例清单：** 用户筛选后盘点当前文件，重算数量、修订链接；不擅自恢复移除项目。
- **候选与入库分开：** 初筛不加入正式库；用户选案后完成详案和导航同步，其余候选继续待选。
- **说明实际深读程度：** 区分文字机制、已查看图像、具尺寸平剖面比较及使用评估；图纸不可读时标缺口，不编尺寸或反复同路重试。
- **转成具体空间比较：** 本地问题、案例动作、迁移条件、比较图纸和改变选择的证据相互对应，兼顾日常、后勤与维护。
- **区分历史与当前：** 计划不等于实施；分期完成不等于整体完成；平台路线与个人行程不等于当前实测客流。

## 证据与输出

事实、推断与待核实信息分别表达。来源记录主体、日期、定位、可读程度及适用范围。设计目标不当成已验证效果，同一稿件转载不当独立证据。

主文档可选择Obsidian／Markdown、DOCX或有可用连接的飞书文档。Markdown沿用用户组织习惯，不为每个案例建立子文件夹。HTML是可选演示，使用黑白编辑式布局，不是默认交付。

图像、正文、排版和外部写入依赖实际工具能力。模板中的图像、数字和项目名是占位，不作为研究成果。

## 目录与按需读取

| 位置 | 职责 |
| --- | --- |
| [SKILL.md](architectural-research/SKILL.md) | 入口、范围、流程与按需路由 |
| [维护地图](architectural-research/README.md) | 规则维护位置 |
| [research-maintenance.md](architectural-research/references/research-maintenance.md) | 定位纠正、筛选、入库及跨笔记同步 |
| [precedent-matching.md](architectural-research/references/precedent-matching.md) | 案例筛选、迁移及深读程度 |
| [evidence-quality.md](architectural-research/references/evidence-quality.md) | 来源、口径、历史与平台信息 |
| `references/`其他文件 | 项目用途、研究方法、设计方向、报告组织及对应格式指南 |
| [check_library.py](architectural-research/scripts/check_library.py) | 只读案例库机械检查 |
| [evals.json](architectural-research/evals/evals.json) | 十个行为场景输入 |
| [HTML骨架](architectural-research/assets/research-book-template.html) | 可选演示模板 |

参考文件按当前任务加载，不要求一次读取全部资料。

## 只读案例库检查

工具使用Python标准库，无额外依赖：

```text
python architectural-research/scripts/check_library.py --library "案例目录" --project-root "项目目录"
```

检查可识别数量、已有编号重复和基本本地链接。默认排除四份已知导航文档与显式未入库候选；其他结构可用`--exclude 文件名`补充排除项。

工具不改文档、不访问外网，不验证来源内容、图纸质量或所有Markdown插件语法。默认分类需先匹配目标库。

本轮已执行六组工具回归、一个实际案例库检查及技能元信息与参考链接检查。`evals/evals.json`是后续语义评测输入，尚未声称全部由独立agent执行。

## English overview

A skill for architectural pre-design research, focused site studies, precedent libraries and ongoing research updates. It grounds design questions in briefs, site evidence and readable references, separating facts, interpretations and unresolved conditions.

Load only the references relevant to the request. Delivery follows the user's chosen Markdown, Word or connected document format; HTML is optional.

Recent improvements cover site identification, correction propagation, current library inventories, candidate-to-library transitions, drawing-readability boundaries and concrete design transfer. The included read-only Python checker validates basic counts, existing IDs and local links; it does not validate research quality or operating outcomes.
