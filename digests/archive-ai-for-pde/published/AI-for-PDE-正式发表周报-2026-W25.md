# AI for PDE / AI for Science 正式发表论文周报

日期范围：2023-06-15 至 2026-06-15 UTC。第 8 期，2026-W25。

## 本期概览

- 纳入候选池：20 篇
- 题名 / DOI 去重后：18 篇
- 正式发表状态明确：12 篇
- 核心入选：9 篇
- 扩展入选：1 篇
- arXiv 高置信匹配：5 篇
- 待继续核验：4 篇

## 本期检索与筛选说明

本轮继续执行“过去三年 + 正式发表优先”的口径，只纳入具有 DOI、出版社页面、SIAM 正式页面或明确期刊卷期信息的论文，排除仅有 arXiv 预印本的结果。为避免再次集中于单一顶会，本轮重点补查 Journal of Computational Physics、Computer Methods in Applied Mechanics and Engineering、SIAM Journal on Scientific Computing、Computer Physics Communications、High Energy Density Physics 与 Physics of Plasmas。

本期形成三条清晰的方法主线：

1. **复杂几何与物理结构约束的神经算子**：PCNO、局部性约束神经算子、PODNO。
2. **神经网络嵌入经典数值流程**：SNF-ROM、MR-DINO、I-PINNs。
3. **直接面向等离子体与辐射流体瓶颈的代理模型**：时变 NLTE 吸收/发射谱代理模型、等离子体发生器温度预测。

---

## 核心入选论文

### 1. PODNO: Proper Orthogonal Decomposition Neural Operators

- 作者：Zilan Cheng, Zhongjian Wang, Li-Lian Wang, Mejdi Azaiez
- Venue：SIAM Journal on Scientific Computing, 48(3), C479-C504
- 正式状态：2025-12-08 接收；2026-05-11 online published
- DOI：10.1137/25M1751372
- official_url：https://doi.org/10.1137/25M1751372
- arXiv：2504.18513
- 核心贡献：以 POD 正交基替代 FNO 中固定 Fourier 基构造积分核，面向高频、振荡和色散型 PDE，并给出广义谱算子的普适逼近分析。
- 可迁移价值：对激波、锐梯度、辐射波前及快速时间振荡问题，比仅偏向低频模式的标准 FNO 更有潜力；也可用于探索基于 FLASH 数据自适应提取空间基函数的神经算子。
- 评分：9/10，core。

### 2. Point cloud neural operator for parametric PDEs on complex and variable geometries

- 作者：Chenyu Zeng, Yanshu Zhang, Jiayi Zhou, Yuhan Wang, Zilin Wang, Yuhao Liu, Lei Wu, Daniel Zhengyu Huang
- Venue：Computer Methods in Applied Mechanics and Engineering
- 正式状态：2025-08-01 published
- DOI：10.1016/j.cma.2025.118022
- official_url：https://doi.org/10.1016/j.cma.2025.118022
- arXiv：2501.14475
- 核心贡献：提出 Point Cloud Neural Operator（PCNO），直接在点云表示上学习复杂、可变几何中的参数化 PDE 解算子，覆盖边界层、自适应网格和拓扑变化。
- 可迁移价值：高度适配 FLASH AMR 数据、ECOGEN 非规则界面和液滴大变形问题，可降低规则网格插值对界面和激波结构的损伤。
- 评分：9/10，core。

### 3. Enforcing the principle of locality for physical simulations with neural operators

- 作者：Jiangce Chen, Wenzhuo Xu, Zeda Xu, Noelia Grande Gutiérrez, Sneha Prabha Narra, Christopher McComb
- Venue：Journal of Computational Physics, 538, 114131
- 正式状态：2025-10-01 published
- DOI：10.1016/j.jcp.2025.114131
- official_url：https://doi.org/10.1016/j.jcp.2025.114131
- arXiv：2405.01319
- 核心贡献：提出 data decomposition enforcing local-dependency（DDELD），显式限制局部预测可见的信息范围，使神经算子的感受域与 PDE 的有限传播和局部依赖结构一致。
- 可迁移价值：对大步长 rollout 的稳定性具有直接启发。LPP-EUV 中激波、热传导和辐射传播具有不同有效作用域，可据此设计分模块、分尺度局部算子，而不是让全局网络无约束混合信息。
- 评分：9/10，core。

### 4. DeepOMamba: State-space model for spatio-temporal PDE neural operator learning

- 作者：Zheyuan Hu, Qianying Cao, Kenji Kawaguchi, George Em Karniadakis
- Venue：Journal of Computational Physics, 540, 114272
- 正式状态：2025-11-01 published
- DOI：10.1016/j.jcp.2025.114272
- official_url：https://doi.org/10.1016/j.jcp.2025.114272
- 核心贡献：系统比较 DeepONet、其他神经算子与 RNN、Transformer、Mamba 等时间模型的组合，最终提出 DeepONet + Mamba 的时空算子结构，以较低计算成本处理长时间积分和高维问题。
- 可迁移价值：可作为自回归长程 rollout 的候选骨干，但对强耦合 RHD 仍需叠加守恒约束、误差校正和多模块耦合训练。
- 评分：8/10，core。

### 5. Efficient PDE-Constrained Optimization Under High-Dimensional Uncertainty Using Derivative-Informed Neural Operators

- 作者：Dingcheng Luo, Thomas O'Leary-Roseberry, Peng Chen, Omar Ghattas
- Venue：SIAM Journal on Scientific Computing, 47(4), C899-C931
- 正式状态：2025-04-24 接收；2025-07-24 online published
- DOI：10.1137/23M157956X
- official_url：https://doi.org/10.1137/23M157956X
- arXiv：2305.20053
- 核心贡献：提出 multi-input reduced-basis derivative-informed neural operator（MR-DINO），同时逼近 PDE 状态及其对优化变量的导数，用于高维不确定性下的 PDE 约束优化。
- 可迁移价值：适合未来对激光能量、脉宽、焦斑、液滴尺寸和材料参数开展快速参数优化与 UQ；强调学习灵敏度而非只学习解场。
- 评分：8/10，core。

### 6. Interface PINNs (I-PINNs): A physics-informed neural networks framework for interface problems

- 作者：Antareep Kumar Sarma, Sumanta Roy, Chandrasekhar Annavarapu, Pratanu Roy, Shriram Jagannathan
- Venue：Computer Methods in Applied Mechanics and Engineering, 429, 117135
- 正式状态：2024-09-01 published
- DOI：10.1016/j.cma.2024.117135
- official_url：https://doi.org/10.1016/j.cma.2024.117135
- 核心贡献：针对尖锐界面两侧使用参数共享但激活函数不同的子网络，显式处理系数和解的强/弱不连续；相较常规 PINN 和 XPINN，在多个界面算例中取得更高精度与更低成本。
- 可迁移价值：对锡液滴—等离子体界面、材料跃迁及多相区域分解具有参考价值，但完整 RHD 中仍需与守恒有限体积框架结合。
- 评分：8/10，core。

### 7. SNF-ROM: Projection-based nonlinear reduced order modeling with smooth neural fields

- 作者：Vedant Puri, Aviral Prakash, Levent Burak Kara, Yongjie Jessica Zhang
- Venue：Journal of Computational Physics, 532, 113957
- 正式状态：2025-07-01 published
- DOI：10.1016/j.jcp.2025.113957
- official_url：https://doi.org/10.1016/j.jcp.2025.113957
- arXiv：2405.14890
- 核心贡献：以平滑神经场构造网格无关的非线性降阶流形，再通过 Galerkin 投影和自动微分推进约化动力学；在对流主导 PDE 上报告最高约 199× 加速。
- 可迁移价值：比纯 latent autoregression 更保留经典投影动力学结构，适合作为液滴大变形和对流主导流场的 ROM 候选。
- 评分：8/10，core。

### 8. Deep operator networks for Bayesian parameter estimation in PDEs

- 作者：Amogh Raj, Carol Eunice Gudumotou, Sakol Bun, Keerthana Srinivasa, Arash Sarshar
- Venue：Computer Physics Communications, 317, 109853
- 正式状态：2025-12 published
- DOI：10.1016/j.cpc.2025.109853
- official_url：https://doi.org/10.1016/j.cpc.2025.109853
- arXiv：2501.10684
- 核心贡献：结合 DeepONet、PINN 物理约束和变分贝叶斯训练，同时求解 PDE、估计未知参数并量化认知与随机不确定性。
- 可迁移价值：适用于从稀疏、含噪实验诊断反演激光沉积、输运系数或材料参数，并向代理模型输出可信区间。
- 评分：8/10，core。

### 9. Deep learning surrogate models to solve time-dependent NLTE absorption and emission spectra

- 作者：Jingsong Zhang, Wengu Chen, Xiaoying Han, Peng Song, Han Wang
- Venue：High Energy Density Physics, 56, 101199
- 正式状态：2025-09 published
- DOI：10.1016/j.hedp.2025.101199
- official_url：https://doi.org/10.1016/j.hedp.2025.101199
- 核心贡献：使用深度残差网络代理时变 NLTE 原子动力学计算，输入包含材料密度、温度、辐射场和初始离化态分布，快速预测吸收谱、发射谱及等离子体状态。
- 可迁移价值：这是本期与 LPP-EUV 最直接相关的论文。NLTE 原子模型可占辐射流体计算成本的重要部分，该工作说明可将 NLTE 作为独立可学习子算子，并与 RHD 主求解器在线耦合。
- 评分：10/10，core。

---

## 扩展入选论文

### 10. Temperature prediction of high-temperature and high-enthalpy plasma generators based on machine learning

- 作者：Yanan Xie, Qihao Jiang, Yiyang Gao, Yanming Liu, Qiang Wei
- Venue：Physics of Plasmas, 32(1), 013504
- 正式状态：2024-12-11 接收；2025-01-16 published
- DOI：10.1063/5.0242129
- official_url：https://doi.org/10.1063/5.0242129
- 核心贡献：基于约 1500 次 ICP 点火实验，使用 XGBoost 预测石英管温度峰值和升温率，并分析电压、进气量和持续时间等参数的重要性。
- 可迁移价值：方法本身不是 PDE 求解器，但展示了“仿真/实验参数—关键热响应—安全运行边界”的轻量代理路线，可用于 LPP-EUV 装置级参数筛选和故障预警。
- 评分：6/10，extended。

---

## 待继续核验 / 暂不入库

| 标题 | 当前状态 | 暂不入库原因 |
|---|---|---|
| Time-Marching Neural Operator–FE Coupling: AI-Accelerated Physics Modeling | CMAME 2025，DOI 10.1016/j.cma.2025.118319 已确认 | 完整作者和卷期元数据尚未稳定回填，下一轮补录 |
| A deep-learning-based surrogate modeling method with application to plasma processing | Chemical Engineering Research and Design 2024，DOI 10.1016/j.cherd.2024.09.031 已确认 | 作者元数据尚未完成交叉核验，避免写入不完整记录 |
| Physics-Informed Latent Space Dynamics Identification for Time-Dependent NLTE Atomic Kinetics | 发现预印本线索 | 尚未确认正式 venue，继续追踪 |
| Learning nonlinear plasma-mirror response: fast surrogate modeling and optimization of ellipticity of attosecond pulses | 2026 in press 线索 | 期刊、DOI 与最终出版信息尚未完整确认 |

## 对当前课题的直接启示

1. **优先把 NLTE 原子动力学定义为独立代理子模块。** 本期 HEDP 论文与“hydro + conduction + radiation/source 子算子”路线高度一致，可先围绕密度、温度、辐射场和离化态建立时变映射，再研究与 FLASH/RHD 的耦合误差。
2. **复杂几何数据不应被强行规整化。** PCNO 和 SNF-ROM 分别提供点云算子与连续神经场路线，可直接面向 AMR、移动界面和不同液滴形态。
3. **长程稳定需要局部性、结构和经典数值推进共同约束。** DDELD、PODNO、SNF-ROM 的共同趋势不是单纯增加网络规模，而是把局部传播、问题自适应基和 Galerkin 动力学嵌入模型。
4. **参数优化应同步学习导数和不确定性。** MR-DINO 与 Bayesian DeepONet 可分别支撑梯度优化和可信度评估，适合后续建立激光参数—EUV 输出—靶形态的闭环设计框架。
5. **PINN 更适合作为界面和局部约束模块。** I-PINNs 对材料界面有效，但不宜直接替代完整守恒型 RHD 求解器。

## 数据写入说明

本期结构化记录保存至 `metadata/published_papers_2026_W25.jsonl`。由于当前 GitHub connector 对既有 JSONL 仅支持整文件替换，为避免覆盖历史 27 条记录，本轮未直接重写 `metadata/published_papers.jsonl`；后续可在具备安全追加能力时合并。README 中目前不存在 `PUBLISHED_DIGEST_START/END` 标记，本轮未改写长历史日报区块。
