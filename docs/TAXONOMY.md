# 研究方向分类与评分规范 — PDE 基座大模型（PDE Foundation Models）

> 本文件是**日报路由例程（daily routine）唯一的方向 / 评分事实来源**。
> 更新方向定义、关键词库或评分标准时，只需修改本文件，路由例程会以此为准。
>
> **主题转向说明**：自 2026-07-22 起，本仓库研究重心由"AI 求解 PDE × 激光等离子体/EUV"
> 转向 **PDE 基座大模型（PDE Foundation Models）** —— 即在多种物理/多类 PDE 上
> 大规模预训练、可跨方程/跨几何/跨分辨率迁移的通用科学计算大模型。

---

## 一、四大追踪方向

> A/B/C 为 PDE 基座大模型核心方向；D 为旧方向"AI 求解 PDE"的保留延续。

### 方向 A：基座架构与预训练（Architectures & Pretraining）

关注"如何构建并训练一个通用 PDE 大模型"的方法层工作。

涵盖：
- 主干架构：Transformer / 神经算子（FNO、Transolver 等）/ 状态空间模型 / 混合架构在大规模 PDE 建模中的应用
- 物理场的 token 化 / patch 化 / 表征学习
- 多物理、多任务预训练目标：自回归 rollout、掩码/去噪重建、流匹配/扩散式预训练
- 上下文算子学习（in-context operator learning）、以 PDE 元信息/符号形式为条件的建模
- 规模化训练技巧（并行、混合精度、长时程稳定性）

关键词库（搜索用）：
- `site:arxiv.org PDE foundation model`
- `site:arxiv.org multiple physics pretraining`
- `site:arxiv.org foundation model partial differential equations pretraining`
- `site:arxiv.org transformer neural operator large-scale PDE`
- `site:arxiv.org in-context operator learning`
- `site:arxiv.org pretrained model physics simulation transformer`
- `site:arxiv.org universal PDE solver transformer`

### 方向 B：数据、基准与缩放规律（Data, Benchmarks & Scaling Laws）

关注支撑基座模型的"数据与评测基础设施"。

涵盖：
- 大规模多物理数据集（The Well、PDEBench、PDEArena、PDEGym 等）
- 统一评测协议、排行榜、跨数据集泛化度量
- 科学基座模型的缩放规律（数据/参数/算力）
- 表征/tokenizer 消融、数据配比与课程策略

关键词库（搜索用）：
- `site:arxiv.org PDE benchmark dataset machine learning`
- `site:arxiv.org large-scale physics dataset foundation model`
- `site:arxiv.org scaling laws scientific machine learning`
- `site:arxiv.org neural operator benchmark evaluation`
- `site:arxiv.org multi-physics dataset pretraining PDE`
- `site:arxiv.org The Well PDEBench PDEArena`

### 方向 C：下游泛化与适配（Generalization & Adaptation）

关注基座模型"训练之后如何用"—— 迁移、微调与泛化能力。

涵盖：
- 零样本/少样本迁移到未见 PDE、几何、边界条件、分辨率
- 微调 / 参数高效微调（LoRA/adapter）用于物理任务
- 上下文自适应、测试时适配
- 分布外鲁棒性；基座先验与经典数值求解器的耦合（混合求解）

关键词库（搜索用）：
- `site:arxiv.org zero-shot PDE neural operator generalization`
- `site:arxiv.org fine-tuning foundation model PDE downstream`
- `site:arxiv.org few-shot operator learning transfer`
- `site:arxiv.org out-of-distribution generalization neural PDE`
- `site:arxiv.org parameter-efficient fine-tuning physics model`
- `site:arxiv.org foundation model transfer new PDE geometry`

### 方向 D：AI 求解 PDE（通用，保留方向）

延续旧研究方向"AI 求解 PDE"的持续追踪。关注**通用的 AI/ML 求解 PDE 方法**，即使其
尚未具备"基座模型"的多物理/规模化属性，只要方法本身有代表性或对基座模型有启发即纳入。

涵盖：
- 神经算子（FNO、DeepONet、Transolver 等）求解单类或参数化 PDE
- 物理信息神经网络（PINN）及其训练/优化改进
- 算子学习理论、神经 PDE 求解器、混合数值-学习方法
- 生成式/扩散式 PDE 求解

关键词库（搜索用）：
- `site:arxiv.org neural operator PDE`
- `site:arxiv.org physics-informed neural network`
- `site:arxiv.org scientific machine learning PDE`
- `site:arxiv.org operator learning partial differential equation`
- `site:arxiv.org neural PDE solver`

> **A 与 D 的边界**：面向多物理/跨方程/规模化预训练的工作归 **A**（基座）；
> 面向单类或参数化 PDE 的通用求解方法归 **D**（通用求解）。二者可交叉标注，主方向写在前。

---

## 二、评分标准（满分 10 分，入选阈值 ≥ 7）

| 维度 | 分值 | 说明 |
|------|------|------|
| **主题相关度** | 0–4 | 与四大方向的契合程度：A/B/C 看"PDE 基座大模型"契合度，D 看"AI 求解 PDE 通用方法"的代表性。 |
| **基座特性 / 通用性** | 0–3 | 对 A/B/C：多物理/多任务预训练、跨方程/几何/分辨率可迁移、规模化证据；对 D：方法的通用性、可迁移性、或对基座模型的启发价值。 |
| **创新性** | 0–3 | 是否提出新架构、新预训练范式、新基准/数据集，或新理论（泛化界、缩放律等）。 |

评分要点：
- 只保留 **总分 ≥ 7** 的论文；数量不设下限，0 篇也正常，**绝不用已推送过的论文凑数**。
- 未达阈值但有价值的工作，可放入"附：本期未入选但值得关注的论文"。
- **优先级**：A/B/C（基座大模型主线）为核心；D（通用 AI 求解 PDE）为保留方向，
  入选门槛一致，但同期名额紧张时优先呈现 A/B/C。
- 纯粹的单方程 PINN/神经算子求解器若无任何通用性或启发价值，通常 ≤ 6 分。

---

## 三、方向标签写法

日报中每篇论文的"分类标签"字段写为：`[A/B/C/D 方向] | [arXiv 分类]`，例如 `A | cs.LG`。
一篇论文可跨方向，用 `A/D` 等表示，主方向写在前。

四大方向速查：
- **A** 基座架构与预训练
- **B** 数据、基准与缩放规律
- **C** 下游泛化与适配
- **D** AI 求解 PDE（通用，保留方向）
