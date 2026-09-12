# 正式发表状态检查与回填例程 · 提示词

> 判定标准见 [PUBLISHED_CRITERIA.md](./PUBLISHED_CRITERIA.md)，
> 数据、发布及调度部署见 [OPERATIONS.md](./OPERATIONS.md)。
> 仓库提示词变化不代表外部定时任务已更新。

你负责检查已有 AI-for-PDE 论文是否出现正式接收或发表版本，生成中文状态报告。

## 1. 选择对象

读取 `CLAUDE.md`、以上规范、`metadata/papers.jsonl` 与运行记录，先执行
`python scripts/papertrack.py check`。缺表或校验失败先处理，不创建空主表继续。
运行标识为 `status-YYYY-MM-DD`（UTC）。

检查已有 arXiv 论文中状态未确认、已接收未发表、已发表但缺字段、上次失败或存在冲突者。
通常距上次成功检查至少 14 天再查，失败不刷新成功检查时间。冲突、失败、高相关、长期未查者
优先，最多 100 篇，记录选择与截断规则。读取统一论文表的 `assessments`，按来源和
`score_scheme` / 历史 schema 识别评分；表中没有顶层 `score_total`。只在同一方案内用总分排序，
缺方案或不可比分数不推断换算。状态检查不重新评分，也不把旧的单个总分复制为新事件评分。
不能只查旧 bootstrap 表。

## 2. 查证身份与状态

arXiv 的 DOI、journal-ref、comments 作为线索，继续核对出版商、正式会议页面和索引服务。
arXiv 元数据变化不一定伴随版本号变化。保存真实查询、时间、候选与证据；未检索不能写“未发现”。

身份匹配与正式状态独立判断：明确关联同一 arXiv ID、且标题作者兼容可确认身份；
标题相似仍须核对作者、摘要和时间。DOI 核对落地页，区分正式 DOI 与预印本自身 DOI。
改标题、增删作者或扩展版保留说明；多个候选或 DOI/venue/日期冲突写待确认。

可保留有依据的 `status_confidence`，但它是规则判断，不是校准概率。
高数字不能绕过身份冲突或正式证据要求。索引匹配本身不能证明正式发表。

## 3. 写入事件

`accepted` 不写成 `published`，未发表日期填 `null`。按 OPERATIONS.md 写入
`metadata/inbox/*.jsonl`，支持 `discovery / assessment / publication / correction`：

- 新确认状态：`publication`，写已核实字段及正式页面证据。
- 成功检查无变化：`assessment`，显式记录本次 `last_status_check`（UTC ISO 时间）、来源、说明，不降级原状态。
- 检索失败：写运行错误与已完成部分，不刷新成功检查时间，不伪造阴性结果。
- 待确认：`assessment` 的附加字段保存候选与冲突，不把候选 DOI/venue 写成当前确认值。
- 明确更正：`correction`，保存证据、被替代事件和原因，原记录保留。

缺失值保持 `null`，旧值无新证据时保留；不补造历史检查时间或运行次数。
生成表和迁移快照禁止手写覆盖。

## 4. 报告与发布

写 `digests/status_updates/arxiv-status-update-YYYYMMDD.md`，记录候选/实际检查、成功/失败/
待确认数，分别统计正式接收、正式发表、更正与无变化。每项给原/新状态、官方链接、匹配依据、
检查时间、研究关联；列冲突、来源异常、未解决字段及运行记录链接。

保存 `metadata/runs/*.json` 和 `run_log_status_update.md` 本期摘要；没有历史报告时从本次开始，
不以当前状态重建过去运行。运行 `python scripts/papertrack.py build`、
`python scripts/papertrack.py check`、`git diff --check`，按 OPERATIONS.md 发布并验证远程 main。

最终回复包含报告路径、实际检查及成功/失败数、接收/发表更新、冲突与更正、无变化数、
校验与发布状态。部分失败说明覆盖局限，本地完成但未发布不能报告 GitHub 已更新。
