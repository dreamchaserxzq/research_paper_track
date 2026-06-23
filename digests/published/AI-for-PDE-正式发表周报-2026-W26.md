# AI for PDE / AI for Science 正式发表论文追踪周报 · 2026-W26（复核更新）

> 检索范围：2023-06-23 至 2026-06-23 UTC  
> 执行日期：2026-06-23  
> 说明：本文件覆盖 2026-06-22 的同周初始版本。按同一 ISO 周幂等规则更新，不创建重复周报。

## 1. 本期概览

本轮对 W26 初始检索进行了 venue 分层复核。正式发表证据优先采用出版商论文页、DOI、卷期页码或 article number、online publication date；arXiv 仅用于题名与作者辅助匹配，不作为正式入选依据。

- 初始候选论文：31 篇
- 去重后候选：29 篇
- 三年窗口内且正式状态明确：17 篇
- 核心入选：10 篇
- 扩展入选：2 篇
- arXiv → 正式发表高置信匹配：4 篇
- 待后续确认：5 篇

与 6 月 22 日的初始版本相比，本次通过直接检索 SISC 卷期页、JCP/CMAME 正式 article 页面及 Physics of Plasmas 专题页面，补回了此前漏检的正式论文。

## 2. 结论先行

本期最值得优先精读的五项工作是：

1. **Neural Network Tearing and Interconnecting Methods for PDEs**：将经典 tearing-and-interconnecting 域分解转化为可并行训练的神经子域求解器，对多物理模块耦合和界面问题最直接。
2. **Hybrid deep learning and iterative methods for accelerated solutions of viscous incompressible flow**：DeepONet 只预测迭代搜索方向，CG/PCG 保证最终鲁棒性，代表“AI 加速传统求解器而非完全替代”的工程路线。
3. **diffSPH**：提供可微分 SPH、GPU 和 solver-in-the-loop 能力，可迁移到运动界面、液滴变形与两相流建模。
4. **HyMeshAI**：面向动态三维 AMR 的学习式网格生成，对 FLASH AMR 数据处理和未来自适应采样有直接启发。
5. **Active operator learning with predictive uncertainty quantification**：将预测不确定性用于算子学习主动采样，适合高成本 FLASH/ECOGEN 数据生成闭环。

## 3. 核心入选论文

### 1. Neural Network Tearing and Interconnecting Methods for PDEs
- 作者：Young Jae Jeon, Hyea Hyun Kim
- Venue：SIAM Journal on Scientific Computing
- 正式发表日期：2026-06-17
- DOI：10.1137/25M1752055
- 类型：original_method
- 核心贡献：提出面向椭圆 PDE 的神经网络 tearing-and-interconnecting 方法；子域网络可独立并行训练，通过迭代接口更新与预条件实现耦合，并给出收敛分析。
- 对当前研究的价值：适合多物理模块、材料界面和非重叠域分解；可作为 hydro、conduction、radiation 等神经子求解器耦合的理论参考。
- 评分：9/10，core。

### 2. Multiscale Neural Networks for Approximating Green’s Functions
- 作者：Wenrui Hao, Rui Peng Li, Yuanzhe Xi, Tianshi Xu, Yahong Yang
- Venue：SIAM Journal on Scientific Computing
- 正式发表日期：2026-04-06
- DOI：10.1137/24M1709601
- 类型：original_method
- 核心贡献：使用多尺度神经网络逼近低正则 Green 函数，并通过多尺度 Barron 空间分析说明其可减小网络规模、加速固定算子 PDE 的训练与求解。
- 对当前研究的价值：对重复调用的扩散、传导和椭圆型子算子具有参考价值，也可用于构造局部快速响应核。
- 评分：8/10，core。

### 3. Rank-Inspired Neural Network for Solving Partial Differential Equations
- 作者：Wentao Peng, Yunqing Huang, Nianyu Yi
- Venue：SIAM Journal on Scientific Computing
- 正式发表日期：2026-05-06
- DOI：10.1137/25M1769995
- 类型：original_method
- 核心贡献：RINN 在 physics-informed extreme learning machine 前加入基于协方差结构的正交化和预处理阶段，降低随机初始化敏感性，再以最小二乘方式施加 PDE 约束。
- 对当前研究的价值：适合作为低成本子问题或快速基线；论文获得 SIAM 代码与数据可复现徽章。
- 评分：8/10，core。

### 4. Active operator learning with predictive uncertainty quantification for partial differential equations
- 作者：Nick Winovich, Mitchell Daneker, Lu Lu, Guang Lin
- Venue：Journal of Computational Physics
- 正式发表日期：2026-06-15
- DOI：10.1016/j.jcp.2026.114791
- 类型：original_method
- 核心贡献：为 DeepONet/FNO 构建轻量预测不确定性框架，可估计分布外误差，并驱动函数空间中的主动学习、贝叶斯优化和快速推理。
- 对当前研究的价值：可用于决定下一批 FLASH/ECOGEN 高保真算例应在哪些参数区间生成，从而形成主动数据闭环。
- 评分：9/10，core。
- arXiv：2503.03178

### 5. A flow-aware training strategy for physics-informed neural networks
- 作者：Pietro Cestola, Luciano Teresi, Antonio De Simone
- Venue：Computer Methods in Applied Mechanics and Engineering
- 正式发表日期：2026-06-15
- DOI：10.1016/j.cma.2026.118910
- 类型：original_method
- 核心贡献：根据物理信息流把计算域划分为测地子域，并按训练阶段逐步激活监督，避免在边界或初值信息尚未传播到的区域产生误导梯度。
- 对当前研究的价值：对具有强对流、传播时延、激波和因果结构的瞬态 RHD/PDE 训练具有直接意义。
- 评分：9/10，core。

### 6. A machine learning method for solving PDEs with a robust initial learning rate based on Lagrange multiplier optimization
- 作者：Jianghua Liu, Jin Zhao, Xuan Zhao, Xiaoli Li
- Venue：Journal of Computational Physics
- 正式发表日期：2026-06-01
- DOI：10.1016/j.jcp.2026.114750
- 类型：original_method
- 核心贡献：基于 Lagrange 乘子和标量辅助变量能量下降思想，为神经 PDE 求解器构造可采用较大初始步长的稳健优化方法。
- 对当前研究的价值：对缓解 PINN/无数据神经求解器的学习率敏感和训练停滞具有方法参考价值。
- 评分：8/10，core。

### 7. Convolution-weighting method for the physics-informed neural network: A primal-dual optimization perspective
- 作者：Chenhao Si, Ming Yan
- Venue：Journal of Computational Physics
- 正式发表日期：2026-06-15
- DOI：10.1016/j.jcp.2026.114773
- 类型：original_method
- 核心贡献：从原始—对偶优化视角提出 CWP-PINN，将孤立点残差权重扩展为空间邻域内连续、卷积式的自适应权重。
- 对当前研究的价值：有助于在锐梯度、局部高残差和不均匀采样区域形成更平滑稳定的训练信号。
- 评分：8/10，core。
- arXiv：2506.19805

### 8. diffSPH: Differentiable smoothed particle hydrodynamics for hybrid machine learning solutions in fluid mechanics
- 作者：Rene Winchenbach, Nils Thuerey
- Venue：Journal of Computational Physics
- 正式发表日期：2026-06-15
- DOI：10.1016/j.jcp.2026.114769
- 类型：framework
- 核心贡献：提供基于 PyTorch/GPU 的开源可微 SPH 框架，覆盖可压缩、弱可压缩和不可压缩流动，可用于反问题、优化和 solver-network 混合建模。
- 对当前研究的价值：与运动界面、液滴变形、多相流和 solver-in-the-loop 学习直接相关，可作为 ECOGEN 阶段之外的重要可微原型路线。
- 评分：9/10，core。
- arXiv：2507.21684

### 9. Hybrid deep learning and iterative methods for accelerated solutions of viscous incompressible flow
- 作者：Heming Bai, Xin Bian
- Venue：Journal of Computational Physics
- 正式发表日期：2026-06-01
- DOI：10.1016/j.jcp.2026.114747
- 类型：solver_acceleration
- 核心贡献：HyDEA 使用 DeepONet 预测压力 Poisson 方程迭代搜索方向，再由 CG/PCG 解析细尺度误差并保证稳健收敛；强调跨几何、跨雷诺数和跨分辨率泛化。
- 对当前研究的价值：是“神经预条件/搜索方向 + 经典迭代修正”路线的直接范例，可迁移到辐射扩散、电子热传导和压力类隐式线性系统。
- 评分：9/10，core。
- arXiv：2506.03016

### 10. HyMeshAI: Deep learning enabled three-dimensional adaptive mesh generator for high-resolution atmospheric simulations
- 作者：Pu Gan, Jinxi Li, Fangxin Fang, Xiaofei Wu, Jiang Zhu, Zifa Wang, Mingming Zhu, Xun Zou
- Venue：Journal of Computational Physics
- 正式发表日期：2026-06-01
- DOI：10.1016/j.jcp.2026.114760
- 类型：framework
- 核心贡献：组合 CNN 网格密度预测与 ANN 节点定位，实现面向不规则几何、可变网格规模和三维动态 AMR 的端到端学习式网格生成。
- 对当前研究的价值：对 FLASH AMR 网格、液滴附近动态加密、学习辅助误差指示和自适应采样具有直接启发。
- 评分：8/10，core。

## 4. 扩展入选论文

### 11. Noise-robust multi-fidelity surrogate modelling for parametric partial differential equations
- 作者：Benjamin M. Kent, Lorenzo Tamellini, Matteo Giacomini, Antonio Huerta
- Venue：Journal of Computational Physics
- 正式发表日期：2026-06-01
- DOI：10.1016/j.jcp.2026.114761
- 类型：original_method
- 核心贡献：针对低保真 PDE 评估中由粗网格、松弛容差和瞬态误差引入的噪声，构建稳健的多指标随机配置代理模型。
- 对当前研究的价值：适合融合不同网格、不同物理配置和不同求解精度的 FLASH/ECOGEN 数据；包含对流—扩散和湍流不可压 Navier–Stokes 测试。
- 评分：7/10，extended。

### 12. A review of machine learning-driven studies of tearing modes in tokamaks
- 作者：C. Rea, S. Benjamin
- Venue：Physics of Plasmas
- 正式发表日期：2026-05-12
- DOI：10.1063/5.0325461
- 类型：review
- 核心贡献：综述机器学习在 tokamak 撕裂模物理解释、起始预测和实时控制中的应用，并强调物理分析、多装置数据库及跨工况验证。
- 对当前研究的价值：虽然不是 LPP-EUV 直接问题，但其“高保真模拟 + 实验诊断 + 物理约束 ML + 控制”的方法体系对等离子体智能建模具有借鉴意义。
- 评分：7/10，extended。

## 5. 按研究方向归纳

### A. AI 求解 PDE / 神经科学计算
本期包括神经网络域分解、Green 函数学习、RINN、流感知 PINN、卷积加权 PINN、稳健学习率优化及主动算子学习。共同趋势是将优化结构、因果传播、子域接口、误差估计或经典数值结构显式嵌入网络训练。

### B. 混合求解器、代理模型与数据闭环
HyDEA、active operator learning 和 noise-robust multi-fidelity surrogate 表明，当前更具工程可行性的路线是让学习模块承担预条件、初值、误差估计、主动采样或低保真校正，而由传统迭代器维持物理一致性与收敛可靠性。

### C. 流体、动态网格与运动界面
diffSPH 和 HyMeshAI 分别覆盖可微粒子流体与学习式 AMR。它们对液滴界面、网格变化、跨分辨率泛化及反问题优化具有较强迁移价值。

### D. 等离子体 / MHD
Physics of Plasmas 的撕裂模综述系统总结了 ML 在 tokamak tearing-mode 解释、预测和控制中的应用。虽然不是 LPP-EUV 直接场景，但其高保真模拟、实验诊断、物理约束 ML 和实时控制框架值得借鉴。

## 6. arXiv 正式状态匹配

本期确认以下高置信匹配，并写入独立状态补丁文件：

- arXiv:2503.03178 → JCP, DOI 10.1016/j.jcp.2026.114791
- arXiv:2506.19805 → JCP, DOI 10.1016/j.jcp.2026.114773
- arXiv:2507.21684 → JCP, DOI 10.1016/j.jcp.2026.114769
- arXiv:2506.03016 → JCP, DOI 10.1016/j.jcp.2026.114747

## 7. 未入选与待确认

以下条目未写入正式入选元数据：

1. **MD-PNOP**：正式 JCP 页面和 DOI 已存在，但卷期标注日期为 2026-07-15，晚于本次执行日期；保留为下一期重点核验对象。
2. **Walsh-Hadamard Neural Operators**：正式页面给出的卷期日期为 2026-10-15，当前不按未来日期入库。
3. **TANTE**、inverse-scattering-inspired FNO、learning hidden physics 等条目：主题高度相关，但本轮未稳定获得完整 DOI、online publication date 或卷期信息。
4. 若干 MLST、CPC、Optics/EUV 结果为预印本、会议摘要或弱相关应用，未用于凑数。
5. 与 W23-W25 既有正式记录重复的条目已按 DOI、arXiv ID 和规范化标题去重。

## 8. 本期判断

本轮修正表明，W26 初始“零入选”主要是检索覆盖不足，而不是该时间段缺少正式成果。近期正式发表工作的主线非常清晰：**域分解与接口耦合、神经预条件/混合迭代、主动学习与 UQ、可微分物理求解器、以及学习辅助 AMR**。这些方向与当前 FLASH/ECOGEN + 分模块代理模型路线高度一致。
