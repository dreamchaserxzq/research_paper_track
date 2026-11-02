# AI for PDE 正式发表论文追踪周报 · 2026-W45

> **报告基准**：2026-11-02 UTC；新增出版发现的常规覆盖窗口为 **2026-10-25 13:01 至 2026-11-02 01:44 UTC**（继 W44 之后，含 48 小时重叠）；同时回溯 **2023-11-02 至 2026-11-02 UTC** 的正式发表历史，并不受三年界限限制地复查已有预印本。  
> **出版状态标准**：官方出版商网页/正式 proceedings；本期选入均为 `published`，不将仅有 arXiv 作为正式证据。ICML 2026 举办日期 **2026-07-06 至 07-11** 与 PMLR Volume 306 的**在线出版日期 2026-09-29**有区别。  
> **计数口径**：12 个不同标题/身份的候选（9 个具 arXiv/DOI，另有 3 篇已在官方 proceedings 中但缺稳定可入库标识）；本期正式入选 5 篇、排除 4 篇、待确认 3 篇。其他历史日期差异为元数据审计项，不重复计入论文候选。

## 1. 本期概览

| 指标 | 数量 | 解释 |
|---|---:|---|
| 原始候选 | 12 | 实际核验的 9 个稳定身份 + 3 个待补标识 |
| 去重后候选 | 12 | 依据统一论文表的 arXiv、DOI、标题/作者身份，不重复计算 |
| 正式状态明确 | 12 | 5 篇入选、4 篇正式但不符筛选阈值、3 篇有 proceedings 但无稳定入库 ID |
| 核心入选（core） | **2** | Geo-NeWF、EqGINO |
| 扩展入选（extended） | **3** | 物理引导粗化、DOD、相场断裂 C-FNO |
| 已有预印本正式状态更新 | **1** | arXiv 2602.02788：preprint → published |
| 新增正式论文身份 | **4** | 2 篇新 arXiv 身份 + 2 篇 DOI-only |
| 待人工确认 | **3** | Origo、MERLIN、ReViT 仍缺可确认的 arXiv ID / DOI |
| 需要另行核对的历史日期记录 | 另列 | W44 个别 ICML 2026 记录将会议日作 publication_date 的可能性 |

本期五篇入选工作均**不是 2026-10-25 之后才首次发表**。三篇 ICML 2026 论文是正式 proceedings 的**历史状态回填**，另外两篇是三年范围内的期刊正式论文补录。避免将“本周发现/回填”等同于“本周发表”。

## 2. 研究趋势与对 PDE 基座模型的意义

1. **复杂几何泛化的路径出现分化。** Geo-NeWF 以几何兼容有限元基与拓扑/守恒结构实现显式物理归纳偏置；EqGINO 通过谱域旋转等变性让 3D 算子对几何姿态变化更稳健。前者优先保证特定离散结构，后者优先保持算子对称性。二者均不是已经验证跨所有 PDE 的统一 foundation model。
2. **多尺度计算预算越来越依赖物理信息。** Physics-Informed Coarsening 使用残差识别应力/应变集中区域，在图多重网格中配置计算资源。对高分辨率点云/非结构网格主干，值得比较“残差自适应 Token 预算”与纯几何密度采样的区别。
3. **连续自适应的低秩物理场表示值得关注。** DOD 允许约化基随参数连续改变，可与固定 POD/Fourier/Gaussian basis 对比，特别适合评测几何变化和高维参数。
4. **强局部特征仍是频谱算子的难点。** 相场脆性断裂的 C-FNO 在全局频谱之外加局部卷积来解析近似尖锐裂纹；这与“边界/界面局部专家 + 全场共享算子”的设计动机相关，但其数据仅验证有限二维断裂设置，不能外推到多物理界面问题。
5. **科学解释需要区分约束保证和经验泛化。** Geo-NeWF 的 FEEC 相容构造提供针对离散结构的保证；EqGINO 的严格对称性针对有限离散群，连续旋转表现是经验性泛化；普通学习损失中的物理正则化则并不等价于离散守恒。

## 3. 核心入选（core）

### 3.1 Structure-Preserving Learning Improves Geometry Generalization in Neural PDEs（Geo-NeWF）

| 字段 | 核验结果 |
|---|---|
| arXiv / 旧状态 | [2602.02788](https://arxiv.org/abs/2602.02788)；仓库原为 `preprint` |
| 新状态 | **published** |
| venue / publisher | ICML 2026 / PMLR，Volume 306，109470–109491 |
| publication_date | **2026-09-29**（PMLR 卷上线日期，不采用 7 月会议日期） |
| DOI | 未在官方出版页确认，`null` |
| 官方链接 | https://proceedings.mlr.press/v306/shaffer26a.html |
| 作者 | Benjamin D. Shaffer、Shawn Koohy、Brooks Kinch、M. Ani Hsieh、Nathaniel Trask |
| 单位 | 本次官方摘要页未独立核验，保持未知 |
| published_category | `operator`（辅类 `pinn`、`enabling`） |
| foundation_model_level | `general_pde_solver` |
| published-v2 评分 | **4 + 3 + 2 = 9/10** |

**方法**：Geo-NeWF 学习与计算网格兼容的低维有限元空间及离散算子，结合 Transformer 几何编码与 Finite Element Exterior Calculus（FEEC），面向新几何的稳态 PDE 解算。它将几何/边界条件直接纳入有限元空间的构造，而不是只把坐标当作网络特征。

**数据与泛化**：官方摘要报告多个稳态 PDE benchmark 和未见几何上的 OOD 测试，强调几何与拓扑变化下的结构保持。**核心贡献**是给出几何泛化与相容离散结构之间的联系。

**局限**：并非已验证的多 PDE 大规模预训练基座；守恒性质依赖具体 FEEC 构造及所求解问题的适用前提。理论保证不能泛化为对所有物理守恒律的自动严格满足。

### 3.2 EqGINO: Equivariant Geometry-Informed Fourier Neural Operators for 3D PDEs

| 字段 | 核验结果 |
|---|---|
| arXiv | [2606.03260](https://arxiv.org/abs/2606.03260) |
| 状态 | **published** |
| venue / publisher | ICML 2026 / PMLR，Volume 306，58996–59026 |
| publication_date | **2026-09-29** |
| DOI | 未在官方出版页确认，`null` |
| 官方链接 | https://proceedings.mlr.press/v306/kim26bp.html |
| 作者 | Sungwon Kim、Juho Song、Seungmin Shin、Guimok Cho、Sangkook Kim、Chanyoung Park |
| 单位 | 本次不从非官方索引代填 |
| published_category | `operator`（辅类 `enabling`） |
| foundation_model_level | `general_pde_solver` |
| published-v2 评分 | **4 + 3 + 2 = 9/10** |

**方法**：将几何信息神经算子与谱域各向同性 Fourier 核组合。其设计针对离散计算域对称性实现严格的离散旋转等变，并在有限旋转训练样本下测试连续方位变化的稳健性。

**数据与泛化**：复杂不规则三维几何、三维 PDE 预测及旋转 OOD；作者提供了公开 arXiv 预印本。主要创新在于同时保持频谱全局作用与几何对称性。

**局限**：严格等变性与连续三维旋转等变的范围不能混淆；与任意新方程零样本求解是不同泛化轴。对具有特定绝对方向的外力、边界或各向异性材料，需在条件表示中同步变换。

## 4. 扩展入选（extended）

### 4.1 Physics-Informed Coarsening for Multigrid Graph Neural Surrogates

- **身份**：[arXiv:2605.31013](https://arxiv.org/abs/2605.31013)；**published**。
- **venue / publisher**：ICML 2026 / PMLR 306:7179–7194；**publication_date**：2026-09-29；**DOI**：null。
- **正式证据**：https://proceedings.mlr.press/v306/bazzi26a.html
- **作者（采用正式 proceedings 署名）**：Amir Bazzi、Ramy Nemer、Alves José、Elie Hachem；**机构**：本次未独立核验。
- **published_category**：`surrogate`（辅类 `enabling`）；**foundation_model_level**：`surrogate_model`；**评分**：3 + 1 + 2 = **6/10**。
- **方法、数据与泛化**：用物理残差估计节点重要性，在多重图网格中保留高应力/应变区，测试线性、非线性与瞬态固体力学预测，并对长轨迹稳定性作比较。
- **为什么是 extended**：物理引导粗化可迁移为通用 Token/网格预算模块，但实验主体是固体力学 surrogate，不构成跨 PDE 基座能力。**匹配备注**：arXiv 与会议最终作者数量存在差异；同一标题、第一作者和方法高度一致，本次入库按正式出版页作者，保留后续身份审计项。

### 4.2 Deep orthogonal decomposition: a continuously adaptive neural network approach to model order reduction of parametrized partial differential equations

- **DOI**：[10.1007/s10444-026-10295-7](https://doi.org/10.1007/s10444-026-10295-7)；**arXiv**：本次未确认；**published**。
- **venue / publisher**：Advances in Computational Mathematics 52, Article 31 / Springer Nature；**publication_date**：**2026-04-17**。
- **作者**：Nicola Rares Franco、Andrea Manzoni、Paolo Zunino、Jan S. Hesthaven；**机构**：本次未独立复核。
- **正式证据**：https://link.springer.com/article/10.1007/s10444-026-10295-7
- **published_category**：`surrogate`（辅类 `enabling`）；**foundation_model_level**：`surrogate_model`；**评分**：3 + 2 + 2 = **7/10**。
- **方法、数据与泛化**：用连续依参数变化的自适应局部基表示解流形，形成 DOD-NN；官方摘要覆盖非线性 PDE、参数化几何和高维参数问题。强调可解释降维与误差传播控制。
- **为什么是 extended**：贡献属于可复用的降阶表示与参数适配，但不是多 PDE 通用解算预训练模型；部署时基更新成本和精度边界需另测。

### 4.3 Parametric phase-field brittle fracture computations with convolutional Fourier neural operators

- **DOI**：[10.1007/s00466-026-02858-8](https://doi.org/10.1007/s00466-026-02858-8)；**arXiv**：本次未确认；**published**。
- **venue / publisher**：Computational Mechanics / Springer Nature；**publication_date**：**2026-09-19**。
- **作者**：Aryan Sinha、Manav Manav、Bogdan Raonic、Siddhartha Mishra、Laura De Lorenzis；**机构**：ETH Zurich（出版商作者信息）。
- **正式证据**：https://link.springer.com/article/10.1007/s00466-026-02858-8
- **published_category**：`surrogate`（辅类 `operator`）；**foundation_model_level**：`surrogate_model`；**评分**：3 + 1 + 2 = **6/10**。
- **方法、数据与泛化**：C-FNO 将全局 Fourier 层与局部空间卷积组合，针对二维 single-edge notched specimens 的初始缺口长度、载荷幅值和角度变化模拟相场裂纹扩展、转折与分叉。
- **为什么是 extended**：对尖锐界面和局部高梯度结构有方法参考意义，但只覆盖特定二维断裂系统；并无跨物理或通用基座模型能力证明。

## 5. 按正式分类总结

| `published_category` | 核心 | 扩展 | 代表 |
|---|---:|---:|---|
| `foundation_model` | 0 | 0 | 本次无新入选，不代表没有在研预印本 |
| `operator` | 2 | 0 | Geo-NeWF、EqGINO |
| `surrogate` | 0 | 3 | 物理粗化、DOD、相场断裂 |
| `pinn` | 0 | 0 | 作为辅类及筛除候选出现 |
| `data` | 0 | 0 | 暂无足够高价值的新正式数据集 |
| `enabling` | 0 | 0 | 以多标签辅类体现 |

上述表只按**主类**计数，`published_categories` 允许交叉标签；零入选不得推断领域零进展。

## 6. Venue 覆盖与排除情况

| venue / 来源 | 本期核验 | 入选 | 未入选或注意事项 |
|---|---|---:|---|
| ICML 2026 / PMLR 306 | 官方 proceedings、摘要、arXiv ID 匹配 | **3** | Origo、MERLIN、ReViT 缺稳定 ID 进入 pending |
| Advances in Computational Mathematics | Springer 正式期刊日期和 DOI | **1** | 1D conservation-law refinement（DOI 10.1007/s10444-026-10357-w）因通用性不足排除 |
| Computational Mechanics | Springer 正式期刊日期和 DOI | **1** | 无其他满足本期筛选的新增 |
| Physics of Plasmas | AIP Oct 2026 已发表记录 | **0** | DustNET 为综述；electron Boltzmann PINN 与 solar-wind ROM 偏单任务 |
| JCP / CMAME / SISC / MLST / Nuclear Fusion | 交叉检索已知条目及近期线索 | **0** | 未取得新的、可独立核验且未入库的高价值结果；不代表完整穷举 |
| NeurIPS 2026 / ICLR / TMLR 等 | 有针对性的正式状态与 venue 检索 | **0** | HotPOT 等近期预印本未在本次获得足以升级的官方证据，保留 preprint |

本次确实检索了多个非 Nature venue，不以单一出版集团为入选过滤条件。由于 AIP 部分详细页面重定向不可访问，相关候选只作为**已识别的排除项**，未以缺失全文的证据撰写超出摘要的技术结论。

## 7. 已有预印本正式发表状态更新

| arXiv | 论文 | 旧状态 → 新状态 | 正式 venue | DOI | publication_date |
|---|---|---|---|---|---|
| [2602.02788](https://arxiv.org/abs/2602.02788) | Geo-NeWF | `preprint` → **`published`** | ICML 2026 / PMLR 306 | null | 2026-09-29 |

官方出处：https://proceedings.mlr.press/v306/shaffer26a.html

**新录入但不算状态更新**：EqGINO、Physics-Informed Coarsening 之前未在统一表中出现；DOD 和相场断裂此前也未以该 DOI 身份入库。它们属于四条新增正式论文身份，不能重复算作已有预印本升级。

## 8. 待人工确认与保留的冲突

1. **Origo: Interpretable Multi-physics PDE Foundation Model through Neural Operator Splitting**。已确认 [ICML 2026 PMLR 正式页](https://proceedings.mlr.press/v306/sun26aa.html)，作者 Li Sun 等，方法强调可组合 neural operator bank 与跨未见 PDE 的机理泛化；本次仍没有独立匹配的 arXiv ID / 正式 DOI。按 `OPERATIONS.md` 不创建仅标题事件，下一步核验正式 DOI 或可对应 arXiv。
2. **Interpretable Functional Koopman Learning with Non-Markovian Closure for Spatiotemporal Systems（MERLIN）**。已确认 [ICML 2026 PMLR 正式页](https://proceedings.mlr.press/v306/lu26u.html)，作者 Wanfeng Lu 等，强调非 Markov 记忆与任意分辨率重建；稳定 arXiv/DOI 仍未核对。暂不以标题创建事件。
3. **ReViT: Rotational-equivariant Vision Transformers for Neural PDE Solvers**。已确认 [ICML 2026 PMLR 正式页](https://proceedings.mlr.press/v306/wei26p.html)，作者 Hao Wei、Björn List、Nils Thuerey；本次未找到可独立确证的 arXiv 或正式 DOI。潜在 core 高价值，但不绕过身份契约入库。
4. **已有历史 publication_date 的一致性复核（不计入上述 3 篇 pending）**。PMLR [Volume 306](https://proceedings.mlr.press/v306/) 标示正式出版于 **2026-09-29**；仓库 W44 若干 ICML 2026 条目记录 **2026-07-06**（会议开始日），可能不符“出版商日期优先”规则。本期**没有覆盖任何既有可信字段**；建议逐条复核 W44 的 ICML 条目并用独立 `correction` 事件处理，经证据确认后再更新正式日期。
5. **Physics-Informed Coarsening 署名差异**。PMLR 2026 正式版本列出 4 位作者，arXiv 摘要版本列出额外合作者；标题与第一作者一致，但应在后续来源审计中保存版本差异。此次未修改原 arXiv 历史证据。

## 9. 排除候选（正式论文不等于必然入选）

| 正式论文 | 官方 DOI / 日期 | 排除原因 |
|---|---|---|
| Neural network-assisted refinement of traditional schemes for one-dimensional scalar conservation laws | [10.1007/s10444-026-10357-w](https://doi.org/10.1007/s10444-026-10357-w), 2026-09-17 | 限于 1D conservation-law 数值格式改进，当前未见足够广的跨系统价值 |
| DustNET: Enabling machine learning and AI models of dusty plasmas | [10.1063/5.0337599](https://doi.org/10.1063/5.0337599), 2026-10-30 | 高相关领域综述，但不是明确可复用的 AI PDE 求解模型/数据基准 |
| A physics-informed neural network approach to solve the spatially inhomogeneous electron Boltzmann equation | [10.1063/5.0342773](https://doi.org/10.1063/5.0342773), 2026-10-14 | 低温等离子体单任务 PINN，尚未见广泛迁移或统一框架证据 |
| Inferring solar-wind plasma structures from sparse probe measurements using recurrent reduced-order learning | [10.1063/5.0349748](https://doi.org/10.1063/5.0349748), 2026-10-13 | 特定观测重建 ROM，而非主要针对跨任务前向 PDE 求解 |

## 10. 证据、数据接口与后续验证假设

**官方核验页面**：本期 5 篇入选以 PMLR 正式 proceedings 或 Springer 期刊页面为主证据；arXiv 页面仅用于对应论文身份。多篇 ICML 论文会议信息来自 PMLR Volume 306；其 online publication_date 按该卷的出版日期填写，禁止用首次 arXiv 日期代替。

**数据写入**：
- `metadata/inbox/2026-11-02.jsonl`：五条新的 `published-v2` publication 事件，其中一条升级既有预印本。
- `metadata/runs/published-2026-W45.json`：本期实际搜索、可识别的 9 个候选及其收录/排除理由；另有 3 个无法入库的无稳定 ID 论文在本报告留痕。
- 兼容视图（`metadata/papers.jsonl`、`paper_registry.jsonl`、`published_papers.jsonl`）及 README 索引须由 `python scripts/papertrack.py build` 重建，不能直接改写。

**对 UPFM 的可证伪假设**：在统一点云/网格输入下，对照（i）几何构造的 FEEC 兼容基、（ii）旋转等变谱核、（iii）应力/残差驱动的自适应 Token 预算、（iv）参数条件化 DOD 基，并在**新几何、新 PDE、旋转 OOD、界面/局部高梯度**四个互不混淆的测试轴上独立做消融；不能仅以某一单 PDE OOD 结果宣称“PDE 基座泛化”。

*检索日期：2026-11-02 UTC；本期发表状态为实际核对的官方记录，并不构成对所有会刊条目的穷举。*
