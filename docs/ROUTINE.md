# 日报路由例程 · 提示词（PDE 基座大模型）

> 本文件是仓库内提示词规范副本；外部调度器是否已加载本版需独立核验。
> 方向、关键词和评分以 [TAXONOMY.md](./TAXONOMY.md) 为准；
> 数据、发布与调度器部署以 [OPERATIONS.md](./OPERATIONS.md) 为准。

你负责 PDE 基座大模型与 AI 求解 PDE 的论文追踪，输出中文日报。

## 1. 准备与窗口

读取 `CLAUDE.md`、以上规范、`docs/LANDMARK_MODELS.md`、`metadata/papers.jsonl`、
`seen_papers.txt` 和 `metadata/runs/*.json`，运行 `python scripts/papertrack.py check`。
区分已有论文、已入选论文与此前排除的候选；排除不代表以后不能重评。

日期统一 UTC，逻辑标识为 `daily-YYYY-MM-DD`，重复执行先检查对应产物。
用 `python scripts/papertrack.py coverage --task daily --at <UTC-ISO时间> --overlap-hours 48`
计算上次成功覆盖位置加 48 小时重叠的窗口。无成功记录时从过去 48 小时启动，明确为起始窗口，
不能声称已覆盖全部历史。来源失败或覆盖不足时标为 degraded/failed，不推进成功位置。
历史补查单列窗口。

## 2. 检索与证据

按 TAXONOMY.md 的 A/B/C/D 四方向执行查询。优先使用能返回可靠 ID、时间和分页信息的来源，
WebSearch 作补充。来源可用性以本次请求为准，不沿用历史 403 等结论。

在 `metadata/runs/*.json` 保存实际查询词、来源、窗口、状态、错误及候选清单；
计数从清单推导。完整来源总量未知时写“实际收集 N 篇，总量未知”，不估写“约 80 篇”
或“全部关键词已覆盖”。候选保存首次提交、版本更新、发现时间与筛选理由，未知日期填 `null`。

按规范化 arXiv ID、DOI 和已关联身份去重。版本、正式状态和更正单列“已有论文更新”，
不计入新增；同期分支或最新 main 已入选的论文重新计算新增。排除候选仍保留在记录里。

## 3. 筛选与摘要

按 TAXONOMY.md 保存评分分项和理由，核心阈值仍为总分 ≥ 7，零篇正常。
另记录研究用途与核验程度。没有多物理预训练不能直接否定几何泛化、失败模式或评测工作的价值。
未达阈值但有具体参考价值者列附录，不混入核心新增。

每篇包括标题、链接、已确认作者/机构、`A/B/C/D | arXiv 分类`、核心贡献、方法与数据、
研究用途、局限、评分分项、核验程度。区分作者声称与核实结果；重点论文填写 TAXONOMY.md
的研究比较字段，未知填 `null`。

## 4. 入库、产物与发布

1. 按 OPERATIONS.md 向 `metadata/inbox/*.jsonl` 追加入选与更新事件，先关联现有论文，
   保留证据，不手改生成表和去重表。
2. 写 `digests/PDE-FM-日报-YYYYMMDD.md`：日期/运行标识、覆盖窗口与计数、A/B/C/D 内容、
   已有论文更新、未入选附录、来源异常、运行记录链接。窗口内新增与历史补录分别统计。
   零篇时仍说明覆盖；检索降级不能写“功能正常”。
3. 保存结构化运行记录，并在 `run_log.md` 记录本次有证据的摘要。历史不重写、不补造查询；
   重试关联同一逻辑运行，不增加第二个成功日报。
4. 执行 `python scripts/papertrack.py build`、`python scripts/papertrack.py check` 和
   `git diff --check`。索引由生成流程维护。里程碑表只增加有证据的重点论文。
5. 按 OPERATIONS.md 明确文件清单发布，核验远程 main；不复制旧版全目录暂存与 rebase 重试命令。

最终回复包含日报路径、实际窗口/候选数、新增与历史补录、已有论文更新、来源异常、
校验结果、提交与远程 main 验证结果。零新增、检索失败、已生成但未发布分别表述。
