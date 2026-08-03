# AI for PDE 正式发表论文追踪周报 · 2026-W32

- **检索范围（UTC）**：2023-08-03 至 2026-08-03
- **运行时间（UTC）**：2026-08-03T09:27:00Z
- **原始候选**：23 篇
- **去重后候选**：20 篇
- **正式发表状态明确**：9 篇
- **本期核心入选**：1 篇
- **本期扩展入选**：2 篇
- **正式发表状态更新**：0 篇
- **待人工确认**：1 篇
- **数据 schema**：`published-v2`

> 本期在 2026-W30 已完成 PDE 基座模型主线集中回填的基础上，重点补查 2026 年正式上线但尚未进入主注册表的神经算子工作。检索坚持出版商页面、正式期刊元数据与 DOI 优先；OpenReview poster、withdrawn/submitted 记录以及仅有 arXiv 的论文均不作为正式入选依据。

## 一、本期概览

本次组合检索覆盖 AI/ML proceedings、科学机器学习期刊、JCP/CMAME/CPC 等计算科学期刊，以及 Crossref/PubMed/出版商索引。经 DOI、标题和仓库全文检索去重后，确认 3 篇此前未进入权威主注册表的正式论文：

1. **PGMNO**：把线性多步时间积分、隐式 BDF 训练与 Mamba/SSM 结合，面向长时 PDE rollout 的稳定性和分辨率外推。
2. **Hermite Neural Operator**：以 Hermite 基函数构造无界域神经算子，使输出天然满足无穷远衰减条件并支持任意坐标查询。
3. **Multi-particle Neural Operator Transformer**：从多粒子反应–扩散动力系统出发重构注意力机制，增强局部空间变化建模。

本期没有发现可与 `metadata/paper_registry.jsonl` 中既有 arXiv 记录进行置信度不低于 0.9 的正式版本匹配，因此不执行自动状态回填。

## 二、趋势总结

### 2.1 长时动力学建模正在从纯网络结构转向“数值积分 × 序列模型”

PGMNO 的重要性不在于单纯把 Transformer 替换为 Mamba，而在于将线性多步推进、BDF 型训练约束和结构化状态空间模型组成统一时间建模框架。该路线说明，PDE 基座模型的长时稳定性可以通过显式引入数值时间离散结构改善，而不必完全依赖 rollout loss 或更大的主干网络。

### 2.2 神经算子的定义域正在由有界规则网格扩展到无界连续域

HNO 使用 Hermite 谱基的指数衰减性质，把远场边界条件直接编码进输出空间。与通过截断区域和人工边界条件处理无界域相比，该设计更接近函数空间层面的结构先验。对统一连续场 PDE 基座模型而言，这提示编码器/解码器不应默认所有物理场都定义在有限矩形盒中，而应允许按定义域类型选择或学习适当的连续基底。

### 2.3 注意力机制开始引入可解释的动力系统构造

MPNOT 把注意力层与多粒子反应–扩散系统联系起来，用粒子交互解释局部信息传播。其价值主要在算子主干的可解释结构设计，而不是新的 PDE 条件体系。此类模块更适合作为可插拔 operator expert，而非单独承担跨方程统一建模。

## 三、核心论文

### 1. PGMNO: A physics-Guided mamba neural operator framework for partial differential equations

- **正式信息**：*Neural Networks*, Volume 201, Article 108845；online first 2026-03-21
- **DOI**：[`10.1016/j.neunet.2026.108845`](https://doi.org/10.1016/j.neunet.2026.108845)
- **分类**：主类 `operator`；兼类 `enabling`
- **基座等级**：`general_pde_solver`
- **方法**：将线性多步数值积分与结构化状态空间模型结合；训练阶段使用隐式 BDF 型多步方案和因果感知学习策略。
- **验证范围**：多类含时 PDE 基准，重点评估预测精度、计算效率、长时稳定性和跨空间离散分辨率外推。
- **主要贡献**：把数值时间推进结构直接纳入神经算子主干，为自回归 PDE 模型的稳定 rollout 提供可迁移设计。
- **局限**：当前仍属于统一网络架构层面的通用算子，尚未展示跨方程符号条件、复杂几何、多离散输入和大规模预训练能力。
- **评分**：相关度 4 / 通用性 2 / 方法价值 2，**总分 8**。
- **证据来源**：[ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0893608026003072)、[PubMed](https://pubmed.ncbi.nlm.nih.gov/41886915/)

## 四、扩展论文

### 1. Hermite neural operator for solving partial differential equations on unbounded domains

- **正式信息**：*Machine Learning: Science and Technology* 7(1), 015004；2026-01-07
- **DOI**：[`10.1088/2632-2153/ae2bbc`](https://doi.org/10.1088/2632-2153/ae2bbc)
- **分类**：`operator`
- **基座等级**：`general_pde_solver`
- **方法**：以 Hermite 函数替代周期 Fourier 基，输出由有限 Hermite 展开构成，从结构上满足无穷远衰减条件。
- **验证范围**：热方程、非线性 Schrödinger 方程；包含训练支撑域外的任意坐标推断测试。
- **主要贡献**：将无界域的远场条件转化为输出函数空间先验，避免人工截断边界与 FNO 周期性伪影。
- **局限**：适用性依赖解在无穷远具有适当衰减；对非衰减波、复杂高维无界域和多尺度远场结构仍需进一步验证。
- **评分**：4 / 2 / 2，**总分 8**。
- **证据来源**：[IOPscience](https://iopscience.iop.org/article/10.1088/2632-2153/ae2bbc)

### 2. Multi-particle neural operator transformer for solving partial differential equations

- **正式信息**：*Neural Networks*, Volume 202, Article 109040；online first 2026-04-25
- **DOI**：[`10.1016/j.neunet.2026.109040`](https://doi.org/10.1016/j.neunet.2026.109040)
- **分类**：主类 `operator`；兼类 `enabling`
- **基座等级**：`general_pde_solver`
- **方法**：基于多粒子反应–扩散动力系统构造 multi-particle attention，增强对局部空间变化的建模并提供动力系统解释。
- **验证范围**：Burgers、Reaction–Diffusion、Navier–Stokes、Allen–Cahn 等多类 PDE。
- **主要贡献**：为 Transformer 型神经算子提供具有动力系统含义的局部交互机制。
- **局限**：实验仍以标准基准为主，未证明跨几何、跨离散、跨维度预训练或 foundation-model 级迁移。
- **评分**：4 / 2 / 1，**总分 7**。
- **证据来源**：[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0893608026005009)、[PubMed](https://pubmed.ncbi.nlm.nih.gov/42096883/)

## 五、分类总结

| `published_category` | 本期新增 | 说明 |
|---|---:|---|
| `foundation_model` | 0 | 未发现新的正式 PDE foundation model；若干 2026 工作仍仅为 arXiv 或非正式 workshop/poster |
| `operator` | 3 | 长时稳定、无界域表示和动力系统注意力三条算子设计路线 |
| `surrogate` | 0 | 本期未单独纳入应用型代理模型 |
| `data` | 0 | 未发现达到收录阈值的新正式数据集或 benchmark |
| `pinn` | 0 | 普通 PINN 增量及 workshop/poster 不收录 |
| `enabling` | 2 | PGMNO 的时间积分–SSM 结合；MPNOT 的动力系统注意力 |

## 六、Venue 覆盖与去重

### 已检索的主要来源

- AI/ML：ICLR、ICML、NeurIPS/OpenReview/PMLR
- 科学机器学习：Nature Machine Intelligence、Nature Computational Science、MLST
- 计算科学：JCP、CMAME、CPC、Neural Networks
- 聚合核验：Crossref、PubMed、出版商全文页、仓库代码搜索

### 已正式发表但未重复计入

- **Deep neural operator for free boundary problems**：已存在于主注册表或 W30 历史记录。
- **NOEM: efficient and scalable finite element method enabled by reusable neural operators**：已被 W30 历史记录覆盖。
- **Geometry-informed neural operator transformer for partial differential equations on arbitrary geometries**：已在 W27 历史记录出现。
- **Walsh-Hadamard Neural Operators for Solving PDEs with Discontinuous Coefficients**：已在 W30 历史记录出现。

### 未入选的主要原因

- OpenReview 页面标记为 `Withdrawn Submission`、`Submitted` 或仅为 AI&PDE poster，不满足正式会议/期刊判定。
- 仅有 arXiv 的 2026 PDE foundation model 下游应用，不作为正式发表论文入选。
- 综述、单一 PDE 小改进或纯应用工作未达到本期相关度与通用性阈值。

## 七、正式发表状态更新

本期 **0 篇**。未发现能够与 `paper_registry.jsonl` 中现有记录进行高置信度匹配且新增 DOI/venue 的条目。对只有中文占位标题或作者信息缺失的 bootstrap 记录，不进行低置信度自动覆盖。

## 八、待人工确认

### Self-composing neural operators for high-frequency and multiscale PDE surrogates

- **候选 DOI**：`10.1016/j.jcp.2026.115189`
- **候选 venue**：*Journal of Computational Physics*, Volume 565, Article 115189
- **问题**：索引页面给出 2026-11-15 的卷期日期，晚于本次运行日；当前检索结果未明确展示可优先采用的 online-first 日期。
- **处理**：暂不写入主注册表。下次运行优先检查 ScienceDirect 的 “Available online” 日期及 Crossref `published-online` 字段。

## 九、对 PDE 基座模型研究的启示

1. **长时演化模块可显式吸收数值积分结构**：PGMNO 表明，多步法和隐式稳定性约束可作为 latent dynamics 的训练协议或专家先验，而不必写死为唯一主干。
2. **定义域类型应进入几何/场表示元数据**：HNO 说明“有界、周期、半无限、全空间”不是普通几何标签，而会决定合适的函数基和远场条件表达。
3. **动力系统解释适合用于专家模块设计**：MPNOT 的粒子交互注意力可视为局部算子专家候选，但仍需由统一 PDE 条件、几何状态和变量语义进行路由。

---

**本期结论**：2026 年正式神经算子研究正在从规则网格上的精度竞争，进一步转向长时稳定性、定义域结构和可解释交互机制。它们尚未替代 PDE foundation model 的统一条件编码与大规模预训练，但可作为下一代基座模型的时间推进、连续场解码和局部专家模块。
