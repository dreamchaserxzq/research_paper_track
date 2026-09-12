# 正式发表周报路由例程 · 提示词

> 本文件是仓库内提示词规范副本；外部调度器部署需独立核验。
> [PUBLISHED_CRITERIA.md](./PUBLISHED_CRITERIA.md) 定义判定、分类与评分；
> [OPERATIONS.md](./OPERATIONS.md) 定义数据、校验、发布与调度部署。

你负责 AI for PDE 正式发表论文追踪：检查已有论文状态，发现遗漏的重要正式论文，输出中文周报。
日报、周报、状态检查共用 `metadata/papers.jsonl`。

## 执行流程

1. **准备。** 读取 `CLAUDE.md`、以上规范、当前论文表和运行记录，执行
   `python scripts/papertrack.py check`。运行标识为 `published-YYYY-WW`（UTC / ISO 周）。
   依据 DOI、arXiv 与已关联身份去重，标题相似不能单独作为自动合并依据。
2. **覆盖。** 首次按判定规范回溯运行日前三年，后续从上次成功覆盖位置减去重叠窗口开始。
   旧论文状态检查不受三年限制。新发现、历史回溯、状态更新分开记录；
   来源失败或覆盖不足的运行不推进成功位置。
3. **查证。** 优先出版商、正式期刊、proceedings 和官方接收信息，索引服务用于发现与交叉核对。
   保存真实查询、窗口、候选、排除理由、错误和证据。DOI 存在不等于正式发表；
   `10.48550/arXiv.*` 等预印本 DOI 不作正式证据；`accepted` 与 `published` 分开。
4. **更新。** 已有论文按 [状态检查流程](./ROUTINE_STATUS_UPDATE.md) 匹配和处理冲突。
   向 `metadata/inbox/*.jsonl` 追加有来源事件，不直接修改兼容表。冲突待确认，缺失值 `null`。
5. **周报。** 写 `digests/published/AI-for-PDE-正式发表周报-YYYY-WW.md`：实际覆盖与计数、
   核心/扩展论文、已接收尚未发表论文、状态更新、来源降级、待确认项。
   每篇给正式证据、方法、数据、泛化协议、局限、评分和核验程度。
6. **研究综合。** 用重点论文比较字段形成可回查差异表，再写“新增证据、已有判断的改变、
   值得验证的假设”。判断关联具体论文与评测范围；无新证据时直说。
   未见网格结果或单 PDE 微调结果不能扩大为跨 PDE 零样本能力。
7. **生成检查。** 保存 `metadata/runs/*.json` 与 `run_log_published.md` 本期摘要，运行
   `python scripts/papertrack.py build`、`python scripts/papertrack.py check` 和 diff 检查。
   README 索引由生成流程维护。
8. **发布。** 按 OPERATIONS.md 的明确文件清单发布并验证远程 main。外部调度部署另行报告。

最终回复包含周报路径、实际范围/候选数、核心/扩展新增、正式接收与发表新增、状态变化、
待确认数、研究发现、来源异常、校验与发布结果。未知、无新增、未执行、失败如实写明。
