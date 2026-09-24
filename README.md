# PDE 基座模型与 AI for PDE 论文追踪

追踪架构与预训练、数据与评测、下游适配，以及通用 AI 求解 PDE 方法。

[论文目录](docs/PAPER_CATALOG.md) · [重点论文对照](docs/RESEARCH_COMPARISON.md) · [全部日报与周报](docs/DIGEST_INDEX.md) · [操作说明](docs/OPERATIONS.md)

当前注册表 **455** 条；去重集 **348** 个 arXiv ID；**8** 项待核验冲突。历史发表状态为记录中的声明，核验程度见各条目。

## 最新日报

<!-- DIGEST_START -->

| 日期 | 报告 |
|---|---|
| 2026-09-24 | [PDE-FM-日报-20260924.md](digests/PDE-FM-日报-20260924.md) |
| 2026-09-23 | [PDE-FM-日报-20260923.md](digests/PDE-FM-日报-20260923.md) |
| 2026-09-22 | [PDE-FM-日报-20260922.md](digests/PDE-FM-日报-20260922.md) |
| 2026-09-21 | [PDE-FM-日报-20260921.md](digests/PDE-FM-日报-20260921.md) |
| 2026-09-19 | [PDE-FM-日报-20260919.md](digests/PDE-FM-日报-20260919.md) |
| 2026-09-18 | [PDE-FM-日报-20260918.md](digests/PDE-FM-日报-20260918.md) |
| 2026-09-17 | [PDE-FM-日报-20260917.md](digests/PDE-FM-日报-20260917.md) |
| 2026-09-15 | [PDE-FM-日报-20260915.md](digests/PDE-FM-日报-20260915.md) |
| 2026-09-14 | [PDE-FM-日报-20260914.md](digests/PDE-FM-日报-20260914.md) |
| 2026-09-13 | [PDE-FM-日报-20260913.md](digests/PDE-FM-日报-20260913.md) |
| 2026-09-12 | [PDE-FM-日报-20260912.md](digests/PDE-FM-日报-20260912.md) |
| 2026-09-11 | [PDE-FM-日报-20260911.md](digests/PDE-FM-日报-20260911.md) |

<!-- DIGEST_END -->

## 正式发表周报

<!-- PUBLISHED_DIGEST_START -->

- [AI-for-PDE-正式发表周报-2026-W35](digests/published/AI-for-PDE-正式发表周报-2026-W35.md)
- [AI-for-PDE-正式发表周报-2026-W34](digests/published/AI-for-PDE-正式发表周报-2026-W34.md)
- [AI-for-PDE-正式发表周报-2026-W33](digests/published/AI-for-PDE-正式发表周报-2026-W33.md)
- [AI-for-PDE-正式发表周报-2026-W32](digests/published/AI-for-PDE-正式发表周报-2026-W32.md)
- [AI-for-PDE-正式发表周报-2026-W31](digests/published/AI-for-PDE-正式发表周报-2026-W31.md)
- [AI-for-PDE-正式发表周报-2026-W30](digests/published/AI-for-PDE-正式发表周报-2026-W30.md)

<!-- PUBLISHED_DIGEST_END -->

## 运行与数据质量

- [遗漏日报恢复记录](docs/RECOVERY_20260912.md)：保留分支原始正文和提交来源。
- [数据质量与冲突报告](docs/reports/DATA_QUALITY.md)：缺失字段、历史重复入选和待核验信息。
- [历史运行日志](run_log.md)与[正式发表日志](run_log_published.md)：原始声明不重写；新运行使用结构化记录。
- 状态回填尚无独立执行证据；本次离线归并不计作联网状态复查。
- 外部调度器当前配置尚未核验。更新仓库提示词后须按操作说明同步部署，才能对后续定时任务生效。

## 本地命令

```bash
python scripts/papertrack.py build
python scripts/papertrack.py check
python -m unittest discover -s tests -v
python scripts/papertrack.py search "foundation"
python scripts/publish.py audit-branches
```

## 维护约定

新增论文与修正写入 `metadata/inbox/*.jsonl`；主表、去重集和本页由程序生成。
原始快照保存在 `metadata/history/2026-09-12/`，分周原始文件继续保留作证据。
方向与评分见 [TAXONOMY](docs/TAXONOMY.md)，发表判定见 [PUBLISHED_CRITERIA](docs/PUBLISHED_CRITERIA.md)，发布只暂存明确列出的任务文件。
