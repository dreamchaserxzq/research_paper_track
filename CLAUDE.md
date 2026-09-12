# CLAUDE.md — 自动化 Agent 操作规范

## 事实来源

本仓库自 2026-07-22 起聚焦 PDE 基座大模型，同时通过 D 方向跟踪 AI 求解 PDE。

- 方向、关键词、评分：`docs/TAXONOMY.md`（A/B/C/D 四方向）。
- 正式接收与发表判定：`docs/PUBLISHED_CRITERIA.md`。
- 数据写入、校验与发布：`docs/OPERATIONS.md`。
- 三类例程：`docs/ROUTINE.md`、`docs/ROUTINE_PUBLISHED.md`、`docs/ROUTINE_STATUS_UPDATE.md`。

仓库提示词更新不代表外部调度器已更新。未完成提示词回读、哈希比对和首次运行核验时，
部署状态必须写为 `unknown` / 未核验。

## 数据维护

`metadata/papers.jsonl` 是生成的当前论文视图；`metadata/paper_registry.jsonl`、
`metadata/published_papers.jsonl` 和 `seen_papers.txt` 是兼容视图，不手工追加或覆盖。
新发现、评分、状态和更正写入 `metadata/inbox/*.jsonl`，保留证据、时间与来源。
`metadata/history/2026-09-12/` 是迁移前快照，禁止改写；缺失历史信息保持 `null`。
检索证据与异常记录在 `metadata/runs/*.json`，只记录真实执行过的查询。

```bash
python scripts/papertrack.py build
python scripts/papertrack.py check
git diff --check
```

## 发布规则

例程产物直接发布到 `origin/main`，不创建 PR；脚本接口和完整步骤见 OPERATIONS.md。

- 只暂存明确列出的本次文件；禁止 `git add -A`，不得带入用户其它文件或已有暂存内容。
- 发布前抓取最新 `origin/main` 并重做去重与校验。分歧时先审查差异、整合内容，重新生成检查。
  禁止把自动 `pull --rebase` 重试当作恢复方案，禁止强推。
- 只有远程 main 包含目标提交，且本次产物能从远程回读核对，才可报告发布成功。
  提交成功或工作分支推送成功均不等于发布成功；第二次推送不能覆盖第一次失败。
- 失败时保留产物与诊断信息。不修改现有鉴权方式，不把占位 `GITHUB_TOKEN` 写入 origin，
  不在日志中输出凭据。
- 本次维护任务没有发布授权时，完成本地生成与校验，报告“本地就绪，未发布”。
  不把例程的发布规则解释为当前开发任务必须提交推送。

## 命名与幂等

- 日报：`digests/PDE-FM-日报-YYYYMMDD.md`（UTC）。
- 旧主题日报保留在 `digests/archive-ai-for-pde/`，不新增旧主题日报。
- 周报：`digests/published/AI-for-PDE-正式发表周报-YYYY-WW.md`（ISO 周）。
- 状态检查：`digests/status_updates/arxiv-status-update-YYYYMMDD.md`。
- 日期与任务类型是逻辑标识；重试不重复入库、不追加第二份日报或第二条成功记录。
- 英文提交信息，如 `Daily PDE-FM digest YYYY-MM-DD`。
- 自动日报作者可使用 `ArXiv Tracker Bot <arxiv-tracker@automated.bot>`，不改全局 Git 配置。
