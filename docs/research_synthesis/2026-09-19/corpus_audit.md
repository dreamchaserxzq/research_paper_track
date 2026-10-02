# 全量语料审计与知识图谱边界

快照日期：2026-09-19；源代码/语料 HEAD：`428741f55fe2301ea7ca3029fedc3e913b07b2cc`。

本次完整读取主表 **454 个身份**、**1016 条来源记录**与 **144 份本地 Markdown 报告**；逐字节 SHA-256 覆盖 217 个输入文件。这里的“全量”指本地登记与报告文本，不是全量论文正文精读或实验复现。

远程引用由主任务统一 fetch。远程未合并分支另有 2026-09-16 日报（0 篇核心入选），其原文与远程同步证据由同目录 remote_20260916_digest.txt / remote_sync.json 保存；该分支候选不并入主表与本图。

## 身份、阅读与内容覆盖

| 项目 | 数量 |
|---|---:|
| 主表身份 | 454 |
| arXiv / DOI / unresolved | {'arxiv': 397, 'doi': 52, 'unresolved': 5} |
| 历史阅读状态 | {'null': 449, 'abstract_checked': 5} |
| 核验标记 | {'legacy_unverified': 444, 'conflict_pending': 5, 'source_checked': 5} |
| 本地报告类别 | {'pde_fm_daily': 58, 'archive_summary': 2, 'historical_daily': 68, 'published_weekly': 16} |
| 冲突字段 / 涉及身份 | 8 / 5 |
| 近似标题重复候选（未合并） | 2 |

报告范围：现行PDE-FM日报58份（2026-07-23至2026-09-19）；归档旧主题日报68份（2026-04-19至2026-07-22）；正式发表周报16份（归档W21–W30共10份，现行W30–W35共6份，W30有两个路径）；归档README/历史摘要2份。目录日期跨度不表示逐日无缺口。

| 字段 | 有记录 | 缺失 |
|---|---:|---:|
| title | 451 | 3 |
| title_zh_summary | 143 | 311 |
| abstract | 122 | 332 |
| method_summary | 344 | 110 |
| contribution_summary | 344 | 110 |
| research_relation | 88 | 366 |
| representation | 0 | 454 |
| conditioning | 0 | 454 |
| pretraining | 0 | 454 |
| training_pdes | 7 | 447 |
| evaluation_pdes | 24 | 430 |
| generalization_axes | 27 | 427 |
| evaluation | 0 | 454 |
| limitations | 0 | 454 |

缺失标题与描述的身份：`arxiv:2605.15179`, `arxiv:2606.14913`, `arxiv:2606.17733`。仅 seen 记录不能提供论文内容，未补写虚构摘要。

## 分类与年代

当前日报方向仅使用 daily_directions（已按现行规则保留）：{'A': 46, 'C': 34, 'D': 25, 'B': 11}；共 88 个身份有现行方向，多标签计数不相加当总数。
2026-07-22 前 A/B/C/D 代表旧 AI-for-PDE×等离子体/EUV 方向；历史 published/legacy 的字母和评分保留为 historical_or_scheme_specific，不映射成现行 A/B/C/D，不跨评分方案排名。
年代证据：{'arxiv_id_month_inferred': 397, 'publication_date_recorded_unverified': 57}。arXiv 编号年月标记 arxiv_id_month_inferred；DOI 记录只能沿用其未复验 publication_date；缺失时 null。first_seen 永远只是采集时间。
最新采集记录为 2026-09-19；最新登记 arXiv 月份为 2026-09，均不证明论文实际发表状态。

## 里程碑及未入库线索

里程碑表 32 行：20 行按 arXiv 标识链接主表，另建 12 个 reference_work 节点。这 12 个是“标识未匹配”，不能宣称独立新增论文；如 The Well/PDEArena 可能已使用 DOI/unresolved 身份登记，possible_same_work 边只提示别名。
全部报告出现 243 个未匹配主表的 arXiv 标识，详见 corpus_manifest.json 的 unregistered_arxiv_mentions。它们可含未入选候选、基线、里程碑与检索线索；不计入454，不默认新论文。

## 知识图谱关系语义

共 658 节点、3610 边。节点类型：{'paper': 454, 'reference_work': 12, 'source': 170, 'topic': 22}；关系类型：{'listed_as_landmark': 32, 'mentioned_in': 685, 'possible_same_work': 4, 'recorded_in': 1016, 'tagged_with': 1873}。
- tagged_with：透明正则规则产生 automated_tag / inferred，保存匹配字段、文本片段与原始行。提及术语不证明实施了方法。
- mentioned_in：报告出现身份编号或 DOI，不等于入选。recorded_in：当前主表的原始记录来源。
- listed_as_landmark：里程碑表明确列出该工作，仍沿用历史未核验等级。
- possible_same_work：近似标题/短名匹配候选，未合并。
- 本图没有 citation、extends 或 outperforms 边；共同主题、年代先后或日报评价不构成论文引用、继承或同协议性能证据。

| 自动主题 | 主表身份数（非互斥） |
|---|---:|
| 物理场表示与编码 | 162 |
| 神经算子与函数空间 | 217 |
| 多物理基座与预训练 | 128 |
| 方程符号与条件化 | 14 |
| 上下文算子学习 | 17 |
| 物理约束与守恒 | 143 |
| 几何网格与拓扑 | 90 |
| 多尺度与频谱 | 85 |
| 长时演化与稳定性 | 87 |
| 生成式求解 | 40 |
| 不确定性与统计推断 | 41 |
| 数据集与评测协议 | 131 |
| 迁移适配与泛化 | 158 |
| 混合求解与模块组合 | 49 |
| 等离子体与动力学 | 92 |
| 激光辐射与EUV | 43 |
| 逼近理论与误差分析 | 71 |
| Transformer与序列架构 | 89 |
| 训练优化与采样 | 29 |
| 反问题辨识与控制 | 25 |
| 效率与计算扩展 | 132 |
| 缩放规律与数据配比 | 6 |

## 近似标题重复候选（保持原身份）

仅字符串相似检索；候选可能只是相近命名的不同方法（例如 PINO 与 Laplace 算子），不是重复判定。

- `arxiv:2111.03794` ↔ `arxiv:2602.12706`；标题相似度 0.9057：Physics-Informed Neural Operator for Learning Partial Differential Equations / Physics-Informed Laplace Neural Operator for Solving Partial Differential Equations。
- `arxiv:2404.12355` ↔ `arxiv:2408.16168`；标题相似度 0.9951：Towards a Foundation Model for Partial Differential Equations: Multi-Operator Learning and Extrapolation / Towards a foundation model for partial differential equations: Multioperator learning and extrapolation。

## 待核验冲突

- `arxiv:2405.19101` / `publication_date`：[{"source_id": "metadata/history/2026-09-12/published_papers.jsonl:28", "value": "2024-12-10"}, {"source_id": "metadata/history/2026-09-12/paper_registry_updates_2026_W30.jsonl:1", "value": "2024-12-10"}, {"source_id": "metadata/history/2026-09-12/published_papers_2026_W28.jsonl:2", "value": "2025"}]。
- `arxiv:2405.19101` / `venue`：[{"source_id": "metadata/history/2026-09-12/published_papers.jsonl:28", "value": "NeurIPS 2024"}, {"source_id": "metadata/history/2026-09-12/paper_registry_updates_2026_W30.jsonl:1", "value": "NeurIPS 2024"}, {"source_id": "metadata/history/2026-09-12/paper_registry_updates_2026_W28.jsonl:1", "value": "ICLR 2025"}, {"source_id": "metadata/history/2026-09-12/published_papers_2026_W28.jsonl:2", "value": "ICLR 2025"}]。
- `arxiv:2403.12553` / `publication_date`：[{"source_id": "metadata/history/2026-09-12/published_papers.jsonl:29", "value": "2024-12-10"}, {"source_id": "metadata/history/2026-09-12/paper_registry_updates_2026_W30.jsonl:2", "value": "2024-12-10"}, {"source_id": "metadata/history/2026-09-12/published_papers_2026_W28.jsonl:3", "value": "2025"}]。
- `arxiv:2403.12553` / `venue`：[{"source_id": "metadata/history/2026-09-12/published_papers.jsonl:29", "value": "NeurIPS 2024"}, {"source_id": "metadata/history/2026-09-12/paper_registry_updates_2026_W30.jsonl:2", "value": "NeurIPS 2024"}, {"source_id": "metadata/history/2026-09-12/paper_registry_updates_2026_W28.jsonl:2", "value": "ICLR 2025"}, {"source_id": "metadata/history/2026-09-12/published_papers_2026_W28.jsonl:3", "value": "ICLR 2025"}]。
- `arxiv:2402.12475` / `publication_date`：[{"source_id": "metadata/history/2026-09-12/published_papers.jsonl:30", "value": "2025-01-08"}, {"source_id": "metadata/history/2026-09-12/paper_registry_updates_2026_W30.jsonl:3", "value": "2025-01-08"}, {"source_id": "metadata/history/2026-09-12/published_papers_2026_W28.jsonl:4", "value": "2025"}]。
- `arxiv:2402.12475` / `venue`：[{"source_id": "metadata/history/2026-09-12/published_papers.jsonl:30", "value": "Communications Physics"}, {"source_id": "metadata/history/2026-09-12/paper_registry_updates_2026_W30.jsonl:3", "value": "Communications Physics"}, {"source_id": "metadata/history/2026-09-12/published_papers_2026_W28.jsonl:4", "value": "Computer Methods in Applied Mechanics and Engineering"}]。
- `doi:10.1137/23m1623707` / `publication_date`：[{"source_id": "metadata/history/2026-09-12/published_papers_2026_W29.jsonl:5", "value": "2025-04-01"}, {"source_id": "metadata/history/2026-09-12/published_papers_2026_W27.jsonl:9", "value": "2025-04-08"}]。
- `arxiv:2305.20053` / `publication_date`：[{"source_id": "metadata/history/2026-09-12/published_papers_2026_W29.jsonl:8", "value": "2025-08-01"}, {"source_id": "metadata/history/2026-09-12/published_papers_2026_W25.jsonl:5", "value": "2025-07-24"}]。

## 可重复生成与检查

```bash
python scripts/build_research_graph.py
python scripts/build_research_graph.py --check
```

--check 离线重建并逐字节比较所有七个输出，验证454身份一对一覆盖、来源路径/行号、图边端点、节点/边ID唯一性、原始输入哈希，以及无引用边。输入或HEAD改变将要求显式重建；不修改正式registry。

阅读层次：本次的全量工作是结构化逐条汇编与文本扫描；5条abstract_checked属于历史记录状态，不表示本次重新读摘要；其余449条不自动提升为已核验。外部重点论文核验由独立 evidence 文件记录，尚未写回主表。

