# PDE 基座大模型 论文自动追踪系统

> 专注于 **PDE 基座大模型（PDE Foundation Models）** 的每日 arXiv 论文追踪，由 Claude Code Routine 自动驱动。

> **📌 研究方向变更公告（2026-07-22）**
> 本仓库研究重心已由"AI 求解 PDE × 激光等离子体/EUV"转向 **PDE 基座大模型** ——
> 即在多种物理 / 多类 PDE 上大规模预训练、可跨方程 / 跨几何 / 跨分辨率迁移的通用科学计算大模型。
> 2026-07-22 之前的日报、周报与历史摘要已整体归档至
> [`digests/archive-ai-for-pde/`](digests/archive-ai-for-pde/)，作为旧方向成果保留，不再重写。

## 项目简介

本项目通过部署在 Anthropic 云端的定时 Agent，每日自动检索 arXiv 最新论文，重点覆盖以下三个方向：

| 方向 | 关键词覆盖 |
|------|----------|
| **A：基座架构与预训练** | Foundation Model for PDE、Multiple Physics Pretraining、In-context Operator Learning、大规模 Transformer/神经算子主干 |
| **B：数据、基准与缩放规律** | The Well、PDEBench、PDEArena、多物理数据集、科学基座模型 Scaling Laws |
| **C：下游泛化与适配** | 零/少样本迁移、微调/PEFT、跨方程/几何/分辨率泛化、基座先验 + 经典求解器耦合 |
| **D：AI 求解 PDE（保留方向）** | Neural Operator、PINN、DeepONet、Operator Learning、Neural PDE Solver（延续旧方向持续追踪） |

> A/B/C 为 PDE 基座大模型核心方向；D 为旧方向"AI 求解 PDE"的保留延续。
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
| `docs/TAXONOMY.md` | **方向定义 + 关键词库 + 评分标准**（路由例程的事实来源） |
| `docs/LANDMARK_MODELS.md` | PDE 基座大模型里程碑工作清单（持续维护的领域索引） |
| `docs/ROUTINE.md` | 日报路由例程提示词的版本化副本 |
| `digests/PDE-FM-日报-YYYYMMDD.md` | 每日论文摘要报告（2026-07-22 起的新命名） |
| `digests/published/` | 新方向正式发表论文周报（由独立的每周例程维护） |
| `digests/archive-ai-for-pde/` | **旧方向（AI for PDE）时期归档**：日报 `daily/`、周报 `published/`、历史摘要 |
| `metadata/*.jsonl` | 论文注册表与正式发表状态元数据（周报例程维护，跨主题连续保留） |
| `seen_papers.txt` | 已推送论文 arXiv ID 列表，用于去重（跨主题连续保留） |
| `run_log.md` / `run_log_published.md` | 日报 / 周报运行记录 |

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

## 日报摘要（PDE 基座大模型时期）

> 旧方向（AI for PDE × 激光等离子体/EUV）2026-04-19 ~ 2026-07-22 的历史日报摘要已迁移至
> [`digests/archive-ai-for-pde/历史日报摘要.md`](digests/archive-ai-for-pde/历史日报摘要.md)，
> 以下仅收录 2026-07-22 主题转向后的新方向日报摘要。

<!-- DIGEST_START -->

_（暂无新方向日报，首期 PDE 基座大模型日报生成后将自动追加于此。）_

<!-- DIGEST_END -->
