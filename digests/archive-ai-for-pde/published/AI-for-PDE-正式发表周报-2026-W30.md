# AI for PDE / AI for Science 正式发表论文周报 · 2026-W30

- **检索范围（UTC）**：2023-07-20 至 2026-07-20
- **运行日期**：2026-07-20
- **候选论文数**：33
- **去重后候选数**：18
- **正式状态明确数**：11
- **核心入选**：10
- **扩展入选**：1
- **arXiv 正式状态更新**：0
- **待人工确认**：4

## 本期概览

本期重点是 2026 年正式发表的神经算子与混合科学计算方法。新增工作覆盖 Nature Machine Intelligence、Nature Computational Science、Journal of Computational Physics、Computer Methods in Applied Mechanics and Engineering、SIAM Journal on Scientific Computing 与 npj Computational Materials，来源横跨 Springer Nature、Elsevier 和 SIAM。方法主线包括：将神经算子嵌入有限元或迭代求解器、自由边界问题、可复用局部算子、主动学习与预测不确定性、POD/多保真降阶以及系统级稳定性和分岔分析。

## 本期重点关注

1. **NOEM**：把可复用神经算子作为有限元单元级计算模块，兼顾 FEM 的结构性与学习代理的速度，对构建可插拔 PDE 专家模块具有直接启发。
2. **Enabling local neural operators to perform equation-free system-level analysis**：将局部神经算子从时间推进代理扩展到固定点、稳定性和分岔分析，说明学习算子可进一步承担“数值分析器”角色。
3. **MD-PNOP**：将神经算子预测嵌入传统迭代求解器，并在 Boltzmann 输运测试中保持物理保真度，契合“模型提供先验、数值求解器负责校正”的混合路线。
4. **Active operator learning with predictive uncertainty quantification**：把误差/不确定性估计直接用于函数空间主动采样，适合昂贵 LPP-EUV 多物理仿真的数据生成规划。

## A. 核心入选论文

### 1. Enabling local neural operators to perform equation-free system-level analysis

- **正式链接**：https://doi.org/10.1038/s42256-026-01265-1
- **发表信息**：Nature Machine Intelligence，2026-07-15，正式期刊论文
- **作者/机构**：Gianluca Fabiani、Hannes Vandecasteele、Somdatta Goswami、Constantinos Siettos、Ioannis G. Kevrekidis 等
- **标签**：local neural operator；equation-free analysis；fixed point；stability；bifurcation
- **arXiv 状态**：存在相关预印本线索，但本期以出版商页面为正式证据
- **核心贡献**：使局部神经算子支持系统级固定点、稳定性与分岔分析，而非仅作为轨迹预测器。
- **方法要点**：从局部演化映射构造全局数值分析操作，并与方程无关的系统分析工具结合。
- **实验对象**：复杂时空动力系统与不可逆转变分析。
- **课题关联**：可迁移到等离子体稳态、失稳阈值和分岔点搜索，为 PDE 基座模型增加稳定性分析能力。
- **评分**：5（SciML/PDE）+2（可迁移物理）+3（创新/venue）= **10/10**。

### 2. Deep neural operator for free boundary problems

- **正式链接**：https://doi.org/10.1038/s42256-026-01233-9
- **发表信息**：Nature Machine Intelligence 8, 806–817 (2026)；2026-05-21
- **作者/机构**：Zongjia Long、Qi Zhou、Aiqing Zhu、Dong Dai、Yiqun Liu 等
- **标签**：free-boundary PDE；neural operator；topological conjugacy；moving interface
- **arXiv 状态**：未作为主要证据
- **核心贡献**：面向随解演化的未知边界建立深度神经算子框架。
- **方法要点**：利用拓扑共轭思想，把自由边界问题映射到更适合算子学习的表示空间。
- **实验对象**：具有移动界面或自由边界的 PDE。
- **课题关联**：直接对应激光烧蚀面、等离子体边界、相界面与变几何问题。
- **评分**：5+2+3=**10/10**。

### 3. NOEM: efficient and scalable finite element method enabled by reusable neural operators

- **正式链接**：https://doi.org/10.1038/s43588-026-00974-2
- **发表信息**：Nature Computational Science 6, 417–429 (2026)；2026-04-28
- **作者/机构**：Weihang Ouyang、Yeonjong Shin、Si-Wei Liu、Lu Lu 等
- **标签**：neural-operator element method；finite element；reusable operator；hybrid solver
- **核心贡献**：把训练好的局部神经算子复用为有限元单元计算组件，降低多尺度求解成本。
- **方法要点**：保持 FEM 的组装结构，以算子代理替代昂贵局部计算，实现跨网格/问题复用。
- **实验对象**：复杂多尺度 PDE 与有限元模拟。
- **课题关联**：对“基本算子专家预训练后可插拔接入全局求解器”的设计高度相关。
- **评分**：5+2+3=**10/10**。

### 4. Principled approaches for extending neural architectures to function spaces for operator learning

- **正式链接**：https://doi.org/10.1038/s42256-026-01267-z
- **发表信息**：Nature Machine Intelligence；2026-07-03
- **作者/机构**：Julius Berner、Miguel Liu-Schiaffini、Jean Kossaifi、Valentin Duruisseaux、Boris Bonev、Kamyar Azizzadenesheli、Anima Anandkumar
- **标签**：function-space architecture；operator learning；discretization consistency
- **核心贡献**：系统给出将有限维神经网络架构提升到函数空间算子架构的原则。
- **方法要点**：强调离散无关性、函数空间映射与架构扩展规则，为构造统一神经算子提供方法论。
- **实验对象**：多类算子学习基准。
- **课题关联**：直接支持跨网格、mesh、point cloud 的统一 PDE 基座模型设计。
- **评分**：5+1+3=**9/10**。

### 5. MD-PNOP: Equation-recast neural operators for minimal-data extrapolation and PDE solver acceleration

- **正式链接**：https://doi.org/10.1016/j.jcp.2026.114844
- **发表信息**：Journal of Computational Physics 557, 114844 (2026)；2026-07-15
- **作者/机构**：Qiyun Cheng、Md Hossain Sahadath、Huihua Yang、Shaowu Pan、Wei Ji
- **标签**：equation-recast operator；minimal data；iterative solver；Boltzmann transport
- **核心贡献**：以方程重构方式增强极少数据外推，并把神经算子嵌入迭代求解器。
- **方法要点**：神经网络提供高质量预测/初值，传统求解器维持物理保真和收敛性。
- **实验对象**：Boltzmann 输运方程等参数化 PDE。
- **课题关联**：直接适合辐射/粒子输运与非平衡等离子体求解器加速。
- **评分**：5+2+2=**9/10**。

### 6. Active operator learning with predictive uncertainty quantification for partial differential equations

- **正式链接**：https://doi.org/10.1016/j.jcp.2026.114791
- **发表信息**：Journal of Computational Physics 555, 114791 (2026)；2026-06-15
- **作者/机构**：Nick Winovich、Mitchell Daneker、Lu Lu、Guang Lin
- **标签**：active operator learning；predictive UQ；OOD；function-space sampling
- **核心贡献**：为神经算子提供预测不确定性，并据此主动选择新增仿真样本。
- **方法要点**：不确定性可泛化到分布外输入/函数空间，并驱动高价值样本采集。
- **实验对象**：参数化 PDE 代理与实时推断。
- **课题关联**：适合昂贵 EUV/LPP 数值数据集的主动生成和置信度控制。
- **评分**：5+2+2=**9/10**。

### 7. EquiNO: A physics-informed neural operator for multiscale simulations

- **正式链接**：https://doi.org/10.1016/j.jcp.2026.114745
- **发表信息**：Journal of Computational Physics 554, 114745 (2026)；2026-06-01
- **作者/机构**：Hamidreza Eivazi、Jendrik-Alexander Tröger、Stefan Wittek、Stefan Hartmann、Andreas Rausch
- **标签**：physics-informed neural operator；FE-OL；equilibrium；periodic BC；multiscale ROM
- **核心贡献**：将有限元与算子学习结合，并内生保持平衡关系与周期边界条件。
- **方法要点**：作为多尺度快速 ROM，相比 FE² 获得约三数量级加速。
- **实验对象**：多尺度材料与力学模拟。
- **课题关联**：对物理约束专家、局部微结构闭合和多尺度材料—等离子体耦合具有迁移价值。
- **评分**：5+1+2=**8/10**。

### 8. Information-Coupled neural operator for computational mechanics and parametric PDEs

- **正式链接**：https://doi.org/10.1016/j.cma.2026.118851
- **发表信息**：Computer Methods in Applied Mechanics and Engineering 453, 118851 (2026)；2026-05-01
- **作者/机构**：Yihan Chen、Wenbin Lu、Junnan Xu、Yuhang He、Wei Li、Jianwei Zheng
- **标签**：information-coupled neural operator；spectral-spatial fusion；computational mechanics
- **核心贡献**：耦合频域与空间域信息，在保留关键谱信息的同时控制计算复杂度。
- **方法要点**：跨域信息融合，兼顾全局频谱建模和局部空间特征。
- **实验对象**：计算力学与参数化 PDE。
- **课题关联**：可用于同时捕获等离子体全局模态与局部激波/边界层。
- **评分**：5+2+2=**9/10**。

### 9. PODNO: Proper Orthogonal Decomposition Neural Operators

- **正式链接**：https://doi.org/10.1137/25M1751372
- **发表信息**：SIAM Journal on Scientific Computing 48(3), C479–C504；在线发表 2026-05-11
- **作者/机构**：Zilan Cheng、Zhongjian Wang、Li-Lian Wang、Mejdi Azaiez；NTU、Bordeaux University 等
- **标签**：POD neural operator；oscillatory PDE；high frequency；ROM
- **核心贡献**：以数据适应的 POD 正交变换替代 FNO 的固定 Fourier 基，针对高频和色散问题。
- **方法要点**：POD 基构造积分核，并给出逼近理论与可复现实验。
- **实验对象**：高频、振荡和色散 PDE。
- **课题关联**：适合 EUV 波场、等离子体波和高频多尺度动力学。
- **评分**：5+2+2=**9/10**。

### 10. A multi-fidelity Bayesian neural operator for mechanics of spinodal metamaterial

- **正式链接**：https://doi.org/10.1038/s41524-026-02112-y
- **发表信息**：npj Computational Materials；2026-05-13
- **作者/机构**：Pu You、Hongshun Chen、Bahador Bahmani、Horacio D. Espinosa 等
- **标签**：multi-fidelity；Bayesian neural operator；nonlinear mechanics；inverse design
- **核心贡献**：融合多保真数据和贝叶斯神经算子，学习完整非线性应力—应变函数映射并支持逆设计。
- **方法要点**：低/高保真仿真联合训练，同时输出预测与不确定性。
- **实验对象**：spinodal metamaterial 非线性力学响应。
- **课题关联**：方法可迁移到多保真辐射流体/等离子体代理与不确定性量化。
- **评分**：4+1+3=**8/10**。

## B. 扩展入选论文

### 11. Neural Network Tearing and Interconnecting Methods for PDEs

- **正式链接**：https://doi.org/10.1137/25M1752055
- **发表信息**：SIAM Journal on Scientific Computing 48(3), C553–C578；在线发表 2026-06-17
- **作者/机构**：Young Jae Jeon、Hyea Hyun Kim；Kyung Hee University
- **类型**：framework / numerical method
- **标签**：domain decomposition；tearing and interconnecting；neural PDE solver
- **核心贡献**：将 tearing-and-interconnecting / 域分解思想与神经网络 PDE 求解结合。
- **方法要点**：通过子域计算和界面耦合改善复杂域可扩展性。
- **实验对象**：分域 PDE 数值求解。
- **课题关联**：可迁移到多区域、多材料和多边界 LPP-EUV 模型，但并非神经算子主线。
- **评分**：4+1+2=**7/10**，按方法框架列为扩展入选。

## 方向汇总

### 方向 A：AI 求解 PDE / Scientific Machine Learning

本期 10 篇核心论文均涉及算子学习、混合求解器、自由边界、函数空间架构或 PDE 数值分析，其中 NOEM、MD-PNOP、PODNO、EquiNO 和 ICNO 对用户 PDE 基座模型设计最有直接价值。

### 方向 B：代理模型、ROM、多保真与 UQ

Active operator learning、PODNO、EquiNO 与 multi-fidelity Bayesian neural operator 分别覆盖主动采样、POD 降阶、多尺度 ROM 和多保真贝叶斯建模。

### 方向 C：科学计算物理应用

覆盖计算力学、材料多尺度、Boltzmann 输运、高频色散 PDE 与自由边界问题。方法可迁移到流体、热、辐射和多物理场仿真。

### 方向 D：激光等离子体 / EUV / Vlasov / MHD

已专项检索 Physics of Plasmas、HEDP、PSST、PPCF、Nuclear Fusion、PRE/PRR、Optics Express、Optica、APL/JAP 与 Laser and Particle Beams。**本期无新增正式入选论文**：高相关条目主要已在 W29 或更早周报登记；其余候选多为纯实验、仅预印本、正式出版日期在未来，或与 AI/科学计算关系不足。MD-PNOP 的 Boltzmann 输运和 PODNO 的高频振荡 PDE 被归入可直接迁移的 A/C 方向。

## 按 venue 组覆盖说明

1. **顶刊/顶会组**：入选 Nature Machine Intelligence 3 篇、Nature Computational Science 1 篇；NeurIPS/ICML/ICLR/JMLR/TMLR 已检索，但本期未发现相对已有注册表的高置信新增正式记录。
2. **计算物理与科学计算组**：入选 JCP 3 篇、CMAME 1 篇、SISC 2 篇。CPC、CiCP、MLST、Engineering with Computers、Applied Mathematical Modelling、IJNME 已检索，但候选重复、相关度不足或缺乏完整正式元数据。
3. **AI for Science / 数据驱动科学组**：入选 npj Computational Materials 1 篇。Digital Discovery、Patterns、Communications Engineering、AIP Advances、APL Machine Learning 等已检索；相关条目多偏化学发现/实验流程，未达到本任务 PDE/科学计算相关阈值。
4. **等离子体/EUV/光学组**：已检索但无符合条件的新增论文，主要因高相关正式论文已在历史周报登记，或新候选仍只有预印本/未来卷期信息。

## 已有 arXiv 论文正式发表状态更新

本期未发现可在 `paper_registry.jsonl` 中高置信补全且不与既有字段冲突的新状态更新，计数为 **0**。

## 待人工确认论文

1. **Walsh-Hadamard neural operators for solving PDEs with discontinuous coefficients**，JCP，DOI 10.1016/j.jcp.2026.115124：出版商页面显示卷期日期为 2026-10-15，晚于本次运行日，不提前入库。
2. **TANTE: Time-adaptive operator learning via neural Taylor expansion**，JCP，DOI 10.1016/j.jcp.2026.115041：卷期日期为 2026-10-01；需等待正式 online publication date/版本记录确认。
3. **Predicting time-dependent flow over complex geometries using operator networks**，CMAME，DOI 10.1016/j.cma.2026.118931：出版商日期 2026-07-01，但需与历史 W26–W29 分周元数据进一步核对标题去重后再入库。
4. **From local interactions to global operators: Scalable Gaussian process operator for physical systems**，JCP，DOI 10.1016/j.jcp.2026.114785：正式状态明确，但需补全作者机构和与历史 Gaussian-process operator 条目的匹配核验。

## 本期未入选原因简述

- 仅有 arXiv 页面、无 DOI/venue/publisher 正式证据；
- 出版商页面显示的卷期日期晚于 2026-07-20，且未确认更早的 online publication date；
- 与科学计算关系偏弱，主要是通用化学/生物预测；
- 纯实验等离子体或光学论文，没有机器学习、代理模型或数值计算方法贡献；
- 与主注册表或 W24–W29 分周 JSONL 重复。
