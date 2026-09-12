# 结构化运行记录

新运行使用 [运行 schema](../../schemas/run.schema.json)，每个运行一个 `.json` 文件。
实例应写在 `schemas/examples/`，本目录只保存实际执行证据。

- `python scripts/papertrack.py coverage --task daily --at 2026-09-12T01:00:00Z` 计算覆盖窗口。
- `python scripts/papertrack.py validate-run path/to/run.json` 验证候选、查询、时间与计数。
- `python scripts/papertrack.py build` 生成 `metadata/run_index.jsonl`，统计从候选集合计算。

成功覆盖必须有实际查询且没有来源失败；降级/失败不推进覆盖位置。首次缺少结构化成功记录时
返回 `bootstrap: true`，需要执行者选择足够的历史补查范围。旧日志中的“约80篇”不转换为真实候选。
论文发表日、arXiv 提交日与首次发现日分别记录；未知时间保持 null。发表周报候选也可用 DOI 标识。
