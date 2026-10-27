# AI for PDE 正式发表论文追踪周报 · 2026-W44

> 本周报只统计已正式发表或已获官方接收证据的 AI-for-PDE / Scientific Machine Learning 工作。  
> 检索范围：**2023-10-27 至 2026-10-27 UTC**。  
> 本期为迁移后首个 `published-YYYY-WW` 结构化运行；正式状态以官方 proceedings / conference 页面为准。

## 1. 本期概览

| 指标 | 数量 |
|---|---:|
| 原始候选 | 9 |
| 去重后候选 | 9 |
| 正式状态明确 | 9 |
| 核心入选（core） | 5 |
| 扩展入选（extended） | 2 |
| 已有预印本正式状态更新 | 5 |
| 新增可入库正式论文 | 2 |
| 待人工确认 / 待补稳定身份 | 2 |

本期最重要的变化来自 **ICML 2026 PMLR Volume 306 正式 proceedings 上线**，使此前若干仅以预印本或“已接收”线索存在的工作可以正式落库；同时，NeurIPS 2026 官方 Downloads 已列出 AOT-POT 与 Phaedra，但截至本次检查尚未找到对应正式 proceedings，因此二者严格记为 **accepted**，不提前记为 published。

## 2. 趋势总结

1. **PDE foundation model 从“扩大模型容量”转向“可组合 / 可对齐机制”。** AOT-POT 通过输入依赖的 operator transformation 对齐多 PDE 解算子；Test-time Generalization 通过测试时算子组合实现未见物理的零样本适配。二者都把“如何组合已有能力”放在核心位置，而非单纯依赖更大共享主干。
2. **物理场表示本身成为基座模型关键瓶颈。** Phaedra 将 morphology 与 gain 分开 tokenization；GPO 则用可学习 Gaussian basis 形成 mesh-agnostic、resolution-agnostic 的显式中间表示，均直接影响跨网格、复杂几何与跨维度能力。
3. **生成式 PDE 求解继续向物理约束和低成本推理靠拢。** PIDDM 将 PDE 约束放入 post-hoc distillation，绕开扩散中间噪声状态难以直接满足 PDE 的问题，并支持单步生成、前向/反问题和部分观测重建。
4. **领域专用 physics-informed operator 仍有价值，但不等同于通用基座模型。** Grad-Shafranov 工作在聚变平衡问题上展示 sim-to-real 与 OOD 稳健性，因此作为 extended 收录，而不提升为 foundation model。
5. **大算子模型的 PEFT 开始形成独立研究线。** F-Adapter 已正式发表于 NeurIPS 2025，并给出 LoRA 在 Fourier operator 上的局限分析及频率自适应 Adapter 方案。

## 3. 核心论文

### 3.1 AOT-POT: Adaptive Operator Transformation for Large-Scale PDE Pre-training

- **正式状态**：accepted
- **venue / publisher**：NeurIPS 2026 / NeurIPS
- **publication_date**：null（尚未确认正式 proceedings）
- **DOI**：null
- **arXiv**：2605.15793
- **作者**：Qitan Lv, Hong Wang, Zhongkai Hao, Wen Wu, Xuenan Xu, Bowen Zhou, Feng Wu, Chao Zhang
- **正式证据**：https://neurips.cc/Downloads/2026
- **published_category**：`foundation_model`
- **foundation_model_level**：`true_foundation_model`
- **selection_tier**：`core`
- **评分**：relevance 5 + generality 3 + value 2 = **10/10**

**方法与贡献**：不再通过单纯增加参数量处理多 PDE 异质性，而是在每个子层前后对隐藏表示执行输入依赖的多流 operator transformation，并利用 Sinkhorn 投影的双随机矩阵稳定混合，使结构差异明显的 PDE solution operators 更容易由统一模型联合建模。

**数据 / 泛化**：arXiv 版本报告 12 个 PDE benchmark，并强调对预训练未见 PDE 类型的 OOD fine-tuning 能力。

**局限**：截至 2026-10-27，本次只确认 NeurIPS 官方 Downloads 列名，尚未确认正式 proceedings 页面，因此不赋予 published 状态或正式发表日期。

### 3.2 Phaedra: Learning High-Fidelity Discrete Tokenization for the Physical Sciences

- **正式状态**：accepted
- **venue / publisher**：NeurIPS 2026 / NeurIPS
- **publication_date**：null
- **DOI**：null
- **arXiv**：2602.03915
- **作者**：Levi Lingsch, Georgios Kissas, Johannes Jakubik, Siddhartha Mishra
- **机构**：ETH Zurich CAMLab / IBM Research Europe（按仓库既有日报记录）
- **正式证据**：https://neurips.cc/Downloads/2026
- **published_category**：`enabling`
- **foundation_model_level**：`enabling_method`
- **selection_tier**：`core`
- **评分**：4 + 3 + 2 = **9/10**

**方法与贡献**：采用 shape-gain / POD 启发的离散 tokenization，将物理场的形态信息和幅值信息分离量化，针对科学场“精细结构 + 大动态范围”同时保真这一问题提供专用 tokenizer。

**泛化价值**：直接服务于物理基座模型的统一场表征，可影响跨 PDE、跨分辨率和 OOD 物理场的预训练质量。

**局限**：当前是关键支撑模块，不是完整 PDE foundation model；正式状态暂为 accepted。

### 3.3 Test-time Generalization for Physics through Neural Operator Splitting

- **正式状态**：published
- **venue / publisher**：ICML 2026 / PMLR
- **publication_date**：2026-07-06
- **DOI**：null
- **arXiv**：2602.00884
- **作者**：Louis Serrano, Jiequn Han, Edouard Oyallon, Shirley Ho, Rudy Morel
- **正式链接**：https://proceedings.mlr.press/v306/serrano26a.html
- **published_category**：`operator`
- **foundation_model_level**：`enabling_method`
- **selection_tier**：`core`
- **评分**：4 + 3 + 2 = **9/10**

**方法与贡献**：基于已有 operator dictionary，在测试时搜索训练算子的组合来近似未见动力学，不更新预训练权重。该机制覆盖参数外推和未见物理组合，并能恢复潜在 PDE 参数。

**研究意义**：这是“专家 / 算子能力组合”路线的强相关正式工作，说明基座模型的泛化可以部分转化为测试时组合搜索，而非要求每个新物理都再训练。

**局限**：依赖已有 operator dictionary 的覆盖范围，组合空间和测试时搜索成本仍是扩展到海量物理机制时的关键问题。

### 3.4 From Basis to Basis: Gaussian Particle Representation for Interpretable PDE Operators

- **正式状态**：published
- **venue / publisher**：ICML 2026 / PMLR
- **publication_date**：2026-07-06
- **DOI**：null
- **arXiv**：2602.21551
- **作者**：Zhihao Li, Yu Feng, Zhilu Lai, Wei Wang
- **正式链接**：https://proceedings.mlr.press/v306/li26aq.html
- **published_category**：`operator`
- **foundation_model_level**：`general_pde_solver`
- **selection_tier**：`core`
- **评分**：4 + 3 + 2 = **9/10**

**方法与贡献**：用可学习 Gaussian basis 将连续物理场映射为带中心、各向异性尺度和权重的显式粒子表示；再在模态空间做 Petrov–Galerkin 测量与全局 Gaussian attention。该表示具有可视化和解释性。

**泛化方式**：resolution-agnostic、支持 irregular geometry，并展示 2D→3D 扩展；固定模态预算下复杂度随样本数近线性增长。

**局限**：Gaussian basis 是否能统一处理强间断、复杂多尺度界面和高度非局部约束，还需要更广泛 PDE 体系验证。

### 3.5 Physics-Informed Distillation of Diffusion Models for PDE-Constrained Generation

- **正式状态**：published
- **venue / publisher**：ICML 2026 / PMLR
- **publication_date**：2026-07-06
- **DOI**：null
- **arXiv**：2505.22391
- **作者**：Yi Zhang, Peng Wang, Difan Zou
- **正式链接**：https://proceedings.mlr.press/v306/zhang26gl.html
- **published_category**：`pinn`
- **foundation_model_level**：`general_pde_solver`
- **selection_tier**：`core`
- **评分**：4 + 2 + 2 = **8/10**

**方法与贡献**：将 PDE constraint 从 diffusion denoising 过程移到 post-hoc distillation 阶段，避免直接对 noisy intermediate state 施加 PDE 约束产生的 Jensen's Gap；蒸馏后支持单步生成。

**任务覆盖**：前向问题、反问题和随机部分观测重建，并在多种 PDE benchmark 上验证。

**局限**：仍依赖先训练生成模型；物理一致性保证属于学习与蒸馏层面的经验约束，并非一般意义上的严格离散守恒保证。

## 4. 扩展论文

### 4.1 F-Adapter: Frequency-Adaptive Parameter-Efficient Fine-Tuning in Scientific Machine Learning

- **正式状态**：published
- **venue**：NeurIPS 2025
- **DOI**：10.52202/085713-3710
- **publication_date**：2025-12-02
- **arXiv**：2509.23173
- **正式链接**：https://proceedings.neurips.cc/paper_files/paper/2025/hash/a12e362d89d4e0b40760f839f91550ee-Abstract-Conference.html
- **published_category**：`enabling`
- **foundation_model_level**：`enabling_method`
- **selection_tier**：`extended`
- **评分**：3 + 2 + 2 = **7/10**

该工作系统研究 Large Operator Models 的 PEFT，指出 stacked LoRA 在 Fourier 层存在随深度放大的逼近误差限制，并提出 Frequency-Adaptive Adapter。其主要价值是基座算子模型的下游高效适配，而非新的通用 PDE solver，因此列 extended。

### 4.2 Physics-informed Neural Operator Learning for Nonlinear Grad-Shafranov Equation

- **正式状态**：published
- **venue / publisher**：ICML 2026 / PMLR
- **publication_date**：2026-07-06
- **DOI**：null
- **arXiv**：2511.19114
- **正式链接**：https://proceedings.mlr.press/v306/ding26w.html
- **published_category**：`pinn`
- **foundation_model_level**：`single_task_method`
- **selection_tier**：`extended`
- **评分**：3 + 1 + 2 = **6/10**

该工作把数据锚点与 PDE residual 结合到 Transformer-KAN Neural Operator 中，针对非线性 Grad–Shafranov 方程评估多参数分布偏移，并在 EXL-50U 输入上与运行中的 equilibrium solver 对比，报告平均相对 RMSE 1.27% 与毫秒级推理。其 sim-to-real 和 OOD 设计有价值，但任务仍集中于单一聚变平衡 PDE，因此不进入 core。

## 5. 分类总结

| published_category | 本期入选 | 代表论文 |
|---|---:|---|
| `foundation_model` | 1 | AOT-POT |
| `operator` | 2 | Test-time Generalization, GPO |
| `pinn` | 2 | PIDDM, Grad-Shafranov TKNO |
| `enabling` | 2 | Phaedra, F-Adapter |
| `surrogate` | 0 | — |
| `data` | 0 | — |

多标签上，operator / enabling 的交叉最明显，说明本期正式工作更多在“表示、组合和适配机制”上推进，而不是新增大型数据体系。

## 6. Venue 覆盖

本期重点核验：

- **ICML 2026 / PMLR Volume 306**：正式 proceedings 已可回查；确认 Test-time Generalization、GPO、PIDDM、Grad-Shafranov TKNO，以及两个缺稳定入库身份的 Origo / MERLIN。
- **NeurIPS 2026**：官方 Downloads 已列 AOT-POT 与 Phaedra；由于会议尚未举行且未确认正式 proceedings，严格记为 accepted。
- **NeurIPS 2025 proceedings**：补回 F-Adapter 的正式主会记录与 DOI。
- **JCP / CMAME / SISC / MLST / Physics of Plasmas / Nuclear Fusion 等**：本次以已有高相关 registry 状态复查为主，未发现比上述候选更高置信且尚未入库的新增 core 正式版本。

未为满足数量而纳入普通单 PDE PINN、小幅 benchmark 改进或只有 arXiv / 项目主页证据的工作。

## 7. 正式发表状态更新

| arXiv | 论文 | 原状态 | 新状态 | 正式 venue | publication_date |
|---|---|---|---|---|---|
| 2605.15793 | AOT-POT | preprint | accepted | NeurIPS 2026 | null |
| 2602.03915 | Phaedra | preprint | accepted | NeurIPS 2026 | null |
| 2602.00884 | Test-time Generalization | preprint | published | ICML 2026 | 2026-07-06 |
| 2511.19114 | Grad-Shafranov TKNO | preprint | published | ICML 2026 | 2026-07-06 |
| 2509.23173 | F-Adapter | preprint | published | NeurIPS 2025 | 2025-12-02 |

其中 F-Adapter 新补 DOI：**10.52202/085713-3710**。

## 8. 待人工确认 / 待补稳定身份

### Origo: Interpretable Multi-physics PDE Foundation Model through Neural Operator Splitting

- **正式状态本身明确**：ICML 2026 PMLR 306:116957–116975。
- **官方链接**：https://proceedings.mlr.press/v306/sun26aa.html
- **价值判断**：高度相关，若能入库预计应为 `foundation_model / true_foundation_model / core`。
- **阻塞点**：本次检索未找到 arXiv ID 或 DOI；当前 OPERATIONS 要求新事件必须提供 arXiv ID 或 DOI，因此未绕过契约创建 canonical event。
- **建议**：后续通过作者主页、OpenReview metadata 或 DOI/索引更新继续补稳定身份；确认后再入库。

### Interpretable Functional Koopman Learning with Non-Markovian Closure for Spatiotemporal Systems (MERLIN)

- **正式状态本身明确**：ICML 2026 PMLR 306:81278–81322。
- **官方链接**：https://proceedings.mlr.press/v306/lu26u.html
- **技术价值**：functional Koopman + Mori–Zwanzig non-Markovian memory，支持稀疏/不规则观测、任意分辨率重建与低维 ROM。
- **阻塞点**：同样未找到 arXiv ID 或 DOI，不能按新事件契约直接写入统一表。
- **建议**：补齐稳定身份后作为 `surrogate / enabling` extended 候选入库。

## 9. 数据写入说明

本期 7 条可稳定识别的正式状态事件写入：

- `metadata/inbox/2026-10-27.jsonl`
- 结构化运行证据：`metadata/runs/published-2026-W44.json`

生成兼容视图（`metadata/papers.jsonl`、`paper_registry.jsonl`、`published_papers.jsonl`）、README 与索引必须由 `scripts/papertrack.py build` 统一生成，不手工覆盖。
