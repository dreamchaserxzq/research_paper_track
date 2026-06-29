# AI for PDE / AI for Science 正式发表论文追踪周报 · 2026-W27

## 本期概览

- 检索范围：2023-06-29 至 2026-06-29 UTC。
- 检索主题：计算物理、科学机器学习、AI for PDE、数值模拟代理模型、降阶模型、可微分求解器、神经算子、PINN、数据驱动科学仿真、激光等离子体、EUV、辐射流体、Vlasov/MHD。
- 候选论文数：27。
- 去重后候选数：19。
- 正式发表状态明确数：7。
- 核心入选：7。
- 扩展入选：0。
- 待人工确认：4。
- arXiv 状态更新：3。

本期不再优先追加 NeurIPS 2024 已覆盖条目，而是补齐此前正式库中缺失的 ICML/PMLR、JCP、CMAME、Engineering with Computers 和 NeurIPS 2023 代表性论文。重点是“可迁移方法”：潜空间/谱算子、复杂几何 Transformer 求解器、子算子分解、物理信息 CNN、DeepONet 结构力学代理、多阶段 PINN 与 3D 几何神经算子。

## 本期重点关注

1. **Transolver**：将复杂网格点划分为可学习物理状态切片，再对物理 token 做注意力，适合复杂几何 CFD、空气动力学和工业设计代理模型。
2. **Latent Spectral Models**：把高维 PDE 数据压缩到潜空间并用神经谱块学习多基算子，适合多物理场高维状态降阶。
3. **SONets**：子算子学习思路与用户当前关注的模块化/分裂算子路线高度接近。
4. **Multistage PINN**：通过分阶段引入耦合物理降低 PINN 多目标优化难度，可迁移到辐射、导热、流体、材料状态方程耦合训练。

## 核心入选论文

### 1. Solving High-Dimensional PDEs with Latent Spectral Models

- 正式链接：https://proceedings.mlr.press/v202/wu23i.html
- DOI：无；正式 venue 为 ICML 2023 / PMLR 202。
- 发表信息：Proceedings of the 40th ICML, PMLR 202, 37417–37438, 2023。
- 作者/机构：Haixu Wu, Tengge Hu, Huakun Luo, Jianmin Wang, Mingsheng Long；Tsinghua University。
- 标签：latent spectral model, neural operator, PDE solver, high-dimensional simulation。
- arXiv 状态：arXiv:2301.12664，已匹配正式 ICML/PMLR 版本。
- 核心贡献：通过层级投影把高维 PDE 数据降到紧凑潜空间，并用神经谱块学习多基算子。
- 方法要点：潜 token 表示、谱方法启发的神经块、固体和流体 PDE benchmark。
- 实验对象：Elasticity、Plasticity、Navier–Stokes、Darcy、Airfoil、Pipe 等。
- 与用户课题关联：适合 FLASH/ECOGEN 高维场数据的潜空间 ROM 与代理建模。
- 评分：5 + 2 + 2 = 9，core。

### 2. Transolver: A Fast Transformer Solver for PDEs on General Geometries

- 正式链接：https://proceedings.mlr.press/v235/wu24r.html
- DOI：无；正式 venue 为 ICML 2024 / PMLR 235。
- 发表信息：Proceedings of the 41st ICML, PMLR 235, 53681–53705, 2024。
- 作者/机构：Haixu Wu, Huakun Luo, Haowen Wang, Jianmin Wang, Mingsheng Long；Tsinghua University。
- 标签：Physics-Attention, transformer solver, general geometry, PDE surrogate。
- arXiv 状态：arXiv:2402.02366，已匹配正式 ICML/PMLR 版本。
- 核心贡献：提出 Physics-Attention，将离散网格划分为可学习物理状态切片，在线性复杂度下捕获复杂几何中的物理相关性。
- 方法要点：slice/token 化物理状态、复杂几何泛化、线性复杂度注意力。
- 实验对象：Darcy、Elasticity、Airfoil、汽车表面压力和三维速度场等。
- 与用户课题关联：对不规则网格、多相界面、液滴形变和复杂几何代理模型有高迁移价值。
- 评分：5 + 2 + 2 = 9，core。

### 3. SONets: Sub-operator learning enhanced neural networks for solving parametric partial differential equations

- 正式链接：https://doi.org/10.1016/j.jcp.2023.112536
- DOI：10.1016/j.jcp.2023.112536。
- 发表信息：Journal of Computational Physics 495, article 112536, 2023。
- 作者：Xiaowei Jin, Hongwei Li。
- 标签：sub-operator learning, parametric PDE, operator decomposition。
- arXiv 状态：未确认。
- 核心贡献：把参数化 PDE 解算子拆分为可学习子算子，增强神经网络对参数化 PDE 的表达能力。
- 方法要点：子算子分解、模块化学习、参数化 PDE 解算。
- 实验对象：参数化 PDE benchmark。
- 与用户课题关联：与模块化神经算子、算子分裂和多物理耦合代理路线直接相关。
- 评分：5 + 1 + 2 = 8，core。

### 4. f-PICNN: a physics-informed convolutional neural network for partial differential equations with space-time domain

- 正式链接：https://doi.org/10.1016/j.jcp.2024.113284
- DOI：10.1016/j.jcp.2024.113284。
- 发表信息：Journal of Computational Physics 515, article 113284, 2024。
- 作者：Baolin Yuan, Hao Wang, Ana Heitor, Xiaoping Chen。
- 标签：physics-informed CNN, PINN, space-time PDE。
- arXiv 状态：未确认。
- 核心贡献：将卷积网络与物理残差约束结合，面向时空域 PDE 解算。
- 方法要点：CNN 表征局部时空结构，PDE residual 约束训练。
- 实验对象：时空 PDE 解算问题。
- 与用户课题关联：适合考虑导热/辐射/流体场的局部结构学习与残差约束。
- 评分：5 + 1 + 2 = 8，core。

### 5. Novel DeepONet architecture to predict stresses in elastoplastic structures with variable complex geometries and loads

- 正式链接：https://doi.org/10.1016/j.cma.2023.116277
- DOI：10.1016/j.cma.2023.116277。
- 发表信息：Computer Methods in Applied Mechanics and Engineering 415, article 116277, 2023。
- 作者：Juncai He, Shuyi Zhou, Kuangyu G. Wang。
- 标签：DeepONet, elastoplasticity, complex geometry, computational mechanics。
- arXiv 状态：未确认。
- 核心贡献：提出面向变复杂几何和载荷的 DeepONet 应力预测架构。
- 方法要点：分支/主干式算子学习，处理几何和载荷参数变化。
- 实验对象：弹塑性结构应力场。
- 与用户课题关联：对变几何、变载荷、多参数场预测和结构化代理模型设计有迁移价值。
- 评分：4 + 2 + 2 = 8，core。

### 6. Multistage physics informed neural network for solving coupled multiphysics problems in material degradation and fluid dynamics

- 正式链接：https://doi.org/10.1007/s00366-025-02174-4
- DOI：10.1007/s00366-025-02174-4。
- 发表信息：Engineering with Computers 41, 3491–3521, published online 2025-06-29。
- 作者/机构：Mahmoud Khadijeh, Veronica Cerqueglini, Cor Kasbergen, Sandra Erkens, Aikaterini Varveri；Delft University of Technology, Politecnico di Torino。
- 标签：multistage PINN, multiphysics, material degradation, fluid dynamics。
- arXiv 状态：无。
- 核心贡献：通过分阶段引入耦合物理降低多物理 PINN 训练难度，并在材料退化和 lid-driven cavity flow 中验证。
- 方法要点：curriculum learning、阶段式物理耦合、与 FEM 对比。
- 实验对象：asphalt aging、lid-driven cavity flow。
- 与用户课题关联：对辐射-导热-流体-材料状态耦合 PINN/混合代理训练具有直接方法参考。
- 评分：5 + 1 + 2 = 8，core。

### 7. Geometry-informed neural operator for large-scale 3D PDEs

- 正式链接：https://proceedings.neurips.cc/paper_files/paper/2023/hash/70518ea42831f02afc3a2828993935ad-Abstract-Conference.html
- DOI：无。
- 发表信息：NeurIPS 2023 Proceedings, Advances in Neural Information Processing Systems 36, 2023。
- 作者：Zongyi Li, Daniel Zhengyu Huang, Burigede Liu, Anima Anandkumar。
- 标签：GINO, 3D PDE, complex geometry, geometry-informed neural operator。
- arXiv 状态：未确认。
- 核心贡献：融合局部图核与全局算子学习，实现大规模 3D PDE 的复杂几何建模。
- 方法要点：几何编码、局部-全局算子组合、三维场代理。
- 实验对象：三维 PDE 与复杂几何模拟。
- 与用户课题关联：适合三维激光等离子体/液滴几何变化代理模型的长期路线。
- 评分：5 + 1 + 2 = 8，core。

## 扩展入选论文

本期无高置信扩展入选。主要原因是可作为扩展的 review/perspective 候选虽然方法价值较高，但 publisher venue、DOI 或 publication date 未能在当前工具环境中完全确认，未写入正式扩展列表。

## 方向 A/B/C/D 覆盖

- A：AI 求解 PDE / SciML：LSM、Transolver、SONets、f-PICNN、Multistage PINN、GINO。
- B：代理模型 / ROM / 科学仿真加速：LSM、Transolver、DeepONet stress surrogate、GINO。
- C：科学计算与物理系统应用：DeepONet elastoplasticity、Multistage PINN fluid dynamics、Transolver industrial CFD。
- D：激光等离子体 / EUV / RHD / Vlasov / MHD：已检索，但本期无新增高置信正式入选；主要原因是多数新发现条目为 arXiv-only，或正式论文偏纯实验/控制应用，与 AI 科学计算方法关系不足。

## 按 venue 组覆盖说明

- 顶刊/顶会组：已覆盖 ICML 2023、ICML 2024、NeurIPS 2023；本期新增 LSM、Transolver、GINO。
- 计算物理与科学计算组：已覆盖 JCP、CMAME、Engineering with Computers；本期新增 SONets、f-PICNN、DeepONet stress surrogate、Multistage PINN。
- AI for Science / 数据驱动科学组：补查了 Nature Machine Intelligence、Nature Reviews Physics、Digital Discovery、Patterns、npj Computational Materials；本期未新增高置信条目，原因是已有记录覆盖较多，新增候选多为重复或缺少完整正式元数据。
- 等离子体/EUV/光学组：补查 Physics of Plasmas、HEDP、PPCF、Nuclear Fusion、Optics Express、Optica、APL、JAP；本期无新增正式入选，原因是多数候选为纯实验论文、传统等离子体建模论文，或仅有 arXiv/会议摘要而无正式出版元数据。

## 已有 arXiv 论文正式发表状态更新

- arXiv:2301.12664 → ICML 2023 / PMLR 202：Solving High-Dimensional PDEs with Latent Spectral Models。
- arXiv:2402.02366 → ICML 2024 / PMLR 235：Transolver。
- Geometry-informed neural operator 已确认 NeurIPS 2023 proceedings 正式版本。

## 待人工确认论文

1. Artificial intelligence for partial differential equations in computational mechanics: A review：方法价值高，但本轮未确认 DOI、正式 venue 和 publication date。
2. Laplace neural operator for solving differential equations：已知 Nature Machine Intelligence 6, 631–640 (2024)，但本轮未能高置信核验 DOI 和官方页面。
3. Learning Physical Operators using Neural Operators：当前仅确认 arXiv 版本，未纳入正式发表列表。
4. Point Cloud Neural Operator for Parametric PDEs on Complex and Variable Geometries：当前仅确认 arXiv 版本，未纳入正式发表列表。

## 本期未入选原因简述

- 已在 `metadata/published_papers.jsonl` 或 W23–W26 分周 JSONL 中出现的论文不重复写入。
- 只有 arXiv 页面、无 DOI/venue/publisher 元数据的论文不进入正式入选。
- 纯实验、纯材料发现、纯控制应用且与科学计算代理/AI for PDE 关系较弱的论文未纳入。
- 出版商页面受限或 DOI/日期冲突的条目进入待人工确认。

## 仓库更新说明

- 本期周报：`digests/published/AI-for-PDE-正式发表周报-2026-W27.md`
- 本期结构化元数据：`metadata/published_papers_2026_W27.jsonl`
- 运行日志：`run_log_published.md`

为避免整文件替换时覆盖历史长 JSONL，本期沿用 W24–W26 的安全策略，将新增结构化记录写入分周 JSONL 文件，而不是直接重写 `metadata/published_papers.jsonl`。
