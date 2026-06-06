# AI for PDE 正式发表论文周报 · 2026-W23

> 执行时间：2026-06-06  
> 检索口径：过去三年内正式发表、正式 proceedings 收录、online first / accepted 且具备明确 venue 信息的论文；排除仅 arXiv 预印本。  
> 本轮重点：AI for PDE、神经算子、PDE 生成式代理、科学计算 surrogate、光学/等离子体相关计算。

## 1. 本轮结论

本轮以正式出版源为准，重点补查 NeurIPS 2024 proceedings 中与 PDE / neural operator / physics simulation 直接相关的条目，并对已有记录做 venue 与 DOI 修正。

- 候选检查：31 篇
- 去重后候选：20 篇
- 正式发表状态明确：12 篇
- 本轮新增入选：9 篇
- 已有记录但元数据修正：3 篇
- arXiv-only，暂不入选：3 篇

本轮最大变化不是发现全新期刊论文，而是确认一批原先只以 arXiv/会议元数据记录的 NeurIPS 2024 正式 proceedings 条目。对后续研究更有价值的是：这些论文集中覆盖 **低数据 PDE 求解、神经算子效率、非线性 PDE 多解、PDE 生成模型、稀疏观测/数据同化、光学场仿真**，比单纯 Nature/Science AI-for-weather 论文更贴近你当前的 AI for PDE 方法储备。

## 2. 核心入选论文

| # | 论文 | Venue | DOI | 方向 | 评分 | 入选理由 |
|---|---|---|---|---|---:|---|
| 1 | P$^2$C$^2$Net: PDE-Preserved Coarse Correction Network for efficient prediction of spatiotemporal dynamics | NeurIPS 2024 | 10.52202/079017-2201 | A/B | 9 | 将高阶数值格式、边界条件编码与神经校正结合；少量轨迹即可在粗网格上预测复杂反应扩散与湍流动力学。Hao Sun 参与，与你此前关注的人和方向高度相关。 |
| 2 | Alias-Free Mamba Neural Operator | NeurIPS 2024 | 10.52202/079017-1678 | A | 9 | 将 Mamba 状态空间机制引入神经算子，目标是以 O(N) 复杂度替代 FNO/GNO/Transformer 的更高复杂度积分结构；适合关注大尺度 PDE 代理的效率瓶颈。 |
| 3 | Newton Informed Neural Operator for Solving Nonlinear Partial Differential Equations | NeurIPS 2024 | 10.52202/079017-3839 | A | 9 | 学习 Newton 非线性迭代映射，面向多解/分岔附近非线性 PDE；比普通端到端代理更接近“数值算法 + 学习模块”的混合路径。 |
| 4 | DiffusionPDE: Generative PDE-Solving under Partial Observation | NeurIPS 2024 | 10.52202/079017-4140 | A/B | 8 | 用扩散模型同时补全缺失系数/场信息并求解 PDE，直接对应稀疏诊断、反问题和不完全观测场景。 |
| 5 | PACE: Pacing Operator Learning to Accurate Optical Field Simulation for Complicated Photonic Devices | NeurIPS 2024 | 10.52202/079017-2156 | B/C | 8 | 面向复杂光子器件全场仿真的 operator learning；虽不是 LPP-EUV plasma，但与 EUV 光学、电磁场快速代理和逆设计方法链条相关。 |
| 6 | How does PDE order affect the convergence of PINNs? | NeurIPS 2024 | 10.52202/079017-0003 | A | 8 | 从理论上解释 PDE 阶数升高导致 PINN 梯度流更难收敛，并给出变量分裂降低 PDE 阶数的思路；对高阶/刚性方程建模有方法论价值。 |

## 3. 扩展入选论文

| # | 论文 | Venue | DOI | 方向 | 评分 | 入选理由 |
|---|---|---|---|---|---:|---|
| 7 | AROMA: Preserving Spatial Structure for Latent PDE Modeling with Local Neural Fields | NeurIPS 2024 | 10.52202/079017-0431 | A/B | 7 | 用局部 neural fields 与 attention 构建低维时空动力学表示，适合不规则网格、点云和复杂几何 PDE。 |
| 8 | On conditional diffusion models for PDE simulations | NeurIPS 2024 | 10.52202/079017-0732 | A/B | 7 | 系统比较条件/后验条件扩散模型在 PDE 预测和稀疏观测同化中的作用，对生成式 PDE solver 设计有参考价值。 |
| 9 | Space-Time Continuous PDE Forecasting using Equivariant Neural Fields | NeurIPS 2024 | 10.52202/079017-2438 | A | 7 | 以等变 neural fields 做连续时空 PDE 预测，强调几何对称性保持、空间/时间外推和复杂几何泛化。 |

## 4. 已有记录的正式元数据修正

| 论文 | 原问题 | 本轮修正 |
|---|---|---|
| Latent Neural Operator for Solving Forward and Inverse PDE Problems | 之前记录为 ICLR 2025 / arXiv 辅助，venue 不准确 | 修正为 NeurIPS 2024 Main Conference，DOI：10.52202/079017-1042，official_url 指向 NeurIPS proceedings。 |
| Data-Efficient Operator Learning via Unsupervised Pretraining and In-Context Learning | 之前 official_url 仍为 arXiv，DOI 缺失 | 修正为 NeurIPS 2024 Main Conference，DOI：10.52202/079017-0201，official_url 指向 NeurIPS proceedings。 |
| The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning | 之前 official_url / DOI 缺失 | 修正为 NeurIPS 2024 Datasets and Benchmarks Track，DOI：10.52202/079017-1430，official_url 指向 NeurIPS proceedings。 |

## 5. arXiv-only，暂不入选但建议后续跟踪

| 论文 | 当前状态 | 跟踪理由 |
|---|---|---|
| A radiation two-phase flow model for simulating plasma-liquid interactions | arXiv-only，未确认正式 venue | 直接命中 LPP-EUV 预脉冲锡液滴两相辐射流体建模；一旦正式发表，应优先入库。 |
| Multi-Diagnostic Characterization of Laser-Produced Tin Plasmas for EUV Lithography | arXiv-only，未确认正式 venue | 涉及 Sn 等离子体 Thomson scattering、干涉诊断和 EUV 光谱，适合作为实验验证背景。 |
| Optimization of EUV output by experimentally validated radiation-hydrodynamic simulations across a broad laser parameter space | arXiv-only，未确认正式 venue | 14 万组 STAR-1D 参数搜索、EUV-CE 优化，若正式发表将是 LPP-EUV 参数优化的重要参考。 |

## 6. 对当前课题的直接启示

1. **优先关注“数值格式内嵌 + 神经校正”路线。** P$^2$C$^2$Net 和 Newton Informed Neural Operator 都不是纯黑箱神经算子，而是把传统数值求解结构作为骨架，再学习校正或迭代映射。这对 LPP-EUV 预脉冲这类强刚性、多尺度、多物理耦合问题更稳健。

2. **生成式 PDE solver 更适合稀疏观测与反问题。** DiffusionPDE 和 conditional diffusion PDE simulations 都指向同一趋势：当边界、源项、物性、初始状态或诊断信息不完整时，生成模型可以同时处理补全与求解。这与实验诊断稀缺的激光等离子体场景高度一致。

3. **Mamba/SSM 神经算子值得持续跟踪，但不能直接替代物理约束。** Alias-Free Mamba Neural Operator 的 O(N) 复杂度很有吸引力，但对 LPP-EUV 这类守恒律、激波、界面、辐射扩散耦合问题，仍需要非负性、守恒性、边界条件和物理量纲约束共同保证长期稳定。

4. **PINN 的理论局限需要提前规避。** PDE 阶数越高、维度越高，PINN 越容易训练困难；变量分裂、算子分裂、低阶系统重写和混合数值块会比直接把完整高阶 PDE 残差塞入 loss 更可靠。

## 7. 本轮更新文件

- 新建：`digests/published/AI-for-PDE-正式发表周报-2026-W23.md`
- 更新：`metadata/published_papers.jsonl`
- 更新：`run_log_published.md`
- 未直接替换：`README.md`。原因：README 当前包含长历史日报区块，contents API 需要整文件替换；为避免误覆盖历史内容，本轮仅在周报与 run_log 中记录正式发表周报状态。
