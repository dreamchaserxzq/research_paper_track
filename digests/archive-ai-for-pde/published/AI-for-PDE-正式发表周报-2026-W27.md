# AI for PDE / AI for Science 正式发表论文追踪周报 · 2026-W27

## 本期概览

- 检索范围：2023-06-29 至 2026-06-29 UTC。
- 检索主题：计算物理、科学机器学习、AI for PDE、数值模拟代理模型、降阶模型、可微分求解器、神经算子、PINN、数据驱动科学仿真、激光等离子体、EUV、辐射流体、Vlasov/MHD。
- 候选论文数：47。
- 去重后候选数：32。
- 正式发表状态明确数：14。
- 核心入选：14。
- 扩展入选：0。
- 待人工确认：3。
- arXiv 状态更新：6。

本次为同一 ISO 周的幂等复核运行，覆盖更新早先的 W27 结果。二次检索重点补齐 Nature Machine Intelligence、SISC、JCP 与 CMAME 中此前遗漏的正式条目，并再次对照 W23–W26 分周元数据去重；PODNO、PCNO、MR-DINO 和 Neural Network Tearing and Interconnecting Methods 等已收录论文未重复写入。

## 本期重点关注

1. **Finite-volume-informed GNN**：直接把有限体积离散写入训练损失，且不依赖预计算标签，与 FLASH/ECOGEN 路线最接近。
2. **Super-fidelity**：神经算子只负责高质量 warm start，传统迭代求解器保持最终精度，是更稳健的工程混合范式。
3. **VINO / FEONet**：分别从变分能量和有限元离散出发实现无标签算子学习，代表“数值离散结构 + 神经算子”的两条重要路线。
4. **RINO / LNO**：分别处理跨分辨率非一致采样与非周期瞬态响应，对 AMR 数据和长程动态建模具有直接启发。

## 核心入选论文

### 1. Solving High-Dimensional PDEs with Latent Spectral Models

- 正式链接：https://proceedings.mlr.press/v202/wu23i.html
- DOI：无；以正式 proceedings 页面为准。
- 发表信息：ICML 2023 / Proceedings of Machine Learning Research，2023-07-23。
- 作者：Haixu Wu, Tengge Hu, Huakun Luo, Jianmin Wang, Mingsheng Long。
- 标签：latent spectral model, neural operator, PDE solver, spectral method, high-dimensional simulation。
- arXiv 状态：arXiv:2301.12664，已匹配正式版本。
- 核心贡献：Latent Spectral Models reduce high-dimensional PDE data into compact latent tokens and apply neural spectral blocks to learn multiple basis operators for PDE-governed tasks.
- 方法要点：层级投影、潜 token、神经谱块、多基算子。
- 实验对象：Elasticity、Plasticity、Navier–Stokes、Darcy、Airfoil、Pipe。
- 与用户课题关联：适合 FLASH/ECOGEN 高维场数据的潜空间降阶与代理建模。
- 评分：5 + 2 + 2 = 9，core。

### 2. Transolver: A Fast Transformer Solver for PDEs on General Geometries

- 正式链接：https://proceedings.mlr.press/v235/wu24r.html
- DOI：无；以正式 proceedings 页面为准。
- 发表信息：ICML 2024 / Proceedings of Machine Learning Research，2024-07-21。
- 作者：Haixu Wu, Huakun Luo, Haowen Wang, Jianmin Wang, Mingsheng Long。
- 标签：Transolver, physics attention, transformer solver, general geometry, PDE surrogate。
- arXiv 状态：arXiv:2402.02366，已匹配正式版本。
- 核心贡献：Transolver introduces Physics-Attention, slicing discretized meshes into learned physical-state tokens to obtain a fast transformer PDE solver on complex geometries.
- 方法要点：Physics-Attention、物理状态切片、线性复杂度注意力。
- 实验对象：Darcy、Elasticity、Airfoil、汽车表面压力与三维速度场。
- 与用户课题关联：适合不规则网格、多相界面、液滴形变和复杂几何代理模型。
- 评分：5 + 2 + 2 = 9，core。

### 3. SONets: Sub-operator learning enhanced neural networks for solving parametric partial differential equations

- 正式链接：https://doi.org/10.1016/j.jcp.2023.112536
- DOI：10.1016/j.jcp.2023.112536。
- 发表信息：Journal of Computational Physics，2023-12-15。
- 作者：Xiaowei Jin, Hongwei Li。
- 标签：sub-operator learning, parametric PDE, neural network, operator decomposition, JCP。
- arXiv 状态：未确认或无对应预印本。
- 核心贡献：SONets decompose parametric PDE solution operators into learnable sub-operators, improving modular operator learning for parametric PDEs.
- 方法要点：子算子分解、模块化学习、参数化 PDE 解算。
- 实验对象：多类参数化 PDE benchmark。
- 与用户课题关联：与模块化神经算子、算子分裂和多物理子系统组合路线直接相关。
- 评分：5 + 1 + 2 = 8，core。

### 4. f-PICNN: a physics-informed convolutional neural network for partial differential equations with space-time domain

- 正式链接：https://doi.org/10.1016/j.jcp.2024.113284
- DOI：10.1016/j.jcp.2024.113284。
- 发表信息：Journal of Computational Physics，2024-10-15。
- 作者：Baolin Yuan, Hao Wang, Ana Heitor, Xiaoping Chen。
- 标签：physics-informed CNN, PINN, space-time PDE, scientific machine learning。
- arXiv 状态：未确认或无对应预印本。
- 核心贡献：f-PICNN combines convolutional architectures with physics-informed residual constraints over space-time domains for PDE solution learning.
- 方法要点：卷积时空表征、PDE 残差约束、无网格采样。
- 实验对象：时空域 PDE 解算问题。
- 与用户课题关联：可用于导热、辐射和流体场的局部时空结构学习及残差约束。
- 评分：5 + 1 + 2 = 8，core。

### 5. Novel DeepONet architecture to predict stresses in elastoplastic structures with variable complex geometries and loads

- 正式链接：https://doi.org/10.1016/j.cma.2023.116277
- DOI：10.1016/j.cma.2023.116277。
- 发表信息：Computer Methods in Applied Mechanics and Engineering，2023-10-01。
- 作者：Juncai He, Shuyi Zhou, Kuangyu G. Wang。
- 标签：DeepONet, elastoplasticity, complex geometry, computational mechanics, surrogate model。
- arXiv 状态：未确认或无对应预印本。
- 核心贡献：A DeepONet variant predicts stress fields in elastoplastic structures under variable complex geometries and loads.
- 方法要点：分支—主干算子学习、几何与载荷编码、应力场预测。
- 实验对象：变几何与变载荷弹塑性结构。
- 与用户课题关联：为变几何、变载荷和多参数全场预测提供结构化算子学习参考。
- 评分：4 + 2 + 2 = 8，core。

### 6. Multistage physics informed neural network for solving coupled multiphysics problems in material degradation and fluid dynamics

- 正式链接：https://doi.org/10.1007/s00366-025-02174-4
- DOI：10.1007/s00366-025-02174-4。
- 发表信息：Engineering with Computers，2025-06-29。
- 作者：Mahmoud Khadijeh, Veronica Cerqueglini, Cor Kasbergen, Sandra Erkens, Aikaterini Varveri。
- 标签：multistage PINN, multiphysics, material degradation, fluid dynamics, curriculum learning。
- arXiv 状态：未确认或无对应预印本。
- 核心贡献：A staged PINN training strategy progressively increases coupled physics complexity for material degradation and fluid dynamics problems.
- 方法要点：课程式训练、分阶段激活耦合物理、与 FEM 对比。
- 实验对象：沥青老化、lid-driven cavity flow。
- 与用户课题关联：对辐射—导热—流体—材料状态耦合训练具有直接参考价值。
- 评分：5 + 1 + 2 = 8，core。

### 7. Geometry-informed neural operator for large-scale 3D PDEs

- 正式链接：https://proceedings.neurips.cc/paper_files/paper/2023/hash/70518ea42831f02afc3a2828993935ad-Abstract-Conference.html
- DOI：无；以正式 proceedings 页面为准。
- 发表信息：NeurIPS 2023，2023-12-10。
- 作者：Zongyi Li, Daniel Zhengyu Huang, Burigede Liu, Anima Anandkumar。
- 标签：GINO, 3D PDE, geometry-informed neural operator, complex geometry, large-scale simulation。
- arXiv 状态：未确认或无对应预印本。
- 核心贡献：Geometry-informed neural operator combines local graph kernels and global operator learning for large-scale 3D PDEs on complex geometries.
- 方法要点：局部图核、全局算子、三维几何编码。
- 实验对象：大规模三维 PDE 与复杂几何。
- 与用户课题关联：适合三维激光等离子体与液滴几何变化代理模型的长期路线。
- 评分：5 + 1 + 2 = 8，core。

### 8. Laplace neural operator for solving differential equations

- 正式链接：https://doi.org/10.1038/s42256-024-00844-4
- DOI：10.1038/s42256-024-00844-4。
- 发表信息：Nature Machine Intelligence，2024-06-24。
- 作者：Qianying Cao, Somdatta Goswami, George Em Karniadakis。
- 标签：Laplace neural operator, transient response, non-periodic signal, operator learning, PDE。
- arXiv 状态：arXiv:2303.10528，已匹配正式版本。
- 核心贡献：LNO embeds pole-residue structure in the Laplace domain to model non-periodic signals, transient responses and large-scale ODE/PDE solution operators.
- 方法要点：Laplace 域极点—留数参数化、非周期信号、瞬态外推。
- 实验对象：Duffing、摆、Lorenz、梁、扩散、反应扩散与全球 Rossby 波。
- 与用户课题关联：对非周期瞬态响应、长时推进和含初始瞬态的多物理动力学建模有参考价值。
- 评分：5 + 1 + 3 = 9，core。

### 9. Finite Element Operator Network for Solving Elliptic-Type Parametric PDEs

- 正式链接：https://doi.org/10.1137/23M1623707
- DOI：10.1137/23M1623707。
- 发表信息：SIAM Journal on Scientific Computing，2025-04-08。
- 作者：Jae Yong Lee, Seungchan Ko, Youngjoon Hong。
- 标签：FEONet, finite element, physics-informed operator learning, parametric PDE, data-free。
- arXiv 状态：未确认或无对应预印本。
- 核心贡献：FEONet combines finite-element discretization and physics-informed operator learning to solve elliptic parametric PDEs without paired input-output training data.
- 方法要点：有限元离散、物理信息算子损失、无成对标签训练、收敛分析。
- 实验对象：椭圆型参数化 PDE、复杂边界与边界层。
- 与用户课题关联：展示传统离散结构与无标签算子学习的深度融合，可迁移到有限体积或有限元混合代理。
- 评分：5 + 2 + 2 = 9，core。

### 10. Learning to solve PDEs with finite volume-informed neural networks in a data-free approach

- 正式链接：https://doi.org/10.1016/j.jcp.2025.113919
- DOI：10.1016/j.jcp.2025.113919。
- 发表信息：Journal of Computational Physics，2025-06-01。
- 作者：Tianyu Li, Yiye Zou, Shufan Zou, Xinghua Chang, Laiping Zhang, Xiaogang Deng。
- 标签：finite volume, graph neural network, data-free, PDE loss, parametric PDE。
- arXiv 状态：未确认或无对应预印本。
- 核心贡献：The framework combines finite-volume discretization with graph neural networks to construct a PDE loss and learn parametric PDE solutions without precomputed paired data.
- 方法要点：有限体积通量、图神经网络、离散 PDE loss、无预计算数据。
- 实验对象：基于控制体离散的参数化 PDE benchmark。
- 与用户课题关联：与 FLASH/ECOGEN 的有限体积离散最贴近，适合作为数据稀缺时的物理约束训练基线。
- 评分：5 + 2 + 2 = 9，core。

### 11. Neural operator-based super-fidelity: A warm-start approach for accelerating steady-state simulations

- 正式链接：https://doi.org/10.1016/j.jcp.2025.113871
- DOI：10.1016/j.jcp.2025.113871。
- 发表信息：Journal of Computational Physics，2025-05-15。
- 作者：Xu-Hui Zhou, Jiequn Han, Muhammad I. Zafar, Eric M. Wolf, Christopher R. Schrock, Christopher J. Roy, Heng Xiao。
- 标签：super-fidelity, warm start, neural operator, CFD acceleration, equivariance。
- arXiv 状态：arXiv:2312.11842，已匹配正式版本。
- 核心贡献：Super-fidelity maps low-fidelity solutions to high-fidelity warm starts with an equivariant vector-cloud neural operator, accelerating steady-state CFD while retaining iterative-solver accuracy.
- 方法要点：低保真到高保真映射、等变 VCNN-e、迭代求解器 warm start。
- 实验对象：椭圆柱低 Re 流动、翼型与三维机翼高 Re 湍流。
- 与用户课题关联：提供“神经网络只做高质量初值、传统求解器保证最终精度”的工程稳健混合范式。
- 评分：5 + 2 + 2 = 9，core。

### 12. DGenNO: a novel physics-aware neural operator for solving forward and inverse PDE problems based on deep, generative probabilistic modeling

- 正式链接：https://doi.org/10.1016/j.jcp.2025.114137
- DOI：10.1016/j.jcp.2025.114137。
- 发表信息：Journal of Computational Physics，2025-10-01。
- 作者：Yaohua Zang, Phaedon-Stelios Koutsourelakis。
- 标签：DGenNO, generative neural operator, weak form, inverse problem, uncertainty。
- arXiv 状态：未确认或无对应预印本。
- 核心贡献：DGenNO uses weak-form physical residuals and deep generative latent-variable modeling for label-free forward and inverse parametric PDE learning with uncertainty representation.
- 方法要点：弱形式残差、生成式潜变量、MultiONet、前向与逆向联合建模。
- 实验对象：高维/不连续输入的参数化 PDE、稀疏或噪声观测逆问题。
- 与用户课题关联：对稀疏数据、逆问题和不确定性量化有价值，可用于受限诊断条件下的等离子体状态反演。
- 评分：5 + 2 + 2 = 9，core。

### 13. Variational Physics-informed Neural Operator (VINO) for solving partial differential equations

- 正式链接：https://doi.org/10.1016/j.cma.2025.117785
- DOI：10.1016/j.cma.2025.117785。
- 发表信息：Computer Methods in Applied Mechanics and Engineering，2025-03-15。
- 作者：Mohammad Sadegh Eshaghi, Cosmin Anitescu, Manish Thombre, Yizheng Wang, Xiaoying Zhuang, Timon Rabczuk。
- 标签：VINO, variational formulation, physics-informed neural operator, data-free, energy minimization。
- arXiv 状态：arXiv:2411.06587，已匹配正式版本。
- 核心贡献：VINO trains neural operators without labels by minimizing a discretized variational energy, reducing the cost of evaluating physics-informed losses at increasing mesh resolution.
- 方法要点：离散能量泛函、变分损失、无标签算子学习、网格加密稳定性。
- 实验对象：多类线性与非线性 PDE，重点考察高分辨率网格。
- 与用户课题关联：提供无标签、能量泛函驱动的算子训练范式，可借鉴到具有变分结构的导热或固体子问题。
- 评分：5 + 2 + 2 = 9，core。

### 14. A resolution independent neural operator

- 正式链接：https://doi.org/10.1016/j.cma.2025.118113
- DOI：10.1016/j.cma.2025.118113。
- 发表信息：Computer Methods in Applied Mechanics and Engineering，2025-09-01。
- 作者：Bahador Bahmani, Somdatta Goswami, Ioannis G. Kevrekidis, Michael D. Shields。
- 标签：RINO, resolution independence, DeepONet, implicit neural representation, point cloud。
- arXiv 状态：arXiv:2407.13010，已匹配正式版本。
- 核心贡献：RINO learns continuous input/output dictionaries with implicit neural representations so operator models can accept arbitrary sensor counts and locations during training and inference.
- 方法要点：连续字典学习、SIREN 隐式表示、任意采样点与分辨率。
- 实验对象：任意点云采样、不同传感器数量与跨分辨率算子学习。
- 与用户课题关联：可直接处理不同传感器位置、点数和离散分辨率，适合 AMR 数据、非一致网格和跨分辨率迁移。
- 评分：5 + 2 + 2 = 9，core。

## 扩展入选论文

本期无扩展入选。二次检索新增的高置信正式论文均达到核心阈值；其余候选要么已在 W23–W26 入库，要么正式元数据仍不完整。

## 方向 A/B/C/D 覆盖

- A：AI 求解 PDE / SciML：LSM、Transolver、SONets、f-PICNN、Multistage PINN、GINO、LNO、FEONet、finite-volume-informed GNN、DGenNO、VINO、RINO。
- B：代理模型 / ROM / 科学仿真加速：LSM、Transolver、DeepONet stress surrogate、GINO、super-fidelity、RINO。
- C：科学计算与物理系统应用：弹塑性、复杂几何 CFD、稳态湍流 warm start、多物理分阶段训练。
- D：激光等离子体 / EUV / RHD / Vlasov / MHD：已补查 HEDP、Physics of Plasmas、PPCF、Nuclear Fusion、Optics Express 等；本期未发现未入库且同时满足“AI 科学计算方法相关 + 正式元数据完整”的新增核心论文。

## 按 venue 组覆盖说明

- 顶刊/顶会组：ICML 2023、ICML 2024、NeurIPS 2023、Nature Machine Intelligence；新增正式核验 LNO。
- 计算物理与科学计算组：JCP、CMAME、SISC、Engineering with Computers；新增 FEONet、finite-volume-informed GNN、super-fidelity、DGenNO、VINO、RINO。
- AI for Science / 数据驱动科学组：补查 Nature Computational Science、Nature Communications、Digital Discovery、Patterns、npj Computational Materials；未发现需要新增且未重复的高置信条目。
- 等离子体/EUV/光学组：补查 Physics of Plasmas、HEDP、PPCF、Nuclear Fusion、Optics Express、Optica、APL、JAP、LPB；多数候选为纯实验、传统模拟或已在 W25/W26 收录。

## 已有 arXiv 论文正式发表状态更新

- arXiv:2301.12664 → ICML 2023 / PMLR 202：Solving High-Dimensional PDEs with Latent Spectral Models。
- arXiv:2402.02366 → ICML 2024 / PMLR 235：Transolver。
- arXiv:2303.10528 → Nature Machine Intelligence 6, 631–640 (2024)：Laplace neural operator。
- arXiv:2312.11842 → Journal of Computational Physics 529, 113871 (2025)：super-fidelity warm start。
- arXiv:2411.06587 → CMAME 437, 117785 (2025)：VINO。
- arXiv:2407.13010 → CMAME 444, 118113 (2025)：RINO。

## 待人工确认论文

1. Artificial intelligence for partial differential equations in computational mechanics: A review：方法价值高，但正式 venue、DOI 与 publication date 尚未完成一致性核验。
2. Learning Physical Operators using Neural Operators：当前只确认 arXiv 版本，未发现可高置信匹配的正式出版记录。
3. PINTO: Physics-informed transformer neural operator：已检索到 CPC 文章号信息，但本轮未完成 DOI、online date 与作者元数据的多源一致性核验，暂不入库。

## 本期未入选原因简述

- 已在 `metadata/published_papers.jsonl` 或 W23–W26 分周 JSONL 中出现的论文不重复写入。
- 只有 arXiv 页面、无明确 venue/publisher 元数据的论文不进入正式入选。
- 纯实验、纯控制应用或与科学计算代理/AI for PDE 关系较弱的论文未纳入。
- 出版日期晚于 2026-06-29 UTC 的 future issue 条目不提前入库。

## 仓库更新说明

- 本期周报：`digests/published/AI-for-PDE-正式发表周报-2026-W27.md`
- 本期结构化元数据：`metadata/published_papers_2026_W27.jsonl`
- arXiv→正式发表补丁：`metadata/paper_registry_updates_2026_W27.jsonl`
- 运行日志：`run_log_published.md`

为避免整文件替换时覆盖历史长 JSONL，本期沿用分周安全写入策略，不直接重写 `metadata/published_papers.jsonl`；README.md 仍因缺少 `PUBLISHED_DIGEST` 标记而未修改。