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

**只收录身份匹配且具备可回查官方证据者。DOI 的存在本身不充分。**

- `published`：出版商/期刊正式页面或会议 proceedings 明确已发表，记录官方链接、venue 和证据时间。
  已正式在线出版的 online first / early access 归 published，细节记在 `publication_type`。
- `accepted`：会议官网、官方 OpenReview 接收决定或出版商明确接收，但尚无正式出版证明。
  in press 若只证明已接收，归 accepted；不能计为已发表，缺发表日期填 `null`。
- `preprint / submitted / unknown`：无上述证据，不进入正式接收/发表主列表。

`10.48550/arXiv.*` 等预印本 DOI 不作为正式发表证据。其它 DOI 也必须核对对应作品类型、
标题、作者与正式版本；数据、代码、勘误等 DOI 不能误归论文正式版。
Crossref / OpenAlex / Semantic Scholar 用于发现和交叉核对，不替代有冲突时的官方查证。
venue 名称、作者主页上的“accepted”或 arXiv comments 是线索，单独不作最终证据。

正式接收与已发表分别统计。每次新断言保存官方 URL、证据类别与实际检查时间。
迁移前记录仅作为历史声明保留，其 `legacy_unverified` 标记不能自动升级。

**不得进入正式入选列表**：仅有 arXiv / 仅有项目主页 / 仅有 GitHub / 仅有个人主页 /
无任何正式出版证明。

arXiv 仅用于：匹配正式版本、查找历史版本、补充摘要、查找代码与数据链接、更新已有记录。

---

## 三、检索时间范围

- 首次或明确历史回溯任务默认 **运行日期向前回溯三年**，日期统一 **UTC**，**不得硬编码**。后续常规运行从上次成功覆盖位置加重叠窗口开始，失败/降级不推进覆盖位置。
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
> 新增带评分事件必须在 `paper` 内填写 `score_scheme: "published-v2"` 和完整的
> `score_relevance`（0–5）、`score_generality`（0–3）、`score_value`（0–2）、`score_total`，
> 总分必须等于三项之和。`registry_schema_version` 可保留用于领域元数据版本，但不能替代
> `score_scheme`。统一表的 `assessments` 按来源和方案保留评分，不设顶层 `score_total`；
> 历史分数不重评，不和 daily-v1 混合排名。

---

## 十、数量策略

不强制数量。首次三年回溯：core 约 5–15 篇、extended 约 5–20 篇；常规运行允许少量新增或无新增。
**不得为凑数纳入弱相关论文。**

---

## 十一、正式发表事件的领域字段

已查证时记录：`title`、`authors`、`venue`、`publisher`、`publication_date`、`doi`、
`official_url`、`abstract`、`keywords`、`sources`、`status`、`selection_tier`、
`published_category`、`foundation_model_level`。

正式状态必须有匹配的论文 ID、venue 与官方证据，具体入库契约见 OPERATIONS.md。
有本次新评分时必须填写第九节的 scheme 与完整分项；纯状态更新不要求重评，
没有新评分依据时省略评分字段，不能只复制历史总分。

补充：`arxiv_id`、`arxiv_url`、`code_url`、`data_url`、`published_categories`、`training_pdes`、
`evaluation_pdes`、`physical_domains`、`generalization_axes`。

规则：新记录作为 `metadata/inbox/*.jsonl` 事件的 `paper` 字段写入，事件外层含稳定 ID、时间和证据，详见 [OPERATIONS.md](./OPERATIONS.md)。缺失字段填 `null`；`accepted` 可没有正式 DOI/发表日期。`metadata/papers.jsonl` 是生成的统一当前表，`published_papers.jsonl` 是兼容视图，不直接写入。历史字段和评分版本保留在源记录，不改写历史。

### `publication_date` 取值优先级
出版商日期 → 会议日期 → Crossref → OpenAlex → Semantic Scholar。
**不得使用** arXiv 日期 / 索引日期 / 页面更新时间。

---

## 十二、去重与幂等

- **身份与去重以生成的 `metadata/papers.jsonl` 为准**，结合 DOI / arXiv 别名和来源。兼容视图不再单独维护去重逻辑。标题相似但作者/版本不明者保留待确认。
- 历史周报正文已归档在 `digests/archive-ai-for-pde/published/`（旧目录），去重时可参考其标题，
  但不作为权威来源。
- 重复运行不得重复论文 / 重复周报 / 重复 README 块 / 重复日志；提交前做 JSON、Markdown、git diff 检查。

---

## 十三、输出与命名

- **周报文件**：`digests/published/AI-for-PDE-正式发表周报-YYYY-WW.md`
  （与日报及归档周报命名一致；标题「AI for PDE 正式发表论文追踪周报」）。
- **README**：通过 `python scripts/papertrack.py build` 生成最近 12 期索引，完整目录另存，不手工重复追加。
- **运行证据**：本次真实查询与候选写入 `metadata/runs/*.json`，`run_log_published.md` 保留可读摘要。检索状态和 Git 发布状态分别报告。
- **Git**：遵循根目录 `CLAUDE.md` 与 [OPERATIONS.md](./OPERATIONS.md)，明确路径暂存、检查暂存快照、发布并回读远程 main；不自动 rebase 重试。提交信息英文，建议 `Update AI for PDE published digest YYYY-WW`。未验证 main 内容不得报告已发布。
