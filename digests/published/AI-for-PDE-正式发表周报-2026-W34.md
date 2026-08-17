# AI for PDE 正式发表论文追踪周报 · 2026-W34

## 1. 本期概览

- **检索范围**：2023-08-17 至 2026-08-17 UTC
- **原始候选**：24 篇
- **结合权威主表与 W30–W33 分周增量审计后候选**：15 篇
- **正式状态明确**：8 篇
- **核心入选**：6 篇
- **扩展入选**：0 篇
- **正式发表状态更新**：0 篇（未对 `paper_registry.jsonl` 做无证据覆盖）
- **待人工确认**：2 篇

本期重点不是继续扩大传统单任务 PINN/代理模型数量，而是补齐三条对 PDE 基座模型更有结构性价值的正式路线：**稀疏 MoE 大规模多 PDE 预训练、复杂几何/局部微分结构感知的神经算子、以及神经算子与经典迭代求解器的热启动混合框架**。

> 仓库审计说明：`metadata/published_papers.jsonl` 仍未包含 W31–W33 的全部正式增量。为避免把历史分周增量误当成本期新增，本轮额外对 W30–W33 分周文件做审计去重。本期新结构化记录保存于 `metadata/published_papers_2026_W34.jsonl`。由于当前 GitHub Connector 对长 JSONL 仅支持整文件替换，本轮没有用不完整内容覆盖权威主表。

## 2. 趋势总结

### Foundation model / 多 PDE 预训练

MoE-POT 将 PDE 预训练显式推进到稀疏专家体系：在 6 个公开 PDE 数据集上预训练 30M–0.5B 参数模型，每次仅激活部分 routed experts，并保留 shared experts 学习跨 PDE 共性。它说明 PDE 基座模型的扩展路线不必等价于“把单一共享主干做得更宽更深”，而可以采用**共享能力 + 方程相关专家能力**的稀疏组合。

### Neural operator / 几何与局部结构

GAOT 和 Riesz Neural Operator 分别从两端补强通用算子能力：GAOT 强化任意几何、非规则域和大型 3D 工业 CFD 的几何泛化；RNO 则通过 Riesz transform 将全局谱信息与局部方向导数结合，针对神经算子容易忽略局部非平稳结构的问题提供新的算子归纳偏置。

### PINN / physics-informed learning

本期没有收录普通单实例 PINN 小改进。PFEM 更值得关注，因为它把 physics-informed operator pretraining 与 FEM 结合：预训练阶段不依赖标注解，并用 FEM differentiation 施加 PDE 约束；随后把神经算子输出作为传统线性/非线性 FEM 求解器初值。

### Surrogate / ROM / 混合数值求解

NOWS 和 PFEM 共同表明一个明显趋势：**AI 模型不必完全替代数值求解器，而可以充当高质量初值、预条件信息或可学习先验**。这类设计保留经典求解器的收敛与高精度能力，同时用学习模型减少迭代次数，是未来高可信 scientific surrogate 的重要落地方向。

### Scientific data / benchmark

本期未发现相对 W33 的 RealPDEBench 等已有正式记录更值得新增的数据/benchmark 工作，因此不为凑数重复纳入。

### Multi-PDE / multi-physics 与泛化

本期的泛化证据主要集中在四个轴：跨 PDE 数据集预训练（MoE-POT）、跨几何与大型非结构域（GAOT）、局部非平稳结构（RNO）、跨几何/材料/边界条件/离散分辨率的 physics-informed warm start（PFEM）。整体趋势正在从“固定网格上的算子拟合”向**条件化、几何感知、结构感知和数值求解闭环**迁移。

## 3. 核心论文

### 3.1 Mixture-of-Experts Operator Transformer for Large-Scale PDE Pre-Training

- **DOI**：无/未分配
- **Venue**：NeurIPS 2025 Main Conference Track
- **Publisher**：NeurIPS
- **publication_date**：2025-12-02
- **作者**：Hong Wang, Haiyang Xin, Jie Wang, Xuanze Yang, Fei Zha, Huanshuo Dong, Yan Jiang
- **正式链接**：https://proceedings.neurips.cc/paper_files/paper/2025/hash/2d23a9991a6f64482bf395628e279f5f-Abstract-Conference.html
- **arXiv**：2510.25803
- **published_category**：`foundation_model`
- **foundation_model_level**：`true_foundation_model`
- **方法**：稀疏 Mixture-of-Experts Operator Transformer；layer-wise router 从 16 个 routed experts 中激活 4 个，并加入 2 个 shared experts。
- **数据 / 物理系统**：6 个公开 PDE 数据集；30M–0.5B 参数规模预训练。
- **泛化方式**：跨 PDE 数据集共享预训练、专家稀疏激活、zero-shot transfer。
- **核心贡献**：把 MoE 的“共享 + 专门化”能力引入大规模 PDE 预训练，并展示参数扩展与推理成本解耦的可行性。
- **局限**：目前仍主要受公开 PDE 数据集覆盖范围约束；对任意几何、边界条件结构化条件和真实实验观测的统一性仍需进一步验证。
- **评分**：相关度 5/5；泛化 3/3；创新与证据 2/2；**总分 10/10**。

### 3.2 Geometry Aware Operator Transformer as an efficient and accurate neural surrogate for PDEs on arbitrary domains

- **DOI**：无/未分配
- **Venue**：NeurIPS 2025 Main Conference Track
- **Publisher**：NeurIPS
- **publication_date**：2025-12-02
- **作者**：Shizheng Wen, Arsh Kumbhat, Levi E. Lingsch, Sepehr Mousavi, Yizhou Zhao, Praveen Chandrashekar, Siddhartha Mishra
- **正式链接**：https://papers.nips.cc/paper_files/paper/2025/hash/e45a448dfa778f6d62729a7bc8633c06-Abstract-Conference.html
- **arXiv**：2505.18781
- **published_category**：`operator`
- **foundation_model_level**：`general_pde_solver`
- **方法**：多尺度 attentional graph neural operator encoder/decoder + geometry embedding + Transformer processor。
- **数据 / 物理系统**：多类 PDE；包含 3 个大型 3D 工业 CFD 数据集。
- **泛化方式**：任意域形状、复杂几何、非规则离散和大型 3D 场景。
- **核心贡献**：把几何处理能力与高效 operator transformer 统一起来，对未来 PDE 基座模型的 geometry codec / geometry-aware backbone 很有直接参考价值。
- **局限**：本身并非多 PDE 大规模预训练基座模型。
- **评分**：4/5 + 3/3 + 2/2 = **9/10**。

### 3.3 Riesz Neural Operator for Solving Partial Differential Equations

- **DOI**：无/未分配
- **Venue**：ICLR 2026 Poster
- **Publisher**：OpenReview
- **publication_date**：2026-04-23
- **作者**：Shouyi Liu, Xiaokang Yang, Yuntian Chen
- **正式链接**：https://openreview.net/forum?id=Vjw7q1quNt
- **arXiv**：未确认
- **published_category**：`operator`
- **foundation_model_level**：`general_pde_solver`
- **方法**：用 Riesz transform 构造谱导数表示，同时保留全局谱结构和局部方向变化。
- **数据 / 物理系统**：多个 PDE benchmark 与复杂真实数据。
- **泛化方式**：跨 PDE benchmark、局部非平稳结构和真实数据。
- **核心贡献**：针对纯全局谱算子对局部导数/非平稳结构表征不足的问题，引入具有明确微分结构含义的算子归纳偏置。
- **局限**：尚不是条件统一、跨方程预训练意义上的 foundation model。
- **评分**：4/5 + 2/3 + 2/2 = **8/10**。

### 3.4 NOWS: Neural Operator Warm Starts for accelerating iterative solvers

- **DOI**：10.1016/j.cma.2026.118989
- **Venue**：Computer Methods in Applied Mechanics and Engineering, Vol. 458, Article 118989
- **Publisher**：Elsevier
- **publication_date**：2026-08-15
- **作者**：Mohammad Sadegh Eshaghi, Cosmin Anitescu, Navid Valizadeh, Yizheng Wang, Xiaoying Zhuang, Timon Rabczuk
- **正式链接**：https://doi.org/10.1016/j.cma.2026.118989
- **arXiv**：2511.02481
- **published_category**：`enabling`
- **foundation_model_level**：`enabling_method`
- **方法**：神经算子生成 Krylov 求解器（CG/GMRES 等）的 warm start。
- **数据 / 物理系统**：多个 PDE 数值求解 benchmark。
- **泛化方式**：可接入 finite difference、finite element、isogeometric analysis、finite volume 等离散框架。
- **核心贡献**：在不替换经典数值离散和求解框架的前提下，用学习式初值把端到端计算时间最高降低约 90%，同时保留底层算法的稳定性/收敛性质。
- **局限**：价值主要体现为 solver accelerator，而不是独立的通用 PDE 模型。
- **评分**：4/5 + 2/3 + 2/2 = **8/10**。

### 3.5 Pretrain finite element method: A pretraining and warm-start framework for PDEs via physics-informed neural operators

- **DOI**：当前出版商页面未显示可可靠写入的 DOI
- **Venue**：Journal of the Mechanics and Physics of Solids, Vol. 214, Article 106682
- **Publisher**：Elsevier
- **publication_date**：2026-08
- **作者**：Yizheng Wang, Zhongkai Hao, Mohammad Sadegh Eshaghi, Cosmin Anitescu, Xiaoying Zhuang, Timon Rabczuk, Yinghua Liu
- **正式链接**：https://www.sciencedirect.com/science/article/pii/S0022509626001833
- **arXiv**：2601.03086
- **published_category**：`enabling`
- **foundation_model_level**：`enabling_method`
- **方法**：Transolver-based PINO + FEM differentiation + FEM warm start。
- **数据 / 物理系统**：线弹性与非线性超弹性，复杂几何、异质材料和任意边界条件。
- **泛化方式**：跨几何、材料分布、边界条件、空间分辨率以及线性/非线性求解器。
- **核心贡献**：不依赖标注解的 operator pretraining 与经典 FEM 精确求解闭环结合，尤其适合高精度工程仿真。
- **局限**：当前验证仍集中在固体力学 PDE 家族，跨物理能力尚不足以判定为 foundation model。
- **评分**：4/5 + 3/3 + 2/2 = **9/10**。

### 3.6 DeltaPhi: Physical States Residual Learning for Neural Operators in Data-Limited PDE Solving

- **DOI**：无/未分配
- **Venue**：NeurIPS 2025 Main Conference Track
- **Publisher**：NeurIPS
- **publication_date**：2025-12-02
- **作者**：Xihang Yue, Yi Yang, Linchao Zhu
- **正式链接**：https://proceedings.neurips.cc/paper_files/paper/2025/hash/12bf28fb68f295f855a5bf0c5a217d6e-Abstract-Conference.html
- **arXiv**：未确认
- **published_category**：`enabling`
- **foundation_model_level**：`enabling_method`
- **方法**：把直接输入→输出学习改写为相近物理状态间 residual learning，作为 architecture-agnostic wrapper 接入不同 neural operators。
- **数据 / 物理系统**：多种物理系统，含规则与非规则域。
- **泛化方式**：低数据量、不同模型架构、规则/非规则域、cross-resolution。
- **核心贡献**：提供一种不改变主干架构即可增强数据效率和泛化的训练范式，对 PDE foundation model 的适配/增量训练有价值。
- **局限**：属于训练增强方法而非独立通用模型。
- **评分**：4/5 + 2/3 + 2/2 = **8/10**。

## 4. 扩展论文

本期无新增 extended。若论文只在单一应用场景上提供性能提升、或者仅属于普通 PINN 变体，即使已正式发表，也没有为了填充数量而纳入。

## 5. 分类总结

| published_category | core | extended | 本期代表 |
|---|---:|---:|---|
| `foundation_model` | 1 | 0 | MoE-POT |
| `operator` | 2 | 0 | GAOT, Riesz Neural Operator |
| `enabling` | 3 | 0 | NOWS, PFEM, DeltaPhi |
| `surrogate` | 0 | 0 | — |
| `data` | 0 | 0 | — |
| `pinn` | 0 | 0 | — |

## 6. Venue 覆盖

本轮重点复核 NeurIPS 2025、ICLR 2026、ICML 2026、TMLR、Nature Machine Intelligence、Nature Computational Science、JCP、CMAME、SISC、MLST 以及计算力学相关 Elsevier 期刊。

- **NeurIPS 2025**：新增 MoE-POT、GAOT、DeltaPhi；ENMA、HyPINO 等已在 W33 入选，不重复。
- **ICLR 2026**：新增 Riesz Neural Operator；P3D、RealPDEBench 已在 W33 入选，不重复。
- **ICML 2026**：W33 已集中回填 PGD-NO、HNO、Particle-Guided Diffusion 等，本期无重复新增。
- **CMAME**：NOWS 在 2026-08-15 进入正式卷期，符合本期正式发表窗口。
- **Journal of the Mechanics and Physics of Solids**：PFEM 已有正式 Volume 214 / Article 106682 页面，纳入本期。
- **JCP / SISC / MLST / Nature 系列**：主要高相关工作已在 W30–W33 分周增量覆盖，本期未发现经去重后更优的新记录。

## 7. 正式发表状态更新

本期没有对 `metadata/paper_registry.jsonl` 自动覆盖写入。原因不是没有发现“预印本后来发表”的现象，而是当前 registry 中存在大量早期 bootstrap 条目、中文概括标题与不完整元数据；在无法做到逐条高置信 title/author/ID 对齐时，遵循“不猜测、不覆盖”的规则。

PFEM（arXiv:2601.03086）已经出现 Elsevier 正式文章页面，但本次没有在已读取的 registry 片段中确认其精确主记录，因此只作为正式论文增量收录，不计入 registry 状态更新数。

## 8. 待人工确认

### 8.1 TGLF-SINN / arXiv:2509.07024

仓库旧 registry 把它概括为“NeurIPS 2025”，但当前可验证记录属于 **NeurIPS 2025 Machine Learning and the Physical Sciences Workshop**。根据 `docs/PUBLISHED_CRITERIA.md`，非正式 workshop 不进入正式发表列表。建议继续保持预印本/待确认状态，除非出现主会 proceedings、期刊 DOI 或其他正式出版记录。

### 8.2 Physics-Informed Laplace Neural Operator / arXiv:2602.12706

当前可确认来源仍以 arXiv 和会议展示/演讲信息为主，未找到满足正式出版判定规则的期刊、主会 proceedings、DOI 或正式接收页面。因此不转为 published。

---

## 仓库一致性说明

本期完成 W34 周报和 `metadata/published_papers_2026_W34.jsonl` 的远程写入与回读核验。由于 GitHub Connector 当前对长 `metadata/published_papers.jsonl`、`metadata/paper_registry.jsonl` 和长 `README.md` 仅支持整文件替换，而本轮无法在不丢失历史内容的前提下安全构造完整替换内容，因此没有声称这些三个目标文件已完成更新。该限制应在后续具备安全增量编辑能力时优先修复：将 W31–W34 的分周正式记录合并回权威主表，并把 README 正式周报摘要恢复为最近 12 期的连续索引。