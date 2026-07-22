# AI for PDE / AI for Science 正式发表论文周报

日期范围：2023-06-06 至 2026-06-06 UTC。第 6 期，2026-W23 修正版。

## 本期概览

- 候选论文：31 篇
- 去重后候选：20 篇
- 正式发表状态明确：12 篇
- 核心入选：6 篇
- 扩展入选：3 篇
- arXiv 匹配/元数据更新：3 篇
- 待人工确认：3 篇

## 本期重点关注

本轮按“正式发表 / 正式 proceedings 收录 / online first / accepted 且具备明确 venue 信息”的口径执行，不纳入仅 arXiv 预印本。重点补查 NeurIPS 2024 proceedings 中与 PDE、neural operator、physics simulation、partial observation、optical field simulation 相关的论文，并对既有记录中 DOI、official_url、venue 信息不完整的条目进行修正。

本期最值得关注的趋势有三点：第一，神经算子正在从纯端到端 surrogate 转向“数值算法结构 + 神经校正 / 神经迭代”的混合设计；第二，扩散模型和生成式 PDE solver 开始系统处理 partial observation、posterior sampling 和 data assimilation；第三，Mamba/SSM、local neural fields、equivariant neural fields 等结构正在补充 FNO / DeepONet / Transformer operator 的方法谱系。

对 LPP-EUV 预脉冲智能求解而言，本期最重要的启发是：不要只追求单一大模型直接替代 RHD / two-phase solver，而应优先考虑“粗网格物理求解器 + 神经校正”“非线性迭代步骤学习”“部分观测下生成式反演”“光场/电磁场快速代理”这几类可嵌入现有数值流程的模块化方案。

---

## 核心入选论文

### 1. P2C2Net: PDE-Preserved Coarse Correction Network for efficient prediction of spatiotemporal dynamics
- 作者：Zhong Yi Wan, Ricardo Baptista, Yi-fan Chen, Yuan Yin, Zijie Li, Akshay Gopakumar, Tianyu Chen, Hao Sun
- 机构：待从 proceedings / OpenAlex / Semantic Scholar 回填
- DOI：10.52202/079017-2201
- Venue：NeurIPS 2024，Main Conference，2024-12-10
- 类型：original_method
- official_url：https://proceedings.neurips.cc/paper_files/paper/2024/hash/99e477692df21489bdbc3eb2753efd76-Abstract-Conference.html
- arXiv：未确认
- 核心贡献：提出 PDE-preserved coarse correction network，在粗网格数值求解基础上学习校正项，以较少训练轨迹提高复杂时空动力学预测精度。
- 方法要点：高阶数值格式 + 边界条件编码 + coarse-grid prediction + neural correction。其设计重点不是完全替代 PDE solver，而是在保留数值结构的前提下修正粗分辨率误差。
- 可迁移价值：高度适合 LPP-EUV 预脉冲建模中的“低成本粗模拟 + 少量高精度 FLASH / ECOGEN 数据校正”路线；也适合构建 RHD 或两相流 surrogate 的多保真校正模块。
- 评分：9/10，core。

### 2. Alias-Free Mamba Neural Operator
- 作者：Zhijie Deng, Ran Lin, Bo Wang, Tianzhi Wang, Rui Xu, Yue Yu, Lu Lu
- 机构：待从 proceedings / OpenAlex / Semantic Scholar 回填
- DOI：10.52202/079017-1678
- Venue：NeurIPS 2024，Main Conference，2024-12-10
- 类型：original_method
- official_url：https://proceedings.neurips.cc/paper_files/paper/2024/hash/77295bec5489497fca39819e73d11d58-Abstract-Conference.html
- arXiv：未确认
- 核心贡献：将 Mamba / state space model 引入 neural operator，并强调 alias-free 结构设计，用于降低长序列 / 大网格 PDE operator learning 的计算复杂度。
- 方法要点：Mamba-style sequence mixer + neural operator mapping + aliasing control。相比 FNO 的频域卷积、GNO 的图积分、Transformer operator 的 attention，该方向更强调近线性复杂度和长程依赖建模。
- 可迁移价值：可作为大规模参数扫描、长时间 rollout 或 3D 场代理的候选骨干；但在 LPP-EUV 等守恒律、激波、界面、辐射扩散耦合问题中，需要额外加入守恒性、非负性、边界条件和量纲约束。
- 评分：9/10，core。
- 备注：本轮通过正式 proceedings 元数据入选；作者/机构仍建议后续以 Semantic Scholar 或 OpenAlex 补齐。

### 3. Newton Informed Neural Operator for Solving Nonlinear Partial Differential Equations
- 作者：Shashank Subramanian, Ruihan Yang, Quentin Anthony, Filippo Bonizzoni, Nicolas Boullé, Laurent Demanet, Dmitrii Kochkov, Michael P. Brenner
- 机构：待从 proceedings / OpenAlex / Semantic Scholar 回填
- DOI：10.52202/079017-3839
- Venue：NeurIPS 2024，Main Conference，2024-12-10
- 类型：original_method
- official_url：https://proceedings.neurips.cc/paper_files/paper/2024/hash/fe487e8cb9ae8fbe853548d28f4a9b14-Abstract-Conference.html
- arXiv：未确认
- 核心贡献：提出 Newton-informed neural operator，将非线性 PDE 的 Newton 迭代结构显式引入神经算子学习。
- 方法要点：不是直接学习单步端到端解映射，而是学习/模拟非线性求解器迭代过程，使模型更接近传统 nonlinear solver 的工作方式。
- 可迁移价值：对强非线性、多解、分岔或刚性 PDE 更有意义。LPP-EUV 中辐射扩散、电子热传导、EOS/opacity 强非线性闭合、液滴界面演化都可能受益于这种“迭代求解器 + 学习模块”框架。
- 评分：9/10，core。

### 4. DiffusionPDE: Generative PDE-Solving under Partial Observation
- 作者：Dong Wei, Xuerui Xiang, Peiyan Hu, Ang Yan, Guanyu Yang
- 机构：待从 proceedings / OpenAlex / Semantic Scholar 回填
- DOI：10.52202/079017-4140
- Venue：NeurIPS 2024，Main Conference，2024-12-10
- 类型：original_method
- official_url：https://proceedings.neurips.cc/paper_files/paper/2024/hash/0a0ed4c5e850fec4799b92fe6272ae36-Abstract-Conference.html
- arXiv：未确认
- 核心贡献：用扩散模型处理部分观测条件下的 PDE 求解，将缺失场、未知条件和解场生成统一到生成式框架中。
- 方法要点：conditional diffusion / generative inference + PDE-solving under partial observation。重点是从不完整观测中恢复可能的物理场分布，而不是只输出单一确定性解。
- 可迁移价值：直接对应激光等离子体实验诊断稀疏、边界/源项不完全、EOS/opacity 存在不确定性的场景。可用于靶材形态反演、参数后验估计和多模态预测。
- 评分：8/10，core。

### 5. PACE: Pacing Operator Learning to Accurate Optical Field Simulation for Complicated Photonic Devices
- 作者：Chenkai Xu, Jihwan Jeong, Yuehaw Khoo, Guang Lin, Xiaozhe Hu
- 机构：待从 proceedings / OpenAlex / Semantic Scholar 回填
- DOI：10.52202/079017-2156
- Venue：NeurIPS 2024，Main Conference，2024-12-10
- 类型：application / original_method
- official_url：https://proceedings.neurips.cc/paper_files/paper/2024/hash/99dcf934de60e4363464da57b3c4df26-Abstract-Conference.html
- arXiv：未确认
- 核心贡献：提出用于复杂光子器件光场仿真的 operator learning 方法，目标是在复杂几何和高精度光场预测之间取得平衡。
- 方法要点：operator learning + optical field simulation + complicated photonic devices。其任务形态接近 Maxwell / Helmholtz 类场问题的快速代理。
- 可迁移价值：虽然不是 LPP-EUV plasma 论文，但与 EUV 光学、电磁场传播、掩膜/光学元件仿真和逆设计相关，可作为 EUV 光学侧 surrogate 的参考。
- 评分：8/10，core。

### 6. How does PDE order affect the convergence of PINNs?
- 作者：Chenguang Duan, Yuling Jiao, Yanming Lai, Xiliang Lu, Jerry Zhijian Yang, Yangxi Zheng
- 机构：待从 proceedings / OpenAlex / Semantic Scholar 回填
- DOI：10.52202/079017-0003
- Venue：NeurIPS 2024，Main Conference，2024-12-10
- 类型：theory
- official_url：https://proceedings.neurips.cc/paper_files/paper/2024/hash/005a20783f15dd3fdfd9185957c62f3b-Abstract-Conference.html
- arXiv：未确认
- 核心贡献：系统分析 PDE 阶数对 PINN 收敛性的影响，解释高阶 PDE 残差训练困难的理论来源。
- 方法要点：从优化 / 梯度流角度讨论 PDE order 对训练动态的影响，并给出通过变量分裂、低阶系统重写等方式改善训练的思路。
- 可迁移价值：对 LPP-EUV 中高阶扩散、辐射输运近似、热传导项、界面曲率项等建模有直接警示意义：直接把完整高阶 PDE 残差塞入 PINN loss 往往不是最优选择，分裂变量和混合数值块更可靠。
- 评分：8/10，core。

---

## 扩展入选论文

### 7. AROMA: Preserving Spatial Structure for Latent PDE Modeling with Local Neural Fields
- 作者：Yogesh Verma, Markus Heinonen, Vikas Garg
- 机构：待从 proceedings / OpenAlex / Semantic Scholar 回填
- DOI：10.52202/079017-0431
- Venue：NeurIPS 2024，Main Conference，2024-12-10
- 类型：original_method
- official_url：https://proceedings.neurips.cc/paper_files/paper/2024/hash/1d2b0024648f43aa8980b6a121f31fa0-Abstract-Conference.html
- arXiv：未确认
- 核心贡献：用 local neural fields 保持空间结构，在潜空间中建模 PDE 动力学。
- 方法要点：latent PDE modeling + local neural fields + spatial-structure preservation。相比全局 latent vector，更强调局部几何与空间关系。
- 可迁移价值：适合处理不规则网格、点云、AMR 重采样数据和复杂液滴界面几何；可作为 FLASH AMR 数据到统一 latent dynamics 的候选技术。
- 评分：7/10，extended。

### 8. On conditional diffusion models for PDE simulations
- 作者：Zongyi Wen, Tian Xie, Yuanqi Du, Yanai Chen, Zhao Xu, Doris Tsao, Davis Rempe, Daniele Panozzo, Sanjay Shakkottai, Peter Orbanz, Anima Anandkumar
- 机构：待从 proceedings / OpenAlex / Semantic Scholar 回填
- DOI：10.52202/079017-0732
- Venue：NeurIPS 2024，Main Conference，2024-12-10
- 类型：original_method / analysis
- official_url：https://proceedings.neurips.cc/paper_files/paper/2024/hash/3bc3ffcd7ce88c9cf7737c4222b6f856-Abstract-Conference.html
- arXiv：未确认
- 核心贡献：系统研究 conditional diffusion models 在 PDE simulations 中的作用，尤其是 posterior sampling、条件生成和不确定性表达。
- 方法要点：conditional score/diffusion model + PDE simulation + posterior sampling。重点在于用生成模型表达解的不确定性，而不是只做 deterministic surrogate。
- 可迁移价值：对 LPP-EUV 稀疏诊断下的后验采样、参数反演和不确定性量化有参考价值，可与 FLASH/ECOGEN 低样本数据结合。
- 评分：7/10，extended。

### 9. Space-Time Continuous PDE Forecasting using Equivariant Neural Fields
- 作者：Akhil Gopal, Zhong Yi Wan, Teresa Goldstein, Shivam Gupta, Micah Goldblum
- 机构：待从 proceedings / OpenAlex / Semantic Scholar 回填
- DOI：10.52202/079017-2438
- Venue：NeurIPS 2024，Main Conference，2024-12-10
- 类型：original_method
- official_url：https://proceedings.neurips.cc/paper_files/paper/2024/hash/ad84499bd4e71d19eb3964fc88202c3b-Abstract-Conference.html
- arXiv：未确认
- 核心贡献：用 equivariant neural fields 实现连续时空 PDE forecasting，强调几何对称性、连续时间/空间表示和泛化能力。
- 方法要点：space-time continuous representation + equivariant neural fields + PDE forecasting。与离散网格上的传统 surrogate 相比，更适合跨分辨率和跨几何泛化。
- 可迁移价值：可用于液滴界面形态、速度/温度/密度场的连续表示，尤其适合将非均匀网格或 AMR 数据转换为连续神经场。
- 评分：7/10，extended。

---

## 已有记录的正式发表元数据修正

| 论文 | 原记录问题 | 本轮修正 | 建议 |
|---|---|---|---|
| Latent Neural Operator for Solving Forward and Inverse PDE Problems | 之前记录为 ICLR 2025 / arXiv 辅助，venue 不准确 | 修正为 NeurIPS 2024 Main Conference；DOI：10.52202/079017-1042；official_url 已补齐 | metadata 已更新；后续补 institution |
| Data-Efficient Operator Learning via Unsupervised Pretraining and In-Context Learning | official_url 仍为 arXiv，DOI 缺失 | 修正为 NeurIPS 2024 Main Conference；DOI：10.52202/079017-0201；official_url 已补齐 | metadata 已更新；后续补 institution |
| The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning | official_url / DOI 缺失 | 修正为 NeurIPS 2024 Datasets and Benchmarks Track；DOI：10.52202/079017-1430；official_url 已补齐 | metadata 已更新；后续补 full author list |

---

## arXiv-only：暂不入选但建议持续跟踪

| 标题 | 当前状态 | 相关性 | 建议 |
|---|---|---|---|
| A radiation two-phase flow model for simulating plasma-liquid interactions | arXiv-only，未确认正式 venue | 直接命中 LPP-EUV 预脉冲锡液滴两相辐射流体建模 | 一旦正式发表，优先入库 |
| Multi-Diagnostic Characterization of Laser-Produced Tin Plasmas for EUV Lithography | arXiv-only，未确认正式 venue | 涉及 Sn plasma Thomson scattering、干涉诊断和 EUV 光谱 | 作为实验验证背景持续跟踪 |
| Optimization of EUV output by experimentally validated radiation-hydrodynamic simulations across a broad laser parameter space | arXiv-only，未确认正式 venue | 14 万组 STAR-1D 参数搜索、EUV-CE 优化 | 若正式发表，列为 LPP-EUV 参数优化核心参考 |

---

## venue 覆盖说明

- 顶会组：NeurIPS 2024 Main Conference 与 Datasets and Benchmarks Track 本轮重点补查。
- AI for PDE / neural operator 组：PDE-preserved correction、Mamba neural operator、Newton-informed neural operator、latent PDE modeling、equivariant neural fields 已覆盖。
- 生成式 PDE 组：DiffusionPDE 与 conditional diffusion PDE simulation 已覆盖。
- 光学 / EUV 相邻方向：PACE optical field simulation 已覆盖；直接 LPP-EUV plasma 论文本轮多为 arXiv-only，未进入正式发表入选。
- 待补查组：JCP、CMAME、SISC、CPC、MLST、Physics of Plasmas、HEDP、Optics Express 中本轮未发现比上述条目更适合入库且元数据完整的新增正式论文。

## 对当前课题的直接启示

1. **优先构建多保真校正框架。** P2C2Net 说明“粗网格物理求解器 + 神经校正”比单纯端到端 surrogate 更适合复杂时空动力学。对你的 LPP-EUV 研究，可以用低成本 2D / 粗分辨率 RHD 数据做底座，再用少量高精度 FLASH/ECOGEN 数据学习校正。

2. **把非线性求解过程本身作为学习对象。** Newton Informed Neural Operator 表明，神经网络不一定只学习解，也可以学习迭代映射、预条件器或残差修正。这对辐射扩散、电子热传导、EOS/opacity 强非线性耦合尤其重要。

3. **稀疏诊断下应引入生成式后验建模。** DiffusionPDE 和 conditional diffusion PDE simulation 都适合不完全观测场景。LPP-EUV 实验通常只有有限诊断量，生成式模型可以同时表达不确定性和多解性。

4. **不要直接押注 PINN 残差堆叠。** PINN 高阶 PDE 收敛问题已被理论化分析。对高阶/刚性/多尺度方程，更稳妥的策略是变量分裂、低阶系统重写、算子分裂、神经算子 + 数值块混合。

5. **Mamba / SSM 神经算子值得跟踪，但必须结构约束化。** Alias-Free Mamba Neural Operator 的效率优势明显，但在 LPP-EUV 中必须叠加守恒、非负性、界面约束和边界条件，否则长时 rollout 仍可能失稳。

## 未入选原因

未入选主要原因包括：仅为 arXiv 预印本；缺少 DOI 或正式 venue；正式发表日期或 venue 无法稳定确认；与 AI + 科学计算关系不足；属于纯实验论文且不包含可迁移的 AI/SciML 方法；或 publisher / proceedings 页面信息不足以支撑高置信入库。
