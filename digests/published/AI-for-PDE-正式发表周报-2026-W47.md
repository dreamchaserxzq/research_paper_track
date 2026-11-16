# AI for PDE 正式发表论文追踪周报 · 2026-W47

> **核验基准**：2026-11-16 UTC。连续发现窗口为 2026-10-31T01:44:26Z 至本次核验时刻；按规则另外回查 2023-11-16 至 2026-11-16 的三年历史与更早的待核验预印本。首次发表日期、预印本提交日期、本期核验/回填日期严格区分。本期主要属于**正式版本历史补录**，不能解释成 2026-W47 新发表的四篇论文。正式归档优先按出版商和官方 proceedings 判定。

## 一、本期概览

| 指标 | 数量 | 口径 |
|---|---:|---|
| 原始候选 | 11 | 不同论文身份/标题：4 篇选入、2 篇排除、5 篇待确认 |
| 去重后候选 | 11 | 以现有统一注册表的 arXiv、DOI、标题及作者核验；7 篇有稳定 arXiv/DOI，4 篇尚缺稳定标识 |
| 官方正式状态明确 | 10 | 4 篇本期选入、2 篇排除和 4 篇仅有正式会议页面但暂无可靠 arXiv/DOI |
| 核心入选 core | 3 | GeoPT、Boundary Extensions、IRNO |
| 扩展入选 extended | 1 | Geometric Forgetting |
| 由预印本升级为正式状态 | 2 | GeoPT、Geometric Forgetting |
| 新增具有稳定身份的正式论文 | 2 | Boundary Extensions、IRNO |
| 待人工确认 pending | 5 | PDE-PFN 的正式接收状态；Origo、MERLIN、ReViT、MiSe-GNN 的稳定身份 |
| 有正式证据但因价值不够未收录 | 2 | IEEE 工程型算子应用；Hall thruster 电流控制 |

**检索状态：degraded。** PMLR ICML 2026 四篇收录论文有直接正式 proceedings 证据；PDE-PFN 尚未获得 NeurIPS 2026 会议官网/官方 OpenReview 接收决定的可复查证据，本次不升级。跨 venue 检索属于定向抽样，不宣称完整覆盖三年全部期刊论文；失败/降级不会推进上次成功检索覆盖终点 2026-11-02T01:44:26.719Z。

## 二、趋势总结与 UPFM 相关性

1. **几何预训练与物理迁移进一步结合。** GeoPT 使用由静态几何构造的合成动力学自监督，降低真实 CFD/固体力学高保真训练样本需求。这提示 UPFM 可以比较真实动力学专家预训练与低成本几何-动力学任务预训练，但不能将微调后迁移称为零样本跨 PDE 能力。
2. **边界条件从数值标签变成全域条件场。** Boundary Extensions 把复杂边界负载学习映射成定义于整个物理域的伪扩展场，适用于统一点云主干的边界条件记忆与融合；不能忽略严格边界残差和守恒验证。
3. **多尺度误差校正与谱偏差控制。** IRNO 的收缩映射与逐步增强频域损失提供候选的专家误差校正路径，需额外比较反复推理成本、任意时间查询能力及稳定性。
4. **几何信息在深层网络中可能被遗忘。** 几何信息中间层再注入是一种能直接实测的结构假设，优先以复杂几何边界层误差和跨网格外推验证，而非仅看均值 NRMSE。
5. **未发现新证据足以把本期方法称为真正的通用 PDE foundation model。** 多 PDE/多几何微调、物理结构兼容性和跨任务零样本泛化是不同指标，周报分开报告。

## 三、核心论文（core）

### 1. GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training

- **作者**：Haixu Wu, Minghao Guo, Zongyi Li, Zhiyang Dou, Mingsheng Long, Kaiming He, Wojciech Matusik。机构以正式论文全文为准，本次未独立提取，不推断。
- **venue / publisher / status**：ICML 2026 / Proceedings of Machine Learning Research (PMLR), Volume 306, pages 135932–135959 / **published**。
- **publication_date**：**2026-09-29**，取 [PMLR Volume 306 发布日期](https://proceedings.mlr.press/v306/)；不是 2026-07-06 会议开幕日期。**DOI**：未确认正式出版社 DOI，记 `null`。
- **正式链接**：[PMLR proceedings](https://proceedings.mlr.press/v306/wu26s.html)。**arXiv**：[2602.20399](https://arxiv.org/abs/2602.20399)，原为 preprint，本期已核验升级。
- **published_category**：`foundation_model`；**foundation_model_level**：`foundation_model_candidate`；**selection_tier**：`core`。
- **方法 / 数据 / 物理系统**：以几何数据进行 dynamics-lifted 自监督预训练，使用超过一百万份预训练样本；下游汽车、飞机、船舶流体和固体碰撞仿真，论文报告标注数据需求降低 20%–60%、收敛加快至约 2 倍。
- **泛化方式与核心贡献**：跨几何、跨物理下游任务的**微调迁移**，通过合成演化任务为几何表示引入动力学信息。
- **局限**：依赖下游微调及几何归一化；尚未证实对未见物理方程的严格 zero-shot 求解或离散守恒。
- **published-v2 评分**：相关度 **4/5** + 泛化 **3/3** + 方法证据 **2/2** = **9/10**。

### 2. Imposing Boundary Conditions on Neural Operators via Learned Function Extensions

- **作者**：Sepehr Mousavi, Siddhartha Mishra, Laura De Lorenzis。机构未独立核实。
- **venue / publisher / status**：ICML 2026 / PMLR 306, pages 90631–90679 / **published**；**publication_date**：**2026-09-29**；正式 DOI 未确认（`null`）。
- **正式链接**：[PMLR proceedings](https://proceedings.mlr.press/v306/mousavi26a.html)。**arXiv**：[2602.04923](https://arxiv.org/abs/2602.04923)，本期首次以正式身份入库。
- **published_category**：`operator`；**foundation_model_level**：`general_pde_solver`；**selection_tier**：`core`。
- **方法 / 数据 / 物理系统**：学习边界数据到全域伪扩展函数的映射，再由普通 domain-to-domain neural operator 消费；18 个数据集覆盖 Poisson、线弹性、超弹性、复杂几何和混合边界条件。
- **泛化方式与核心贡献**：不同边界类型、边界分段、多分量边界激励的条件化适配；为复杂边界提供可与既有算子主干解耦的学习式接口。
- **局限**：学习的扩展场不自动保证任意下游网络精确满足边界约束，也不构成跨所有 PDE 的零样本证明。
- **published-v2 评分**：相关度 **4/5** + 泛化 **2/3** + 方法证据 **2/2** = **8/10**。

### 3. Iterative Refinement Neural Operators are Learned Fixed-Point Solvers: A Principled Approach to Spectral Bias Mitigation

- **作者**：Xiaotian Liu, Shuyuan Shang, Xiaopeng Wang, Pu Ren, Yaoqing Yang。机构未独立核实。
- **venue / publisher / status**：ICML 2026 / PMLR 306, pages 78216–78247 / **published**；**publication_date**：**2026-09-29**；正式 DOI 未确认（`null`）。
- **正式链接**：[PMLR proceedings](https://proceedings.mlr.press/v306/liu26dm.html)。**arXiv**：[2605.24041](https://arxiv.org/abs/2605.24041)，本期首次以正式身份入库。
- **published_category**：`operator`；**foundation_model_level**：`enabling_method`；**selection_tier**：`core`。
- **方法 / 数据 / 物理系统**：预训练神经算子给粗预测，学习的迭代残差修正器通过固定点递推处理高频误差；渐进谱损失控制频带。实验包括湍流及 Active Matter 等数据。
- **泛化方式与核心贡献**：将修正模块用于预训练算子，研究不同迭代步数下的收敛/频域表现；论文报告湍流相对误差改善最高约 56.05%（特定设置，不是全任务平均）。
- **局限**：收敛理论有局部收缩假设；迭代次数增加了推理成本，与单次连续时间查询并不等价。
- **published-v2 评分**：相关度 **4/5** + 泛化 **1/3** + 方法证据 **2/2** = **7/10**。

## 四、扩展论文（extended）

### 4. Do Neural Operators Forget Geometry? The Forgetting Hypothesis in Deep Operator Learning

- **作者**：Yanming Xia, Angelica I. Aviles-Rivero。机构未独立核实。
- **venue / publisher / status**：ICML 2026 / PMLR 306, pages 138068–138086 / **published**；**publication_date**：**2026-09-29**；正式 DOI 未确认（`null`）。
- **正式链接**：[PMLR proceedings](https://proceedings.mlr.press/v306/xia26a.html)。**arXiv**：[2605.05862](https://arxiv.org/abs/2605.05862)，已有预印本本期升级。
- **published_category**：`enabling`；**foundation_model_level**：`enabling_method`；**selection_tier**：`extended`。
- **方法 / 系统 / 泛化**：利用中间层几何探测揭示深层算子中几何约束表征逐层衰减，提出在中间层反复注入几何记忆以改善复杂域学习。
- **为何 extended**：主要是归因诊断和条件注入技术，而非独立的通用 PDE 求解框架；对于边界/几何条件传递很重要，但证据尚不足以评估全类 PDE 的可靠泛化。
- **局限**：对任意三维非结构网格、严格边界满足和守恒性的验证仍需进一步实验。
- **published-v2 评分**：相关度 **3/5** + 泛化 **2/3** + 方法证据 **2/2** = **7/10**。

## 五、分类汇总

| published_category | 本期入选 | 论文 |
|---|---:|---|
| `foundation_model` | 1 | GeoPT（core） |
| `operator` | 2 | Boundary Extensions、IRNO（core） |
| `enabling` | 1 | Geometric Forgetting（extended） |
| `surrogate` | 0 | 相关方向在多类别中出现，暂无独立主类入选 |
| `pinn` | 0 | 无达到入选标准的独立新论文 |
| `data` | 0 | 无达到入选标准的独立新论文 |

以上按主类统计，不对一个论文的多个 `published_categories` 重复计数。

## 六、Venue 覆盖、排除与边界

- **ICML 2026 / PMLR 306**：定向核验 GeoPT、边界函数扩展、IRNO、几何遗忘以及 Origo、MERLIN、ReViT、MiSe-GNN；其中 4 篇已收录，其他 4 篇有正式 proceedings 但尚无可核实 arXiv/DOI，依据仓库事件契约继续 pending。PMLR 卷的正式在线发布日期为 2026-09-29。
- **IEEE WorldSUAS 2026 / IEEE Xplore**：[Neural Operators for Physics-Informed Modeling in Complex Engineering Systems](https://ieeexplore.ieee.org/abstract/document/11767230)，DOI `10.1109/WorldSUAS70880.2026.11767230`。官方索引显示 2026-11-06 加入 IEEE Xplore，**索引日期不是出版日期**；仅为常规工程应用，多 PDE 泛化证据不足，排除，且详细页直接打开受限。
- **Journal of Electric Propulsion / Springer Nature**：[Real-time machine learning control of a Hall thruster discharge plasma](https://link.springer.com/article/10.1007/s44205-026-00229-2)，DOI `10.1007/s44205-026-00229-2`，正式日期 **2026-11-11**。其核心是实验时序系统辨识和放电电流反馈控制，并非跨物理 PDE 求解器，排除。
- **NeurIPS 2026 / OpenReview**：重点复查 PDE-PFN，但未获得明确的会议官方接收证据，因此不把外部论文聚合网站上的会议标签视作正式接收。
- **JCP、CMAME、SISC、TMLR、MLST、Physics of Plasmas、Nuclear Fusion、Nature 系列**：执行了综合检索提示词/索引的定向查询，但本轮没有另取得可同时匹配稳定身份、正式出版状态、重要性门槛的新增高置信论文。该描述不等于全量检索上述期刊逐篇正文。

## 七、正式发表状态更新

| 稳定身份 | 原仓库状态 | 核验结果 | 正式 DOI | 日期 | 证据 |
|---|---|---|---|---|---|
| [arXiv:2602.20399](https://arxiv.org/abs/2602.20399) GeoPT | preprint | ICML 2026 / PMLR 306, published | null（未确认） | 2026-09-29 | [PMLR](https://proceedings.mlr.press/v306/wu26s.html) |
| [arXiv:2605.05862](https://arxiv.org/abs/2605.05862) Geometric Forgetting | preprint | ICML 2026 / PMLR 306, published | null（未确认） | 2026-09-29 | [PMLR](https://proceedings.mlr.press/v306/xia26a.html) |

两篇尚未加入统一表的新正式身份为 arXiv:2602.04923 和 arXiv:2605.24041。**不得把 PMLR 会议日期或者 arXiv/DataCite DOI 冒充正式在线出版日期/正式 DOI。**

## 八、待人工确认（pending）

| 候选 | 已有证据与冲突点 | 建议 |
|---|---|---|
| [PDE-PFN](https://arxiv.org/abs/2610.13334)（arXiv:2610.13334） | arXiv 有身份；外部聚合页面标 NeurIPS 2026，但未核验会议官网/官方接收决定 | 仅待官方 NeurIPS/OpenReview 接收决定，仍为 preprint，不写 publication 事件 |
| [Origo](https://proceedings.mlr.press/v306/sun26aa.html) | ICML 2026 PMLR 正式 proceedings 明确，缺核准的 arXiv/正式 DOI | 追溯作者/出版商稳定 ID，勿仅标题生成新事件 |
| [MERLIN](https://proceedings.mlr.press/v306/lu26u.html) | 正式 PMLR 页面明确，未能查得匹配的 arXiv/正式 DOI | 优先核验作者与出版商版本一致性 |
| [ReViT](https://proceedings.mlr.press/v306/wei26p.html) | 正式 PMLR 页面明确，尚无核准的 arXiv/正式 DOI；易与同卷另一篇 `REViT` 图像论文混淆 | 必须按完整标题和作者核对 |
| [MiSe-GNN](https://proceedings.mlr.press/v306/nguyen26a.html) | PMLR 收录正式标题为 *Error-Driven Graph Augmentation for Mesh-Based PDE Surrogates*，MiSe-GNN 是方法名；尚缺核准 arXiv/正式 DOI | 核对正式标题与稳定 ID 后再写入 |

此外，历史已有 8 项注册表冲突继续保留；既往部分 ICML 2026 日期误取会议开幕日期的问题应作为独立 correction 审计，不在本期强制覆盖。

## 九、对 UPFM 的下一步可验证假设

优先采用受控消融，不把四项研究混成一个大模块：**(1)** 对固定几何/多物理目标，用 GeoPT 风格的几何-动力学预训练对比纯专家预训练，统一真实求解数据和 GPU 预算；**(2)** 将 Boundary Extensions 作为边界条件记忆的候选输入，分别测 Dirichlet/Neumann/混合边界、边界外推和离散守恒；**(3)** 在统一主干每层/每隔数层注入几何条件，观察深度增加后的边界误差与几何探测准确率；**(4)** 为 IRNO 式修正建立误差-迭代次数-显存成本曲线，并与非自回归连续时间查询直接比较。所有结论按 PDE 家族、几何和边界条件分层报告。

## 十、记录与审计说明

本次 4 条 published-v2 publication 证据事件记录于 `metadata/inbox/2026-11-16.jsonl`，原始查询与候选判断记录于 `metadata/runs/published-2026-W47.json`。主表、正式发表兼容视图与 README 均应由 `python scripts/papertrack.py build` 决定性重建，**禁止直接手工编辑生成视图**。出版商/会议证据验证不等同于用 GitHub 自动校验器核验外部链接时效。

*本报告的参考时间为 2026-11-16 UTC；未确认值始终标注为 null / pending。*
