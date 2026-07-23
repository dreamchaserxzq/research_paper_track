# AI for PDE 论文自动追踪系统

> 计算物理 × 科学机器学习交叉领域的每日 arXiv 论文追踪，由 Claude Code Routine 自动驱动。

> **📌 重点检索方向变更（2026-07-22）**
> 当前重点已聚焦到 **PDE 基座大模型（PDE Foundation Models）** ——
> 即在多种物理 / 多类 PDE 上大规模预训练、可跨方程 / 跨几何 / 跨分辨率迁移的通用科学计算大模型；
> 同时保留对整个"AI 求解 PDE"大方向的持续追踪（方向 D）。
> 2026-07-22 之前的日报、周报与历史摘要已整体归档至
> [`digests/archive-ai-for-pde/`](digests/archive-ai-for-pde/)，作为旧方向成果保留，不再重写。

## 项目简介

本项目通过部署在 Anthropic 云端的定时 Agent，每日自动检索 arXiv 最新论文，重点覆盖以下四个方向：

| 方向 | 关键词覆盖 |
|------|----------|
| **A：基座架构与预训练** | Foundation Model for PDE、Multiple Physics Pretraining、In-context Operator Learning、大规模 Transformer/神经算子主干 |
| **B：数据、基准与缩放规律** | The Well、PDEBench、PDEArena、多物理数据集、科学基座模型 Scaling Laws |
| **C：下游泛化与适配** | 零/少样本迁移、微调/PEFT、跨方程/几何/分辨率泛化、基座先验 + 经典求解器耦合 |
| **D：AI 求解 PDE** | Neural Operator、PINN、DeepONet、Operator Learning、Neural PDE Solver、代理模型（Surrogate Model）、数据生成与生成式求解、主动学习、可微分/混合数值方法等整个 AI-for-PDE 大方向 |

> A/B/C 为 PDE 基座大模型核心方向；D 覆盖除基座模型以外的整个"AI 求解 PDE"大方向。
> 方向定义、关键词库与评分标准的**唯一事实来源**是 [`docs/TAXONOMY.md`](docs/TAXONOMY.md)。

## 工作流程

```
每日 UTC 01:00（北京时间 09:00）
        │
        ▼
  读取 docs/TAXONOMY.md（方向/关键词/评分）+ seen_papers.txt（去重集）
        │
        ▼
  WebSearch 检索 48h 内新论文（三方向并行）
        │
        ▼
  去重（跳过 seen_papers.txt 中已有 ID）
        │
        ▼
  10 分制评分筛选（≥ 7 分入选，数量不设下限）
        │
        ▼
  生成中文摘要报告（Markdown 格式）
        │
        ▼
  提交到仓库（日报文件 + seen_papers.txt + run_log.md + README）
```

## 仓库结构

| 路径 | 说明 |
|------|------|
| `docs/TAXONOMY.md` | **日报**方向定义 + 关键词库 + 评分标准（日报例程的事实来源） |
| `docs/PUBLISHED_CRITERIA.md` | **周报**正式发表判定 + venue + 分类 + 评分（周报例程的事实来源） |
| `docs/LANDMARK_MODELS.md` | PDE 基座大模型里程碑工作清单（持续维护的领域索引） |
| `docs/ROUTINE.md` | 日报路由例程提示词的版本化副本 |
| `docs/ROUTINE_PUBLISHED.md` | 周报路由例程提示词的版本化副本 |
| `docs/ROUTINE_STATUS_UPDATE.md` | 正式发表状态回填例程提示词的版本化副本 |
| `digests/PDE-FM-日报-YYYYMMDD.md` | 每日论文摘要报告（2026-07-22 起的新命名） |
| `digests/published/AI-for-PDE-正式发表周报-YYYY-WW.md` | 正式发表论文周报（由独立的每周例程维护） |
| `digests/archive-ai-for-pde/` | **旧方向（AI for PDE）时期归档**：日报 `daily/`、周报 `published/`、历史摘要 |
| `digests/status_updates/` | arXiv 正式发表状态回填报告（由状态回填例程维护） |
| `metadata/*.jsonl` | 论文注册表与正式发表状态元数据（周报 / 状态回填例程维护，跨主题连续保留） |
| `seen_papers.txt` | 已推送论文 arXiv ID 列表，用于去重（跨主题连续保留） |
| `run_log.md` / `run_log_published.md` / `run_log_status_update.md` | 日报 / 周报 / 状态回填运行记录 |

## 评分标准（满分 10，入选阈值 ≥ 7）

- **主题相关度**（0–4 分）：与"PDE 基座大模型"核心主题的契合程度
- **基座特性强度**（0–3 分）：多物理/多任务预训练、可迁移、规模化的证据
- **创新性**（0–3 分）：新架构、新预训练范式、新基准/数据集或新理论

详见 [`docs/TAXONOMY.md`](docs/TAXONOMY.md)。

## 触发方式

- **定时触发**：每日 UTC 01:00 自动运行
- **手动触发**：在 [Claude Code Scheduled](https://claude.ai/code/scheduled) 页面点击 Run now

## 技术栈

- **运行平台**：Anthropic Cloud（Claude Code Remote Agent）
- **数据来源**：WebSearch（arXiv export API 在云端常返回 403）
- **存储**：GitHub 仓库自动提交

---

## 日报摘要

> 2026-04-19 ~ 2026-07-22 的历史日报摘要（重点转向前）已迁移至
> [`digests/archive-ai-for-pde/历史日报摘要.md`](digests/archive-ai-for-pde/历史日报摘要.md)，
> 以下仅收录 2026-07-22 重点转向后的日报摘要。

<!-- DIGEST_START -->

_（暂无新方向日报，首期日报生成后将自动追加于此。）_

第70期 · 2026-07-23 · [📄 查看完整日报](digests/PDE-FM-日报-20260723.md)
检索情况： 20个关键词查询+12次专项验证 → 约90篇去重论文（功能正常）
入选5篇论文（评分≥7）：

| # | arXiv ID | 标题摘要 | 方向 | 评分 |
|---|----------|---------|------|------|
| 1 | 2510.25803 | MoE-POT 稀疏MoE大规模PDE预训练算子Transformer（USTC，NeurIPS 2025） | A | 10/10 |
| 2 | 2605.15793 | AOT-POT 自适应算子变换大规模PDE预训练（USTC/上海AI Lab/清华） | A | 10/10 |
| 3 | 2603.01406 | 神经PDE求解器边界索引算子族非可识别性理论（Georgia Tech，ICLR 2026） | C | 9/10 |
| 4 | 2607.07718 | LLT 局部线性Transformer高效PDE算子学习（Tel Aviv） | A | 7/10 |
| 5 | 2601.11428 | FNO跨PDE族失效模式压力测试大规模诊断框架 | C/D | 7/10 |

本期最值得关注： MoE-POT 与 AOT-POT 分别以"专家扩容"与"算子对齐变换"两条互补路线推进大规模PDE预训练，是本期基座大模型主线最直接的进展；同时"One Operator to Rule Them All"从理论上揭示了神经算子在边界条件分布偏移下的不可识别性，为基座模型的OOD泛化设计敲响警钟。

<!-- DIGEST_END -->

## 正式发表论文周报

> 由**每周例程**维护：跟踪 AI 求解 PDE 领域**已正式发表 / 正式接收**的论文（补充 DOI、venue、
> 出版状态，并回填 arXiv 预印本的正式版本）。完整周报见 [`digests/published/`](digests/published/)；
> 2026-07-22 前的旧周报归档于
> [`digests/archive-ai-for-pde/published/`](digests/archive-ai-for-pde/published/)。

<!-- PUBLISHED_DIGEST_START -->

_（暂无正式发表周报摘要，首期生成后将自动追加于此，保留最近 12 期。）_

<!-- PUBLISHED_DIGEST_END -->

## 正式发表状态回填

> 由**状态回填例程**维护：定期复查仓库已收录的 arXiv 论文是否已出现正式发表版本，
> 回填 DOI / venue / 出版状态到 `metadata/`，报告见 [`digests/status_updates/`](digests/status_updates/)。

<!-- STATUS_UPDATE_START -->

_（暂无状态回填摘要，首期运行后将自动追加于此。）_

<!-- STATUS_UPDATE_END -->
