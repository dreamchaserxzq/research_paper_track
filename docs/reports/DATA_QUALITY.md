# 数据归并质量报告

> 离线归并当前可得证据；未重新联网核验全部历史论文。源快照有 SHA-256 校验，冲突不会丢弃。

| 项目 | 数量 |
|---|---:|
| papers | 455 |
| selected_arxiv_ids | 348 |
| reported_formal | 121 |
| conflicts | 8 |
| legacy_unverified | 444 |
| missing_title | 3 |
| missing_authors | 327 |
| daily_files | 62 |
| weekly_files | 6 |
| structured_runs | 10 |

## 待核验冲突

完整机器记录见 [conflicts.jsonl](../../metadata/conflicts.jsonl)。当前选值保留主表优先级，不表示冲突已经解决。用 correction 事件明确 supersedes 源记录后才能消除冲突。

| 论文 | 字段 | 处理 |
|---|---|---|
| arxiv:2405.19101 | venue | pending |
| arxiv:2405.19101 | publication_date | pending |
| arxiv:2403.12553 | venue | pending |
| arxiv:2403.12553 | publication_date | pending |
| arxiv:2402.12475 | venue | pending |
| arxiv:2402.12475 | publication_date | pending |
| arxiv:2305.20053 | publication_date | pending |
| doi:10.1137/23m1623707 | publication_date | pending |

## 历史重复入选

| arXiv | 原始日期 |
|---|---|
| 2511.21861 | 2026-06-15, 2026-08-21 |
| 2512.23192 | 2026-07-05, 2026-08-09 |
| 2604.25985 | 2026-06-02, 2026-07-19 |
| 2605.11691 | 2026-05-29, 2026-08-07 |
| 2607.24513 | 2026-08-02, 2026-08-09 |
| 2608.07053 | 2026-09-08, 2026-09-09 |
| 2608.11937 | 2026-09-08, 2026-09-09 |

重复出现的原始日报不改写；当前去重集只保留一个 ID。没有结构化运行证据的历史统计不转换成精确查询数量。
