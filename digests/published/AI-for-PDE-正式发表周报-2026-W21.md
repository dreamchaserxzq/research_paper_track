# AI for PDE 正式发表论文周报

日期范围：2023-05-24 至 2026-05-24 UTC。第 3 期，三年回溯 + venue 分层检索。

## 本期概览

候选论文 28 篇，去重后 16 篇，正式发表状态明确 5 篇，新增入选 2 篇，累计入选 5 篇，arXiv 匹配 2 篇，待人工确认 2 篇。

## 检索修正说明

本次已修正上一轮“结果过度集中于 Nature”的问题。重新检索时按三组 venue 分层覆盖：顶刊/顶会组、计算物理与科学计算组、等离子体/EUV/光学组。若结果集中在同一 publisher 或 Nature 系列，触发二次检索，专门补查 JCP、CMAME、MLST、SISC、CPC、Physics of Plasmas、HEDP、Optics Express 等领域期刊。

## 本期重点

最值得关注的非 Nature 论文是 RelaxNet。它针对 Boltzmann 碰撞算子构造结构保持神经网络代理，并在 arXiv 元数据中给出正式相关 DOI 10.1016/j.jcp.2023.112317，对稀薄气体、动理学方程、非平衡输运和等离子体电子动力学 surrogate 都有直接参考价值。

## 方向 A：AI 求解 PDE / Scientific Machine Learning

### Neural general circulation models for weather and climate
- DOI：10.1038/s41586-024-07744-y
- Venue：Nature，2024-07-22，632:1060-1066
- 作者：Dmitrii Kochkov et al.
- 链接：https://www.nature.com/articles/s41586-024-07744-y
- 核心贡献：将可微分大气动力学求解器与神经网络物理参数化结合。
- 与课题关联：对应到 LPP-EUV，可保留守恒律/几何离散骨架，只学习热传导、辐射输运、EOS/opacity 校正等高成本闭合模块。
- 评分：10/10。

### RelaxNet: A structure-preserving neural network to approximate the Boltzmann collision operator
- DOI：10.1016/j.jcp.2023.112317
- Venue：Journal of Computational Physics，2023
- 作者：Tianbai Xiao, Martin Frank
- 链接：https://arxiv.org/abs/2211.08149
- arXiv：2211.08149
- 核心贡献：提出 RelaxNet，用结构保持神经网络近似 Boltzmann 五重碰撞积分，并保持 positivity、conservation、invariance 与 H-theorem 等关键结构。
- 方法要点：以类 BGK relaxation 结构改造 ResNet，用神经网络近似平衡分布与速度相关弛豫时间，把昂贵碰撞积分替换为神经网络张量计算。
- 与课题关联：对 LPP-EUV 中电子非平衡动力学、输运闭合、NLTE 动力学或动理学-流体耦合 surrogate 有直接启发。
- 评分：9/10。

## 方向 B：数据生成、代理模型与科学仿真 surrogate

### Learning skillful medium-range global weather forecasting
- DOI：10.1126/science.adi2336
- Venue：Science，2023-12-22
- 作者：Remi Lam et al.
- 链接：https://doi.org/10.1126/science.adi2336
- 核心贡献：GraphCast 使用图神经网络进行全球中期天气预报，是高维连续场快速代理模型代表。
- 与课题关联：其图结构时空消息传递可迁移到非规则网格、AMR 数据或液滴靶材形态演化建模。
- 评分：9/10。

### Accurate medium-range global weather forecasting with 3D neural networks
- DOI：10.1038/s41586-023-06185-3
- Venue：Nature，2023-07-05，619:533-538
- 作者：Kaifeng Bi et al.
- 链接：https://www.nature.com/articles/s41586-023-06185-3
- arXiv：2211.02556
- 核心贡献：Pangu-Weather 用 3D Earth-specific Transformer 建模全球天气场演化。
- 与课题关联：可借鉴三维多变量场编码、分层时间推进和误差累积控制，用于靶材形态时序预测。
- 评分：9/10。

### Probabilistic weather forecasting with machine learning
- DOI：10.1038/s41586-024-08252-9
- Venue：Nature，2024-12-04，637:84-90
- 作者：Ilan Price et al.
- 链接：https://www.nature.com/articles/s41586-024-08252-9
- 核心贡献：GenCast 用生成式模型实现概率天气预报，从确定性 surrogate 扩展到 ensemble。
- 与课题关联：可迁移到 LPP-EUV 预脉冲不确定性量化，在不同激光、液滴、EOS/opacity 参数下生成分布式靶材形态预测。
- 评分：8/10。

## 方向 C：激光等离子体 / EUV / 辐射流体 / Vlasov / MHD

已检索 Physics of Plasmas、High Energy Density Physics、Plasma Physics and Controlled Fusion、Nuclear Fusion、Optics Express、Optica、Applied Physics Letters、Journal of Applied Physics 等 venue。未发现可同时满足三年窗口、正式发表状态、AI/PDE 或 surrogate 硬门槛的新增方向 C 论文。若干 radiation hydrodynamics surrogate、NLTE kinetics surrogate、ICF optimization、MHD neural operator 条目仍停留在 arXiv 或元数据不完整状态，未强行收录。

## venue 覆盖说明

- 顶刊/顶会组：入选 Nature 3 篇、Science 1 篇。
- 计算物理与科学计算组：入选 JCP 1 篇；CMAME/MLST/SISC/CPC 已检索但无可严格确认且评分达标的新条目。
- 等离子体/EUV/光学组：已检索但无符合条件论文；主要原因是纯实验论文较多，或相关 ML surrogate 仍未确认正式发表。

## arXiv 正式发表状态更新

| arXiv ID | 标题 | DOI | 正式 venue | 置信度 | 建议 |
|---|---|---|---|---|---|
| 2211.02556 | Pangu-Weather | 10.1038/s41586-023-06185-3 | Nature | 1.0 | 待 paper_registry 初始化后回填 |
| 2211.08149 | RelaxNet | 10.1016/j.jcp.2023.112317 | Journal of Computational Physics | 1.0 | 待 paper_registry 初始化后回填 |

## 待人工确认论文

| 标题 | 候选 venue | 问题 | 建议 |
|---|---|---|---|
| Physics-data combined machine learning for parametric reduced-order modelling of nonlinear dynamical systems in small-data regimes | CMAME | publication_date 为 2023-02，早于当前三年窗口起点 2023-05-24 | 不入选本期，可作为历史背景 |
| 若干 plasma surrogate / radiation hydrodynamics surrogate 预印本 | arXiv | 缺少正式 DOI 或 publisher venue | 后续继续跟踪 |

## 未入选原因

主要原因包括：仅为 arXiv 预印本；缺少 DOI 或正式 venue；publication_date 不在三年窗口内；与 AI for PDE 或仿真代理关系不足；publisher 页面无法确认 publication_date。
