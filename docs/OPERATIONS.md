# 维护、数据与发布操作手册

本手册统一数据写入和发布流程。脚本执行确定性的归并、校验与发布验证；文献检索、证据判断、
摘要与研究综合仍由执行者完成。当前仓库没有证明外部调度器已经加载这些流程。

## 数据流与事实来源

| 路径 | 角色 | 写入规则 |
|---|---|---|
| `metadata/history/2026-09-12/` | 迁移前原始快照 | 保留原字节与来源，不修改 |
| `metadata/inbox/*.jsonl` | 新发现、评估、状态、更正事件 | 追加独立事件，保留证据 |
| `digests/` | 历史交付与本次报告 | 历史身份不重写；补档记录原提交 |
| `metadata/source_records.jsonl` | 历史记录与来源追踪视图 | 程序生成 |
| `metadata/papers.jsonl` | 当前统一论文表 | 程序生成，检索与关联以此为准 |
| `metadata/paper_registry.jsonl` | 主注册表兼容视图 | 程序生成，不手工修改 |
| `metadata/published_papers.jsonl` | 正式状态兼容视图 | 程序生成；历史声明不等于本次核验 |
| `seen_papers.txt` | 历史已交付论文 ID 集合 | 程序生成；不含所有排除候选 |
| `metadata/runs/*.json` | 本次真实查询与筛选记录 | 每个逻辑运行一份，保存重试关联 |
| `docs/PAPER_CATALOG.md`、`docs/RESEARCH_COMPARISON.md` | 论文目录与研究比较 | 程序生成 |
| `docs/DIGEST_INDEX.md`、README 索引 | 阅读入口 | 程序生成 |
| `docs/reports/DATA_QUALITY.md` | 缺失、冲突与核验状态 | 程序生成，缺口不能当成已解决 |

稳定身份优先使用规范化 arXiv ID，再用 DOI，缺少 ID 时才使用完全一致的标题与作者组合。
标题近似、作者不全、不同 DOI/venue 等歧义不得自动强并。别名与来源保留，不能用当前 checkout
提交代替历史论文或运行的身份。

`selected_for_digest` 表示历史入选/交付，生成去重表时保留；后续降分或更正不会擦除已经交付
的事实。`verification` 区分 `legacy_unverified`、`source_checked`、`conflict_pending`。
迁移保留的 DOI、venue 和 status 是历史声明，不能因 JSON 可解析就算正式证据已核验。
冲突未解决时保持 pending，不能按文件日期直接取“最新”值。

## 新事件契约

每行一个 JSON 对象。以下是结构示例，尖括号值必须替换，不能作为实际记录直接入库：

```json
{
  "event_id": "daily-YYYY-MM-DD:<arxiv_id>:discovery",
  "event_type": "discovery",
  "recorded_at": "YYYY-MM-DDTHH:MM:SSZ",
  "paper": {
    "arxiv_id": "<规范化ID>",
    "title": "<核实后的标题>",
    "authors": ["<已确认作者>"],
    "status": "preprint",
    "submitted_at": null,
    "updated_at": null
  },
  "evidence": [
    {
      "url": "https://arxiv.org/abs/<规范化ID>",
      "kind": "arxiv_abstract",
      "checked_at": "YYYY-MM-DDTHH:MM:SSZ"
    }
  ],
  "selected": true
}
```

- `event_type` 支持 `discovery`、`assessment`、`publication`、`correction`。
- `event_id` 在库内唯一。同一运行的相同事件沿用原 ID，避免重试追加；新证据使用新 ID。
- `recorded_at` 是实际记录时间，`evidence.checked_at` 是实际查证时间，均为 UTC ISO 时间。
- 新事件的 `paper` 必须给出 `arxiv_id` 或 `doi`。只有标题的历史记录可保留，但新发现尚无可靠 ID 时先留在待确认材料，不绕过入库校验。缺失字段用 `null`，不以空数组表示未知数量。
- `evidence.kind` 包括 `arxiv_abstract`、`paper_fulltext`、`code`、`publisher`、
  `proceedings`、`acceptance`；kind 是人工判定，链接仍需实际打开核对。
- 正式状态事件必须有对应官方证据。出版信息用 publisher/proceedings；接收信息用 acceptance。
  arXiv 页面或预印本 DOI 不能独自证明正式发表。
- 更正事件可用 `supersedes` 列出 `metadata/source_records.jsonl` 中实际存在的 `source_id`，并在 `paper.notes` 说明原因。它会撤销该源记录对当前字段选择的贡献，因此必须把仍有效且仅该源拥有的字段复制进更正事件，并保留对应证据。
  原始记录仍可追查，历史交付标志不被擦除；不能跨论文身份替代。更改 arXiv 身份须单独审查迁移，不能借普通更正强行合并。
- 评分、评估协议、研究用途等附加元数据写在 `paper` 内，字段含义见 TAXONOMY.md。
  **新增事件只要带任何评分字段，就必须提供完整的方案与分项：**
  日报使用 `score_scheme: "daily-v1"`、`score_relevance`（0–4）、`score_generality`（0–3）、
  `score_innovation`（0–3）、`score_total`；正式周报使用 `score_scheme: "published-v2"`、
  `score_relevance`（0–5）、`score_generality`（0–3）、`score_value`（0–2）、`score_total`。
  总分须等于对应三个分项之和。无新评分依据的状态事件不要复制或估填不完整评分。
- 统一论文表的 `assessments` 按来源和 scheme 保留评分，不提供顶层 `score_total`。
  历史分数及 schema 原样保留，不重评、不跨方案相加或排名；状态检查排序需读取有明确方案的 assessments。
- 状态检查无变化时用 assessment 保留检查证据；失败只记运行错误，不刷新成功检查时间。
  候选正式版本保存在附加候选字段，不把待确认 DOI 当成当前确定值。

日常只往 inbox 写新事件。迁移后不要再生成新的 `paper_registry_updates_YYYY_WW.jsonl` 或
`published_papers_YYYY_WW.jsonl`；这些旧文件作为历史来源保留。

## 检索与运行记录

运行标识采用任务类型和日期/ISO 周：`daily-YYYY-MM-DD`、`published-YYYY-WW`、
`status-YYYY-MM-DD`；只用字母、数字、下划线、点和连字符，不用冒号。重复执行复用逻辑标识，不能双计成功次数。

```json
{
  "run_id": "daily-YYYY-MM-DD",
  "task_type": "daily",
  "started_at": "YYYY-MM-DDTHH:MM:SSZ",
  "completed_at": "YYYY-MM-DDTHH:MM:SSZ",
  "coverage_start": "YYYY-MM-DDTHH:MM:SSZ",
  "coverage_end": "YYYY-MM-DDTHH:MM:SSZ",
  "previous_successful_coverage_end": null,
  "status": "success",
  "queries": [
    {
      "query": "<实际执行的查询>",
      "source": "arxiv",
      "status": "success",
      "error": null,
      "candidate_ids": ["<规范化候选ID>"]
    }
  ],
  "candidates": [
    {
      "arxiv_id": "<规范化ID>",
      "submitted_at": null,
      "updated_at": null,
      "discovered_at": "YYYY-MM-DDTHH:MM:SSZ",
      "decision": "selected",
      "reason": "<评分与入选依据>",
      "discovery_type": "backfill"
    }
  ],
  "digest_path": "digests/PDE-FM-日报-YYYYMMDD.md"
}
```

`status` 为 success/degraded/failed，描述检索执行和覆盖；它**不是 Git 发布状态**。
`decision` 为 selected/excluded/pending；`discovery_type` 为 new/backfill/version_update。
候选支持 `arxiv_id` 或 `doi`，查询 ID 可用原 ID 或 `arxiv:` / `doi:` 前缀，须与候选别名一致。
`new` 必须有落在窗口内的 submitted_at，`version_update` 必须有窗口内 updated_at；日期未知时保留 null，归 backfill 并在 reason 说明时间未知。发现时间必须真实。查询 ID 应对应候选清单，清单数量由程序推导，
不能填估计数冒充精确结果。仅收集部分结果时明确范围和降级原因；零候选与检索失败分别记录。

```bash
python scripts/papertrack.py coverage --task daily --at 2026-09-13T00:00:00Z --overlap-hours 48
```

此命令只计算窗口，不执行检索。使用真实本次时间替换示例；从上次成功 coverage_end 向前重叠，
无成功记录时为初次 48 小时窗口。失败/降级不推进成功位置。周报首次三年回溯另按
PUBLISHED_CRITERIA.md 指定窗口；历史状态检查不受发现窗口限制。不得补造迁移前历史查询，
历史 Markdown 中的估计数保留在原文，不写成新的结构化运行证据。

## 生成与检查

```bash
python scripts/papertrack.py build
python scripts/papertrack.py check
python scripts/papertrack.py validate-run metadata/runs/<本次运行文件>.json
git diff --check
```

build 根据快照、事件和日报证据生成当前表与阅读视图；check 校验格式、身份、事件、运行记录、
重复项和生成一致性。它不等于自动打开所有外部链接核实科学结论。生成两次应得到相同内容。
发现冲突或缺失先看 DATA_QUALITY.md 与源记录；不要修改生成文件来掩盖校验错误。

## 发布到 main

完整产物准备好后，根据本次 diff 列出**每一个**允许发布的路径。不传目录、不用通配符。
以下命令仅是接口说明，`...` 必须替换成完整文件清单：

```bash
git fetch origin --prune
git status --short
git diff --stat
python scripts/publish.py publish --message 'Daily PDE-FM digest YYYY-MM-DD' --files README.md ...
```

publish 会拒绝清单外已有暂存内容，检查工作区和导出的暂存快照，明确范围暂存/提交，
推送 main 和当前分支，再抓取远程检查提交包含关系及文件内容。HTML 等不属于例程产物的文件
不得进入发布清单。README、生成视图、相关 inbox、运行记录、日报和日志应作为一组检查。

已有提交可独立验证：

```bash
python scripts/publish.py verify --commit <完整提交SHA> --files <明确文件路径> ...
```

成功必须证明：远程 main 包含目标提交，而且远程当前版本的相关文件与该提交内容一致。
push 返回 0、工作分支有日报、摘要写“完成”均不满足此条件。
失败后保留本地成果，报告阶段/错误；不自动 rebase，不强推，不重写日志伪装成功。
main 前进或存在分歧时，审查远程变更、论文重复与日报差异，整合后重新 build/check，
重新确认具体提交与文件再发布。

本次开发维护未获发布授权时只完成本地工作。提交前应检查 `git diff --cached --check`
和暂存范围；不要代改用户其它文件。

## 遗漏工作分支与补档

```bash
git fetch origin --prune
python scripts/publish.py audit-branches
```

audit-branches 只读当前远程跟踪引用，本身不 fetch。区分“只在分支”“本地已恢复待发布”
与“main 已包含”；内容不同要审阅，不能按文件名直接判相同。
补档保留原日期、原始提交 SHA 和原文，新增恢复说明；重复发现留在历史正文，但当前表按论文
身份去重。旧主题档案合并导致的路径差异，需要人工核对内容来源，不用当前 HEAD 回填历史提交。

## 外部调度器部署

当前这些文档的修改只完成仓库侧准备。外部调度器、账号、实际运行提示词与定时配置未核验，
不得报告“自动任务已修复并上线”。

部署时依次完成：

1. 对三份 ROUTINE 文档及其依赖的 CLAUDE、TAXONOMY、PUBLISHED_CRITERIA、OPERATIONS
   计算 SHA-256；记录本地版本/提交及哈希。
2. 在有授权的实际调度环境更新提示词或入口，保留原配置与可恢复副本。
3. 从调度器回读已保存提示词和依赖版本，与仓库哈希核对；只上传但未回读不算部署验证。
4. 核对工作目录、Python、Git 鉴权、时间区、例程入口和文件权限；一次受控运行须生成合法运行记录。
5. 检查首次真实运行的窗口、候选、生成检查和远程 main 回读结果，记录部署时间与该次 run_id。
   仓库 build/check 通过不能代替这一步。

可用 `sha256sum CLAUDE.md docs/ROUTINE.md docs/ROUTINE_PUBLISHED.md docs/ROUTINE_STATUS_UPDATE.md docs/TAXONOMY.md docs/PUBLISHED_CRITERIA.md docs/OPERATIONS.md`
生成本地指纹。后续任一依赖修改需重新比对。尚未接入的调度器与核验时间保持 unknown/null，
不按当前时间填一个虚构的上线记录。
