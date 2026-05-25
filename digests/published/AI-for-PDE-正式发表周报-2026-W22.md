# AI for PDE / AI for Science 正式发表论文追踪周报 · 2026-W22

## 本期概览

- 检索范围：2023-05-25 至 2026-05-25 UTC
- 候选论文数：36
- 去重后论文数：22
- 正式发表状态明确或具备正式会议/期刊记录线索：8
- 核心入选：5
- 扩展入选：3
- arXiv 匹配更新：5
- 待人工确认：5

本期按 venue 分层检索，重点覆盖 AI for PDE、Scientific Machine Learning、神经算子、PDE benchmark、天气/气候 surrogate 与 AI for Science 数据集。已跳过 `metadata/published_papers.jsonl` 中已有 DOI/标题记录，包括 NeuralGCM、GraphCast、Pangu-Weather、GenCast、PINO、FourCastNet、CHGNet、GNoME、RelaxNet 与 neural operators review。

## 本期重点关注

1. **Latent Neural Operator**：面向正/逆 PDE 问题的潜空间神经算子，强调降低显存与提升训练效率；可迁移到高维辐射流体、输运与等离子体参数扫描代理模型。
2. **BENO**：面向复杂边界椭圆 PDE 的边界嵌入神经算子；对 EUV 光学边界、等离子体边界层与辐射输运边界条件建模有方法价值。
3. **Data-Efficient Operator Learning**：用无监督预训练和 in-context learning 降低昂贵 PDE 数据需求；适合作为高成本多物理仿真代理训练策略。

## 核心入选论文

### 1. Latent Neural Operator for Solving Forward and Inverse PDE Problems

- 正式链接：OpenReview / conference record 待补全；辅助版本：https://arxiv.org/abs/2406.03923
- DOI：null
- 发表信息：ICLR 2025；conference paper；publication_date 暂记 2025-04-24
- 作者/机构：Tian Wang, Chuang Wang；机构待补全
- 标签：neural operator, latent operator, inverse problem, PDE surrogate
- arXiv 版本状态：已匹配 arXiv:2406.03923
- 核心贡献：将 PDE operator learning 从几何空间映射到潜空间，使用 Physics-Cross-Attention 编码/解码，在正问题和反问题中降低显存并提升效率。
- 方法要点：latent representation、cross-attention、任意点插值/外推、正反问题统一训练。
- 实验对象：多类 PDE benchmark 与 inverse problem benchmark。
- 与用户课题关联：可迁移到 LPP-EUV 中高维参数化辐射流体、输运、热传导与等离子体诊断反演。
- 评分：5 + 2 + 2 = **9/10**

### 2. BENO: Boundary-embedded Neural Operators for Elliptic PDEs

- 正式链接：OpenReview / ICLR 记录待补全；辅助版本：https://arxiv.org/abs/2401.09323
- DOI：null
- 发表信息：ICLR 2024；conference paper；publication_date 暂记 2024-05-07
- 作者/机构：Haixin Wang, Jiaxin Li, Anubhav Dwivedi, Kentaro Hara, Tailin Wu；机构待补全
- 标签：elliptic PDE, boundary condition, neural operator, GNN, Transformer
- arXiv 版本状态：已匹配 arXiv:2401.09323
- 核心贡献：把边界信息显式嵌入神经算子，用于复杂几何与非齐次边界条件下的椭圆 PDE 求解。
- 方法要点：边界嵌入、图结构编码、Transformer 表示、Green function 启发。
- 实验对象：复杂几何椭圆方程与边界值问题。
- 与用户课题关联：EUV 光学、等离子体鞘层、辐射输运和复杂靶面几何都高度依赖边界条件表达。
- 评分：5 + 2 + 2 = **9/10**

### 3. Data-Efficient Operator Learning via Unsupervised Pretraining and In-Context Learning

- 正式链接：NeurIPS proceedings 待补全；辅助版本：https://arxiv.org/abs/2402.15734
- DOI：null
- 发表信息：NeurIPS 2024；proceedings article；publication_date 暂记 2024-12-10
- 作者/机构：Wuyang Chen, Jialin Song, Pu Ren, Shashank Subramanian, Dmitriy Morozov, Michael W. Mahoney；LBNL / UC Berkeley 等
- 标签：operator learning, unsupervised pretraining, in-context learning, PDE data efficiency
- arXiv 版本状态：已匹配 arXiv:2402.15734
- 核心贡献：用无标签 PDE 输入做物理启发式预训练，并用相似性检索式 in-context learning 提升 OOD 泛化。
- 方法要点：无监督预训练、重构代理任务、in-context examples、低数据 operator learning。
- 实验对象：多类 PDE operator learning benchmark。
- 与用户课题关联：降低 LPP-EUV 中高保真仿真样本需求，适合昂贵多物理数据生成场景。
- 评分：5 + 1 + 2 = **8/10**

### 4. GNOT: A General Neural Operator Transformer for Operator Learning

- 正式链接：PMLR / ICML 记录待补全；辅助版本：https://arxiv.org/abs/2302.14376
- DOI：null
- 发表信息：ICML 2023 / PMLR；conference paper；publication_date 暂记 2023-07-23
- 作者/机构：Zhongkai Hao, Zhengyi Wang, Hang Su, Chengyang Ying, Yinpeng Dong, Songming Liu, Ze Cheng, Jian Song 等；Tsinghua University 等
- 标签：neural operator transformer, irregular mesh, operator learning, PDE
- arXiv 版本状态：已匹配 arXiv:2302.14376
- 核心贡献：提出通用神经算子 Transformer，面向不规则网格、多尺度与异构输入输出的 PDE operator learning。
- 方法要点：heterogeneous normalized attention、geometric gating、soft domain decomposition。
- 实验对象：多类 PDE benchmark，包括不规则网格和多尺度场。
- 与用户课题关联：适合复杂几何网格、辐射流体多变量场和等离子体代理模型。
- 评分：5 + 1 + 2 = **8/10**

### 5. MgNO: Efficient Parameterization of Linear Operators via Multigrid

- 正式链接：OpenReview / TMLR 记录待补全；辅助版本：https://arxiv.org/abs/2310.19809
- DOI：null
- 发表信息：TMLR / OpenReview 记录待复核；journal article；publication_date 暂记 2024-10-16
- 作者/机构：Juncai He, Xinliang Liu, Jinchao Xu；机构待补全
- 标签：multigrid, neural operator, PDE, operator parameterization
- arXiv 版本状态：已匹配 arXiv:2310.19809
- 核心贡献：将多重网格结构嵌入神经算子线性算子参数化，提高训练效率并降低过拟合。
- 方法要点：multigrid hierarchy、linear operator parameterization、operator layer regularity。
- 实验对象：参数化 PDE operator learning benchmark。
- 与用户课题关联：多重网格思想可迁移到高分辨率辐射流体/输运方程的多尺度代理结构。
- 评分：5 + 1 + 1 = **7/10**

## 扩展入选论文

### 6. ClimaX: A foundation model for weather and climate

- 正式链接：PMLR / ICML 记录待补全；辅助版本：https://arxiv.org/abs/2301.10343
- DOI：null
- 发表信息：ICML 2023 / PMLR；conference paper；publication_date 暂记 2023-07-23
- 作者/机构：Tung Nguyen, Johannes Brandstetter, Ashish Kapoor, Jayesh K. Gupta, Aditya Grover；Microsoft Research / UCLA 等
- 类型：framework
- 标签：foundation model, weather, climate, surrogate, Transformer
- arXiv 版本状态：已匹配 arXiv:2301.10343
- 核心贡献：面向天气与气候多变量连续场的基础模型，支持异构数据预训练与多任务微调。
- 与用户课题关联：对多变量物理场 foundation model 和 surrogate 训练有可迁移价值。
- 评分：4 + 1 + 2 = **7/10**

### 7. The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning

- 正式链接：NeurIPS Datasets and Benchmarks 记录待补全
- DOI：null
- 发表信息：NeurIPS 2024 Datasets and Benchmarks；proceedings article；publication_date 暂记 2024-12-10
- 作者/机构：Polymathic AI collaboration；机构待补全
- 类型：dataset / benchmark
- 标签：physics simulations, benchmark, scientific machine learning, surrogate training
- 核心贡献：提供多样化物理仿真数据集，用于科学机器学习模型训练、预训练和泛化评估。
- 与用户课题关联：可作为预训练/评估科学仿真代理模型的数据规范参考。
- 评分：4 + 1 + 2 = **7/10**

### 8. PDEArena: A benchmark suite for neural PDE solvers

- 正式链接：NeurIPS Datasets and Benchmarks 记录待补全
- DOI：null
- 发表信息：NeurIPS 2023 Datasets and Benchmarks；proceedings article；publication_date 暂记 2023-12-10
- 作者/机构：PDEArena authors；机构待补全
- 类型：benchmark
- 标签：neural PDE solver, benchmark, PDE, evaluation
- 核心贡献：为神经 PDE 求解器提供标准化评估任务和横向比较基准。
- 与用户课题关联：适合作为 LPP-EUV 代理模型评估协议设计参考。
- 评分：4 + 1 + 1 = **6/10**

## 方向 A/B/C/D 分节

### A. AI 求解 PDE / Scientific Machine Learning

入选：Latent Neural Operator、BENO、Data-Efficient Operator Learning、GNOT、MgNO、PDEArena。重点集中在神经算子结构、复杂边界、低数据训练和标准 benchmark。

### B. 数据生成、代理模型、降阶模型与科学仿真加速

入选：Data-Efficient Operator Learning、ClimaX、The Well。重点为低样本 operator learning、天气/气候 foundation model 和大规模物理仿真数据集。

### C. 科学计算与物理系统应用

入选：ClimaX、The Well。直接物理系统包括天气/气候连续场和多类物理仿真数据；本期未新增材料/分子动力学正式论文，因为已有 CHGNet、GNoME 记录已在上期收录。

### D. 激光等离子体 / EUV / 辐射流体 / Vlasov / MHD

已检索但无新增核心入选。主要原因：本轮发现的等离子体/EUV 强相关候选多为 arXiv-only、纯实验论文、或出版元数据不足；正式发表证据不足者列入待人工确认。

## 按 venue 组覆盖说明

- 顶刊/顶会组：已检索 Nature、Science、NMI、Nature Computational Science、Nature Communications、Science Advances、PNAS、NeurIPS、ICML、ICLR、JMLR、TMLR。新增入选主要来自 ICLR/ICML/NeurIPS/TMLR 记录；Nature/Science 系列新增项多与已有记录重复或不在本期新增范围。
- 计算物理与科学计算组：已检索 JCP、CMAME、CPC、SISC、CiCP、MLST、Engineering with Computers、Applied Mathematical Modelling、IJNME。本期未新增正式入选，主要原因是可确认出版元数据不足、与 AI/科学计算关系弱或已被既有记录覆盖。
- AI for Science / 数据驱动科学组：已检索 Digital Discovery、npj Computational Materials、Patterns、Communications Engineering、Nature Reviews Physics / Methods Primers、AIP Advances、APL Machine Learning 等。新增入选偏 benchmark/foundation-model；已有材料方向正式论文已在上期收录。
- 等离子体/EUV/光学组：已检索 Physics of Plasmas、HEDP、PSST、PPCF、Nuclear Fusion、PRE、PRR、Optics Express、Optica、APL、JAP、Laser and Particle Beams。未新增正式入选；主要原因是 AI + 等离子体/EUV 交叉候选正式出版证据不足或相关度不达 6 分。

## 已有 arXiv 论文正式发表状态更新

- arXiv:2406.03923 → Latent Neural Operator：匹配到正式会议记录线索，精确 OpenReview ID 待补全。
- arXiv:2401.09323 → BENO：匹配到正式会议记录线索，精确 OpenReview ID 待补全。
- arXiv:2402.15734 → Data-Efficient Operator Learning：匹配到 NeurIPS 2024 记录线索，精确 proceedings URL 待补全。
- arXiv:2302.14376 → GNOT：匹配到 ICML/PMLR 记录线索，精确 PMLR URL 待补全。
- arXiv:2310.19809 → MgNO：匹配到 TMLR/OpenReview 记录线索，精确页面待补全。

## 待人工确认论文

1. Diffeomorphism Neural Operator for various domains and parameters of partial differential equations：方法高度相关，但本轮未确认正式 venue/DOI。
2. Physics-informed Discretization-independent Deep Compositional Operator Network：方法相关，但正式出版状态未确认。
3. Operator Learning: Algorithms and Analysis：综述价值高，但正式出版状态和日期需复核。
4. NeurIPS 2024 ML4CFD Competition retrospective：CFD surrogate benchmark 价值高，但本轮检索到的版本疑似 arXiv/后续稿，正式记录待查。
5. Plasma / EUV machine-learning simulation 候选若干：多数为 arXiv-only 或纯实验/诊断模型，未进入正式入选。

## 本期未入选原因简述

- 仅有 arXiv 页面，未发现 DOI、journal-ref、publisher 页面或正式会议记录。
- Crossref/OpenAlex/Semantic Scholar 元数据与标题或日期不一致。
- 出版日期不在三年窗口内或仅能确认 deposited/indexed 日期。
- 论文为纯实验、纯诊断或一般机器学习应用，与科学计算代理/PDE 方法关系弱。
- 与上期 `published_papers.jsonl` 已有论文重复，按 DOI/标题去重跳过。
