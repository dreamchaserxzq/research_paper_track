# AI for PDE / AI for Science 正式发表论文追踪周报 · 2026-W29

## 本期概览

- 检索范围：2023-07-13 至 2026-07-13 UTC
- 候选论文数：31
- 去重后候选数：19
- 正式发表或正式接收状态明确数：12
- 核心入选：11
- 扩展入选：1
- arXiv 状态更新：0
- 待人工确认：5

本期以仓库主注册表和 W24–W28 分周元数据为去重基线，重点补齐此前已完成出版证据核验、但尚未进入主注册表的计算物理与等离子体方向记录。来源覆盖 Elsevier、SIAM、AIP Publishing、Cambridge University Press 和 Optica Publishing Group。

## 本期重点关注

1. **A physics-constrained deep learning treatment of runaway electron dynamics**：将 PINN 用于参数化伴随相对论 Fokker–Planck 问题，直接服务托卡马克逃逸电子动力学代理。
2. **Neural-Integrated Meshfree (NIM) Method**：把可微分神经表示与无网格离散和变分残差结合，代表传统数值方法与神经求解器融合路线。
3. **Finite Element Operator Network** 与 **Orthogonal Polynomial Neural Operator**：分别从有限元系数映射和非周期边界条件处理角度提升神经算子的数值结构一致性。

## 核心入选论文

### 1. Derivative-Informed Neural Operator: An efficient framework for high-dimensional parametric derivative learning

- 正式链接：https://doi.org/10.1016/j.jcp.2023.112555
- DOI：10.1016/j.jcp.2023.112555
- 发表信息：Journal of Computational Physics, 2024-01-01, 496, 112555
- 作者/机构：Thomas O'Leary-Roseberry, Peng Chen, Umberto Villa, Omar Ghattas；The University of Texas at Austin
- 标签：derivative-informed neural operator；parametric PDE；inverse problem；optimization；surrogate
- arXiv 版本状态：arXiv:2206.10745，作为辅助匹配
- 核心贡献：Derivative-informed neural operators learn both parametric PDE maps and their derivatives, using low-rank compression to reduce derivative-data and training costs.
- 方法要点：围绕 derivative-informed neural operator、parametric PDE、inverse problem 构建正式发表的方法或应用框架。
- 实验对象：A 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：直接相关。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 5/5；物理迁移 2/2；创新与 venue 2/3；总分 9/10。

### 2. Out-of-distributional risk bounds for neural operators with applications to the Helmholtz equation

- 正式链接：https://doi.org/10.1016/j.jcp.2024.113168
- DOI：10.1016/j.jcp.2024.113168
- 发表信息：Journal of Computational Physics, 2024-10-01, 514, 113168
- 作者/机构：Jose Antonio Lara Benitez, Takashi Furuya, Florian Faucher, Anastasis Kratsios 等；机构信息待补全
- 标签：neural operator；out-of-distribution generalization；Helmholtz equation；wave propagation
- arXiv 版本状态：arXiv:2301.11509，作为辅助匹配
- 核心贡献：Transformer-inspired neural operators and out-of-distribution risk bounds for Helmholtz forward maps.
- 方法要点：围绕 neural operator、out-of-distribution generalization、Helmholtz equation 构建正式发表的方法或应用框架。
- 实验对象：A 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：方法可迁移。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 5/5；物理迁移 1/2；创新与 venue 2/3；总分 8/10。

### 3. Neural-Integrated Meshfree (NIM) Method: A differentiable programming-based hybrid solver for computational mechanics

- 正式链接：https://doi.org/10.1016/j.cma.2024.117024
- DOI：10.1016/j.cma.2024.117024
- 发表信息：Computer Methods in Applied Mechanics and Engineering, 2024-07-01, 427, 117024
- 作者/机构：Honghui Du, QiZhi He；University of Minnesota
- 标签：differentiable solver；meshfree method；computational mechanics
- arXiv 版本状态：arXiv:2311.12915，作为辅助匹配
- 核心贡献：Differentiable neural representations combined with meshfree partition-of-unity discretization and variational residual formulations.
- 方法要点：围绕 differentiable solver、meshfree method、computational mechanics 构建正式发表的方法或应用框架。
- 实验对象：A 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：直接相关。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 5/5；物理迁移 2/2；创新与 venue 2/3；总分 9/10。

### 4. D2NO: Efficient handling of heterogeneous input function spaces with distributed deep neural operators

- 正式链接：https://doi.org/10.1016/j.cma.2024.117084
- DOI：10.1016/j.cma.2024.117084
- 发表信息：Computer Methods in Applied Mechanics and Engineering, 2024-08-01, 428, 117084
- 作者/机构：Zecheng Zhang, Christian Moya, Lu Lu, Guang Lin 等；机构信息待补全
- 标签：distributed neural operator；heterogeneous sensors；DeepONet；multifidelity
- arXiv 版本状态：arXiv:2310.18888，作为辅助匹配
- 核心贡献：Distributed operator learning across heterogeneous input-function subsets and sensor layouts.
- 方法要点：围绕 distributed neural operator、heterogeneous sensors、DeepONet 构建正式发表的方法或应用框架。
- 实验对象：A 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：方法可迁移。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 5/5；物理迁移 1/2；创新与 venue 2/3；总分 8/10。

### 5. Finite Element Operator Network for Solving Elliptic-Type Parametric PDEs

- 正式链接：https://doi.org/10.1137/23M1623707
- DOI：10.1137/23M1623707
- 发表信息：SIAM Journal on Scientific Computing, 2025-04-01, 47, C501-C528
- 作者/机构：Jae Yong Lee, Seungchan Ko, Youngjoon Hong；Seoul National University
- 标签：finite element operator network；elliptic PDE；convergence analysis
- arXiv 版本状态：未发现必要 arXiv 匹配
- 核心贡献：Finite-element coefficient-map operator learning for parametric elliptic PDEs with convergence analysis.
- 方法要点：围绕 finite element operator network、elliptic PDE、convergence analysis 构建正式发表的方法或应用框架。
- 实验对象：A 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：直接相关。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 5/5；物理迁移 2/2；创新与 venue 2/3；总分 9/10。

### 6. Render unto Numerics: Orthogonal Polynomial Neural Operator for PDEs with Nonperiodic Boundary Conditions

- 正式链接：https://doi.org/10.1137/23M1556320
- DOI：10.1137/23M1556320
- 发表信息：SIAM Journal on Scientific Computing, 2024-07-12, 46, C323-C348
- 作者/机构：Ziyuan Liu, Haifeng Wang, Hong Zhang, Kaijun Bao 等；National University of Defense Technology
- 标签：orthogonal polynomial neural operator；spectral method；nonperiodic boundary conditions
- arXiv 版本状态：arXiv:2206.12698，作为辅助匹配
- 核心贡献：Orthogonal polynomial neural operator with exact treatment of nonperiodic Dirichlet, Neumann, and Robin boundary conditions.
- 方法要点：围绕 orthogonal polynomial neural operator、spectral method、nonperiodic boundary conditions 构建正式发表的方法或应用框架。
- 实验对象：A 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：直接相关。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 5/5；物理迁移 2/2；创新与 venue 2/3；总分 9/10。

### 7. The ADMM-PINNs Algorithmic Framework for Nonsmooth PDE-Constrained Optimization: A Deep Learning Approach

- 正式链接：https://doi.org/10.1137/23M1566935
- DOI：10.1137/23M1566935
- 发表信息：SIAM Journal on Scientific Computing, 2024-12-01, 46, C659-C687
- 作者/机构：Yongcun Song, Xiaoming Yuan, Hangrui Yue；机构信息待补全
- 标签：ADMM；PINN；PDE-constrained optimization；inverse problem
- arXiv 版本状态：arXiv:2302.08309，作为辅助匹配
- 核心贡献：ADMM separates nonsmooth regularization from smooth PDE-constrained optimization in a PINN framework.
- 方法要点：围绕 ADMM、PINN、PDE-constrained optimization 构建正式发表的方法或应用框架。
- 实验对象：A 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：方法可迁移。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 5/5；物理迁移 1/2；创新与 venue 2/3；总分 8/10。

### 8. Efficient PDE-Constrained Optimization Under High-Dimensional Uncertainty Using Derivative-Informed Neural Operators

- 正式链接：https://doi.org/10.1137/23M157956X
- DOI：10.1137/23M157956X
- 发表信息：SIAM Journal on Scientific Computing, 2025-08-01, 47
- 作者/机构：Dingcheng Luo, Thomas O'Leary-Roseberry, Peng Chen, Omar Ghattas；The University of Texas at Austin
- 标签：PDE-constrained optimization；uncertainty quantification；derivative-informed neural operator
- arXiv 版本状态：未发现必要 arXiv 匹配
- 核心贡献：Derivative-informed neural operators accelerate PDE-constrained optimization under high-dimensional uncertainty.
- 方法要点：围绕 PDE-constrained optimization、uncertainty quantification、derivative-informed neural operator 构建正式发表的方法或应用框架。
- 实验对象：B 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：直接相关。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 5/5；物理迁移 2/2；创新与 venue 2/3；总分 9/10。

### 9. A physics-constrained deep learning treatment of runaway electron dynamics

- 正式链接：https://doi.org/10.1063/5.0253370
- DOI：10.1063/5.0253370
- 发表信息：Physics of Plasmas, 2025-04-02, 32
- 作者/机构：Christopher J. McDevitt, Jonathan S. Arnaud, Xian-Zhu Tang；University of Florida, Los Alamos National Laboratory
- 标签：runaway electrons；Fokker-Planck equation；PINN；plasma surrogate
- arXiv 版本状态：arXiv:2412.12980，作为辅助匹配
- 核心贡献：A PINN solves a parametric adjoint relativistic Fokker-Planck problem for runaway-electron density dynamics.
- 方法要点：围绕 runaway electrons、Fokker-Planck equation、PINN 构建正式发表的方法或应用框架。
- 实验对象：D 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：直接相关。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 5/5；物理迁移 2/2；创新与 venue 3/3；总分 10/10。

### 10. A physics-constrained deep learning surrogate model of the runaway electron avalanche growth rate

- 正式链接：https://doi.org/10.1017/S0022377824000679
- DOI：10.1017/S0022377824000679
- 发表信息：Journal of Plasma Physics, 2024-08-01, 90, 905900409
- 作者/机构：Jonathan S. Arnaud, T. B. Mark, Christopher J. McDevitt；机构信息待补全
- 标签：runaway electron；avalanche growth；plasma surrogate
- arXiv 版本状态：未发现必要 arXiv 匹配
- 核心贡献：A physics-constrained neural surrogate estimates runaway-electron avalanche growth rates over plasma parameters.
- 方法要点：围绕 runaway electron、avalanche growth、plasma surrogate 构建正式发表的方法或应用框架。
- 实验对象：D 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：直接相关。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 4/5；物理迁移 2/2；创新与 venue 3/3；总分 9/10。

### 11. Fast and Generalizable Light Field Propagation Modelling in Optical Fiber by Physics-Informed Neural Operator

- 正式链接：https://doi.org/10.1364/CLEO_SI.2024.STh3J.4
- DOI：10.1364/CLEO_SI.2024.STh3J.4
- 发表信息：CLEO: Science and Innovations 2024, 2024-05-05, STh3J.4
- 作者/机构：Xiao Luo, Min Zhang, Yuchen Song, Xiaotian Jiang 等；Beijing University of Posts and Telecommunications
- 标签：physics-informed neural operator；light propagation；optical surrogate
- arXiv 版本状态：未发现必要 arXiv 匹配
- 核心贡献：An unsupervised physics-informed neural operator models optical-fiber light propagation across configurations.
- 方法要点：围绕 physics-informed neural operator、light propagation、optical surrogate 构建正式发表的方法或应用框架。
- 实验对象：C 方向中的 PDE、连续场或等离子体/光学科学计算任务。
- 与用户课题关联：直接相关。可用于 LPP-EUV 的代理建模、物理约束训练、参数优化、不确定性分析或混合数值求解器设计。
- 评分：AI+科学计算 4/5；物理迁移 2/2；创新与 venue 2/3；总分 8/10。

## 扩展入选论文

### 1. A review of machine learning-driven studies of tearing modes in tokamaks

- 类型：review；is_review=true
- 正式链接：https://doi.org/10.1063/5.0325461
- DOI：10.1063/5.0325461
- 发表信息：Physics of Plasmas, 2026-05-12
- 核心贡献：Review of machine-learning methods for tearing-mode interpretation, onset prediction, avoidance, suppression, and control.
- 与用户课题关联：直接相关。该综述系统梳理机器学习在 tokamak tearing mode / MHD 诊断、预测与控制中的应用。
- 评分：AI+科学计算 3/5；物理迁移 2/2；创新与 venue 2/3；总分 7/10。

## 方向 A：AI 求解 PDE / Scientific Machine Learning

本期入选包括 DINO、NIM、D2NO、有限元算子网络、正交多项式神经算子和 ADMM-PINNs，覆盖导数学习、无网格可微分求解、异构输入函数空间、有限元系数映射、非周期边界条件及非光滑 PDE 约束优化。

## 方向 B：代理模型、ROM 与科学仿真加速

本期包含高维不确定性下的 PDE 约束优化代理，以及等离子体逃逸电子增长率 surrogate。

## 方向 C：科学计算与物理系统应用

入选工作覆盖 Helmholtz 波动问题、计算力学、Boltzmann/Fokker–Planck 类输运问题与光场传播。

## 方向 D：激光等离子体 / EUV / Vlasov / MHD

本期重点为逃逸电子动力学、逃逸电子雪崩增长率代理和 tearing mode 机器学习综述；未发现可高置信新增的 EUV 光源或辐射流体力学正式论文。

## 按 venue 组的覆盖说明

- **顶刊/顶会组**：已检索但无新增符合条件论文。主要原因是相关高分论文已在 W23–W28 入库，新增结果多为 arXiv-only 或元数据重复。
- **计算物理与科学计算组**：入选 JCP、CMAME、SISC 共 8 篇，正式 DOI、卷/页码或 article number 明确。
- **AI for Science / 数据驱动科学组**：已检索但无新增符合条件论文。主要原因是高相关条目与既有 registry 重复，或相关性不足。
- **等离子体/EUV/光学组**：入选 Physics of Plasmas、Journal of Plasma Physics 与 Optica proceedings 共 4 篇；EUV 光源和辐射流体方向未发现新的高置信正式条目。

## 已有 arXiv 论文正式发表状态更新

本期未产生新的 registry 状态补丁。部分入选论文带有高置信 arXiv 辅助匹配，但其正式状态此前已确认。

## 待人工确认论文

1. A Runaway Electron Avalanche Surrogate for Partially Ionized Plasmas：仅确认 arXiv 版本，尚未发现正式 publisher/DOI 记录。
2. Surrogate Modeling of Landau Damping with Deep Operator Networks：仅确认 arXiv 版本。
3. The Machine Learning Approach to Moment Closure Relations for Plasma: A Review：正式 venue/DOI 未完成核验。
4. 两篇 2026 年 EUV/辐射输运神经算子候选：检索结果仅有预印本或 indexed date，未满足 publication_date 规则。

## 本期未入选原因简述

- 仅有 arXiv 页面，缺少 DOI、journal-ref、正式会议页或 publisher metadata；
- publication_date 无法与 deposited/indexed date 区分；
- 已存在于 W23–W28 分周元数据或主 published_papers.jsonl；
- 纯实验论文，AI/科学计算方法贡献不足；
- 与 PDE、连续场、科学仿真或用户课题的迁移价值不足。
