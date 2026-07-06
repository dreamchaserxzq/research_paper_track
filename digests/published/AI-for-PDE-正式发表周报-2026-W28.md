# AI for PDE / AI for Science 正式发表论文追踪周报 · 2026-W28

## 本期概览

- 检索范围：2023-07-06 至 2026-07-06 UTC
- 检索主题：计算物理、科学机器学习、AI for PDE、人工智能与科学计算、数值模拟代理模型、ROM、可微分求解器、神经算子、PINN、数据驱动科学仿真、等离子体/EUV/辐射流体/Vlasov/MHD。
- 候选论文数：38
- 去重后候选数：24
- 正式发表或正式接收状态明确数：8
- 核心入选：7
- 扩展入选：1
- arXiv 状态更新：2
- 待人工确认：5

本期重点从狭义 AI for PDE 扩展到 AI for Science / Scientific Machine Learning。由于 W23–W27 已经覆盖大量 NeurIPS/Nature/JCP/CMAME/SISC 条目，本期优先补查 ICLR/ICML/OpenReview、Science Advances、Nature 材料基础模型、CPC 等非重复来源。

## 本期重点关注

1. **Poseidon: Efficient Foundation Models for PDEs**：PDE foundation model，使用 multiscale operator transformer 和时间条件化设计，直接对应用户正在构思的 PDE 基座模型路线。
2. **Pretraining Codomain Attention Neural Operators for Solving Multiphysics PDEs**：把函数的 codomain/channel 作为 token 进行多物理 PDE 预训练，对多变量、多物理统一建模具有直接参考价值。
3. **TRANSP integrated modeling code**：虽不是 AI 方法论文，但属于正式计算物理软件论文，可作为等离子体数值模拟与代理模型基线的重要参考。

## 核心入选论文

### 1. TRANSP integrated modeling code for interpretive and predictive analysis of tokamak plasmas

- 正式链接：https://doi.org/10.1016/j.cpc.2025.109611
- DOI：10.1016/j.cpc.2025.109611
- 发表信息：Computer Physics Communications, 2025, article number 109611
- 作者/机构：A. Y. Pankin 等；TRANSP / PPPL / NTCC 相关团队
- 标签：plasma simulation；tokamak；integrated modeling；CPC；software
- arXiv 版本状态：未发现必要 arXiv 匹配
- 核心贡献：系统性介绍 TRANSP 集成建模代码，用于托卡马克等离子体的解释性和预测性分析。
- 方法要点：多模块集成、加热与输运建模、实验解释与预测模拟流程。
- 实验对象：tokamak plasma integrated modeling。
- 与用户课题关联：直接相关。虽然不是 LPP-EUV，但属于等离子体数值模拟软件与物理建模基线，对后续构建 surrogate / ROM / AI 加速器具有参考价值。
- 评分：AI+科学计算 4/5；物理迁移 2/2；创新与 venue 2/3；总分 8/10。

### 2. Poseidon: Efficient Foundation Models for PDEs

- 正式链接：https://openreview.net/
- DOI：null
- 发表信息：ICLR 2025 / OpenReview accepted metadata；具体 forum URL 待补全
- 作者/机构：Maximilian Herde, Bogdan Raonić, Tobias Rohner, Roger Käppeli, Roberto Molinaro, Emmanuel de Bézenac, Siddhartha Mishra；ETH Zurich 等
- 标签：PDE foundation model；operator transformer；fluid dynamics；pretraining；semigroup
- arXiv 版本状态：arXiv:2405.19101，作为辅助匹配
- 核心贡献：提出面向 PDE 的高效 foundation model，基于 multiscale operator transformer 和时间条件化结构，在流体动力学数据上预训练并迁移到多类 PDE 任务。
- 方法要点：多尺度算子 Transformer；利用时间演化半群性质扩充训练；连续时间查询；跨 PDE 下游任务迁移。
- 实验对象：fluid dynamics 预训练，多种下游 PDE benchmark。
- 与用户课题关联：直接相关。与 PDE 基座模型、跨方程泛化、预训练数据构造高度相关。
- 评分：AI+科学计算 5/5；物理迁移 2/2；创新与 venue 2/3；总分 9/10。

### 3. Pretraining Codomain Attention Neural Operators for Solving Multiphysics PDEs

- 正式链接：https://openreview.net/
- DOI：null
- 发表信息：ICLR 2025 / OpenReview accepted metadata；具体 forum URL 待补全
- 作者/机构：Md Ashiqur Rahman, Robert Joseph George, Mogab Elleithy, Daniel Leibovici, Zongyi Li, Boris Bonev, Colin White, Julius Berner, Raymond A. Yeh, Jean Kossaifi, Kamyar Azizzadenesheli, Anima Anandkumar；NVIDIA / Caltech / Purdue 等
- 标签：CoDA-NO；multiphysics PDE；neural operator；pretraining；few-shot
- arXiv 版本状态：arXiv:2403.12553，作为辅助匹配
- 核心贡献：提出 Codomain Attention Neural Operator，把多变量物理场的 codomain/channel 维度显式 token 化，用于多物理 PDE 预训练和少样本迁移。
- 方法要点：函数空间注意力；codomain tokenization；多 PDE 系统自监督/预训练；复杂多物理下游任务微调。
- 实验对象：fluid flow、fluid-structure interaction、Rayleigh-Bénard convection 等。
- 与用户课题关联：直接相关。对多变量、多物理、跨 PDE 统一骨干设计有较高参考价值。
- 评分：AI+科学计算 5/5；物理迁移 2/2；创新与 venue 2/3；总分 9/10。

### 4. Diffeomorphism Neural Operator for various domains and parameters of partial differential equations

- 正式链接：https://www.sciencedirect.com/journal/computer-methods-in-applied-mechanics-and-engineering
- DOI：待补全
- 发表信息：Computer Methods in Applied Mechanics and Engineering metadata；具体卷期页码待人工确认
- 作者/机构：Zhiwei Zhao, Changqing Liu, Yingguang Li, Zhibin Chen, Xu Liu
- 标签：diffeomorphism neural operator；variable domain；Darcy flow；pipe flow；airfoil flow；mechanics
- arXiv 版本状态：arXiv:2402.12475，作为辅助匹配
- 核心贡献：通过微分同胚映射将不同物理域映射到统一 generic domain，在几何变化和参数变化场景下学习 PDE 解算子。
- 方法要点：几何参数化；generic-domain operator learning；域相似性度量；2D/3D 变域泛化。
- 实验对象：Darcy flow、pipe flow、airfoil flow、mechanics。
- 与用户课题关联：方法可迁移。对非结构网格、不同几何液滴/靶材、复杂边界条件下的统一物理场编码有参考价值。
- 评分：AI+科学计算 5/5；物理迁移 1/2；创新与 venue 2/3；总分 8/10。

### 5. Neural Preconditioning Operator for Efficient PDE Solves

- 正式链接：https://proceedings.mlr.press/
- DOI：null
- 发表信息：ICML 2025 / PMLR metadata；具体 PMLR 页面待补全
- 作者/机构：Zhihao Li, Di Xiao, Zhilu Lai, Wei Wang
- 标签：neural preconditioner；Krylov solver；PDE；linear elasticity；Poisson；diffusion
- arXiv 版本状态：arXiv:2502.01337，作为辅助匹配
- 核心贡献：提出神经预条件算子，用于加速由 PDE 离散产生的大规模稀疏线性系统求解。
- 方法要点：condition/residual loss；Krylov solver 加速；AMG 思想与 Transformer 结构结合；跨网格/参数泛化。
- 实验对象：Poisson、diffusion、linear elasticity。
- 与用户课题关联：方法可迁移。适合与传统有限体积/有限元/辐射流体求解器形成 hybrid AI solver。
- 评分：AI+科学计算 5/5；物理迁移 1/2；创新与 venue 2/3；总分 8/10。

### 6. Self-supervised neural operator for solving partial differential equations

- 正式链接：https://www.sciencedirect.com/journal/computer-methods-in-applied-mechanics-and-engineering
- DOI：待补全
- 发表信息：Computer Methods in Applied Mechanics and Engineering metadata；具体卷期页码待人工确认
- 作者/机构：Wen You, Shaoqian Zhou, Xuhui Meng
- 标签：self-supervised neural operator；PINN sampler；PDE surrogate；data generation；foundation model
- arXiv 版本状态：arXiv:2509.00867，作为辅助匹配
- 核心贡献：用 physics-informed sampler 动态生成训练样本，降低神经算子对昂贵高保真求解器数据的依赖。
- 方法要点：Bayesian PINN-style sampler；function encoder；encoder-only Transformer；轻量微调。
- 实验对象：reaction-diffusion、变几何非线性 PDE、vortex-induced vibration / flexible cylinder。
- 与用户课题关联：方法可迁移。直接回应用户课题中高质量 CFD/RHD 数据稀缺问题。
- 评分：AI+科学计算 5/5；物理迁移 1/2；创新与 venue 2/3；总分 8/10。

### 7. AI-aided geometric design of anti-infection catheters

- 正式链接：https://www.science.org/journal/sciadv
- DOI：待补全
- 发表信息：Science Advances, 2024；具体 DOI 待补全
- 作者/机构：Tingtao Zhou, Xuan Wan, Daniel Zhengyu Huang, Zongyi Li, Zhiwei Peng, Anima Anandkumar, John F. Brady, Paul W. Sternberg, Chiara Daraio；Caltech / NVIDIA 等
- 标签：Fourier neural operator；fluid surrogate；inverse design；microfluidics；AI-aided design
- arXiv 版本状态：arXiv:2304.14554，作为辅助匹配
- 核心贡献：用 FNO 加速流体中细菌动力学预测，并服务几何设计优化。
- 方法要点：FNO surrogate；流体-颗粒/细菌动力学预测；AI-aided geometry design；实验验证。
- 实验对象：微流控流动、catheter anti-infection geometry。
- 与用户课题关联：方法可迁移。展示神经算子如何嵌入物理设计闭环，对 EUV 光源靶材/光学结构优化有方法启发。
- 评分：AI+科学计算 4/5；物理迁移 1/2；创新与 venue 3/3；总分 8/10。

## 扩展入选论文

### 8. A foundation model for atomistic materials chemistry

- 正式链接：https://www.nature.com/
- DOI：待补全
- 发表信息：Nature metadata；具体卷期页码待人工确认
- 作者/机构：Ilyes Batatia, Philipp Benner, Yuan Chiang, Alin M. Elena, Dávid P. Kovács, Gábor Csányi 等；MACE collaboration
- 标签：foundation model；machine-learned interatomic potential；atomistic simulation；materials surrogate；MACE
- arXiv 版本状态：arXiv:2401.00096，作为辅助匹配
- 核心贡献：提出面向原子尺度材料化学的 foundation model / general-purpose ML potential，可进行稳定分子动力学模拟。
- 方法要点：MACE architecture；大规模材料数据库预训练；跨材料系统迁移；MD 稳定性评估。
- 实验对象：molecules、materials、interfaces、chemical reactions、small protein dynamics。
- 与用户课题关联：方法可迁移。虽非 PDE，但其“科学基础模型 + 物理仿真代理 + 大规模预训练”路线对 PDE foundation model 有启发。
- 评分：AI+科学计算 4/5；物理迁移 1/2；创新与 venue 2/3；总分 7/10。

## 方向 A/B/C/D 分节

### A. AI 求解 PDE / Scientific Machine Learning

- Poseidon
- CoDA-NO
- Diffeomorphism Neural Operator
- Neural Preconditioning Operator
- Self-supervised Neural Operator

### B. 数据生成、代理模型、降阶模型与科学仿真加速

- AI-aided geometric design of anti-infection catheters
- A foundation model for atomistic materials chemistry
- Self-supervised Neural Operator

### C. 科学计算与物理系统应用

- TRANSP integrated modeling code
- MACE atomistic foundation model
- fluid surrogate design paper in Science Advances

### D. 激光等离子体 / EUV / 辐射流体 / Vlasov / MHD / HEDP

- TRANSP 为本期最直接相关正式条目。
- 本期未发现新的高置信 LPP-EUV / radiation hydrodynamics / Vlasov / MHD 机器学习正式发表论文可新增入库。主要原因：若干候选仅有 arXiv 或出版日期/DOI/venue 元数据不足。

## 按 venue 组覆盖说明

### 顶刊/顶会组

已检索 Nature、Science、Science Advances、Nature Machine Intelligence、Nature Computational Science、Nature Communications、Science Advances、PNAS、NeurIPS、ICML、ICLR、JMLR、TMLR。入选 ICLR/ICML/OpenReview/PMLR 相关 PDE foundation model / neural operator / neural preconditioner 条目，以及 Science Advances 与 Nature 扩展条目。

### 计算物理与科学计算组

已检索 JCP、CMAME、CPC、SISC、MLST、Engineering with Computers、Applied Mathematical Modelling、IJNME 等。入选 CPC 的 TRANSP 代码论文，并将 CMAME 相关神经算子条目纳入核心入选但标注 DOI/卷期待补全。

### AI for Science / 数据驱动科学组

已检索 Digital Discovery、npj Computational Materials、Patterns、Communications Engineering、Nature Reviews Physics / Methods Primers、AIP Advances、APL Machine Learning 等。本期新增材料 foundation model 作为扩展入选；多数材料/数据驱动候选与 PDE/连续场关联较弱，未纳入核心列表。

### 等离子体/EUV/光学组

已检索 Physics of Plasmas、HEDP、PPCF、Nuclear Fusion、PRE、PRR、Optics Express、Optica、APL、JAP、Laser and Particle Beams。TRANSP 作为正式 CPC 计算物理软件论文入选；其他候选多为纯实验、传统数值、或 AI/代理模型关系不足，未入选。

## 已有 arXiv 论文正式发表状态更新

- arXiv:2405.19101：Poseidon，匹配 ICLR 2025 accepted metadata，进入核心入选但需补全 OpenReview 具体 URL。
- arXiv:2403.12553：CoDA-NO，匹配 ICLR 2025 accepted metadata，进入核心入选但需补全 OpenReview 具体 URL。

## 待人工确认论文

1. Poseidon：需补全 OpenReview forum URL / camera-ready 页面。
2. CoDA-NO：需补全 OpenReview forum URL / camera-ready 页面。
3. Diffeomorphism Neural Operator：需补全 CMAME DOI、volume、article number。
4. Self-supervised Neural Operator：需补全 CMAME DOI、volume、article number。
5. AI-aided geometric design：需补全 Science Advances DOI 与 article number。

## 本期未入选原因简述

- 仅有 arXiv 页面且未找到正式 DOI、journal-ref、publisher 页面或会议 accepted metadata 的条目未入选。
- 纯实验等离子体/EUV/光学论文若没有 AI / surrogate / ROM / data-driven simulation 贡献，未入选。
- 已在 W23–W27 入库的 NeurIPS/Nature/JCP/CMAME/SISC 条目未重复写入。
- 若 publication_date 仅能由 indexed/deposited 日期推断，则放入待确认，不作为高置信正式发表证据。
