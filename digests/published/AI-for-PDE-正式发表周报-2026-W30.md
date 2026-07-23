# AI for PDE 正式发表论文追踪周报 · 2026-W30

- **检索范围（UTC）**：2023-07-23 至 2026-07-23
- **运行时间（UTC）**：2026-07-23T06:55:53Z
- **原始候选**：48 篇
- **去重后候选**：31 篇
- **正式发表状态明确**：20 篇
- **本期核心入选**：9 篇
- **本期扩展入选**：0 篇
- **正式发表状态更新**：3 篇
- **待人工确认**：4 篇
- **数据 schema**：`published-v2`

> 本周报是 2026-07-22 仓库研究重点调整后的首份活跃周报。2026-07-20 生成的旧版 W30 周报保留在
> `digests/archive-ai-for-pde/published/` 中作为历史审计材料；本报告不重复抄录其 11 篇论文，而是完成
> 主注册表规范化回填，并补齐 PDE 基座大模型主线中此前遗漏或正式元数据错误的关键论文。

## 一、本期概览

本次检索采用“出版商 / 正式 proceedings 优先、聚合数据库交叉核验、arXiv 仅作匹配辅助”的证据链。
在 31 篇去重候选中，20 篇已能确认正式发表或正式接收；其中 11 篇已由 2026-07-20 的归档周报覆盖，
本期将另外 9 篇高价值论文写入权威主注册表 `metadata/published_papers.jsonl`。

本期最重要的结果不是单纯增加论文数量，而是完成三项数据治理修正：

1. **Poseidon**：旧分周元数据误记为 ICLR 2025；正式记录为 **NeurIPS 2024**，DOI 为
   `10.52202/079017-2311`。
2. **CoDA-NO**：旧分周元数据误记为 ICLR 2025；正式记录为 **NeurIPS 2024**，DOI 为
   `10.52202/079017-3306`。
3. **DNO**：旧分周元数据误记为 CMAME 且缺 DOI；正式记录为 **Communications Physics 8, 15
   (2025)**，DOI 为 `10.1038/s42005-024-01911-3`。

## 二、趋势总结

### 2.1 基座模型：从“通用主干”走向可验证的跨 PDE 迁移

Poseidon、DPOT、OmniArch、PDE-Transformer、PROSE-PDE 与 CoDA-NO 已形成较清晰的技术谱系：

- **规模化预训练**：DPOT 将模型扩展到 0.5B 参数，并在 10 余个 PDE 数据集、10 万余条轨迹上训练。
- **跨维度统一**：OmniArch 明确进行 1D–2D–3D 联合预训练。
- **多模态条件**：PROSE-PDE 同时建模方程符号与数值轨迹，缓解多算子学习中的歧义。
- **多物理变量建模**：CoDA-NO 沿物理量 / 通道值域进行 token 化，支持耦合多物理系统预训练。
- **连续时间与半群结构**：Poseidon 用时间条件层归一化和半群训练策略增强连续时间建模。
- **统一高容量主干**：PDE-Transformer 验证了跨 16 类 PDE 的共享 Transformer backbone。

### 2.2 算子学习：几何、时间与物理变量成为三类核心条件

DNO 通过微分同胚映射处理变化几何；CoDA-NO 显式组织不同物理变量；PITA 处理自回归时间错位。
这表明下一代 PDE 基座模型不应只把方程类别作为标签，而应把 **几何、物理变量结构、时间推进机制**
都设计成可组合条件。

### 2.3 泛化：零样本、少样本和 in-context 三条路线并行

- Poseidon、DPOT、OmniArch 主要依赖大规模预训练后微调或零样本迁移。
- CoDA-NO 强调少样本多物理适配。
- VICON 将 in-context operator learning 推进到稠密二维多物理流体数据，并支持不规则采样频率。
- PROSE-PDE 用符号模态增强对未见方程的外推。

### 2.4 长时 rollout：误差控制从损失函数转向训练协议

PITA 将不同时间步发现的动力学进行自监督对齐，直接针对自回归 shortcut 与误差积累。
这类“训练协议级”方法可作为现有 PDE foundation model 的外挂式增强模块，而非重新设计完整主干。

## 三、核心论文

### 1. Poseidon: Efficient Foundation Models for PDEs

- **正式信息**：NeurIPS 2024；DOI：`10.52202/079017-2311`
- **分类**：`foundation_model`、`operator`
- **基座等级**：`true_foundation_model`
- **方法**：多尺度 Operator Transformer、时间条件 LayerNorm、基于 PDE 半群性质的数据扩增 / 训练。
- **数据与任务**：在大规模流体动力学数据上预训练，覆盖 15 个下游任务与多类未见 PDE / 算子。
- **泛化证据**：新物理、少样本适配、模型与数据规模扩展。
- **主要贡献**：正式确立了“预训练—下游适配—未见物理泛化”的 PDE foundation model 评价范式。
- **局限**：预训练物理仍以流体动力学为主；跨复杂几何、强耦合多物理和非网格离散仍需更直接验证。
- **评分**：相关度 5 / 通用性 3 / 方法价值 2，**总分 10**。

### 2. Pretraining Codomain Attention Neural Operators for Solving Multiphysics PDEs

- **正式信息**：NeurIPS 2024；DOI：`10.52202/079017-3306`
- **分类**：`foundation_model`、`operator`
- **基座等级**：`true_foundation_model`
- **方法**：沿函数值域 / 物理通道构造 tokens，把位置编码、自注意力与归一化扩展到函数空间。
- **数据与任务**：流体、流固耦合、Rayleigh–Bénard 对流等耦合多物理系统。
- **泛化证据**：同一模型学习多个 PDE 系统，并在少样本下游任务中迁移。
- **主要贡献**：物理变量不再只是输入通道，而成为可交互、可预训练的语义实体。
- **局限**：不同变量集合、单位体系和通道数量大幅变化时的可扩展 token 词表仍需解决。
- **评分**：5 / 3 / 2，**总分 10**。

### 3. DPOT: Auto-Regressive Denoising Operator Transformer for Large-Scale PDE Pre-Training

- **正式信息**：ICML 2024，PMLR 235:17616–17635
- **分类**：`foundation_model`、`operator`
- **基座等级**：`true_foundation_model`
- **方法**：自回归去噪预训练与可扩展 Fourier Attention。
- **数据与任务**：10 余个 PDE 数据集、10 万余条轨迹，模型规模最高约 0.5B 参数。
- **泛化证据**：多类下游 PDE，包含三维任务。
- **主要贡献**：证明 PDE 预训练可以沿模型规模与数据规模扩展，而不局限于小型算子网络。
- **局限**：自回归模型仍受长时误差积累影响；条件表达与几何适配不如专门条件化模型明确。
- **评分**：5 / 3 / 2，**总分 10**。

### 4. OmniArch: Building Foundation Model for Scientific Computing

- **正式信息**：ICML 2025，PMLR 267:9860–9887
- **分类**：`foundation_model`、`operator`
- **基座等级**：`true_foundation_model`
- **方法**：Fourier Encoder–Decoder、Transformer 动力学主干、PDE-Aligner 物理对齐微调。
- **数据与任务**：PDEBench 上 1D、2D、3D 联合预训练，多尺度、多物理任务。
- **泛化证据**：in-context 与 zero-shot 新物理适配。
- **主要贡献**：把跨维度统一编码、时间动力学和物理对齐放进同一系统。
- **局限**：统一 Fourier 表征对非规则 mesh、点云和复杂边界的适用性仍有限。
- **评分**：5 / 3 / 2，**总分 10**。

### 5. PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations

- **正式信息**：ICML 2025，PMLR 267:23562–23602
- **分类**：`foundation_model`、`operator`
- **基座等级**：`foundation_model_candidate`
- **方法**：借鉴 Diffusion Transformer 的可扩展主干；对不同物理通道分别构造时空 tokens，并进行通道级自注意力。
- **数据与任务**：16 类 PDE 的大规模规则网格数据。
- **泛化证据**：预训练模型在多个下游任务中优于从头训练和若干物理 foundation model。
- **主要贡献**：提供了信息密度稳定、适合多变量 PDE 的统一 Transformer backbone。
- **局限**：证据主要来自规则网格；跨几何、跨离散和条件可执行性仍未充分证明。
- **评分**：5 / 3 / 2，**总分 10**。

### 6. Towards a foundation model for partial differential equations: Multioperator learning and extrapolation

- **正式信息**：Physical Review E 111, 035304 (2025)；DOI：`10.1103/PhysRevE.111.035304`
- **分类**：`foundation_model`、`operator`
- **基座等级**：`true_foundation_model`
- **方法**：PROSE-PDE 以方程符号和数值场为双模态输入 / 输出，联合学习多个解算子与控制方程。
- **数据与任务**：多种一维、含时、非线性、常系数 PDE。
- **泛化证据**：对训练中未见的模型或数据进行方程与解轨迹外推。
- **主要贡献**：证明符号 PDE 条件可以减少多算子学习的非适定性，并提升未见方程外推。
- **局限**：当前实验集中于一维常系数 PDE；高维、复杂几何和多物理条件仍待扩展。
- **评分**：5 / 3 / 2，**总分 10**。

### 7. Diffeomorphism neural operator for various domains and parameters of partial differential equations

- **正式信息**：Communications Physics 8, 15 (2025)；DOI：`10.1038/s42005-024-01911-3`
- **分类**：`operator`、`surrogate`
- **基座等级**：`general_pde_solver`
- **方法**：将不同物理域微分同胚映射到公共 generic domain，在公共域上学习统一神经算子。
- **数据与任务**：Darcy 流、管流、翼型流和三维力学。
- **泛化证据**：跨形状、尺寸、分辨率与参数变化，并对未见几何给出稳定预测。
- **主要贡献**：把变几何问题转化为统一坐标域中的算子学习问题。
- **局限**：依赖可构造且稳定的微分同胚；拓扑改变、自由边界和非同胚域不直接适用。
- **评分**：4 / 3 / 2，**总分 9**。

### 8. Physics-informed Temporal Alignment for Auto-regressive PDE Foundation Models

- **正式信息**：ICML 2025，PMLR 267:80223–80258
- **分类**：`enabling`、`foundation_model`
- **基座等级**：`enabling_method`
- **方法**：从观测轨迹中构造自监督物理时间对齐信号，使不同时间步学习到的动力学保持一致。
- **数据与任务**：多种含时 PDE 与既有自回归 PDE foundation model。
- **泛化证据**：长时 rollout 和分布外数据上提升准确性与稳健性。
- **主要贡献**：无需已知解析物理先验，即可作为已有基座模型的训练增强模块。
- **局限**：主要改进时间一致性，不能替代跨方程条件编码、几何建模与物理守恒机制。
- **评分**：5 / 2 / 2，**总分 9**。

### 9. VICON: Vision In-Context Operator Networks for Multi-Physics Fluid Dynamics Prediction

- **正式信息**：Transactions on Machine Learning Research；2026-01-15 正式接收
- **分类**：`foundation_model`、`operator`、`surrogate`
- **基座等级**：`foundation_model_candidate`
- **方法**：将二维物理场切分为视觉 patches，以 in-context 条件—输出函数对驱动新的算子预测。
- **数据与任务**：三个二维流体动力学基准，支持不同时间步长和不完整观测。
- **泛化证据**：多物理 in-context 迁移、灵活 rollout、丢帧和采样频率变化下的稳健性。
- **主要贡献**：缓解逐空间点 token 化的二次复杂度，使 in-context operator learning 扩展到稠密二维场。
- **局限**：仍以二维流体系统为主；不规则 mesh / 图 / 点云及更广多物理变量集合尚未验证。
- **评分**：5 / 2 / 2，**总分 9**。

## 四、扩展论文

本期无扩展入选。按照 `PUBLISHED_CRITERIA.md` 的“不凑数”原则，未将仅有相邻 AI-for-Science
价值、但对 PDE 求解链条贡献较弱的论文纳入扩展层。

## 五、分类总结

| `published_category` | 本期数量 | 代表论文 | 观察 |
|---|---:|---|---|
| `foundation_model` | 8 | Poseidon、DPOT、OmniArch、PROSE-PDE | 正式发表的 PDE 基座模型已形成清晰谱系 |
| `operator` | 8 | CoDA-NO、DNO、PDE-Transformer、VICON | 变量、几何、时间与提示上下文成为主要条件维度 |
| `surrogate` | 2 | DNO、VICON | 重点由单一固定域代理转向可迁移、多条件代理 |
| `enabling` | 1 | PITA | 长时稳定性开始由独立训练机制解决 |
| `data` | 0 | — | 本期无新的正式数据 / benchmark 核心入选 |
| `pinn` | 0 | — | 本期无达到基座或通用层级的正式 PINN 新增 |

> 同一论文可对应多个 `published_category`，因此分类数量不与论文总数相加等同。

## 六、Venue 覆盖

### 已检索并入选

- **顶级 AI 会议**：NeurIPS 2024、ICML 2024、ICML 2025。
- **通用物理 / 计算物理期刊**：Physical Review E、Communications Physics。
- **机器学习期刊**：Transactions on Machine Learning Research。
- **正式证据来源**：NeurIPS Proceedings、PMLR、APS、Springer Nature、TMLR / OpenReview。
- **交叉核验来源**：arXiv、DBLP、OpenReview、出版商索引；arXiv 不作为正式发表的唯一证据。

### 已检索但未在本期重复入选

JCP、CMAME、SISC、Nature Machine Intelligence、Nature Computational Science 与
npj Computational Materials 的 11 篇正式论文已由 2026-07-20 的归档 W30 周报覆盖，本期不重复生成记录。

### 主要排除原因

- 仅有 arXiv / submitted 状态，没有正式 venue 或正式接收证据。
- 仅解决单一算例，缺乏通用 PDE 求解、跨条件泛化或可迁移方法贡献。
- 旧分周文件已有记录且正式元数据无变化。
- 出版日期晚于本次运行日，禁止提前标记为 published。

## 七、正式发表状态更新

| 论文 | 原记录 | 本次正式核验 | 处理 |
|---|---|---|---|
| Poseidon | ICLR 2025、无 DOI、通用 OpenReview URL | NeurIPS 2024，DOI `10.52202/079017-2311` | 以 `published-v2` 正确记录写入主注册表 |
| CoDA-NO | ICLR 2025、无 DOI、通用 OpenReview URL | NeurIPS 2024，DOI `10.52202/079017-3306` | 以 `published-v2` 正确记录写入主注册表 |
| DNO | CMAME 2025、无 DOI | Communications Physics 8, 15 (2025)，DOI `10.1038/s42005-024-01911-3` | 以 `published-v2` 正确记录写入主注册表 |

旧分周 JSONL 不覆盖、不删除，用于审计历史；权威去重与后续状态判断以
`metadata/published_papers.jsonl` 中的新规范记录为准。

## 八、待确认论文

| 论文 | 当前问题 | 已有证据 | 建议 |
|---|---|---|---|
| Neural Preconditioning Operator for Efficient PDE Solves | 旧记录称 ICML 2025，但当前未定位到精确 PMLR 条目 | arXiv 与项目页存在 | 下次按作者和论文题名复查 ICML / PMLR / OpenReview |
| Self-supervised neural operator for solving partial differential equations | 旧记录称 CMAME 2026，但 DOI、卷期与文章号缺失 | arXiv 与期刊级线索 | 通过 Crossref、Elsevier article-in-press 页面复核 |
| PDEformer-2: A Versatile Foundation Model for PDEs | 仍以预印本证据为主 | arXiv / 项目页 | 等待正式会议或期刊接收记录 |
| PROSE-FD: A multimodal PDE foundation model for forecasting fluid dynamics | 仅确认预印本与项目引用 | arXiv / 代码仓库 | 跟踪是否出现正式会议 proceedings 或期刊 DOI |

## 九、对 PDE 基座大模型研究的直接启示

1. **条件编码应当结构化而非仅加标签**：CoDA-NO、PROSE-PDE、DNO 分别证明物理变量、方程符号和几何
   都应作为独立条件对象进入模型。
2. **基座主干与增强模块应解耦**：PITA 说明长时一致性可以由外挂式训练协议解决，不必全部堆进主干架构。
3. **跨维度不等于跨离散**：OmniArch 已覆盖 1D–3D，但规则网格、mesh、graph、point cloud 的统一仍是
   独立挑战。
4. **真正的 foundation model 需要迁移证据**：仅在多个 PDE 上联合训练不足以判为基座模型，还需要
   零 / 少样本、未见物理、未见条件或 in-context 泛化证据。
5. **变几何与自由边界应区分处理**：DNO 适合可微分同胚的域变化；拓扑变化和随解演化的边界仍需
   自由边界神经算子或隐式几何机制。

## 十、幂等与数据治理说明

- 本期只向主注册表追加 9 条不存在的规范记录。
- DOI、arXiv ID 与规范化标题均已检查，无主注册表内重复。
- 旧版 W30 归档周报和分周 JSONL 保留，不重写历史。
- 当前活跃周报路径首次创建；README 的正式周报区块由占位文本替换为本期摘要。
- 重复运行时应检测同一 DOI / arXiv ID / 标题，不再追加记录或 README 块。
