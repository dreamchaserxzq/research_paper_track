# AI for PDE 正式发表论文追踪周报 · 2026-W48

> 核验基准：**2026-11-23 UTC**。连续发现窗口从 **2026-10-31T01:44:26.719Z**（上次成功覆盖终点 2026-11-02T01:44:26.719Z 减 48 小时）至本次检查；另回顾 2023-11-23 至 2026-11-23 三年内正式版本，既有预印本状态复查不受三年起点限制。**本期核验/补录日期不等于论文首次发表日期。**
>
> **关键口径**：NeurIPS 2026 [官方 Downloads](https://neurips.cc/Downloads/2026) 已列出相关论文，按 `accepted` 记录，**不是 proceedings 已发表**；`publication_date=null`。ICML 2026 / PMLR 306 [正式出版](https://proceedings.mlr.press/v306/) 日期为 **2026-09-29**，不是会议举办日期 2026-07-06 至 11。

## 一、本期概览

| 指标 | 数量 | 说明 |
|---|---:|---|
| 原始候选论文 | **12** | 7 篇入选、1 篇排除、4 篇已有官方 proceedings 但缺核实稳定论文标识 |
| 去重后候选 | **12** | 已对统一表和正式发表视图按 arXiv、DOI、标题、作者交叉检查 |
| 正式状态明确 | **11** | 7 篇入选（其中 NeurIPS accepted 5、ICML published 2）和 4 篇待补 ID 的正式 PMLR 论文 |
| core | **4** | Hodge 算子、PDE-PFN、ECHO、CoupledFlow |
| extended | **3** | sTCL、TINNs、OpInf-LLM |
| 既有预印本升级 | **3** | Hodge、PDE-PFN、ECHO |
| 新增正式身份 | **4** | CoupledFlow、sTCL、TINNs、OpInf-LLM |
| 待人工确认 | **4** | Origo、MERLIN、ReViT、MiSe-GNN 的稳定 arXiv/正式 DOI |
| 排除 | **1** | Physics-informed fine-tuning 的 ICLR 2026 workshop 版本缺独立主会正式出版证据 |

**检索状态：degraded**。本期定向核验 NeurIPS 2026 官方名单、ICML 2026 PMLR、arXiv 对应身份和 Nature/Elsevier 线索；部分 Elsevier 详细页面因访问限制不可完整回查，不能宣称三年全量扫库。依照仓库规则，不推进上次成功覆盖检查点 2026-11-02T01:44:26.719Z。本期七篇属于“正式状态新确认/历史补录”，**并非七篇在 2026-W48 新出版**。

## 二、趋势与研究判断

1. **复杂多物理耦合转向可学习的条件流结构。** CoupledFlow 将不同过程的交互编码在结构约束的条件均值流中，并通过多输出 GP 插值提供耦合信息；这为 UPFM 的并行专家候选与统一耦合主干提供可比较路线，但流匹配中“生成时间”与真实 PDE 物理时间不可直接等同。
2. **超高分辨率轨迹表示和长时预测解耦。** ECHO 先对时空数据做层次压缩，再对整段轨迹生成，避免完全逐时自回归；其压缩和非自回归片段预测值得在质量/能量守恒、突变状态和跨网格场景做严格消融。
3. **in-context PDE solver 进入正式接收名单。** PDE-PFN 的 noisy approximate PINN prior 与 Transformer 条件化可实现不更新权重的样本内查询，但任务之间预训练迁移、上下文条件与严格 zero-shot 要分别评价。
4. **几何拓扑、微分结构与局部动力学显式分工。** Hodge 算子把拓扑主导的成分与可学习局部动力学分离，对复杂几何、非规则网格和守恒场表征有启发；与“无需硬编码结构”的数据驱动路线应公平比较模型容量与先验成本。
5. **物理约束逐渐进入导数、参数和模块接口。** sTCL 在训练期利用 PDE 残差导出的切向一致性而无需离线导数标签；TINNs 将真实时间映射至参数轨迹；两者不直接代表统一 PDE 基座模型，但可作轻量插件与泛化基线。
6. **科学 LLM 与数值模型职责分离。** OpInf-LLM 利用语言模型调度参数化低秩动力学工具，强调稳健的模型调用，而非让语言模型直接逐点生成可信解场。

## 三、核心论文（core，4 篇）

### 1. CoupledFlow: One-Step Neural Operators for Coupled Multi-Physics PDEs

- **作者**：Trong Khiem Tran, Minh Long Bui, Phi Le Nguyen, Mrinal Sen, Sanjay Srinivasan, Trong Nghia Hoang, Jana Doppa。机构本轮未从官方全文独立提取，不推断。
- **状态 / venue / publisher**：**accepted** / NeurIPS 2026 / NeurIPS；**publication_date**：`null`；**DOI**：`null`（未确认正式版本）。
- **正式接收证据**：[NeurIPS 2026 官方 Downloads](https://neurips.cc/Downloads/2026)，可按完整标题搜索；**arXiv**：[2611.10945](https://arxiv.org/abs/2611.10945)（此前未入统一表，本期新身份）。
- **分类**：`published_category=operator`；附类 `foundation_model, surrogate`；`foundation_model_level=general_pde_solver`；`selection_tier=core`。
- **方法 / 物理系统**：structure-constrained flow matching，学习由完整多物理态条件化的各过程平均速度场；用 posterior multi-output GP 生成跨过程相关的条件插值，推导平均流一致性约束与分布误差界。论文摘要报告在多种耦合 PDE 基准上优于若干基线，但本轮未从全文提取各工况详细清单。
- **泛化与价值**：联合条件与过程交互建模、面向耦合多物理系统的一步预测；有助检验 UPFM 中“专家候选 → 统一耦合轨迹”是否优于独立专家输出直接求和。
- **局限**：尚无证据证明对任意未见耦合类型、界面条件或非周期复杂几何均能零样本准确求解；一步生成不等于任意物理时间查询或离散守恒。
- **published-v2**：相关度 **4/5** + 泛化 **3/3** + 方法证据 **2/2** = **9/10**。

### 2. Efficient Generative Transformer Operators For Million-Point PDEs（ECHO）

- **作者**：Armand Kassaï Koupaï, Lise Le Boudec, Patrick Gallinari；机构未独立核实。
- **状态 / venue / publisher**：**accepted** / NeurIPS 2026 / NeurIPS；**publication_date**：`null`；**DOI**：`null`。
- **接收证据**：[NeurIPS 2026 官方 Downloads](https://neurips.cc/Downloads/2026)；**arXiv**：[2512.04974](https://arxiv.org/abs/2512.04974)，由 preprint 升级。
- **分类**：`published_category=operator`；附类 `foundation_model, surrogate`；`foundation_model_level=foundation_model_candidate`；`selection_tier=core`。
- **方法 / 任务**：层次卷积编码—解码实现论文报告的约 **100 倍时空压缩**，并以生成式 Transformer 预测完整轨迹片段；目标包含百万点 PDE 轨迹、稀疏输入到高分辨率输出、条件/无条件生成以及正向、逆向和插值任务。
- **泛化方式**：跨分辨率、复杂几何、长时段的表征复用与任务适配，不将多任务训练误称为零样本跨物理能力。
- **局限**：局部激波、高频结构和边界通量在高压缩率下的保真性需独立测量；片段预测不自然等同于连续时间解码或严格质量、动量、能量守恒。
- **published-v2**：相关度 **4/5** + 泛化 **3/3** + 方法证据 **2/2** = **9/10**。

### 3. PDE-PFN: Prior-Data Fitted Neural PDE Solver

- **作者**：Jaehyeon Park, Mingu Kang, Dongseok Lee, Woojin Cho, Kookjin Lee, Anthony Gruber, Youngjoon Hong, Noseong Park；机构未独立核实。
- **状态 / venue / publisher**：**accepted** / NeurIPS 2026 / NeurIPS；**publication_date**：`null`；**DOI**：`null`。
- **接收证据**：[NeurIPS 2026 官方 Downloads](https://neurips.cc/Downloads/2026) 列有完整标题；**arXiv**：[2610.13334](https://arxiv.org/abs/2610.13334)。过去 W46–W47 缺官方接收证明而 pending，本次确认。
- **分类**：`published_category=foundation_model`；附类 `operator, pinn`；`foundation_model_level=foundation_model_candidate`；`selection_tier=core`。
- **方法 / 数据 / 系统**：PFN 式 Transformer 使用低成本、不完全准确的 PINN 解作为预训练先验，学习基于上下文和空间坐标查询的 PDE 解场预测；论文涉及二维对流—扩散—反应，以及浅水、可压缩 NS 等下游设置，部分跨系统结果需要微调。
- **泛化与核心贡献**：不更新测试权重的 in-context 条件预测，强调对近似先验噪声的鲁棒性与查询输入灵活性。
- **局限**：同族 PDE 的条件预测与跨 PDE family 的 zero-shot 不是同一指标；需单独报告微调、先验依赖、长时间极端演化、守恒和预算敏感性。
- **published-v2**：相关度 **5/5** + 泛化 **3/3** + 方法证据 **1/2** = **9/10**。价值项保守打分，因为强泛化结论仍需更细的任务分层验证。

### 4. Topology-Preserving Neural Operator Learning via Hodge Decomposition

- **作者**：Dongzhe Zheng, Tao Zhong, Christine Allen-Blanchette；机构未独立核实。
- **状态 / venue / publisher**：**published** / ICML 2026 / PMLR 306，pp.164029–164060；**publication_date**：**2026-09-29**；正式 DOI：`null`。
- **正式链接**：[PMLR proceedings](https://proceedings.mlr.press/v306/zheng26aj.html)；**arXiv**：[2605.13834](https://arxiv.org/abs/2605.13834)，原 preprint，本次升级。
- **分类**：`published_category=operator`；附类 `enabling`；`foundation_model_level=general_pde_solver`；`selection_tier=core`。
- **方法 / 系统**：Hodge Spectral Duality (HSD) 基于离散微分形式和正交分解，把拓扑自由度交给结构保持空间，把可学习的局部几何动力学交给混合 Eulerian–Lagrangian 分支；在几何图和物理场算子任务上评价精度与物理不变量。
- **泛化与贡献**：构建一个有代数结构约束的可学习算子，降低拓扑模态与局部动力学模态相互干扰；适合比较 UPFM 的“参考物理核 + 可学习修正”的结构设计。
- **局限**：拓扑分解需要离散几何结构，训练/预处理成本需核算；不把图任务精度扩展宣称为任意三维工业复杂几何或零样本多 PDE 通用求解。
- **published-v2**：相关度 **4/5** + 泛化 **2/3** + 方法证据 **2/2** = **8/10**。

## 四、扩展论文（extended，3 篇）

### 5. Derivative-Informed Training of Neural Operators On-the-Fly via Sketched Tangent Consistency

- **作者**：Xinhan Yang, Lu Lu, Shancong Mou；机构未独立核实。
- **正式状态**：**accepted**，NeurIPS 2026，publisher NeurIPS；**publication_date/DOI**：`null` / `null`。
- **证据**：[NeurIPS 2026 官方 Downloads](https://neurips.cc/Downloads/2026)；**arXiv**：[2609.32797](https://arxiv.org/abs/2609.32797)（新正式身份）。
- **分类**：`published_category=enabling`，附类 `operator, pinn`；`foundation_model_level=enabling_method`。
- **贡献**：sTCL 以已知 PDE 的可微残差构造随机方向切向一致性约束，避免离线雅可比标签与庞大灵敏度数据；论文摘要涉及 Helmholtz、非线性扩散反应、Burgers、Allen–Cahn、Navier–Stokes。
- **局限 / extended 原因**：属优化与训练增强模块，不是独立可部署通用求解器；对于不定或鞍点算子需良好条件化，前提是可用的已知方程残差。
- **published-v2**：**3/5 + 2/3 + 2/2 = 7/10**。

### 6. TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs

- **作者**：Chen-Yang Dai, Che-Chia Chang, Te-Sheng Lin, Ming-Chih Lai, Chieh-Hsin Lai；机构未独立核实。
- **正式状态**：**published**，ICML 2026 / PMLR 306, pp.22358–22384；**publication_date**：2026-09-29；**DOI**：`null`。
- **证据**：[PMLR 正式论文](https://proceedings.mlr.press/v306/dai26a.html)；**arXiv**：[2601.20361](https://arxiv.org/abs/2601.20361)（新正式身份）。
- **分类**：`published_category=pinn`，附类 `enabling`；`foundation_model_level=enabling_method`。
- **方法**：以时间决定连续的网络参数轨迹 $\theta(t)$，使不同时间的空间表示能适配不同尺度的解结构，并用 Levenberg–Marquardt 优化 PDE 残差和初始/边界条件。论文报告在部分瞬态 PDE 基准比 PINN 提高相对误差和收敛效率。
- **局限 / extended 原因**：主要为单实例 PINN 表征与优化方法，需对每个问题训练，不等同于预训练后任意初值、方程和时间直接查询的统一解算子。
- **published-v2**：**3/5 + 1/3 + 2/2 = 6/10**。

### 7. OpInf-LLM: Parametric PDE Solving with LLMs via Operator Inference

- **作者**：Zhuoyuan Wang, Hanjiang Hu, Xiyu Deng, Saviz Mowlavi, Yorie Nakahira；机构未独立核实。
- **正式状态**：**accepted**，NeurIPS 2026，publisher NeurIPS；**publication_date/DOI**：`null` / `null`。
- **证据**：[NeurIPS 2026 官方 Downloads](https://neurips.cc/Downloads/2026)；**arXiv**：[2602.01493](https://arxiv.org/abs/2602.01493)（新正式身份）。
- **分类**：`published_category=surrogate`，附类 `enabling`；`foundation_model_level=surrogate_model`。
- **方法**：利用少量数值解训练低秩 operator-inference 模型，语言模型将用户的 PDE/参数描述转化为数值工具调用，通过低维 ODE 积分及 POD 解码完成参数化正向求解。论文介绍热、Burgers 与二维方腔流动等基准。
- **局限 / extended 原因**：实质依赖已覆盖问题族的 ROM 数据，LLM 是求解器编排接口而非自行学习可泛化的解算子；对于新耦合和复杂边界需额外数值验证。
- **published-v2**：**3/5 + 2/3 + 1/2 = 6/10**。

## 五、按 published_category 的归类

| 主类 key | 入选数 | 本期 |
|---|---:|---|
| `foundation_model` | 1 | PDE-PFN（core，正式接收） |
| `operator` | 3 | CoupledFlow、ECHO、Hodge（core） |
| `enabling` | 1 | sTCL（extended） |
| `pinn` | 1 | TINNs（extended） |
| `surrogate` | 1 | OpInf-LLM（extended） |
| `data` | 0 | 有相关数据与压缩机制，但无新的独立高价值正式数据集身份 |

按主类只计一次；不将跨类别附类重复记入总入选数。

## 六、Venue 覆盖、排除与正式状态界限

| Venue / 来源 | 本期核验与入选 | 说明 |
|---|---|---|
| NeurIPS 2026 官方 Downloads | 5 篇正式 **accepted** | CoupledFlow、ECHO、PDE-PFN、sTCL、OpInf-LLM；尚无正式 proceedings 证据，不得填 published 或出版日期 |
| ICML 2026 / PMLR 306 | 2 篇正式 **published** | Hodge、TINNs；出版日期按 PMLR 卷统一发布日期 **2026-09-29** |
| ICML 2026 / PMLR 306 其他 | 4 篇正式页面、**未入库** | Origo、MERLIN、ReViT、MiSe-GNN 缺核实稳定 arXiv/DOI，保留 pending |
| ICLR 2026 workshop | 1 篇排除 | *Physics-informed fine-tuning of foundation models for PDEs*（arXiv:2603.15431）存在 ICLR workshop 线索，但不足以证明主会正式发表，不能误收 |
| Nature Machine Intelligence / Nature 系列 | 定向核查、无新增入选 | 本次检索到的 *Deep neural operator for free boundary problems* 和 *Principled approaches for extending neural architectures...* 已在注册表中，避免重复 |
| JCP、CMAME、SISC、MLST、Physics of Plasmas、Nuclear Fusion | 关键词/期刊检索，未新增高置信身份 | 不能把单次定向搜索说成逐篇全量；部分 Elsevier 详情页受限，本次覆盖保持 degraded |

**出版日期纪律**：2026 年 NeurIPS 的会议名单不代表已出版；ICML 2026 在 7 月举办但 PMLR 卷在 9 月在线发布。不可用 arXiv 投稿日期、网页抓取时间、DOI 索引日期取代正式发表日期。

## 七、正式发表状态更新（既有预印本）

| 论文 | 原统一表状态 | 本期已核验证据 | DOI | publication_date |
|---|---|---|---|---|
| [arXiv:2605.13834](https://arxiv.org/abs/2605.13834) Hodge | preprint | [ICML 2026 PMLR 正式发表](https://proceedings.mlr.press/v306/zheng26aj.html) | null | 2026-09-29 |
| [arXiv:2610.13334](https://arxiv.org/abs/2610.13334) PDE-PFN | preprint / W47 pending | [NeurIPS 2026 官方正式接收名单](https://neurips.cc/Downloads/2026) | null | null（尚未正式出版） |
| [arXiv:2512.04974](https://arxiv.org/abs/2512.04974) ECHO | preprint | [NeurIPS 2026 官方正式接收名单](https://neurips.cc/Downloads/2026) | null | null（尚未正式出版） |

其他四篇作为**新正式身份**而不是上述已有记录的状态修正。本轮不覆盖任何已有高置信、互相冲突的 DOI/venue/date；历史 8 项冲突仍按 pending 审计。

## 八、待人工确认与来源限制

| 候选 | 已有证据 / 缺口 | 处理 |
|---|---|---|
| [Origo](https://proceedings.mlr.press/v306/sun26aa.html) | PMLR 306 已收录，但未获得可靠 arXiv ID 或正式 DOI | 按作者与全标题补稳定 ID；相关性高，暂不绕过事件契约写标题-only |
| [MERLIN](https://proceedings.mlr.press/v306/lu26u.html) | 正式会议页面存在，未能取得稳定论文 ID | 对齐作者与正式版本 |
| [ReViT](https://proceedings.mlr.press/v306/wei26p.html) | 正式会议页面，但与同名其他 ReViT / REViT 论文存在混淆风险 | 必须核对全标题、作者再入库 |
| [MiSe-GNN](https://proceedings.mlr.press/v306/nguyen26a.html) | 方法名，正式标题是 *Error-Driven Graph Augmentation for Mesh-Based PDE Surrogates*；未取得可靠稳定 ID | 按正式标题与作者确认 arXiv/DOI |
 
上期 PDE-PFN 的“是否正式接收”疑问**本期已经解决**，因此不再计入 pending。另有 Elsevier 个别详细页访问错误，正式来源不足的线索不强行入库。

## 九、面向 UPFM 的可复现实验建议

**第一组**：以 CoupledFlow 为对照，将基础算子专家独立候选与耦合主干输出放在同一数据、相同算力、相同预测时域条件下，单独测试源项、全场耦合和界面耦合；不要把物理时间与流匹配采样时间混淆。

**第二组**：以 ECHO 的高压缩完整轨迹片段与 UPFM 连续时间查询为两种不同计算范式，记录 NRMSE、频谱误差、梯度误差、质量/动量/能量误差和 GPU 秒数，按非周期边界、冲击波、相变、复杂几何分组。

**第三组**：用 Hodge 的拓扑先验、TINNs 的时间变权和 sTCL 的物理导数一致性做独立消融，分别计量结构先验维护成本、时间条件参数开销与高阶自动微分成本。

## 十、可审计记录

- 7 条正式状态事件：`metadata/inbox/2026-11-23.jsonl`。
- 真实来源查询、入选/排除与降级：`metadata/runs/published-2026-W48.json`。
- 统一论文表、正式发表兼容表和 README **必须由仓库 `python scripts/papertrack.py build` 生成**；本周报不是主表的替代品。
- 新正式身份不等于首次发表日期，历史预印本升级不计为新 arXiv 发现。

*数据判断截止 2026-11-23 UTC。以上方法/性能判断基于本期检查到的官方摘要和匹配版本，不代表已独立复现实验。*
