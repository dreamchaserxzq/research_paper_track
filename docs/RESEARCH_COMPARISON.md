# 重点论文证据对照

> 仅展示仓库已有证据，不把摘要描述补写成已验证的实验事实。详见来源记录。

| 论文 | 模型层级 | 训练 PDE | 评测 PDE | 泛化轴 | 代码 | 核验 |
|---|---|---|---|---|---|---|
| [OmniArch: Building Foundation Model for Scientific Computing](https://arxiv.org/abs/2402.16014) | true_foundation_model | unknown | unknown | unknown | unknown | legacy_unverified |
| [DPOT: Auto-Regressive Denoising Operator Transformer for Large-Scale PDE Pre-Training](https://arxiv.org/abs/2403.03542) | true_foundation_model | unknown | unknown | unknown | unknown | legacy_unverified |
| [Towards a Foundation Model for Partial Differential Equations: Multi-Operator Learning and Extrapolation](https://arxiv.org/abs/2404.12355) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [Poseidon: Efficient Foundation Models for PDEs](https://arxiv.org/abs/2405.19101) | true_foundation_model | unknown | unknown | unknown | unknown | conflict_pending |
| [VICON: Vision In-Context Operator Networks for Multi-Physics Fluid Dynamics Prediction](https://arxiv.org/abs/2411.16063) | foundation_model_candidate | unknown | unknown | unknown | unknown | legacy_unverified |
| [BCAT: A Block Causal Transformer for PDE Foundation Models for Fluid Dynamics](https://arxiv.org/abs/2501.18972) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [SPDEBench: An Extensive Benchmark for Learning Regular and Singular Stochastic PDEs](https://arxiv.org/abs/2505.18511) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [Overtone: Cyclic Patch Modulation for Clean, Efficient, and Flexible Physics Emulators](https://arxiv.org/abs/2507.09264) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [PDEformer-2: A Versatile Foundation Model for Two-Dimensional Partial Differential Equations](https://arxiv.org/abs/2507.15409) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [HyPINO: Multi-Physics Neural Operators via HyperPINNs and the Method of Manufactured Solutions](https://arxiv.org/abs/2509.05117) | foundation_model_candidate | linear elliptic PDEs, hyperbolic PDEs, parabolic PDEs | seven PINN benchmark problems | PDE family, source term, geometry, Dirichlet/Neumann boundary conditions, zero-shot transfer, PINN initialization | [链接](https://github.com/rbischof/hypino) | legacy_unverified |
| [Towards a Physics Foundation Model（General Physics Transformer, GPhyT）](https://arxiv.org/abs/2509.13805) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [MORPH: PDE Foundation Models with Arbitrary Data Modality](https://arxiv.org/abs/2509.21670) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [Axial Neural Networks for Dimension-Free Foundation Models（XNN）](https://arxiv.org/abs/2510.13665) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [Walrus: A Cross-Domain Foundation Model for Continuum Dynamics](https://arxiv.org/abs/2511.15684) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [Towards a Foundation Model for Partial Differential Equations Across Physics Domains](https://arxiv.org/abs/2511.21861) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [REALM: Benchmarking Neural Surrogates on Realistic Spatiotemporal Multiphysics Flows](https://arxiv.org/abs/2512.18595) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [RealPDEBench: A Benchmark for Complex Physical Systems with Real-World Data](https://arxiv.org/abs/2601.01829) | enabling_method | unknown | five paired real/simulation physical-system datasets | sim-to-real, real-vs-synthetic gap, multiple physical systems, robustness, foundation-model evaluation | [链接](https://github.com/AI4Science-WestlakeU/RealPDEBench) | legacy_unverified |
| [HyCOP: Hybrid Composition Operators for Interpretable Learning of PDEs](https://arxiv.org/abs/2605.00820) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [Practical Scaling Laws: Converting Compute into Performance in a Data-Constrained World](https://arxiv.org/abs/2605.09189) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |
| [Do Physics Foundation Models Learn Generalizable Physics? A Bias-Aware Benchmark Across Physical Regimes and Distribution Shifts](https://arxiv.org/abs/2605.29283) | unknown | unknown | unknown | unknown | unknown | legacy_unverified |

后续核验字段：表征、条件输入、预训练预算、划分与基线、局限、数据/权重许可证。用带证据的 assessment 事件填写；不要从模型名称推断。
