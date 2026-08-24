# AI for PDE 正式发表论文追踪周报 · 2026-W35

## 1. 本期概览

- **检索范围（UTC）**：2023-08-24 至 2026-08-24
- **原始候选**：21 篇
- **去重后候选**：12 篇
- **正式状态明确**：5 篇
- **核心入选**：4 篇
- **扩展入选**：1 篇
- **正式发表状态更新**：2 篇
- **待人工确认**：0 篇
- **数据 schema**：`published-v2`

本期重点是补齐此前预印本库中已经出现、但正式出版信息尚未回填的高价值工作，并继续查漏 ICLR 2026 与计算流体/算子学习期刊。最明显的技术信号有三条：**连续时间神经算子正在引入 flow matching；Mamba/SSM 正在向任意几何和异构离散扩展；长时程稳定性越来越依赖显式的全局谱耦合或物理/数值结构先验。**

> 仓库说明：权威主表 `metadata/published_papers.jsonl` 与 `metadata/paper_registry.jsonl` 含有较长历史内容。当前 GitHub Contents API 的安全写操作仍要求整文件替换；本轮已写入可审计的 W35 增量文件与状态更新补丁，但未用不完整内容覆盖权威主表。后续应执行一次专门的历史增量归并维护，将 W31–W35 分周记录安全汇入主表。

## 2. 趋势总结

### Foundation model / 连续时间动力学

CFO 不再把时间演化固定成离散自回归步进，而是用 temporal spline 构造速度场，再通过 flow matching 学习连续时间 PDE dynamics。其关键价值不是“生成式”标签本身，而是把**时间分辨率、非均匀采样与长时程 rollout**从固定步长训练接口中解耦。对未来 PDE foundation model，这种连续时间语义比单纯增加 Transformer 深度更值得关注。

### Neural operator / SSM 与任意几何

Adaptive Mamba Neural Operators 将 Mamba/状态空间模型与 Takenaka–Malmquist reproducing-kernel 表示结合，目标直接覆盖 point cloud、structured mesh、regular grid 和 irregular domain。它说明 SSM 类架构开始从规则序列建模进入真正的函数空间/算子学习问题，尤其值得关注其几何与离散无关性。

### 长时程稳定性与谱耦合

DRIFT-Net 针对局部窗口 attention 在长时间 rollout 中全局耦合传播缓慢的问题，显式设置低频全局 spectral branch 和局部 image branch。其意义在于：对多尺度流体动力学，**全局一致低频模式与局部非平稳结构应当在架构层面同时存在**，而不是依赖层数堆叠间接传播。

### Physics-informed operator

PILNO（Physics-Informed Laplace Neural Operator）已经获得 JCP 正式卷册/文章号与 DOI。它把 Laplace-domain neural operator 与 physics-informed 约束结合，属于“频域/变换域算子 + 物理监督”的路线。出版商正式 publication date 本轮未独立确认，因此没有用 Crossref deposited/indexed date 替代。

### Surrogate / ROM

Spectral modal operator learning framework（SPOD-DeepONet）将频率分辨的模态表示引入 DeepONet，解耦空间模态与时间动力学，对非定常流中的高频结构和非线性模态交互更友好。其通用性低于前述工作，因此列为 extended，而非为凑数提升到 core。

### Scientific data / benchmark 与 multi-physics

本期未发现相对 W33 的 RealPDEBench 等已有正式记录更具增量价值的新 benchmark。多物理方面，AMO 的验证跨 fluid / solid / finance，CFO 跨 Lorenz、Burgers、diffusion-reaction 与 shallow-water；但二者目前都还不满足仓库规则中 `true_foundation_model` 所要求的更强大规模预训练证据，因此保持 `general_pde_solver` 判定。

## 3. 核心论文

### 3.1 CFO: Learning Continuous-Time PDE Dynamics via Flow-Matched Neural Operators

- **DOI**：无 / 未分配
- **Venue**：ICLR 2026
- **Publisher**：ICLR
- **publication_date**：2026-04-23
- **作者**：Xianglong Hou, Xinquan Huang, Paris Perdikaris
- **机构**：University of Pennsylvania
- **正式链接**：https://proceedings.iclr.cc/paper_files/paper/2026/hash/8bfbf4ec87e1e331f0b1adc483b53b6b-Abstract-Conference.html
- **arXiv**：2512.05297；此前注册表仅为预印本，本期确认 ICLR 2026 正式发表
- **published_category**：`operator`
- **foundation_model_level**：`general_pde_solver`
- **方法**：对时间轨迹拟合 spline，以导数构造近似 PDE velocity field，再用 flow matching 训练 neural operator；推理通过 ODE integration 查询任意时间点。
- **数据 / 物理系统**：Lorenz、1D Burgers、2D diffusion-reaction、2D shallow water。
- **泛化方式**：非均匀时间采样、时间分辨率变化、任意时间查询、长时程与 reverse-time inference。
- **核心贡献**：把连续时间语义和 flow matching 引入 PDE operator learning；仅使用部分非均匀时间点训练仍能优于完整数据的自回归基线。
- **局限**：仍需数值积分完成推理；跨复杂几何和大规模多物理预训练证据有限。
- **评分**：相关度 4/5；泛化 3/3；价值 2/2；**总分 9/10**。

### 3.2 Adaptive Mamba Neural Operators

- **DOI**：无 / 未分配
- **Venue**：ICLR 2026
- **Publisher**：ICLR
- **publication_date**：2026-04-23
- **作者**：Zeyuan Song, Zheyu Jiang
- **机构**：Oklahoma State University
- **正式链接**：https://proceedings.iclr.cc/paper_files/paper/2026/hash/dfd1da26fd06a73e4561ecea7d44a97e-Abstract-Conference.html
- **arXiv**：2607.18043
- **published_category**：`operator`
- **foundation_model_level**：`general_pde_solver`
- **方法**：以 Takenaka–Malmquist systems / reproducing kernels 重构 SSM 的函数空间表示，形成 Mamba 型 neural operator。
- **数据 / 物理系统**：fluid physics、solid physics、finance 中的多个 PDE benchmark。
- **泛化方式**：point cloud、structured mesh、regular grid、irregular domain 与不同几何。
- **核心贡献**：把 Mamba/SSM 的高效序列归纳偏置推进到跨网格、跨几何的 operator learning，并提供更明确的函数空间解释。
- **局限**：尚无多 PDE 大规模统一预训练与真实实验数据闭环证据。
- **评分**：4/5 + 3/3 + 2/2 = **9/10**。

### 3.3 DRIFT-Net: A Spectral-Coupled Neural Operator for PDEs Learning

- **DOI**：无 / 未分配
- **Venue**：ICLR 2026
- **Publisher**：ICLR
- **publication_date**：2026-04-23
- **作者**：Jiayi Li, Flora D. Salim
- **机构**：University of New South Wales
- **正式链接**：https://proceedings.iclr.cc/paper_files/paper/2026/hash/c951d202164800b0c45f4e7fbf91cae2-Abstract-Conference.html
- **arXiv**：2509.24868
- **published_category**：`operator`
- **foundation_model_level**：`general_pde_solver`
- **方法**：global low-frequency spectral branch + local image branch，并在各层进行 bandwise coupling。
- **数据 / 物理系统**：Navier–Stokes benchmarks。
- **泛化方式**：重点是 long-horizon rollout 和多尺度频谱稳定性，而非跨 PDE 零样本泛化。
- **核心贡献**：显式解决局部窗口 attention 对全局谱信息传播不足的问题，在更少参数下改善 rollout 误差与吞吐。
- **局限**：验证物理族较窄；更接近高质量 backbone/结构改进，而非独立 foundation model。
- **评分**：4/5 + 2/3 + 2/2 = **8/10**。

### 3.4 Physics-Informed Laplace Neural Operator for Solving Partial Differential Equations

- **DOI**：10.1016/j.jcp.2026.115291
- **Venue**：Journal of Computational Physics, Vol. 566, Article 115291
- **Publisher**：Elsevier
- **publication_date**：本轮未从出版商独立确认，保持 `null`
- **作者**：Heechang Kim, Qianying Cao, Hyomin Shin, Seungchul Lee, George Em Karniadakis, Minseok Choi
- **正式链接**：https://doi.org/10.1016/j.jcp.2026.115291
- **arXiv**：2602.12706；此前注册表为预印本，本期确认正式 JCP 版本
- **published_category**：`pinn`
- **foundation_model_level**：`general_pde_solver`
- **方法**：Laplace-domain neural operator + physics-informed constraints。
- **核心贡献**：把变换域 operator learning 与物理残差监督结合，为时间依赖 PDE 提供不同于 FNO/时域自回归的建模路径。
- **局限**：正式出版日期仍需出版商页面进一步回填；目前证据不足以归为 foundation model。
- **评分**：4/5 + 2/3 + 2/2 = **8/10**。

## 4. 扩展论文

### Spectral modal operator learning framework with decoupled spatial and temporal representations for unsteady flows

- **DOI**：10.1063/5.0327449
- **Venue**：Physics of Fluids 38(6), 064123
- **Publisher**：AIP Publishing
- **publication_date**：2026-06-22（Published Online）
- **作者 / 机构**：Chaeyun Won, Jongmok Lee, Anna Lee（POSTECH）；Bumsoo Park（Seoul National University of Science and Technology）；Seungchul Lee（KAIST）
- **正式链接**：https://doi.org/10.1063/5.0327449
- **published_category**：`surrogate`
- **foundation_model_level**：`surrogate_model`
- **技术贡献**：以 SPOD 的频率分辨模态作为 DeepONet 表示，减少空间/时间模态强耦合对高频非定常动力学的限制。
- **为何属于 extended**：方法对 ROM/operator-learning 接口有价值，但验证仍集中在非定常流与参数化 surrogate，跨 PDE、跨几何与大规模预训练通用性有限。
- **评分**：3/5 + 1/3 + 2/2 = **6/10**。

## 5. 分类总结

| published_category | core | extended | 代表工作 |
|---|---:|---:|---|
| `operator` | 3 | 0 | CFO, AMO, DRIFT-Net |
| `pinn` | 1 | 0 | PILNO |
| `surrogate` | 0 | 1 | SPOD-DeepONet |
| `foundation_model` | 0 | 0 | 本期无达到该等级的新正式工作 |
| `data` | 0 | 0 | 本期无新增 |
| `enabling` | 0 | 0 | 作为副分类出现在多篇记录中 |

## 6. Venue 覆盖

本轮按规则覆盖/复查 ICLR 2026、ICML/NeurIPS 已有正式 proceedings、JCP、CMAME、Physics of Fluids、Physics of Plasmas、SISC、CPC、MLST 及与 operator/surrogate 相关的正式出版元数据。ICLR 2026 补出 3 篇此前未进入正式周报的高价值工作；JCP 确认 PILNO 正式版本；Physics of Fluids 补充一篇 extended。其他 venue 本轮没有发现同时满足“未去重 + 正式证据充分 + 技术价值达到收录标准”的新增项，因此不强制凑数。

## 7. 正式发表状态更新

| arXiv ID | 原状态 | 正式状态 | DOI / venue | 处理 |
|---|---|---|---|---|
| 2512.05297 | arXiv / venue 缺失 | published | ICLR 2026 | 已生成高置信 registry patch |
| 2602.12706 | arXiv / DOI 缺失 | published | 10.1016/j.jcp.2026.115291 / JCP 566, 115291 | 已生成高置信 registry patch；publication_date 暂不猜测 |

## 8. 待人工确认

本期没有需要因元数据冲突而进入 `pending` 的论文。PILNO 的 `publication_date` 尚未由出版商页面独立确认，但 DOI、venue、volume/article number 已足以确认正式发表身份；因此它不是“正式状态待确认”，而只是一个待补全的非关键日期字段。

## 9. 仓库写入与审计说明

- W35 结构化增量：`metadata/published_papers_2026_W35.jsonl`
- W35 状态补丁：`metadata/paper_registry_updates_2026_W35.jsonl`
- 本周报：`digests/published/AI-for-PDE-正式发表周报-2026-W35.md`
- 权威主表与 README：本轮不采用截断内容覆盖；如无法在 Connector 中完成完整安全重写，则保持原文件不变并在运行日志中明确记录。
