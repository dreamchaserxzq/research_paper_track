# AI for PDE 正式发表论文追踪周报 · 2026-W46

> **检索日期**：2026-11-09 UTC。常规覆盖窗口：2026-10-31 01:44 至 2026-11-09 01:20 UTC（W45 上次成功覆盖点回退约 48 小时）。历史回溯：2023-11-09 至 2026-11-09 UTC；既有预印本的正式状态复查不限三年。
>
> **出版事实与检索事实分开**：5 篇入选中的 4 篇是历史正式论文的补录或状态回填，只有 FBKAN 于本次覆盖窗口内（2026-11-05）正式在线出版。由于无法独立取得 PDE-PFN 的 NeurIPS 官方接收决定，本轮结构化运行状态记为 **degraded**，不据此推进成功覆盖检查点。

## 一、本期概览

| 指标 | 数量 | 说明 |
|---|---:|---|
| 原始候选 | **12** | 5 收录，2 排除，5 待确认 |
| 去重后候选 | **12** | 对照统一注册表的 arXiv、DOI 及标题作者身份；没有重复计算 |
| 官方正式状态明确 | **11** | 5 收录 + 2 正式但不相关 + 4 有 PMLR 官方 proceedings、尚缺可信稳定论文标识 |
| 核心入选 core | **3** | DISCO、Flowers、Diffusion Last Layer |
| 扩展入选 extended | **2** | RLMesh、FBKAN |
| 既有预印本正式状态更新 | **1** | DISCO：preprint → published |
| 新增正式论文身份 | **4** | Flowers、Diffusion Last Layer、RLMesh、FBKAN |
| 已发表 / 正式接收新增断言 | **5 / 0** | 本期五条正式出版事件均为 published |
| 待人工确认 | **5** | Origo、MERLIN、ReViT、MiSe-GNN、PDE-PFN |
| 已正式发表但排除 | **2** | Neural SINDy、OPCNet：主要研究 ODE |
| 覆盖质量 | **degraded** | NeurIPS/OpenReview 官方接收线索未能完成核验 |

本期 8 篇有稳定 arXiv/DOI 标识可进入结构化候选（5 入选、2 排除、1 pending），另外 4 篇虽已有正式 PMLR 页面，但没有得到可靠匹配的 arXiv 或论文 DOI，遵守仓库事件契约而只列入周报待确认。**正式存在不等于可安全合并入统一注册表**。

## 二、研究趋势与重要判断

1. **可组合的算子模块不等于已验证的跨 PDE 零样本泛化**。DISCO 从短轨迹生成低参数量演化算子，Flowers 学习空间位移与特征重采样，Diffusion Last Layer（DLL）在算子输出端学习低秩随机系数分布，分别对准动力学识别、非局部传输与概率输出。三者的作用位置、计算成本与泛化协议均不同。
2. **空间预算需要区分生成端与模型端**。RLMesh 在高保真数据生成端优化网格点；Flowers 在推理模型内部通过可学习采样位移实现空间交互；上一期物理残差引导粗化作用于图层节点分配。比较这些模块时应分别计入数值求解、模型训练和单次推理成本。
3. **局部子域与全场耦合应分开设计**。FBKAN 使用局部 KAN 子网络与多级域分解，适合研究多尺度表示和局部高梯度，但局部逼近准确并不自动保证跨子域边界的连续通量或全局守恒。
4. **概率物理预测不能只看 NRMSE**。DLL 关注随机 PDE 场分布和长时滚动稳定性，后续应增加分位区间覆盖、校准误差、守恒漂移及扩散采样成本指标。
5. **正式发表与预印本热度分工**。HotPOT 和近期统一潜空间预印本值得持续追踪，但本次没有足以将其提升为正式发表/接收状态的官方证据。

## 三、核心入选论文（core）

### 3.1 DISCO: learning to DISCover an evolution Operator for multi-physics-agnostic prediction

| 字段 | 正式核验信息 |
|---|---|
| 论文身份 | [arXiv:2504.19496](https://arxiv.org/abs/2504.19496)，仓库此前为 preprint |
| 正式状态 | **published** |
| DOI | 未在正式页面确认，null |
| Venue / Publisher | ICML 2025 / PMLR Volume 267，44750–44774 |
| publication_date | **2025-10-06**（PMLR 卷在线出版日期） |
| 官方证明 | https://proceedings.mlr.press/v267/morel25a.html |
| 作者 | Rudy Morel、Jiequn Han、Edouard Oyallon |
| 机构 | 本次官方摘要页未独立确认 |
| published_category | **foundation_model**；辅类 operator、enabling |
| foundation_model_level | **foundation_model_candidate** |
| published-v2 评分 | **相关度 4 + 泛化 2 + 创新证据 2 = 8/10** |

**方法与系统**：由短时间的观测场序列通过超网络识别或生成小型演化算子，然后以时间积分进行预测。官方论文报告多物理演化数据的预训练和下游适配，用动力学识别与状态推进分离的方式实现跨任务迁移。

**核心贡献**：为“共享识别主干 + 任务相关小算子”提供可学习的替代方案。**泛化与局限**：主要证据来自所测试物理和初值分布，仍依赖短轨迹输入，不能把其大规模预训练宣传直接等同于任意未见 PDE、边界、离散几何的严格零样本解算。本期为已有预印本正式版本回填，非本周首次发表。

### 3.2 Flowers: A Warp Drive for Neural PDE Solvers

| 字段 | 正式核验信息 |
|---|---|
| 论文身份 | [arXiv:2603.04430](https://arxiv.org/abs/2603.04430) |
| 正式状态 | **published** |
| DOI | 未在 PMLR 页面确认，null |
| Venue / Publisher | ICML 2026 / PMLR Volume 306，91390–91418 |
| publication_date | **2026-09-29** |
| 官方证明 | https://proceedings.mlr.press/v306/muser26a.html |
| 作者 | Till Muser、Alexandra Spitzer、Matti Lassas、Maarten V. De Hoop、Ivan Dokmanić |
| 机构 | 具体单位未按正式作者详情独立核验 |
| published_category | **operator**；辅类 enabling |
| foundation_model_level | **general_pde_solver** |
| published-v2 评分 | **相关度 4 + 泛化 2 + 创新证据 2 = 8/10** |

**方法与系统**：网络预测多头空间位移场，并沿位移方向重采样特征，将空间 warp 作为非局部信息传输模块；在多尺度残差网络中与 attention、FNO 等空间混合方法形成替代关系。论文报告流动、波动及其他 2D/3D 时变 PDE，包含约 17M 和 150M 参数规模测试。

**贡献与局限**：提供高效非局部算子传播的另一路径。多任务基准的误差改善不证明任意新 PDE 的零样本求解，近线性成本也依赖固定的采样/头数设定；未宣称对一般复杂边界或任意点云自动保证守恒。

### 3.3 Generative Neural Operators through Diffusion Last Layer（DLL）

| 字段 | 正式核验信息 |
|---|---|
| 论文身份 | [arXiv:2602.04139](https://arxiv.org/abs/2602.04139) |
| 正式状态 | **published** |
| DOI | 未在 PMLR 页面确认，null |
| Venue / Publisher | ICML 2026 / PMLR Volume 306，97234–97262 |
| publication_date | **2026-09-29** |
| 官方证明 | https://proceedings.mlr.press/v306/park26aa.html |
| 作者 | Sungwon Park、Anthony Zhou、Hongjoong Kim、Amir Barati Farimani |
| 机构 | 本次未单独核验 |
| published_category | **operator**；辅类 enabling |
| foundation_model_level | **enabling_method** |
| published-v2 评分 | **相关度 4 + 泛化 2 + 创新证据 2 = 8/10** |

**方法与系统**：使用输入条件下的低秩、Karhunen–Loève 启发式场表示，在低维系数空间运行条件扩散模型，作为确定性神经算子的可插拔概率输出层；在随机强迫 PDE 和长时间滚动场景中评价统计保真性。

**贡献与局限**：可为现有主干提供分布预测与不确定性表达，不必直接用扩散模型生成完整空间场。但多步扩散采样开销、长期随机轨迹的校准与守恒性质均需独立测试；其 OOD 统计泛化不能替代跨 PDE 正向求解能力。

## 四、扩展入选论文（extended）

### 4.1 Accelerating PDE Surrogates via RL-Guided Mesh Optimization（RLMesh）

- **身份 / 状态**：[arXiv:2603.02066](https://arxiv.org/abs/2603.02066)，**published**；DOI 未确认。
- **Venue / Publisher / Date**：AISTATS 2026 / PMLR Volume 300，3286–3294 / **2026-08-30**（卷正式上线日期）；[官方论文页](https://proceedings.mlr.press/v300/meng26a.html)。
- **作者**：Yang Meng、Ruoxi Jiang、Zhuokai Zhao、Chong Liu、Rebecca Willett、Yuxin Chen；具体单位本次未独立核验。
- **类别与评分**：published_category **enabling**（辅类 surrogate、data）；foundation_model_level **enabling_method**；**3 + 1 + 2 = 6/10**。
- **方法 / 物理 / 泛化**：以强化学习优化模拟网格点布局，用较低成本代理估计采样策略对高保真数据及后续 surrogate 训练的收益。官方实验覆盖 1D Burgers 和 2D Darcy。
- **扩展层级原因**：可迁移为 PDE 训练集的自适应数据生成策略，但尚无对复杂三维几何、多物理、湍流的全面泛化证明；它更侧重数据预算，而不是通用算子基础模型。

### 4.2 Finite basis Kolmogorov-Arnold networks: Domain decomposition for data-driven and physics-informed problems（FBKAN）

- **身份 / 状态**：[arXiv:2406.19662](https://arxiv.org/abs/2406.19662)，**published**；DOI **[10.1007/s10444-026-10376-7](https://doi.org/10.1007/s10444-026-10376-7)**。
- **Venue / Publisher / Date**：Advances in Computational Mathematics，Vol.52 Article 103 / Springer Nature / **2026-11-05**；[官方期刊页](https://link.springer.com/article/10.1007/s10444-026-10376-7)。
- **作者**：Amanda A. Howard、Bruno Jacob、Sarah Helfert、Alexander Heinlein、Panos Stinis；机构详情未独立复核。
- **类别与评分**：published_category **pinn**（辅类 enabling）；foundation_model_level **enabling_method**；**3 + 1 + 2 = 6/10**。
- **方法 / 物理 / 泛化**：把有限基 KAN 分配到多个局部子域并行训练，扩展为多级子域架构，结合 physics-informed 约束处理多尺度与带噪数据问题。
- **扩展层级原因**：域分解与多尺度表示具有模块化复用潜力，但不是跨 PDE 预训练基座。跨域接口约束、连续通量、分布式训练通信与物理保证仍需补充验证。

## 五、按正式主分类汇总

| published_category | core | extended | 本期代表 |
|---|---:|---:|---|
| foundation_model | 1 | 0 | DISCO（仅 foundation_model_candidate） |
| operator | 2 | 0 | Flowers、DLL |
| enabling | 0 | 1 | RLMesh |
| pinn | 0 | 1 | FBKAN |
| surrogate | 0 | 0 | RLMesh 为辅类 |
| data | 0 | 0 | 数据生成是 RLMesh 辅类 |

分类按**主类**单计数，支持多个辅类；本期无新入选类别不等于该研究领域没有进展。

## 六、Venue 核验覆盖与排除

| Venue / 官方来源 | 本期实际核验与结果 |
|---|---|
| ICML 2025 / PMLR 267 | DISCO 正式 proceedings，**1 篇核心**（已有预印本状态回填） |
| ICML 2026 / PMLR 306 | Flowers、DLL **2 篇核心**；Origo、MERLIN、ReViT、MiSe-GNN 均有 proceedings 但缺确认的可入库身份，保留 pending |
| AISTATS 2026 / PMLR 300 | RLMesh **1 篇扩展** |
| Advances in Computational Mathematics / Springer | FBKAN **1 篇扩展**（2026-11-05 在线发表） |
| Nonlinear Dynamics / Springer | Neural SINDy 已发表，但主要为 ODE 方程识别，排除 |
| Neural Processing Letters / Springer | OPCNet 已发表，但集中振荡 ODE 拟合，排除 |
| NeurIPS 2026 / OpenReview | PDE-PFN 官方决定未能取得；HotPOT 等没有可回查的正式接收证据，**0 篇** |
| JCP、CMAME、SISC、MLST、Physics of Plasmas、Nuclear Fusion | 对近期线索进行定向检索，未获得可独立核验且未收录的本期高价值新正式论文；**不是全量穷举** |

## 七、正式版本状态更新

| arXiv | 原状态 | 本次正式状态 | Venue / Publisher | DOI | publication_date |
|---|---|---|---|---|---|
| [2504.19496](https://arxiv.org/abs/2504.19496)（DISCO） | preprint | **published** | ICML 2025 / PMLR Vol.267 | null | **2025-10-06** |

正式证据：https://proceedings.mlr.press/v267/morel25a.html 。

其余 Flowers、DLL、RLMesh、FBKAN 属于四个**新增论文身份**，不是既有注册表的预印本正式状态升级。本期没有修改任何已存在的可信 DOI、venue 或 publication_date。

## 八、待人工确认与未解决事项

1. **Origo: Interpretable Multi-physics PDE Foundation Model through Neural Operator Splitting**。[ICML 2026 官方论文页](https://proceedings.mlr.press/v306/sun26aa.html)。具算子库组合与多物理泛化研究价值，但仍未取得可独立匹配的 arXiv 或正式 DOI，继续 W45 pending。
2. **MERLIN: Interpretable Functional Koopman Learning with Non-Markovian Closure for Spatiotemporal Systems**。[ICML 2026 官方论文页](https://proceedings.mlr.press/v306/lu26u.html)。非 Markov 记忆与分辨率泛化值得关注；稳定 arXiv/DOI 仍需证实，继续 pending。
3. **ReViT: Rotational-equivariant Vision Transformers for Neural PDE Solvers**。[ICML 2026 官方论文页](https://proceedings.mlr.press/v306/wei26p.html)。旋转等变 CFD/MHD 相关结果需研究，但缺确认的 arXiv/正式 DOI，继续 pending。
4. **Error-Driven Graph Augmentation for Mesh-Based PDE Surrogates（MiSe-GNN）**。[ICML 2026 官方论文页](https://proceedings.mlr.press/v306/nguyen26a.html)。网格图依据误差信息自适应加边以改善非局部传播；本次未独立找到可靠的 arXiv/DOI，暂不绕过入库身份契约。
5. **PDE-PFN: Prior-Data Fitted Neural PDE Solver**。[arXiv:2610.13334](https://arxiv.org/abs/2610.13334)。第三方名单出现 NeurIPS 2026 线索，但官方 NeurIPS/OpenReview 接收决定本轮无法访问。**仍保持 preprint，不当作 accepted 或 published**；本轮相关来源查询标记失败，运行覆盖 degraded。

**另外需要元数据审计**：W45 曾指出 W44 部分 ICML 2026 条目将会议开幕日 **2026-07-06** 填为 publication_date，而 PMLR 306 的正式在线出版日为 **2026-09-29**。该问题与五个论文 pending 分开计算，本轮不擅自覆盖历史正式日期；应逐篇按照 source_records 与 correction 事件规范处理。

正式发表但本期排除：
- **Neural SINDy: robust discovery of governing equations using neural ODEs and sparse identification**，[DOI 10.1007/s11071-026-13122-2](https://doi.org/10.1007/s11071-026-13122-2)，出版于 2026-11-06；主要处理 ODE 系统识别。
- **OPCNet: Oscillatory Pattern Capturing Network for Highly Oscillatory Data**，[DOI 10.1007/s11063-026-11896-5](https://doi.org/10.1007/s11063-026-11896-5)，出版于 2026-11-04；强调振荡 ODE 模型，PDE 前向求解普适性不足。

## 九、对 UPFM 的可证伪实验建议

**算子专家组合实验**：固定总参数和训练数据，在多 PDE、非均匀几何、分辨率转移及长时间查询四条轴线上，将 DISCO 的轨迹条件化小算子、Flowers 的空间 warp、普通 Fourier/graph/attention 层并列作为不同主干/专家候选，测量预测误差、稳定性、全链路耗时。不要将某一流动基准的优势解释为通用 PDE foundation 能力。

**概率和守恒实验**：在确定性 forward 模型上附加 DLL 系数扩散层，与普通均值预测及直接时序不确定性头比较，报告输出分布校准、时间间隔外推、守恒误差和采样开销。FBKAN 域分解与 RLMesh 模拟网格采样应分别消融，不能合称同一“自适应网格模块”。

## 十、记录与审计说明

- **正式事件**：metadata/inbox/2026-11-09.jsonl；5 条有可核实身份的 publication 事件，均含官方证据、published-v2 方案和完整评分。DISCO 是唯一既有预印本的正式升级。
- **运行证据**：metadata/runs/published-2026-W46.json；7 组来源核验、8 个具 ID 的候选、1 项未完成的官方接收查询，明确标记 degraded，不推进上次成功覆盖日期。
- **生成视图**：应由 scripts/papertrack.py build 重建统一表、两份兼容表、README 最近 12 期正式周报索引与数据质量报告；不得直接修改生成文件。
- **官方来源入口**：[PMLR ICML 2025 Volume 267](https://proceedings.mlr.press/v267/)、[PMLR AISTATS 2026 Volume 300](https://proceedings.mlr.press/v300/)、[PMLR ICML 2026 Volume 306](https://proceedings.mlr.press/v306/)、[FBKAN Springer](https://link.springer.com/article/10.1007/s10444-026-10376-7)。
- **证据边界**：对 Springer 与 PMLR 官方页面核查仅构成本次明确论文的正式证据，不代表三年内所有 venue 穷举；任一预印本只凭 arXiv 或作者主页都不得升级为已接收或已发表。

*报告核验基准：2026-11-09 UTC；发表日期、发现日期和仓库回填日期分别记录。*
