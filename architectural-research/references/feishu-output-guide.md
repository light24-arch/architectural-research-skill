# 飞书文档输出指南

用户选择飞书主文档时加载。确认真实文档已创建、返回链接后，按 SKILL.md 询问 HTML 演示需求；
连接不可用时不宣称已交付飞书文档，保留草稿并说明其他可用选项。

规则来源：任务范围遵循 [SKILL.md](../SKILL.md)；章节、数量和策略结构遵循 [report-structure.md](report-structure.md)；证据遵循 [evidence-quality.md](evidence-quality.md)。排版不改变研究范围。
> 当输出阶段用户选择「输出到飞书文档」（或直接说「输出飞书 / Feishu」）时启用。
> 把最终研究报告渲染成**干净线性 Markdown**，用 `lark-cli docs +create --doc-format markdown`
> 一次性导入为飞书云文档，返回链接交付给用户。

**为什么用 Markdown 而非 XML**：lark-doc 默认 XML（表达能力更强），但本报告篇幅长、
目标是「干净线性、易编辑」，Markdown 的标题 / 列表 / GFM 表格已完全够用，且 agent 生成
Markdown 远比手写冗长 XML 稳健。这是对 lark-doc 默认约定的有意偏离。

---

## Step 0 — 认证（前置）

先确认环境实际存在并支持此版本的 lark-cli（或可用飞书连接），再确认用户身份已登录；不可用则保留本地 Markdown，不能直接调用不存在的工具。以下命令是可用时的示例：

```bash
lark-cli auth status
```

- 若用户身份显示 missing / expired（refresh token 过期），先重登：

```bash
lark-cli auth login --domain docs
```

（设备码授权，交互式，跟随提示完成。）**未重登就创建，文档会落到应用（bot）空间**，不是用户自己的「我的空间」。

---

## Step 1 — 生成干净线性 Markdown

完整研究沿用 report-structure.md「完整报告九模块」；专题、案例库和补充沿用各自范围，渲染为 Markdown。
映射规则见下表。

### 内容 → Markdown 映射

| 报告内容 | 飞书 Markdown |
|---|---|
| 封面（项目名 + 元信息） | `# 项目名 — 建筑前期研究报告` + `>` 引用块放日期 / 来源 |
| 模块（01–09） | `## NN 模块名` |
| 小节 | `### X.Y 小节名` |
| KPI 数字行 | 2 列表格（`指标 \| 数值`） |
| 卡片网格（信息 / 待补充 / 人群画像） | 无序列表 `-` |
| 链 A→B→C（文化转译 / 挑战→机会） | 编号列表 `1. A → B → C` |
| 对比表 / 面积表 / 风险表 | GFM 表格 |
| 策略卡（8 要素） | `### 策略名` + 带标签无序列表（`- 设计问题：…`） |
| 挑战卡 + 标签 | `###` + 段落（`问题标签：场地/气候/…`） |
| 脚注 `注：…` | 段落，前缀 `注：` |
| 图片 + 图注 | `![图 X：…](url)` + 图注段落（仅 URL 图） |

### 转义规则（务必遵守）

- 表格 cell 内的 `|` 要写成 `\|`。
- 行首的 `#`、`-`、`+`、`>` 若为字面量，需加 `\` 前缀（避免被解析成标题 / 列表 / 引用）。
- 字面量 `<` 写成 `\<`（避免被当作 XML 标签解析）。
- 完整规则见 lark-doc 的 `lark-doc-md.md`。

---

## Step 2 — 导入飞书文档

把报告内容写成 cwd 下的临时 Markdown 文件（`@file` 只接受 cwd 相对路径，绝对路径会报
`unsafe file path`）：

```bash
# 假设内容已写到 ./_feishu_report.md
lark-cli docs +create \
  --doc-format markdown \
  --title "<项目名>_前期研究报告" \
  --content @./_feishu_report.md \
  --as user
```

返回 JSON 中取：

- `data.document.url` —— 文档链接，**作为最终交付给用户**。
- `data.document.document_id` —— 文档 token，供后续 `docs +update` 追加 / 修改。

---

## Step 3 — 交付与清理

1. 把 `data.document.url` 作为最终链接交给用户。
2. 删除临时文件 `rm ./_feishu_report.md`。

---

## 后续管理（可选提示，不在本次实现范围）

- 追加章节：`lark-cli docs +update --doc <doc_id> --command append --content @./xxx.md`
- 精确修改：`lark-cli docs +update --doc <doc_id> --command str_replace --pattern ... --content ...`
- 详见 lark-doc 的 `lark-doc-update.md`。

---

## 图片处理（v1 限制）

- 仅支持网络 URL 图片：`![图注](https://...)`（markdown 导入时自动下载）。
- 本地图片暂跳过，并在原文标注「（待手动插入图片）」；需上传时用 lark-drive（列为后续扩展）。
