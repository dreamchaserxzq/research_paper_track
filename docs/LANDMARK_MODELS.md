# PDE 基座大模型 · 里程碑工作清单（Living Survey）

> 本文件是 PDE 基座大模型领域**代表性工作的持续维护清单**，供路由例程评分时作横向对照，
> 也是新读者快速进入该领域的索引。
>
> **维护规则**：路由例程每期若发现应纳入清单的新里程碑工作（新基座模型 / 新基准 /
> 新缩放律研究），在对应分区追加一行；已有条目如状态更新（如正式发表）可就地修订。
> **arXiv ID 若标注"待核验"，应在下一次维护时用 WebSearch 确认后回填，切勿臆造。**

图例：🏗️ 基座模型 / 架构　📊 数据集 · 基准　📈 缩放律 · 理论

---

## A. 基座模型与架构

| 名称 | 一句话定位 | arXiv | 方向 |
|------|-----------|-------|------|
| 🏗️ DeepONet | 算子学习开山之作，学习函数到函数的映射 | 1910.03193 | A |
| 🏗️ OmniArch | 首个多尺度/多物理科学计算基础模型原型，PDEBench上1D-2D-3D统一预训练+PDE-Aligner物理知情微调（2024年2月，ICML2025接收） | 2402.16014 | A |
| 🏗️ FNO（Fourier Neural Operator） | 谱域算子学习，众多基座模型的主干 | 2010.08895 | A |
| 🏗️ PROSE-PDE | 双模态（数值+符号）多算子学习基座模型，支持跨方程外推 | 2404.12355 | A |
| 🏗️ ICON（In-Context Operator Networks） | 以上下文示例进行零样本算子推理 | 2304.07993 | A/C |
| 🏗️ MPP（Multiple Physics Pretraining） | Polymathic AI，多物理自回归预训练 | 2310.02994 | A |
| 🏗️ UPT（Universal Physics Transformers） | 统一网格/粒子表示的物理 Transformer | 2402.12365 | A |
| 🏗️ PDEformer-1 | 以符号 PDE 形式为条件的通用求解器 | 2402.12652 | A |
| 🏗️ MAE-PDE（Masked Autoencoders are PDE Learners） | 掩码自编码预训练用于 PDE 表征 | 2403.17728 | A |
| 🏗️ UPS | 跨模态适配高效构建 PDE 求解基座（FNO-Transformer，暖启动自 LLM） | 2403.07187 | A |
| 🏗️ DPOT | 自回归去噪算子 Transformer，大规模 PDE 预训练 | 2403.03542 | A |
| 🏗️ Unisolver | PDE 条件 Transformer 迈向通用神经 PDE 求解器 | 2405.17527 | A |
| 🏗️ Poseidon | 面向 PDE 的高效基座模型，强调样本效率 | 2405.19101 | A |
| 🏗️ PDEformer-2 | 二维通用 PDE 基础模型，40TB 预训练 | 2507.15409 | A |
| 🏗️ Walrus | 连续体动力学基础模型（含等离子体预训练场景） | 2511.15684 | A/C |
| 🏗️ GPhyT（General Physics Transformer） | 1.8TB多物理预训练，无需显式PDE条件+上下文零样本泛化未见系统 | 2509.13805 | A |
| 🏗️ MORPH | LANL模态无关自回归基座模型，统一处理1D–3D、标量/向量混合场异构数据 | 2509.21670 | A/C |
| 🏗️ HyCOP | 模块化混合组合算子：数值子求解器+可学习闭合查询条件化组合，可解释+跨基准OOD泛化 | 2605.00820 | A/D |
| 🏗️ HyPINO | 超网络生成PINN的多物理零样本算子，无需微调超越Poseidon/PINO基线 | 2509.05117 | A/C |
| 🏗️ PDE-FM | Mamba状态空间主干+谱-空间联合tokenization，The Well 12异质多物理数据集一次预训练免改架构迁移，6/12领域SOTA（IBM Research） | 2511.21861 | A |
| 🏗️ VICON | 视觉Transformer化ICON，patch级上下文算子学习，多物理流体基准大幅超越DPOT/MPP（UCLA/NUS/UCSD，TMLR2026） | 2411.16063 | A/C |
| 🏗️ XNN（Axial Neural Networks） | 维度无关轴向神经网络，解决物理基座模型跨维度预训练效率瓶颈（KAIST/NYU，NeurIPS2025 Spotlight） | 2510.13665 | A |
| 🏗️ BCAT | 分块因果Transformer流体动力学PDE基座模型，整帧自回归预测+跨几何/参数规模化预训练（UCLA） | 2501.18972 | A |
| 🏗️ Overtone | 循环patch调制架构无关模块，赋予Transformer物理仿真基座模型推理期算力弹性+长时程谐波误差抑制，The Well多物理基准验证（Polymathic AI/Flatiron Institute） | 2507.09264 | A |

## B. 数据集与基准

| 名称 | 一句话定位 | arXiv | 方向 |
|------|-----------|-------|------|
| 📊 PDEArena | 多时空尺度广义 PDE 建模基准（Gupta & Brandstetter） | 2209.15616 | B |
| 📊 PDEBench | 多物理 PDE 基准与数据集 | 2210.07182 | B |
| 📊 The Well | Polymathic AI，15TB / 16 数据集多物理仿真集合（NeurIPS 2024） | 2412.00568 | B |
| 📊 Physics-FM 泛化基准 | 面向物理基座模型的偏差感知泛化基准（跨物理区间/分布偏移） | 2605.29283 | B/C |
| 📊 RealPDEBench | 首个真实世界-仿真配对物理系统基准，直击sim-to-real鸿沟（Westlake，ICLR 2026 Oral） | 2601.01829 | B |
| 📊 SPDEBench | 首个随机PDE（Φ⁴/波动/N-S/KdV）统一大型基准，含噪声采样误差与奇异SPDE重整化处理 | 2505.18511 | B |
| 📊 REALM | 首个真实工业级时空多物理反应流神经代理基准（高马赫反应流/推进发动机/火灾），揭示维度-刚性-网格不规则性缩放壁垒 | 2512.18595 | B |

## C. 缩放规律与理论

| 名称 | 一句话定位 | arXiv | 方向 |
|------|-----------|-------|------|
| 📈 Practical Scaling Laws | 数据受限/多轮训练场景下的闭式缩放律扩展，覆盖FNO等科学ML架构族 | 2605.09189 | B |

---

**说明**：本清单为主题转向（2026-07-22）时的初始种子，覆盖公认里程碑；所有 arXiv ID 均已
经 WebSearch 核验（缩放律分区留待后续补充）。清单不追求穷尽，只收录对"PDE 基座大模型"
主线有代表性的工作。
