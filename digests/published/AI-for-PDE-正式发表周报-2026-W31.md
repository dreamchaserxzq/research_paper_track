# AI for PDE 正式发表论文追踪周报 · 2026-W31

- **周次（ISO）**：2026-W31（2026-07-27 至 2026-08-02）
- **历史检索截面（UTC）**：2023-07-27 至 2026-07-27
- **补档执行时间（UTC）**：2026-08-03T09:46:00Z
- **原始候选**：18 篇
- **仓库与候选内去重后**：10 篇
- **正式发表状态明确**：6 篇
- **本期核心入选**：2 篇
- **本期扩展入选**：1 篇
- **正式发表状态更新**：0 篇
- **待人工确认**：2 篇
- **数据 schema**：`published-v2`

> 本报告是对缺失的 2026-W31 进行历史补档。检索与正式发表判定以 **2026-07-27** 为时间截面，
> 但补档操作发生于 2026-08-03。为保持审计时间线，已经在 W32 首次发现并写入的 PGMNO、
> Hermite Neural Operator 与 MPNOT 不向前搬迁，也不在本期重复计数。

## 一、本期概览

本期补查 SIAM Journal on Scientific Computing、Journal of Computational Physics、Mechanical Systems
and Signal Processing、Engineering Applications of Artificial Intelligence、Physical Review E、
Machine Learning: Science and Technology 等来源。经 DOI、标题和仓库分周元数据去重后，补充三篇
此前遗漏的正式论文：

1. **PI-DeepONet on unknown manifolds**：把点云流形识别、微分算子近似、前向算子学习与 Bayesian
   inverse problem 连接起来。
2. **SV-PINO**：通过分离变量将动态 PDE 转换为低维 ODE 系数学习问题，显式处理高频、高阶与复杂边界。
3. **GAPI-DeepONet**：以几何条件网络逐层调制 trunk 表征，在二维流动和三维传热问题上验证跨几何泛化。

三篇工作均不是多 PDE 预训练意义上的 foundation model，但分别补强了 **非规则几何表征、
解析结构注入和几何条件化** 三条对 PDE 基座模型直接相关的技术路线。

## 二、趋势总结

### 2.1 从已知网格走向未知流形与点云定义域

未知流形工作不要求预先给出解析参数化或固定网格，而是从随机点云恢复局部几何与微分结构，再训练
PI-DeepONet。对统一连续场模型而言，这说明几何编码器需要同时支持坐标、邻域和离散微分信息，而不能
把规则网格索引当作默认前提。

### 2.2 结构先验可以进入解空间，而不只进入损失函数

SV-PINO 先利用分离变量、特征函数或小波把 PDE 重写，再由神经算子学习低维系数。与仅在 loss 中加入
PDE residual 相比，这种做法把先验直接写入表示空间和求解路径。未来基座模型可将此类模块作为
可插拔的结构专家，但不宜把某一特定可分离假设固化到统一主干。

### 2.3 几何条件化应作用于解码查询过程

GAPI-DeepONet 不只把几何作为额外输入，而是用几何条件网络逐层调制 trunk。其启示是：几何信息需要
影响“在何处、以何种局部坐标和尺度查询场值”的过程，而不是仅生成一个全局 geometry token。

## 三、核心论文

### 1. Solving Forward and Inverse Partial Differential Equation Problems on Unknown Manifolds via Physics-Informed Neural Operators

- **正式信息**：*SIAM Journal on Scientific Computing* 48(1), C136–C163；online 2026-02-09
- **DOI**：[`10.1137/24M1675254`](https://doi.org/10.1137/24M1675254)
- **分类**：主类 `operator`；兼类 `pinn`、`surrogate`
- **基座等级**：`general_pde_solver`
- **方法**：以点云描述未知流形；使用 diffusion maps 或 GMLS 构造微分算子近似；训练 DeepONet /
  PI-DeepONet 求解前向 PDE，并将代理算子嵌入 MCMC 进行逆问题估计。
- **泛化维度**：流形几何、点云采样、带边界/无边界流形、线性/半线性 PDE、前向/逆向任务。
- **主要贡献**：将几何发现、无网格微分、算子学习与 Bayesian inversion 统一在同一框架中。
- **局限**：仍需要构造稳定的离散微分算子；对高维流形、强非线性动力学和大规模跨 PDE 预训练未验证。
- **评分**：相关度 4 / 通用性 3 / 方法价值 2，**总分 9**。

### 2. Separated-variable physics informed neural operators for solving dynamic PDEs

- **正式信息**：*Mechanical Systems and Signal Processing* 251, 114195；2026-05-01
- **DOI**：[`10.1016/j.ymssp.2026.114195`](https://doi.org/10.1016/j.ymssp.2026.114195)
- **分类**：主类 `operator`；兼类 `pinn`、`enabling`
- **基座等级**：`general_pde_solver`
- **方法**：通过分离变量将动态 PDE 投影到特征函数或小波空间，把高维 PDE 转化为一组 ODE 系数学习问题。
- **泛化维度**：高频结构、高阶 PDE、复杂边界以及缺少显式 PDE 形式的离散动力系统。
- **主要贡献**：把解析求解结构与神经算子组合，缓解 spectral bias 和高阶自动微分优化困难。
- **局限**：依赖问题具有可用的变量分离或合适基底；对强耦合、非分离、多几何 PDE 的统一性有限。
- **评分**：4 / 2 / 2，**总分 8**。

## 四、扩展论文

### 3. A geometry-adaptive physics-informed operator framework generalized for arbitrary geometries

- **正式信息**：*Engineering Applications of Artificial Intelligence* 174, 114457；2026-06-15
- **DOI**：[`10.1016/j.engappai.2026.114457`](https://doi.org/10.1016/j.engappai.2026.114457)
- **分类**：主类 `operator`；兼类 `pinn`、`surrogate`
- **方法**：GAPI-DeepONet 将几何表示送入 branch，并通过 geometry-adaptive conditioning network
  对 trunk 特征进行逐层调制。
- **验证范围**：圆柱绕流、NACA 翼型流动和三维散热器传热。
- **主要贡献**：将几何从静态输入升级为对坐标查询网络的动态条件。
- **局限**：主要验证三个工程问题；尚未证明跨拓扑、跨离散方式或跨 PDE 家族迁移。
- **评分**：4 / 2 / 1，**总分 7**。

## 五、分类总结

| 主类 | 核心 | 扩展 | 说明 |
|---|---:|---:|---|
| `operator` | 2 | 1 | 三篇均以学习 PDE 解算子为中心 |
| `pinn`（兼类） | 2 | 1 | 使用 PDE 约束或 physics-informed 训练 |
| `surrogate`（兼类） | 1 | 1 | 未知流形逆问题与几何变化工程代理 |
| `enabling`（兼类） | 1 | 0 | SV-PINO 提供结构化表示与求解机制 |

本期无 `true_foundation_model` 新增。三篇论文更适合作为 PDE 基座模型的几何适配、结构专家或
physics-informed 训练组件。

## 六、正式发表状态更新

未发现与 `metadata/paper_registry.jsonl` 中现有记录达到置信度不低于 0.9 的匹配，因此本期不自动
回填 DOI 或 venue。

## 七、待人工确认

### 1. Self-composing neural operators for high-frequency and multiscale PDE surrogates

- DOI：`10.1016/j.jcp.2026.115189`
- 问题：出版商页面给出的正式卷期日期为 **2026-11-15**，晚于 W31 历史截面；未确认截面日前是否已有
  可采用的 online-first 日期。
- 处理：不提前入库，待出版商补充明确的 Article in Press / available online 日期后复查。

### 2. Walsh-Hadamard neural operators for solving PDEs with discontinuous coefficients

- DOI：`10.1016/j.jcp.2026.115124`
- 问题：出版商页面卷期日期为 **2026-10-15**，晚于 W31 历史截面。
- 处理：不以未来卷期日期倒推正式发表状态，继续待确认。

## 八、未入选与去重说明

- **Operator learning augmented PINNs for sharp features**：正式发表于 *Physical Review E*，
  但主要是 PINN + 预训练 DeepONet 的特定增强，跨任务通用性证据不足，本期评分未达 7。
- **Derivative-constrained PINNs**：约束建模有价值，但属于普通 PINN 方法扩展，未达到本周报的优先级。
- **Physics-informed CNO for wavefields**：正式元数据完整，但集中于 Helmholtz 波场单一应用，按排除规则不入选。
- **EquiNO、Mamba Neural Operator 等**：已由 W30 或更早分周元数据覆盖，不重复。
- **PGMNO、Hermite Neural Operator、MPNOT**：保留在实际发现它们的 W32，不在历史补档中回迁。
- 仅有 arXiv、SSRN 或未来卷期信息的候选不进入正式入选列表。

## 九、数据与仓库操作

- 本期增量元数据：`metadata/published_papers_2026_W31.jsonl`
- 权威主注册表：由于 GitHub connector 对长 JSONL 仅支持整文件替换，且返回内容可能截断，本次不冒险
  覆盖 `metadata/published_papers.jsonl`；增量文件作为可审计补丁保留。
- README：同样因长文件整文件替换风险，本次不修改，周报可通过固定路径直接访问。
- W32：内容和元数据不修改，三篇论文与本期无重复。
