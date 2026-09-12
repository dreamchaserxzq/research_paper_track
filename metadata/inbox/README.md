# 输入事件

此目录接收经过来源核验的新论文、评分、发表状态及修正事件，每个 `.jsonl` 文件每行一个事件。
使用 [事件 schema](../../schemas/event.schema.json) 和 [操作说明](../../docs/OPERATIONS.md)。

执行 `python scripts/papertrack.py build` 生成主表与索引，再执行 `check`。文件内容保持追加；
修正使用新 `correction` 事件和 `supersedes`，不要删除原始证据。历史来源 ID 在
[来源记录](../source_records.jsonl) 中。`selected_for_digest` 记录历史已入选，修正不会清除已送达历史。

尚未重新核验的旧论文由 `metadata/history/2026-09-12` 导入，不伪装成新的已核验事件。
