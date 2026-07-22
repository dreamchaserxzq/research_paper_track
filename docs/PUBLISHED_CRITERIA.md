# 正式发表周报 · 判定标准 / Venue / 分类规范

> 本文件是**每周"正式发表论文周报"例程（weekly routine）唯一的判定 / venue / 分类事实来源**，
> 与日报的 [`TAXONOMY.md`](./TAXONOMY.md) 对称。修改收录标准、venue 列表、分类或评分时只改本文件，
> 周报例程以此为准。
>
> **职责边界**：日报（[`ROUTINE.md`](./ROUTINE.md) + `TAXONOMY.md`）负责最新 **arXiv 预印本**；
> 本周报负责**已正式发表 / 正式接收**的论文，并回填预印本的正式版本。两者共享同一去重集与仓库。

---

## 一、任务定位与范围

系统跟踪 **AI 求解 PDE（AI for PDE）** 的完整研究生态 —— 不仅 PDE 基座大模型，也覆盖其上下游：
PDE 基座模型、通用 PDE 求解器、神经算子、代理模型（surrogate）、降阶模型（ROM）、
数据驱动 PDE 求解、科学机器学习、PDE 数据生成、物理约束学习、多物理仿真模型、
科学仿真基础模型，以及 PDE benchmark / 数据集 / 软件框架。

核心问题：**如何用 AI 学习、近似、加速、泛化、自动化地求解偏微分方程**，
研究链条从传统 AI PDE solver 一直到 PDE foundation model。

---

## 二、正式发表判定

**只收录具备明确正式发表 / 正式接收证据者。** 满足任一即可：

- 存在有效 DOI
- 出版商页面显示 published / online first / early access / in press
- 正式期刊页面确认发表，或正式会议 proceedings
- 已具备正式 venue，或已有卷期 / 页码 / article number
- Crossref / OpenAlex / Semantic Scholar 提供可靠出版信息
- 会议官网或 OpenReview 页面确认正式接收

**不得进入正式入选列表**：仅有 arXiv / 仅有项目主页 / 仅有 GitHub / 仅有个人主页 /
无任何正式出版证明。

arXiv 仅用于：匹配正式版本、查找历史版本、补充摘要、查找代码与数据链接、更新已有记录。

---

## 三、检索时间范围

- 默认 **运行日期向前回溯三年**，日期统一 **UTC**，**不得硬编码**。
  （例：运行日 `2026-07-22` → 检索范围 `2023-07-22 至 2026-07-22 UTC`。）
- 对已有记录中 `status ∈ {preprint, submitted, unknown}` 或缺 DOI / venue / publication_date 的论文，
  **即使 arXiv 时间超过三年，也应复查其正式发表状态**。

---

## 四、分类体系（named categories）

> ⚠️ **不复用日报 A/B/C/D 字母**（日报字母含义不同，混用会误读）。周报用**具名类别**，
> 写入独立字段 `published_category`（主类）与 `published_categories`（可多类）。

| 类别 key | 含义 | 涵盖 |
|----------|------|------|
| `foundation_model` | PDE 基座模型 | foundation model、universal / generalist PDE solver、scientific simulation foundation model、多 PDE 预训练 |
| `operator` | 通用 PDE 求解模型 | neural operator、operator learning、FNO、DeepONet、transformer / graph PDE solver、mesh-independent / continuous solver |
| `surrogate` | 代理与降阶模型 | surrogate、emulator、reduced-order model (ROM)、differentiable surrogate、simulation accelerator |
| `data` | 数据生成与数据体系 | PDE dataset、simulation / synthetic generation、self-supervised PDE data、benchmark、软件框架 |
| `pinn` | 科学机器学习方法 | PINN、physics-informed / physics-constrained learning、differentiable physics、hybrid numerical-AI solver |
| `enabling` | 支撑技术 | 表征学习、预训练、迁移学习、uncertainty、optimization、architecture、PDE 条件编码、专家/模块化模型 |

---

## 五、基座模型判定（`foundation_model_level`）

**不得仅凭标题出现 foundation / universal / general / large 判定**，须综合：
预训练能力（多 PDE / 多任务 / 大规模数据 / 自监督 / 迁移）、泛化能力（跨 PDE / 物理 / 几何 /
分辨率 / 离散形式、zero-/few-shot）、表征统一性（grid / mesh / graph / point cloud / continuous field）、
条件化能力（方程 / 参数 / 边界 / 初值 / 几何）、扩展能力（模型 / 数据规模、新任务 / 新物理）。

取值：

| 值 | 含义 |
|----|------|
| `true_foundation_model` | 真正具备多任务预训练 + 通用表示 + 跨任务适配 |
| `foundation_model_candidate` | 有基座趋势但能力不足 |
| `general_pde_solver` | 通用 PDE 求解模型 |
| `surrogate_model` | 代理模型 |
| `enabling_method` | 关键支撑技术 |
| `single_task_method` | 单任务方法 |

---

## 六、Venue 检索范围（分层）

- **AI / ML**：NeurIPS、ICML、ICLR、JMLR、TMLR、AAAI、IJCAI
- **科学机器学习**：Nature Machine Intelligence、Nature Computational Science、Nature Communications、
  Science Advances、PNAS、Machine Learning: Science and Technology (MLST)、APL Machine Learning
- **计算科学**：Journal of Computational Physics (JCP)、CMAME、Computer Physics Communications、
  SIAM J. Scientific Computing (SISC)、J. Scientific Computing、Computational Mechanics
- **应用数学 / 物理**：Journal of Fluid Mechanics、Physical Review Fluids、Physical Review E、
  Physical Review Research、Chaos
- **数据与科学仿真**：Geoscientific Model Development (GMD)、JAMES、Physics of Plasmas、
  Nuclear Fusion、Computational Materials Science

仅收录具有 AI-for-PDE 求解价值的论文；正式 workshop 之外的非正式 workshop 不计入正式入选。

---

## 七、筛选层级（`selection_tier`）

| tier | 内容 |
|------|------|
| `core` | PDE 基座模型、通用 PDE solver、重要 neural operator、高价值 surrogate、重要数据集、关键 AI-PDE 方法 |
| `extended` | 支撑技术、benchmark、数据生成、ROM、PINN、高价值应用 |
| `pending` | 出版信息冲突 / DOI 不确定 / 分类存在争议 —— 待人工确认 |

---

## 八、排除规则

原则上不收录：① 只有 arXiv；② 单一 PDE 且无推广价值；③ 普通 PINN 小改进；
④ 普通 baseline 应用；⑤ 纯工程应用；⑥ 与 PDE 无关的 LLM；⑦ 仅单一 benchmark 提升；
⑧ 标题宣传 foundation model 但能力不足；⑨ 非正式 workshop。

---

## 九、评分标准（满分 10）

| 维度 | 字段 | 分值 | 说明 |
|------|------|------|------|
| PDE 相关度 | `score_relevance` | 0–5 | 5 真 foundation model；4 通用 solver / 大规模 operator；3 重要 AI-PDE 方法；2 高价值 surrogate 或单任务；1 一般应用；0 无关 |
| 泛化能力 | `score_generality` | 0–3 | 3 跨 PDE/物理/几何；2 多任务迁移；1 有限外推；0 固定任务 |
| 创新与证据 | `score_value` | 0–2 | 2 方法与实验均突出；1 正式发表且有价值；0 贡献有限 |
| 合计 | `score_total` | 0–10 | 三项之和 |

> **Schema 说明**：以上为 **published-v2** 评分字段。历史记录（2026-07 前）使用 v1 字段
> `score_ai_scicomp / score_transfer_physics / score_innovation_venue`，予以保留、不回改；
> 新记录一律带 `registry_schema_version: "published-v2"` 以便区分与统计。

---

## 十、数量策略

不强制数量。首次三年回溯：core 约 5–15 篇、extended 约 5–20 篇；常规运行允许少量新增或无新增。
**不得为凑数纳入弱相关论文。**

---

## 十一、元数据字段（`metadata/published_papers.jsonl`，每行一条 JSON）

必填：`title`、`authors`、`venue`、`publisher`、`publication_date`、`doi`、`official_url`、
`abstract`、`keywords`、`sources`、`status`、`selection_tier`、`published_category`、
`foundation_model_level`、`score_relevance`、`score_generality`、`score_value`、`score_total`、
`registry_schema_version`（= `"published-v2"`）。

补充：`arxiv_id`、`arxiv_url`、`code_url`、`data_url`、`published_categories`、`training_pdes`、
`evaluation_pdes`、`physical_domains`、`generalization_axes`。

规则：缺失字段填 `null`；不重复（按 DOI / arXiv ID / 标题+作者+venue 去重）；追加写入不覆盖历史。

### `publication_date` 取值优先级
出版商日期 → 会议日期 → Crossref → OpenAlex → Semantic Scholar。
**不得使用** arXiv 日期 / 索引日期 / 页面更新时间。

---

## 十二、去重与幂等

- **去重以 `metadata/published_papers.jsonl` 为准**（跨主题连续保留，在仓库根 `metadata/`）。
- 历史周报正文已归档在 `digests/archive-ai-for-pde/published/`（旧目录），去重时可参考其标题，
  但不作为权威来源。
- 重复运行不得重复论文 / 重复周报 / 重复 README 块 / 重复日志；提交前做 JSON、Markdown、git diff 检查。

---

## 十三、输出与命名

- **周报文件**：`digests/published/AI-for-PDE-正式发表周报-YYYY-WW.md`
  （与日报及归档周报命名一致；标题「AI for PDE 正式发表论文追踪周报」）。
- **README**：更新 `<!-- PUBLISHED_DIGEST_START -->` 与 `<!-- PUBLISHED_DIGEST_END -->` 之间，
  **保留最近 12 期**（超出则裁剪最旧块）。
- **运行日志**：追加 `run_log_published.md`（时间、范围、候选、新增、更新、Git 状态、异常）。
- **Git**：遵循根目录 `CLAUDE.md` —— 直接推 `main`、**不创建 PR**、提交信息英文，
  建议 `update AI for PDE published digest YYYY-WW`。推送失败不得声称成功，须记录原因。
