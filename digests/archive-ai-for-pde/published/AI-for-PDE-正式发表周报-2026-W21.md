# AI for PDE / AI for Science 正式发表论文周报

日期范围：2023-05-24 至 2026-05-24 UTC。第 4 期，放宽检索限制后重跑。

## 本期概览

- 候选论文：42 篇
- 去重后候选：24 篇
- 正式发表状态明确：10 篇
- 核心入选：6 篇
- 扩展入选：4 篇
- arXiv 匹配更新：4 篇
- 待人工确认：4 篇

## 本期重点关注

本次按“人工智能 + 科学计算 / AI for Science / Scientific Machine Learning”放宽检索，不再只保留狭义 AI for PDE 或 LPP-EUV 强相关论文。入选范围扩展到神经算子、可微分求解器、AI 天气与气候 surrogate、Boltzmann 动理学代理、材料科学机器学习势函数、主动学习材料发现与综述/框架类论文。

对用户课题而言，最重要的启发是：LPP-EUV 预脉冲智能求解不应只追踪等离子体方向论文，也应系统吸收天气/气候代理模型、材料机器学习势函数、Boltzmann/输运代理和神经算子综述中的方法论，例如可学习闭合、生成式不确定性量化、结构保持代理、主动学习数据生成和多尺度 surrogate。

---

## 核心入选论文

### 1. Neural general circulation models for weather and climate
- DOI：10.1038/s41586-024-07744-y
- Venue：Nature，2024-07-22，632:1060-1066
- 类型：original_method
- 核心贡献：NeuralGCM 将可微分大气动力学求解器与神经网络物理参数化耦合。
- 方法要点：differentiable dynamical core + learned physics module + 在线端到端训练。
- 可迁移价值：适合借鉴到辐射流体代码中，用神经网络学习电子热传导、辐射输运、EOS/opacity 校正等高成本闭合。
- 评分：10/10，core。

### 2. RelaxNet: A structure-preserving neural network to approximate the Boltzmann collision operator
- DOI：10.1016/j.jcp.2023.112317
- Venue：Journal of Computational Physics，2023
- 类型：original_method
- arXiv：2211.08149
- 核心贡献：提出结构保持神经网络代理 Boltzmann 碰撞算子，保持 positivity、conservation、invariance 与 H-theorem。
- 方法要点：用类 BGK relaxation 结构改造 ResNet，把昂贵五重碰撞积分替换为神经网络张量计算。
- 可迁移价值：对电子非平衡动力学、输运闭合、NLTE 动力学或动理学-流体耦合 surrogate 有直接参考价值。
- 评分：9/10，core。

### 3. Learning skillful medium-range global weather forecasting
- DOI：10.1126/science.adi2336
- Venue：Science，2023-12-22
- 类型：original_method
- 核心贡献：GraphCast 使用图神经网络进行全球中期天气预报，是高维连续场快速代理模型代表。
- 方法要点：基于球面图结构和时空消息传递建模大气场演化。
- 可迁移价值：图结构时空消息传递可迁移到非规则网格、AMR 数据或液滴靶材形态演化建模。
- 评分：9/10，core。

### 4. Accurate medium-range global weather forecasting with 3D neural networks
- DOI：10.1038/s41586-023-06185-3
- Venue：Nature，2023-07-05，619:533-538
- 类型：original_method
- arXiv：2211.02556
- 核心贡献：Pangu-Weather 用 3D Earth-specific Transformer 建模全球天气场演化。
- 方法要点：三维多变量场编码和 hierarchical temporal aggregation 控制自回归误差累积。
- 可迁移价值：可用于靶材形态时序预测、多变量物理场编码和长时程 rollout 稳定性设计。
- 评分：9/10，core。

### 5. Physics-Informed Neural Operator for Learning Partial Differential Equations
- DOI：10.1145/3648506
- Venue：ACM Journal on Data Science，2024
- 类型：original_method
- arXiv：2111.03794
- 核心贡献：PINO 将数据损失与高分辨率 PDE 物理约束结合，用于学习参数化 PDE 解算子。
- 方法要点：粗分辨率数据训练 + 更高分辨率 PDE residual 约束，使神经算子具备 zero-shot super-resolution 能力。
- 可迁移价值：直接对应用户关心的“粗分辨率数据 + 高分辨率物理约束”问题，可用于 FLASH/ECOGEN 数据上构建物理约束神经算子。
- 评分：9/10，core。

### 6. FourCastNet: A Global Data-driven High-resolution Weather Model using Adaptive Fourier Neural Operators
- DOI：未确认
- Venue：PASC '23: Proceedings of the Platform for Advanced Scientific Computing Conference，2023
- 类型：application / framework
- arXiv：2202.11214
- 核心贡献：将 Adaptive Fourier Neural Operator 用于全球高分辨率天气预报，实现快速中期预报和大集合预测。
- 方法要点：AFNO token mixer + 高分辨率 ERA5 数据训练 + 快速 inference。
- 可迁移价值：对 LPP-EUV 参数扫描和 surrogate ensemble 很有参考价值，尤其是频域算子结构与快速 rollout。
- 评分：8/10，core。

---

## 扩展入选论文

### 7. Probabilistic weather forecasting with machine learning
- DOI：10.1038/s41586-024-08252-9
- Venue：Nature，2024-12-04，637:84-90
- 类型：original_method
- 核心贡献：GenCast 用条件生成式模型实现概率天气预报，从确定性 surrogate 扩展到 ensemble。
- 方法要点：条件扩散模型 + 自回归 15 天集合预报。
- 可迁移价值：可用于 LPP-EUV 预脉冲不确定性量化，在不同激光、液滴、EOS/opacity 参数下生成分布式靶材形态预测。
- 评分：8/10，extended。

### 8. CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling
- DOI：10.1038/s42256-023-00716-3
- Venue：Nature Machine Intelligence，2023-09-14，5:1031-1041
- 类型：framework / application
- arXiv：2302.14231
- 核心贡献：CHGNet 构建带电荷/磁矩信息的通用图神经网络机器学习势函数，用于固体材料大规模原子模拟。
- 方法要点：预训练于 Materials Project Trajectory 数据，预测能量、力、应力与 magnetic moments。
- 可迁移价值：对高成本微观物理模块替代、电子态相关参数化和材料响应 surrogate 有参考价值。
- 评分：8/10，extended。

### 9. Scaling deep learning for materials discovery
- DOI：10.1038/s41586-023-06735-9
- Venue：Nature，2023-11-29，624:80-85
- 类型：application / framework
- 核心贡献：GNoME 通过图神经网络和主动学习扩展无机晶体材料发现，显著提高稳定材料筛选效率。
- 方法要点：候选结构生成 + GNN 稳定性预测 + DFT 验证 + data flywheel 主动学习。
- 可迁移价值：其主动学习数据闭环可迁移到 LPP-EUV 参数空间探索，用少量高精度仿真不断更新代理模型。
- 评分：7/10，extended。

### 10. Neural operators for accelerating scientific simulations and design
- DOI：10.1038/s42254-024-00712-5
- Venue：Nature Reviews Physics，2024-04-08，6:320-328
- 类型：perspective / review
- 核心贡献：系统总结神经算子作为科学仿真 surrogate 和 inverse design 工具的原理、优势与应用。
- 方法要点：强调函数空间映射、zero-shot super-resolution、物理约束集成和可微分逆设计。
- 可迁移价值：可作为用户课题中神经算子路线的综述性入口，帮助组织 FNO/DeepONet/GNO/Transformer operator 的方法谱系。
- 评分：7/10，extended。

---

## venue 覆盖说明

- 顶刊/顶会组：Nature、Science、Nature Machine Intelligence、Nature Reviews Physics、PASC 已覆盖。
- 计算物理与科学计算组：Journal of Computational Physics 已覆盖；CMAME、SISC、CPC、MLST 已检索但本轮未找到元数据完整且优先级高于现有入选的新增条目。
- AI for Science / 数据驱动科学组：材料发现、机器学习势函数、主动学习与 foundation potential 已覆盖。
- 等离子体/EUV/光学组：已检索 Physics of Plasmas、HEDP、Optics Express 等，但多数为纯实验或 arXiv-only，未进入正式入选。

## arXiv 正式发表状态更新

| arXiv ID | 标题 | DOI | 正式 venue | 置信度 | 建议 |
|---|---|---|---|---|---|
| 2211.02556 | Pangu-Weather | 10.1038/s41586-023-06185-3 | Nature | 1.0 | 待 paper_registry 初始化后回填 |
| 2211.08149 | RelaxNet | 10.1016/j.jcp.2023.112317 | Journal of Computational Physics | 1.0 | 待 paper_registry 初始化后回填 |
| 2111.03794 | PINO | 10.1145/3648506 | ACM Journal on Data Science | 0.95 | 待 paper_registry 初始化后回填 |
| 2302.14231 | CHGNet | 10.1038/s42256-023-00716-3 | Nature Machine Intelligence | 1.0 | 待 paper_registry 初始化后回填 |

## 待人工确认论文

| 标题 | 候选 venue | 问题 | 建议 |
|---|---|---|---|
| A foundation model for atomistic materials chemistry | Nature / arXiv | 本轮未能稳定确认 DOI 与正式页码 | 下次用 Crossref/OpenAlex 复核后加入 |
| PDEBench: An Extensive Benchmark for Scientific Machine Learning | NeurIPS Datasets and Benchmarks / arXiv | 正式 proceedings 元数据未稳定确认，且 arXiv 时间早于窗口 | 待确认 |
| Physics-data combined machine learning for parametric reduced-order modelling | CMAME | publication_date 早于本轮三年窗口起点 | 作为历史背景，不入库 |
| 若干 plasma surrogate / radiation hydrodynamics surrogate 预印本 | arXiv | 缺少正式 DOI 或 publisher venue | 继续跟踪 |

## 未入选原因

未入选主要原因包括：仅为 arXiv 预印本；缺少 DOI 或正式 venue；publication_date 不在三年窗口内；与 AI + 科学计算关系不足；publisher 页面无法确认 publication_date；或属于纯实验论文而非 AI/SciML 方法论文。
