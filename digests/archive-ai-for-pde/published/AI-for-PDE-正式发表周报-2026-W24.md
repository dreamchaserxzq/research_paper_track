# AI for PDE / AI for Science 正式发表论文周报

日期范围：2023-06-08 至 2026-06-08 UTC。第 7 期，2026-W24。

## 本期概览

- 候选论文：18 篇
- 去重后候选：14 篇
- 正式发表状态明确：11 篇
- 核心入选：7 篇
- 扩展入选：4 篇
- arXiv 匹配/元数据更新：0 篇
- 待人工确认：4 篇

## 本期重点关注

本轮继续按“正式发表 / 正式 proceedings 收录 / online first / accepted 且具备明确 venue 信息”的口径执行，排除仅 arXiv 预印本。本轮重点补查 ICML 2024 / PMLR Volume 235 中与 PDE、neural operator、PINN、physics-aware surrogate、神经多重网格、保守图神经求解器、PDE 数据生成相关的正式论文。

与上一期 NeurIPS 2024 偏“神经算子新架构 / 生成式 PDE / partial observation”的主题不同，本期更偏向 **可嵌入数值流程的工程化 SciML 方法**：PDE foundation pre-training、graph transformer neural operator、保守 GNN 求解器、神经算子预条件器、神经多重网格、物理感知递归卷积、低秩自适应 ROM、PDE 数据生成加速和参数化 PINN。

对 LPP-EUV 预脉冲智能求解而言，本期最重要的启发是：正式顶会论文已经明显从“单一网络拟合解场”转向“数值结构内嵌 + 可证明/可控求解模块 + 数据生成闭环”。这更符合你当前 FLASH/ECOGEN + 小样本高保真数据 + AI surrogate 的路线。

---

## 核心入选论文

### 1. DPOT: Auto-Regressive Denoising Operator Transformer for Large-Scale PDE Pre-Training
- 作者：Zhongkai Hao, Chang Su, Songming Liu, Julius Berner, Chengyang Ying, Hang Su, Anima Anandkumar, Jian Song, Jun Zhu
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:17616-17635，2024-07-21 至 2024-07-27
- 类型：foundation_model / original_method
- official_url：https://proceedings.mlr.press/v235/hao24d.html
- arXiv：未在本轮稳定确认
- 核心贡献：提出 auto-regressive denoising operator transformer，用于大规模 PDE 预训练。模型使用 Fourier attention，可扩展到最高约 0.5B 参数，并在 10+ PDE 数据集、10 万级轨迹上预训练。
- 方法要点：auto-regressive denoising pre-training + operator transformer + Fourier attention + large-scale PDE dataset pre-training。重点解决 PDE 数据长轨迹、多尺度、维度变化和下游任务迁移问题。
- 可迁移价值：对构建 LPP-EUV 预脉冲“多算例预训练 + 少量高保真微调”的 PDE foundation surrogate 有直接参考价值。尤其适合将 Navier-Stokes、辐射扩散、两相流、热传导等子问题统一到预训练框架中。
- 评分：9/10，core。

### 2. HAMLET: Graph Transformer Neural Operator for Partial Differential Equations
- 作者：Andrey Bryutkin, Jiahao Huang, Zhongying Deng, Guang Yang, Carola-Bibiane Schönlieb, Angelica I Aviles-Rivero
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:4624-4641，2024-07-21 至 2024-07-27
- 类型：original_method
- official_url：https://proceedings.mlr.press/v235/bryutkin24a.html
- arXiv：未在本轮稳定确认
- 核心贡献：提出 graph transformer neural operator，用模块化输入编码器把微分方程信息直接纳入求解过程，并适配任意几何和多种输入格式。
- 方法要点：graph transformer + modular input encoders + equation-aware operator learning。HAMLET 强调对复杂数据、噪声和有限数据场景的鲁棒性。
- 可迁移价值：适合处理 FLASH AMR / ECOGEN 网格、非规则液滴界面、轴对称 r-z 数据和多输入物理参数。相比规则网格 FNO，图结构方法更适合复杂几何。
- 评分：9/10，core。

### 3. Graph Neural PDE Solvers with Conservation and Similarity-Equivariance
- 作者：Masanobu Horie, Naoto Mitsume
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:18785-18814，2024-07-21 至 2024-07-27
- 类型：original_method
- official_url：https://proceedings.mlr.press/v235/horie24a.html
- arXiv：未在本轮稳定确认
- 核心贡献：提出兼具守恒律和 similarity-equivariance 的图神经 PDE 求解器，强调 GNN 与传统数值求解器之间的结构相似性。
- 方法要点：graph neural solver + conservation law + physical symmetry / similarity-equivariance。论文显示物理约束可显著改善未见空间域上的泛化。
- 可迁移价值：直接对应 LPP-EUV 中最关键的稳定性问题：质量、动量、能量和相分数守恒。对液滴界面、激波、非规则网格上的 surrogate 设计尤其有价值。
- 评分：9/10，core。

### 4. Neural operators meet conjugate gradients: The FCG-NO method for efficient PDE solving
- 作者：Alexander Rudikov, Vladimir Fanaskov, Ekaterina Muravleva, Yuri M. Laevsky, Ivan Oseledets
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:42766-42782，2024-07-21 至 2024-07-27
- 类型：original_method / solver_acceleration
- official_url：https://proceedings.mlr.press/v235/rudikov24a.html
- arXiv：未在本轮稳定确认
- 核心贡献：提出将 neural operator 用作 flexible conjugate gradient 的预条件器，而不是直接用神经网络替代 PDE 求解器。
- 方法要点：discretization-invariant neural operator + nonlinear preconditioner + flexible conjugate gradient。其训练目标和数据采样围绕“学习高效预条件器”设计。
- 可迁移价值：对辐射扩散、热传导、压力泊松方程、隐式时间推进等线性/非线性子求解器都有启发。LPP-EUV 代码中昂贵的隐式线性系统求解可考虑 neural preconditioner，而非端到端替代。
- 评分：9/10，core。

### 5. UGrid: An Efficient-And-Rigorous Neural Multigrid Solver for Linear PDEs
- 作者：Xi Han, Fei Hou, Hong Qin
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:17354-17373，2024-07-21 至 2024-07-27
- 类型：original_method / theory
- official_url：https://proceedings.mlr.press/v235/han24a.html
- arXiv：未在本轮稳定确认
- 核心贡献：提出 U-Net 与 Multigrid 原理结合的神经多重网格线性 PDE 求解器，并给出收敛性和正确性证明。
- 方法要点：U-Net + multigrid + residual loss + unsupervised training。重点不是黑箱拟合，而是将经典多重网格结构与神经网络表达结合。
- 可迁移价值：对辐射扩散、热传导和泊松型子问题非常相关。若未来在 JAX/FLASH surrogate 中替代部分线性求解步骤，UGrid 路线比纯 PINN 更可控。
- 评分：8/10，core。

### 6. PARCv2: Physics-aware Recurrent Convolutional Neural Networks for Spatiotemporal Dynamics Modeling
- 作者：Phong C.H. Nguyen, Xinlun Cheng, Shahab Azarfar, Pradeep Seshadri, Yen T. Nguyen, Munho Kim, Sanghun Choi, H.S. Udaykumar, Stephen Baek
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:37649-37666，2024-07-21 至 2024-07-27
- 类型：application / original_method
- official_url：https://proceedings.mlr.press/v235/nguyen24c.html
- arXiv：未在本轮稳定确认
- 核心贡献：扩展 physics-aware recurrent convolutions，用于非定常、快速瞬态和对流主导系统建模。
- 方法要点：differentiator-integrator architecture + advection-reaction-diffusion operators + hybrid integral solver。实验包括 Burgers、Navier-Stokes 和 shock-induced reaction problems。
- 可迁移价值：高度相关于 LPP-EUV 中的快速瞬态、强对流、激波、锐梯度和快速变形材料界面。可作为靶材形态时序预测或中后期流体 surrogate 的候选结构。
- 评分：8/10，core。

### 7. Accelerating PDE Data Generation via Differential Operator Action in Solution Space
- 作者：Huanshuo Dong, Hong Wang, Haoyang Liu, Jian Luo, Jie Wang
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:11395-11411，2024-07-21 至 2024-07-27
- 类型：data_generation / original_method
- official_url：https://proceedings.mlr.press/v235/dong24d.html
- arXiv：未在本轮稳定确认
- 核心贡献：提出 DiffOAS，通过在解空间中施加微分算子 action 来加速 PDE 数据生成，目标是降低神经算子训练数据生成成本。
- 方法要点：先获得少量基本 PDE 解，再组合这些解并施加微分算子生成新的高精度 PDE 数据点。论文报告 10,000 实例数据生成可达 300× 加速。
- 可迁移价值：正中你的数据瓶颈：高保真 LPP-EUV 仿真成本高。尽管该方法未必能直接处理强非线性 RHD，但“少量基解 + 物理算子 action 扩增数据”的思想值得用于低维子问题和可线性化近似模块。
- 评分：8/10，core。

---

## 扩展入选论文

### 8. Vectorized Conditional Neural Fields: A Framework for Solving Time-dependent Parametric Partial Differential Equations
- 作者：Jan Hagnberger, Marimuthu Kalimuthu, Daniel Musekamp, Mathias Niepert
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:17189-17223，2024-07-21 至 2024-07-27
- 类型：original_method
- official_url：https://proceedings.mlr.press/v235/hagnberger24a.html
- arXiv：未在本轮稳定确认
- 核心贡献：提出 Vectorized Conditional Neural Fields，把时间依赖参数化 PDE 的解表示为可条件化的神经场，并并行处理多个时空 query points。
- 方法要点：conditional neural field + initial-condition / parameter conditioning + attention over spatio-temporal queries。强调参数泛化、时空零样本超分辨率、连续时间外推和 1D/2D/3D 支持。
- 可迁移价值：适合将液滴形态、速度/密度/温度场表示为连续神经场，处理不同激光参数、不同初始液滴状态和不同时间采样。
- 评分：7/10，extended。

### 9. CoLoRA: Continuous low-rank adaptation for reduced implicit neural modeling of parameterized partial differential equations
- 作者：Jules Berman, Benjamin Peherstorfer
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:3565-3583，2024-07-21 至 2024-07-27
- 类型：reduced_order_model / original_method
- official_url：https://proceedings.mlr.press/v235/berman24b.html
- arXiv：未在本轮稳定确认
- 核心贡献：提出 Continuous Low Rank Adaptation，用少量离线轨迹预训练后，连续地在时间上自适应低秩权重，以快速预测新物理参数和新初值下的解场演化。
- 方法要点：continuous low-rank adaptation + implicit neural model + data-driven or equation-driven variational adaptation。强调数据稀缺场景和 Galerkin-optimal 近似。
- 可迁移价值：适合 LPP-EUV 参数扫描中的 reduced surrogate。可将激光能量、脉宽、焦斑、液滴半径等参数作为低秩适应条件。
- 评分：7/10，extended。

### 10. Parameterized Physics-informed Neural Networks for Parameterized PDEs
- 作者：Woojin Cho, Minju Jo, Haksoo Lim, Kookjin Lee, Dongeun Lee, Sanghyun Hong, Noseong Park
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:8510-8533，2024-07-21 至 2024-07-27
- 类型：original_method
- official_url：https://proceedings.mlr.press/v235/cho24b.html
- arXiv：未在本轮稳定确认
- 核心贡献：提出 Parameterized PINNs，通过显式编码 PDE 参数的 latent representation，避免每个参数点重复训练 PINN。
- 方法要点：parameter embedding / latent parameter representation + PINN residual learning。适用于需要在参数空间中多点评估的设计优化和 UQ 场景。
- 可迁移价值：可用于 LPP-EUV 参数化求解的早期原型，但对强非线性、多尺度和不连续界面问题仍需与神经算子、数值块或数据监督结合。
- 评分：7/10，extended。

### 11. Learning from Integral Losses in Physics Informed Neural Networks
- 作者：Ehsan Saleh, Saba Ghaffari, Tim Bretl, Luke Olson, Matthew West
- 机构：待从 OpenReview / Semantic Scholar 回填
- DOI：未分配 / 未确认
- Venue：ICML 2024，PMLR 235:43077-43111，2024-07-21 至 2024-07-27
- 类型：theory / training_method
- official_url：https://proceedings.mlr.press/v235/saleh24a.html
- arXiv：未在本轮稳定确认
- 核心贡献：研究 partial integro-differential equations 下 PINN integral loss 的训练偏差问题，并提出 delayed target 等修正方法。
- 方法要点：integral residual / partial integro-differential equations + deterministic sampling + double sampling + delayed target。测试包括奇异电荷 Poisson、Maxwell 弱解和 Smoluchowski coagulation。
- 可迁移价值：对辐射输运、碰撞积分、不透明度积分、非局域热流闭合等含积分算子的模型很关键。它提示不能简单用低样本 Monte Carlo 残差近似替代真实积分 loss。
- 评分：7/10，extended。

---

## 待人工确认 / 暂不入库论文

| 标题 | 当前状态 | 原因 | 建议 |
|---|---|---|---|
| Positional Knowledge is All You Need: Position-induced Transformer (PiT) for Operator Learning | ICML 2024 / PMLR 正式收录 | 与 operator learning 相关，但对 PDE 和物理求解器的直接性弱于本期入选条目 | 后续若构建 Transformer operator 方法谱系，可补录 |
| Gaussian Plane-Wave Neural Operator for Electron Density Estimation | ICML 2024 / PMLR 正式收录 | 与电子密度估计相关，但偏分子/材料电子结构，离 LPP-EUV PDE surrogate 主线较远 | 作为材料/电子结构 surrogate 背景跟踪 |
| Hierarchical Neural Operator Transformer with Learnable Frequency-aware Loss Prior for Arbitrary-scale Super-resolution | ICML 2024 / PMLR 正式收录 | 题目相关，但偏图像/超分辨率，未优先入选 | 若后续关注多分辨率场重建，可补录 |
| Learning Physical Operators using Neural Operators | arXiv-only，未确认正式 venue | 与 operator splitting 和物理算子学习高度相关，但本轮未确认正式发表 | 持续跟踪，正式发表后优先入库 |

---

## venue 覆盖说明

- 本轮主覆盖：ICML 2024 / PMLR Volume 235。
- 重点主题：PDE foundation model、graph transformer neural operator、physics-aware recurrent surrogate、conservative GNN PDE solver、neural multigrid、neural preconditioner、PDE data generation、parameterized PINN。
- 与上一期差异：上一期主要补 NeurIPS 2024，本期主要补 ICML 2024，减少对 arXiv 线索的依赖，优先选择 PMLR 正式页面可验证条目。
- DOI 情况：PMLR 条目通常以 proceedings URL、PMLR volume/page 和 BibTeX 作为正式元数据，本轮未强行填 DOI；统一标为“未分配 / 未确认”。

## 对当前课题的直接启示

1. **数据生成本身需要成为研究对象。** DiffOAS 显示 PDE 数据生成可以用数学结构加速，而不是一味堆高保真模拟。你的 LPP-EUV 数据稀缺问题可拆成“可结构化扩增的子问题”和“必须高保真模拟的核心样本”。

2. **神经网络更适合作为求解器组件，而非完全替代求解器。** FCG-NO、UGrid、Graph Neural PDE Solvers 都体现了这一趋势：神经网络可以做预条件器、多重网格模块、保守通量映射或校正项。

3. **守恒性和对称性要前置设计。** 对液滴靶材演化、两相流和辐射流体问题，质量/动量/能量守恒、界面物理、轴对称几何约束不能只靠后处理修正。

4. **大规模 PDE 预训练值得关注，但应与多物理子系统拆解结合。** DPOT 代表 PDE foundation model 方向，但 LPP-EUV 的强耦合、材料物性和辐射/热传导刚性意味着更适合“子系统预训练 + 耦合微调”而不是单模型全吞。

5. **PINN 应作为局部约束工具，而非主求解框架。** Parameterized PINN 和 integral loss 论文说明 PINN 仍有价值，但它更适合参数化小问题、局部残差约束、低阶子模块或后验修正，不宜直接承担完整 RHD + 两相流主求解。

## 未入选原因

未入选主要原因包括：仅为 arXiv 预印本；缺少正式 venue；正式页面未给出足够的 PDE / SciML 相关性；偏图像超分辨率、材料电子结构或通用 ML 方法而非 PDE 求解主线；或虽与 operator learning 相关但相对本期入选论文优先级较低。
