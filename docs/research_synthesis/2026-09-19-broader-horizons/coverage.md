# 证据、范围与缺口

研究快照：2026-09-19。本轮共 64 个唯一来源，64 条阅读记录；图谱 138 个节点、296 条关系。

来源包括论文、作者讲义/书籍及官方文档，不把它们统称为同等深度的论文精读。

| 阅读范围 | 唯一来源数 |
|---|---:|
| 正文相关章节 | 56 |
| 书籍部分章节 | 2 |
| 仅摘要 | 3 |
| 官方文档或目录 | 3 |

| 专题 | 来源记录 | 正文相关节 | 书籍部分章 | 摘要 | 官方文档/目录 |
|---|---:|---:|---:|---:|---:|
| AI 基础与生成 | 18 | 18 | 0 | 0 | 0 |
| AI 推理与行动 | 18 | 18 | 0 | 0 | 0 |
| PDE 数值方法 | 19 | 13 | 2 | 2 | 2 |
| 跨域机制与学科背景 | 9 | 7 | 0 | 1 | 1 |

## 边界

- 正文阅读指来源清单里明确标出的机制、实验或讨论章节；未逐页核对所有附录、证明和结果表。
- 没有复现论文、训练模型或对作者代码作全面审计；X1—X9 都是未验证研究问题，新颖性未确立。
- 既有454条登记及42个重点回查工作保留在上一快照，本轮不把它们计入重新阅读。
- 截止日期表示本次调研时间，不表示截至当天的新文献已经穷尽；2026年材料是按问题选取的样本。
- 年份可能是首发年、正式出版年或书籍版本年；以来源的版本说明为准。动态文档未确证出版年时留空。
- 实时搜索结果曾出现打不开的全文；降级为摘要/官方目录的来源保留访问限制，不用检索摘要代替正文。
- 图谱边是知识组织与证据链接；没有提取全体文献的真实引用网络。
- 现有注册表、历史评分与定时任务未因此扩展；新成果本地生成，未提交或远程发布。

## 2026年来源

以下按本次来源记录列出；这不是“2026最新工作”的完整排行榜。

- [Qwen3.5-Omni Technical Report](https://arxiv.org/html/2604.15804v2)：正文相关章节；§2.1 Overview；§2.2 Audio Transformer；§2.3 Audio-visual Timestamp；§2.4 Speech Generation / ARIA；§2.5 Designs for Streaming and Concurrency；§3 Pretraining
- [How Text Quality Interventions Reshape Neural Scaling Laws for LLMs: Empirical Study](https://proceedings.iclr.cc/paper_files/paper/2026/file/6544c0b53cc1ea51d0c7086b536830a8-Paper-Conference.pdf)：正文相关章节；p.1 Abstract（实验范围）；§2 Background, p.3（联合 scaling 拟合）；§3 QualityPajama, p.4；§4, pp.4–7（干预及验证集依赖）；§5 / Figure 5 与 §6 Discussion, p.9
- [Verifiable Process Rewards for Agentic Reasoning](https://arxiv.org/html/2605.10325v2)：正文相关章节；初读v1（2026-05-11）：§2.1–§2.4，命题1–3；§3表1–2；2026-09-19定向复核v2（2026-05-27）：§2.1–§2.4，命题1–3；§3表1–2及§3.1–§3.3相关实验说明；arXiv v2版本说明：更正minor typos及LLM-assisted data extraction errors；未进行全篇版本差异审计
- [Reasoning Arena: Trace Tournaments When Verifiable Rewards Fall Short](https://arxiv.org/html/2606.09380v1)：正文相关章节；v1，2026-06-08；§3、§4；§5表1–2
- [Continual Calibration: Coverage Can Collapse Before Accuracy in Lifelong LLM Fine-Tuning](https://arxiv.org/html/2604.23987v1)：正文相关章节；v1，2026-04-27；§2；§4.2–§4.6；§5定理6、7和命题8；§6
- [Accelerating High-Order Finite Element Simulations at Extreme Scale with FP64 Tensor Cores](https://arxiv.org/html/2603.09038v1)：正文相关章节；§I–II：数值应用、FP64动机与离线PDE求解成本；§III开头和摘要：小GEMM映射与扩展实验口径
- [Mosaic: A Benchmark Suite for Differentiable Physics Solvers](https://arxiv.org/html/2606.27895v1)：正文相关章节；v1, 2026-06-26; §3.1–3.3, §4.3–4.4, Discussion and Limitations

## 逐项可回查清单

| 来源 | 年份 | 阅读范围 | 实际位置 |
|---|---:|---|---|
| [Attention Is All You Need](https://arxiv.org/html/1706.03762v7) | 2017 | 正文相关章节 | §3.1 Encoder and Decoder Stacks；§3.2 Attention（含 scaled dot-product 与 multi-head） |
| [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/html/2111.06377v3) | 2021 | 正文相关章节 | §3 Approach；§4.1 Main Properties（遮挡比例、解码器与重建目标消融） |
| [DINOv3](https://arxiv.org/html/2508.10104v1) | 2025 | 正文相关章节 | §3.2 Large-Scale Self-Supervised Learning；§4.1 Loss of Patch-Level Consistency Over Training；§4.2 Gram Anchoring Objective |
| [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/html/2103.00020v1) | 2021 | 正文相关章节 | §2.1 Natural Language Supervision；§2.2 Creating a Sufficiently Large Dataset；§2.3 Selecting an Efficient Pre-Training Method；§2.4 Choosing and Scaling a Model |
| [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/html/2212.04356v1) | 2022 | 正文相关章节 | §2.1 Data Processing；§2.2 Model；§2.3 Multitask Format；§2.4 Training Details；§6 Limitations and Future Work |
| [Qwen3-Omni Technical Report](https://arxiv.org/html/2509.17765v1) | 2025 | 正文相关章节 | §2.1 Overview；§2.2 Audio Transformer；§2.3 Perceivation / TM-RoPE；§2.4 Speech Generation；§2.5 Designs for Streaming and Concurrency |
| [Qwen3.5-Omni Technical Report](https://arxiv.org/html/2604.15804v2) | 2026 | 正文相关章节 | §2.1 Overview；§2.2 Audio Transformer；§2.3 Audio-visual Timestamp；§2.4 Speech Generation / ARIA；§2.5 Designs for Streaming and Concurrency；§3 Pretraining |
| [Denoising Diffusion Probabilistic Models](https://arxiv.org/html/2006.11239v2) | 2020 | 正文相关章节 | §2 Background；§3.2 Reverse Process；§3.4 Simplified Training Objective；Algorithms 1–2 |
| [Flow Matching for Generative Modeling](https://arxiv.org/html/2210.02747v2) | 2022 | 正文相关章节 | §3 Flow Matching；§3.1 Conditional Probability Paths and Vector Fields；§3.2 Conditional Flow Matching / Theorems 1–2；§4 / §4.1 Gaussian Conditional Paths（含 VE/VP diffusion 特例） |
| [Scalable Diffusion Models with Transformers](https://arxiv.org/html/2212.09748v2) | 2022 | 正文相关章节 | §3.1 Preliminaries；§3.2 Diffusion Transformer Design Space |
| [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/html/2312.00752v2) | 2023 | 正文相关章节 | §3.1 Selection as a Means of Compression；§3.2 Improving SSMs with Selection；§3.3 Efficient Implementation of Selective SSMs |
| [Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality](https://arxiv.org/html/2405.21060v1) | 2024 | 正文相关章节 | §5.1 Scalar-Identity Structured State Space Models；§5.2 1-Semiseparable Structured Masked Attention；§5.3 Structured State-Space Duality |
| [DeepSeek-V3 Technical Report](https://arxiv.org/html/2412.19437v2) | 2024 | 正文相关章节 | §2.1.1 Multi-Head Latent Attention；§2.1.2 DeepSeekMoE with Auxiliary-Loss-Free Load Balancing；§2.2 Multi-Token Prediction；§3.3 FP8 Training |
| [Training Compute-Optimal Large Language Models](https://arxiv.org/html/2203.15556v1) | 2022 | 正文相关章节 | §3 Estimating the Optimal Parameter/Training Tokens Allocation；§3.1 Fixed Model Sizes；§3.3 Fitting a Parametric Loss Function；§5 Discussion and Conclusion |
| [DataComp-LM: In search of the next generation of training sets for language models](https://arxiv.org/html/2406.11794v4) | 2024 | 正文相关章节 | §1 Introduction；§3.1 DCLM-Pool / Decontamination；§3.2 Competition Scales；§3.3 Benchmark Tracks；§3.4 Training；§3.5 Evaluation |
| [How Text Quality Interventions Reshape Neural Scaling Laws for LLMs: Empirical Study](https://proceedings.iclr.cc/paper_files/paper/2026/file/6544c0b53cc1ea51d0c7086b536830a8-Paper-Conference.pdf) | 2026 | 正文相关章节 | p.1 Abstract（实验范围）；§2 Background, p.3（联合 scaling 拟合）；§3 QualityPajama, p.4；§4, pp.4–7（干预及验证集依赖）；§5 / Figure 5 与 §6 Discussion, p.9 |
| [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision](https://arxiv.org/html/2407.08608v2) | 2024 | 正文相关章节 | §2.2 GPU Hardware Characteristics and Execution Model；§2.3 Standard Attention and Flash Attention；§3.1 Producer-Consumer Asynchrony；§3.3 Low-Precision with FP8；§5 Discussion, Limitations, Conclusion |
| [Reconciling modern machine learning practice and the bias-variance trade-off](https://arxiv.org/html/1812.11118v2) | 2018 | 正文相关章节 | §1 Introduction / Figure 1；§4 Concluding Thoughts / Inductive Bias |
| [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/html/2201.11903v6) | 2022 | 正文相关章节 | v6，2023-01-10；§1、§2、§3.1 |
| [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/html/2305.18290v1) | 2023 | 正文相关章节 | §3、§4，式(3)–(7)；§5开头 |
| [Let's Verify Step by Step](https://arxiv.org/html/2305.20050v1) | 2023 | 正文相关章节 | §2.1–§2.6；§3–§5；§6.3 |
| [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/html/2408.03314v1) | 2024 | 正文相关章节 | §1–§4；§5.1–§5.2；图1与§7结果概览 |
| [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/html/2501.12948v1) | 2025 | 正文相关章节 | §2.1–§2.3概览；§2.2.1–§2.2.4；§4.2、§5 |
| [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/html/2504.13837v1) | 2025 | 正文相关章节 | §1；§2.1–§2.2；§3.1实验设定；表1、图1–2 |
| [Verifiable Process Rewards for Agentic Reasoning](https://arxiv.org/html/2605.10325v2) | 2026 | 正文相关章节 | 初读v1（2026-05-11）：§2.1–§2.4，命题1–3；§3表1–2；2026-09-19定向复核v2（2026-05-27）：§2.1–§2.4，命题1–3；§3表1–2及§3.1–§3.3相关实验说明；arXiv v2版本说明：更正minor typos及LLM-assisted data extraction errors；未进行全篇版本差异审计 |
| [Reasoning Arena: Trace Tournaments When Verifiable Rewards Fall Short](https://arxiv.org/html/2606.09380v1) | 2026 | 正文相关章节 | v1，2026-06-08；§3、§4；§5表1–2 |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/html/2210.03629v3) | 2022 | 正文相关章节 | v3，2023-03-10；§1、§2；§3–§4任务概览 |
| [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/html/2310.06770v1) | 2023 | 正文相关章节 | §2.1–§2.3；§3；§4.1 |
| [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/html/2404.07972v1) | 2024 | 正文相关章节 | §1；§2.1–§2.3；§5小节目录与原文摘要的失败归因 |
| [Mastering Diverse Domains through World Models](https://arxiv.org/pdf/2301.04104v1) | 2023 | 正文相关章节 | v1 PDF印刷页1–7：概览、Symlog Predictions、World Model Learning、Actor Critic Learning |
| [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](https://arxiv.org/html/2501.10100v1) | 2025 | 正文相关章节 | §III-A–III-C；§IV-E相关结果；§V |
| [π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/html/2504.16054v1) | 2025 | 正文相关章节 | §II–§IV概览；§V-B–§V-E；§VI；附录A-D评测取消说明 |
| [Towards Causal Representation Learning](https://arxiv.org/html/2102.11107v1) | 2021 | 正文相关章节 | §II；§V后半；§VI–§VII开头 |
| [A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/html/2107.07511v1) | 2021 | 正文相关章节 | §1–§1.1；§3.3；§4.1–§4.2 |
| [Continual Calibration: Coverage Can Collapse Before Accuracy in Lifelong LLM Fine-Tuning](https://arxiv.org/html/2604.23987v1) | 2026 | 正文相关章节 | v1，2026-04-27；§2；§4.2–§4.6；§5定理6、7和命题8；§6 |
| [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/html/2401.05566v1) | 2024 | 正文相关章节 | §1；§3.2–§3.3；§6 |
| [Finite Difference and Spectral Methods for Ordinary and Partial Differential Equations](https://people.maths.ox.ac.uk/trefethen/pdetext.html) | 1996 | 书籍部分章节 | 作者未完成书稿，第4章§4.2–4.3，PDF第8–11页：线性适定假设与Lax理论；第7章PDF第2页：全局基与边界限制 |
| [AMath 574: Conservation Laws and Finite Volume Methods — lectures 5 and 15](https://faculty.washington.edu/rjl/classes/hyperbolic2013/am574w2011/index.html) | 2011 | 正文相关章节 | Lecture 5，PDF第12–14页：Godunov通量差更新；Lecture 15，PDF第39–40页：弱熵条件与Lax–Wendroff定理 |
| [Runge–Kutta Discontinuous Galerkin Methods for Convection-Dominated Problems](https://helper.ipam.ucla.edu/publications/pcatut2005/pcatut_5477_reprint2.pdf) | 2001 | 正文相关章节 | §1，PDF第2–5页：空间弱式、块对角质量矩阵、RK步骤和非线性限制 |
| [Finite element exterior calculus: from Hodge theory to numerical stability](https://arxiv.org/pdf/0906.4325v3) | 2010 | 正文相关章节 | §1.1，PDF第3–4页：Poisson弱式与Galerkin；§3.2.2，PDF第24–26页：mixed well-posedness、Theorems 3.2–3.3；摘要与引言：subcomplex/cochain projection |
| [Implicit-Explicit Runge-Kutta Methods for Time-Dependent Partial Differential Equations](https://steveruuth.org/wp-content/uploads/2020/10/ars.pdf) | 1997 | 仅摘要 | 作者托管论文可读摘要与Introduction搜索提取；PDF正文文本编码损坏，未据损坏正文作公式核查 |
| [Challenges in Geometric Numerical Integration](https://www.unige.ch/~hairer/preprints/hairer-pisa.pdf) | 2014 | 正文相关章节 | §1–2，PDF第1–5页：保结构、后向误差分析和修正方程；摘要的高振荡边界 |
| [Iterative Methods for Sparse Linear Systems, Second Edition](https://www-users.cse.umn.edu/~saad/IterMethBook_2ndEd.pdf) | 2003 | 书籍部分章节 | §6.5，书页171–180：GMRES与重启/实现；第9章预条件章节相关段；§14.1，书页470–472：子域与界面矩阵分块 |
| [Algebraic Multigrid Methods](https://arxiv.org/pdf/1611.01917) | 2017 | 正文相关章节 | §2.3–2.4，PDF第12–14页：离散谱与条件数；§4.1–4.2：基本迭代；§5平滑器讨论PDF第38页及摘要粗空间条件 |
| [Entropy stability theory for difference approximations of nonlinear conservation laws and related time-dependent problems](https://www.math.umd.edu/~tadmor/pub/TV%2Bentropy/Tadmor_Acta2003.pdf) | 2003 | 正文相关章节 | §4，PDF第15–16页：Corollary 4.1和熵保守基准；摘要的耗散比较思想 |
| [An optimal control approach to a posteriori error estimation in finite element methods](https://www.cambridge.org/core/journals/acta-numerica/article/abs/an-optimal-control-approach-to-a-posteriori-error-estimation-in-finite-element-methods/5C67A03F528C6FA69F37A97DF5C3BE19) | 2001 | 仅摘要 | 出版社摘要：adjoint weights、目标误差与自适应反馈；Volume 10 May 2001元数据 |
| [Asymptotic-Preserving Schemes for Multiscale Physical Problems](https://arxiv.org/pdf/2112.05920) | 2022 | 正文相关章节 | §1，PDF第3–5页：AP交换图、式(1.1)–(1.6)；微观到宏观极限说明 |
| [Inverse problems: A Bayesian perspective](https://web.stanford.edu/class/ee378a/REFS/stuart.pdf) | 2010 | 正文相关章节 | §4.2，PDF第51–52页：后验定义、Assumptions 2.6、Theorems 4.1–4.2；引言的函数空间正则化 |
| [A Survey of Projection-Based Model Reduction Methods for Parametric Dynamical Systems](https://kiwi.oden.utexas.edu/papers/Parametric-model-reduction-survey-Benner-Gugercin-Willcox.pdf) | 2015 | 正文相关章节 | §2.1–2.2，PDF第9–10页：参数系统、trial/test投影和假设；引言的offline/online分工 |
| [Multilevel Monte Carlo methods](https://people.maths.ox.ac.uk/~gilesm/files/acta15.pdf) | 2015 | 正文相关章节 | §2.1，PDF第6–7页：MSE分解、跨层差分、Theorem 1的alpha/beta/gamma条件 |
| [AMReX and pyAMReX: Looking beyond the exascale computing project](https://arxiv.org/pdf/2403.12179v2) | 2024 | 正文相关章节 | §1–2，PDF第2–3页：AMR粗细同步、数据结构和嵌入边界；§3.1–3.2：硬件可移植、kernel fusion |
| [Multilevel Interior Penalty Methods on GPUs](https://arxiv.org/html/2405.18982v2) | 2024 | 正文相关章节 | §2.1–2.2：SIPG、sum factorization与Cartesian假设；§3：vertex-patch multigrid；§5.2 mixed precision标题及摘要 |
| [Accelerating High-Order Finite Element Simulations at Extreme Scale with FP64 Tensor Cores](https://arxiv.org/html/2603.09038v1) | 2026 | 正文相关章节 | §I–II：数值应用、FP64动机与离线PDE求解成本；§III开头和摘要：小GEMM映射与扩展实验口径 |
| [PETSc SNES: Nonlinear Solvers — official manual](https://petsc.org/release/manual/snes/) | 未确定 | 官方文档或目录 | Nonlinear Solvers总述；Newton-based Methods / Line Search Newton；Matrix-Free Methods的文档入口 |
| [SUNDIALS ARKODE 7.7.0: Mathematical Considerations and Butcher Tables](https://sundials.readthedocs.io/en/v7.7.0/arkode/Mathematics_link.html) | 未确定 | 官方文档或目录 | §2.2.13–2.2.15：显式稳定步限制、固定步模式、非线性/线性代数求解；Butcher Tables中A/L稳定注记 |
| [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/html/2506.13131v1) | 2025 | 正文相关章节 | v1, 2025-06-16; §2.1–2.6, §6; §3仅浏览应用范围 |
| [Solving olympiad geometry without human demonstrations](https://research.google/pubs/solving-olympiad-geometry-without-human-demonstrations/) | 2024 | 仅摘要 | Google Research官方论文页面 Abstract; Nature正文打开失败 |
| [Learning to Optimize Multigrid PDE Solvers](https://proceedings.mlr.press/v97/greenfeld19a/greenfeld19a.pdf) | 2019 | 正文相关章节 | ICML 2019 PDF, §3–4, PDF pp.3–8; 特别§4 setup、零空间与表1–4 |
| [Data-driven discretization: machine learning for coarse graining of partial differential equations](https://arxiv.org/html/1808.04930v3) | 2018 | 正文相关章节 | v3正文 .2 Models for time integration, Pseudo-linear representation, Appendix III polynomial accuracy constraints |
| [Solver-in-the-Loop: Learning from Differentiable Physics to Interact with Iterative PDE-Solvers](https://arxiv.org/html/2007.00016v1) | 2020 | 正文相关章节 | v1, §2学习交互与NON/PRE/SOL; §3.1–3.2; §4 forced advection-diffusion; Appendix A |
| [Neural Preconditioning via Krylov Subspace Geometry](https://arxiv.org/html/2507.15452v1) | 2025 | 正文相关章节 | v1, §3, §5–6, §7.2–7.4, §8 |
| [PRDP: Progressively Refined Differentiable Physics](https://arxiv.org/html/2502.19611v1) | 2025 | 正文相关章节 | v1, §2.3, §3 controlling/applying refinement, §4.1–4.4, Appendix E thresholds |
| [Mosaic: A Benchmark Suite for Differentiable Physics Solvers](https://arxiv.org/html/2606.27895v1) | 2026 | 正文相关章节 | v1, 2026-06-26; §3.1–3.3, §4.3–4.4, Discussion and Limitations |
| [Artificial Intelligence: A Modern Approach — Full Table of Contents](https://aima.cs.berkeley.edu/contents.html) | 未确定 | 官方文档或目录 | 作者官网目录 Parts II–VI; Chapters 3–22; 只核对目录结构 |

主要未深读方向及下一轮补充顺序见 [学习与追踪路线](learning_roadmap.md)。
