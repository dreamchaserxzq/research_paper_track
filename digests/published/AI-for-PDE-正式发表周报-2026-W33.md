# AI for PDE 正式发表论文追踪周报 · 2026-W33

- **检索范围（UTC）**：2023-08-12 至 2026-08-12
- **运行时间（UTC）**：2026-08-12T11:53:00Z
- **原始候选**：25 篇
- **去重后候选**：22 篇
- **正式发表状态明确**：15 篇
- **本期核心入选**：9 篇
- **本期扩展入选**：1 篇
- **正式发表状态更新**：7 篇
- **待人工确认**：0 篇
- **数据 schema**：`published-v2`

> 本期以 2025 NeurIPS、2026 ICLR、2026 ICML 正式论文为主，并复查 W32 的 JCP 待确认项。筛选仍以“是否对通用 PDE 求解、基座预训练、复杂几何/大规模计算、生成式求解或真实数据评测具有可迁移价值”为核心，而不是按标题中的 `foundation` / `operator` 关键词机械收录。

## 一、本期概览

本次检索发现一个明显变化：高价值正式工作正在从“提出新的神经算子骨干”进一步分化为五条更具体的能力路线。

1. **多 PDE / 零样本能力**：HyPINO 用 HyperPINN + 人造解/MMS 数据 + physics-informed 无标签训练，直接面向跨椭圆、双曲、抛物 PDE 的零样本求解。
2. **三维与超大规模可扩展性**：P3D 聚焦可扩展 3D surrogate，PGD-NO 则把几何编码前移为预计算，使千万节点级网格成为可处理对象。
3. **真实数据与 sim-to-real 评测**：RealPDEBench 把 PDE 模型评测从纯数值模拟扩展到成对的真实/模拟物理系统。
4. **生成式 PDE 求解**：Particle-Guided Diffusion 与 Physics-Informed Diffusion in Spectral Space 分别从 SMC 物理引导和谱空间 latent diffusion 出发，处理部分观测、逆问题与不确定性。
5. **数值算法先验进入算子结构**：Hyperbolic Neural Operator 与 SC-NO 分别吸收 FMM 式近远场层级和固定点/多重网格式迭代思想。

## 二、趋势总结

### 2.1 PDE 基座模型的数据生成正在走向“可控合成 + 物理监督”

HyPINO 的方法与传统“先大量跑求解器再训练”不同：它用 Method of Manufactured Solutions 构造解析目标场及对应源项，再结合 physics-informed 无标签样本训练生成 PINN 的超网络。对多 PDE 基座预训练而言，这类数据路径的价值很高——基础算子或标准 PDE 族可以通过人造解快速扩充覆盖，而不必完全依赖昂贵数值模拟。

### 2.2 可扩展性已经从分辨率外推转向真正的 3D / 千万节点问题

P3D 和 PGD-NO 反映了同一趋势的两种实现：前者通过局部计算与全局上下文结合，把 3D surrogate 从训练尺度扩到大空间分辨率；后者则将几何分解预计算并形成 geometry tokens，使神经算子内存随网格规模近线性增长。未来 PDE 基座模型若只在 2D 规则网格上比较误差，已经不足以覆盖“可部署的通用求解器”这一目标。

### 2.3 “通用”评测开始要求真实数据闭环

RealPDEBench 的意义不只是新增 benchmark，而是明确把模型放到 paired real/simulation 数据上检验。对 foundation model，今后的泛化轴除了跨 PDE、参数、几何、分辨率，还应增加 **simulation-to-real gap**、测量噪声和不可控现实条件。

### 2.4 生成式求解器正在成为部分观测与逆问题的重要分支

Particle-Guided Diffusion 将 PDE residual 与观测约束嵌入扩散采样并用 SMC 组织粒子；Physics-Informed Diffusion in Spectral Space 则在谱 latent 中建模联合分布并在推理阶段加入物理约束。二者共同表明：对于多解、欠定、稀疏测量和后验推断问题，“单值确定性 operator”并不是唯一合理输出接口。

### 2.5 经典快速求解器思想正在重返神经算子架构

HNO 用类似 Fast Multipole Method 的层级近远场思想设计交互结构；SC-NO 通过重复组合同一 backbone 模拟固定点/多重网格/域分解式迭代。这类设计比无约束堆叠 Transformer 层更接近“可解释 operator expert”，也更适合未来模块化基座主干。

## 三、核心论文

### 1. HyPINO: Multi-Physics Neural Operators via HyperPINNs and the Method of Manufactured Solutions

- **正式信息**：NeurIPS 2025 Main Conference Track
- **分类**：`foundation_model` + `operator` + `pinn` + `enabling`
- **基座等级**：`foundation_model_candidate`
- **方法**：Swin Transformer 超网络根据 PDE 参数生成目标 PINN；训练同时使用 MMS 构造的有标签解析解和 physics-informed 无标签样本。
- **覆盖能力**：二维线性椭圆、双曲、抛物 PDE；变化的源项、几何、Dirichlet/Neumann 混合边界及内部边界。
- **主要贡献**：把“多 PDE 零样本求解”与可规模化合成数据生成打通，并支持 residual-driven 迭代修正。
- **局限**：目前主要是二维线性 PDE 族，距离复杂多物理、非结构离散和高维通用基座仍有明显距离。
- **评分**：5 / 3 / 2，**总分 10**。
- **正式来源**：NeurIPS 2025 proceedings。

### 2. P3D: Highly Scalable 3D Neural Surrogates for Physics Simulations with Global Context

- **正式信息**：ICLR 2026 Poster
- **分类**：`foundation_model` + `operator` + `surrogate` + `enabling`
- **基座等级**：`foundation_model_candidate`
- **方法**：以局部 3D 表征结合全局 Transformer context，重点解决高分辨率 3D 物理场的计算与显存扩展。
- **主要贡献**：把预训练式 3D surrogate 推向远大于训练 crop 的部署尺度，为 3D PDE foundation model 的空间缩放提供直接范式。
- **局限**：仍以固定数据域上的 3D surrogate 为主，方程、边界、变量语义的显式条件化能力有限。
- **评分**：5 / 3 / 2，**总分 10**。

### 3. RealPDEBench: A Benchmark for Complex Physical Systems with Real-World Data

- **正式信息**：ICLR 2026 Oral
- **分类**：`data` + `foundation_model` + `enabling`
- **基座等级**：`enabling_method`
- **方法/数据**：提供多组 paired real/simulation 物理系统数据，并用统一任务和指标评估传统 surrogate、神经算子及预训练 PDE 模型。
- **主要贡献**：将 AI-for-PDE 的 benchmark 目标从“模拟数据上的平均误差”推进到 sim-to-real、噪声、现实偏差与模型鲁棒性。
- **局限**：benchmark 本身不提出新的求解骨干；覆盖的现实系统数量仍有限。
- **评分**：5 / 3 / 2，**总分 10**。

### 4. Particle-Guided Diffusion Models for Partial Differential Equations

- **正式信息**：ICML 2026 Poster / Proceedings of the 43rd ICML
- **分类**：`operator` + `pinn` + `enabling`
- **基座等级**：`general_pde_solver`
- **方法**：用 PDE residual 与观测约束引导扩散采样，并嵌入 Sequential Monte Carlo 形成粒子化生成式 PDE solver。
- **覆盖能力**：多个 benchmark PDE，以及 multiphysics / interacting PDE systems。
- **主要贡献**：把物理约束、部分观测和生成式后验采样统一在可扩展的 SMC 框架中。
- **评分**：4 / 3 / 2，**总分 9**。

### 5. Hyperbolic Neural Operator

- **正式信息**：ICML 2026 Poster
- **分类**：`operator` + `enabling`
- **基座等级**：`general_pde_solver`
- **方法**：用双曲空间表达层级 near/far interaction，引入类似 Fast Multipole Method 的多尺度路由先验。
- **验证范围**：6 个 PDE benchmark + 2 个大规模非结构 CFD 任务。
- **主要贡献**：将经典快速算法的层级压缩思想转化为可学习 attention prior，对复杂网格与长程交互具有直接价值。
- **评分**：4 / 3 / 2，**总分 9**。

### 6. PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-Scale Physics Simulations

- **正式信息**：ICML 2026 Poster
- **分类**：`operator` + `surrogate` + `enabling`
- **基座等级**：`general_pde_solver`
- **方法**：预先做几何分解并提取 geometry tokens，将昂贵几何编码从端到端网络前向中移出。
- **主要贡献**：获得近线性内存扩展，可处理超过 1000 万节点的工业网格，直接针对单 GPU/单节点瓶颈。
- **局限**：更偏向大规模工业 surrogate，跨 PDE 预训练与显式方程条件化尚不是重点。
- **评分**：4 / 2 / 2，**总分 8**。

### 7. Physics-Informed Diffusion Models in Spectral Space

- **正式信息**：ICML 2026；作者页面标记 accepted / to appear in proceedings
- **分类**：`pinn` + `operator` + `surrogate` + `enabling`
- **基座等级**：`general_pde_solver`
- **方法**：在缩放谱表示的 latent space 中进行 diffusion，并在推理阶段通过 PDE 与测量约束进行 physics-informed posterior sampling。
- **验证范围**：Poisson、Helmholtz、不可压 Navier–Stokes；forward / inverse / sparse-observation inference。
- **主要贡献**：将函数正则性、降维和生成式 PDE 推断结合，特别适合部分观测与逆问题。
- **评分**：4 / 2 / 2，**总分 8**。

### 8. ENMA: Tokenwise Autoregression for Continuous Neural PDE Operators

- **正式信息**：NeurIPS 2025 Main Conference Track
- **分类**：`foundation_model` + `operator` + `surrogate`
- **基座等级**：`foundation_model_candidate`
- **方法**：将不规则空间观测编码为统一 latent，使用 flow-matching 训练的 masked autoregressive Transformer 逐 token 生成时空状态。
- **主要贡献**：支持 in-context conditioning 和 one-shot surrogate modeling，为连续场表示与生成式 latent dynamics 提供较完整组合。
- **评分**：4 / 3 / 2，**总分 9**。

### 9. Self-composing neural operators for high-frequency and multiscale PDE surrogates

- **正式信息**：Journal of Computational Physics, Volume 565, Article 115189
- **DOI**：`10.1016/j.jcp.2026.115189`
- **分类**：`operator` + `enabling`
- **基座等级**：`general_pde_solver`
- **方法**：重复组合同一个参数共享 backbone，模拟 fixed-point / multigrid / domain-decomposition 迭代，并用 Train-and-Unroll 逐渐增加展开深度。
- **主要贡献**：以参数效率较高的迭代式 operator 处理高频与多尺度问题。
- **状态变化**：W32 因未来卷期日期而待确认；本期已获得 Elsevier 正式文章记录与 DOI，转为正式入选。
- **评分**：4 / 2 / 2，**总分 8**。

## 四、扩展论文

### CINOC: Cardinality-Invariant Neural Operator Policies for Scalable PDE Control

- **正式信息**：ICML 2026 regular
- **分类**：`operator` + `enabling`
- **基座等级**：`enabling_method`
- **方法**：把 PDE control 写成从状态场到连续控制函数的 operator learning，并通过可微 PDE solver 端到端训练。
- **泛化**：传感器数、执行器数、agent 数量变化；支持小群体训练后 zero-shot 扩到更大群体，并对 agent failure 有鲁棒性。
- **价值**：说明连续 operator interface 不只适用于状态预测，也可以成为控制策略的统一接口。
- **为何列为扩展**：核心任务是 PDE control，而不是前向 PDE 解算。
- **评分**：3 / 3 / 2，**总分 8**。

## 五、分类总结

| `published_category` / 多标签 | 本期相关论文数 | 观察 |
|---|---:|---|
| `foundation_model` | 4 | HyPINO、P3D、RealPDEBench（评测支撑）、ENMA |
| `operator` | 9 | 主流仍是 operator，但重点已分化到生成、3D、几何、大规模与控制 |
| `surrogate` | 4 | P3D、PGD-NO、PISD、ENMA |
| `data` | 1 | RealPDEBench 提供真实/模拟联合 benchmark |
| `pinn` | 3 | HyPINO、Particle-Guided Diffusion、PISD |
| `enabling` | 8 | 数据生成、几何缩放、生成式推断、经典算法先验、控制均属于关键支撑能力 |

## 六、Venue 覆盖与筛选

### 本期正式入选来源

- **NeurIPS 2025**：HyPINO、ENMA
- **ICLR 2026**：P3D、RealPDEBench
- **ICML 2026**：Particle-Guided Diffusion、PGD-NO、Hyperbolic Neural Operator、Physics-Informed Diffusion in Spectral Space、CINOC
- **Journal of Computational Physics**：SC-NO

### 已核验但未入选的典型候选

- 单一方程/单一工程场景的 physics-informed operator：正式发表证据充分，但跨任务价值不足。
- 普通 PINN 训练或采样小改进：未达到本例程对 `core/extended` 的通用性阈值。
- 只改局部 attention / spectral block、未证明多 PDE 或复杂几何扩展价值的 operator：不为凑数纳入。
- ICLR/ICML submission、withdrawn 或仅 workshop/poster 页面而无正式主会接收证据者：排除。

## 七、正式发表状态更新

本期共形成 **7 条高置信正式状态补丁**：

| arXiv ID / 既有候选 | 正式状态 |
|---|---|
| `2509.05117` HyPINO | → NeurIPS 2025 正式 proceedings |
| `2506.06158` ENMA | → NeurIPS 2025 正式 proceedings |
| `2601.01829` RealPDEBench | → ICLR 2026 Oral |
| `2601.23262` Particle-Guided Diffusion | → ICML 2026 Poster / proceedings |
| `2602.09708` Physics-Informed Diffusion in Spectral Space | → ICML 2026 accepted / proceedings |
| `2605.25867` CINOC | → ICML 2026 regular |
| `2508.20650` SC-NO | W32 pending → JCP DOI / 正式文章 |

补丁写入 `metadata/paper_registry_updates_2026_W33.jsonl`。若主 `paper_registry.jsonl` 中存在对应 arXiv 记录，可在后续安全合并时应用；本次不对长主 JSONL 进行整文件覆盖。

## 八、待人工确认

本期 **0 篇**。SC-NO 已从 W32 待确认转正；其 JCP 卷期日期为 2026-11-15，但 Elsevier 已提供正式 Article 115189 与 DOI，因此按照本仓库“DOI / publisher formal article / online record 即可判定正式发表”的规则收录。

## 九、对 PDE 基座模型设计的直接启示

1. **基础专家数据完全可以大量使用 MMS / 人造解生成。** HyPINO 提供了正式顶会证据：先构造目标解，再由控制方程反推源项，是扩展多 PDE 训练分布的有效路线。
2. **几何编码应考虑“可预计算、可复用”。** PGD-NO 的 geometry tokens 说明，静态几何不一定每层重复编码；可把几何结构转化为只读 memory / support representation。
3. **主干专家可以吸收经典求解器结构，而不是只按网络范式划分。** HNO 对应 FMM 式近远场专家，SC-NO 对应迭代/多重网格式专家。
4. **生成式求解最好作为条件化执行模式，而非替代确定性主干。** Particle-Guided Diffusion 与 PISD 的优势主要出现在部分观测、逆问题与后验多解场景。
5. **基座模型评测必须加入真实物理数据。** RealPDEBench 表明，下一阶段 benchmark 应明确区分 simulation accuracy 与 real-world transfer，而不是只做 held-out numerical trajectories。

---

**本期结论**：2026 年正式发表的 AI-for-PDE 工作正在快速补齐 PDE foundation model 的“工程可扩展性”和“任务完整性”：一端是 HyPINO/ENMA 的跨任务与生成式适配，另一端是 P3D/PGD-NO/HNO/SC-NO 的 3D、复杂网格与快速算法先验，再加上 RealPDEBench 的真实数据评测。对下一代 PDE 基座模型而言，竞争焦点正从单纯的 backbone 精度转向 **可扩展预训练数据、统一连续表示、复杂几何、大规模执行、部分观测推断以及真实世界泛化**。
