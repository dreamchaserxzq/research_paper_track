# AI for PDE 论文自动追踪系统

> 专注于**计算物理 × 科学机器学习**交叉领域的每日 arXiv 论文追踪，由 Claude Code Routine 自动驱动。

## 项目简介

本项目通过部署在 Anthropic 云端的定时 Agent，每日自动检索 arXiv 最新论文，重点覆盖以下三个方向：

| 方向 | 关键词覆盖 |
|------|-----------|
| **A：AI 求解 PDE** | Neural Operator、PINN、DeepONet、Foundation Model for PDE |
| **B：数据生成与代理模型** | Surrogate Model、Generative Model、Active Learning for PDE |
| **C：激光等离子体 / EUV 计算** | Laser-Plasma ML、EUV Simulation、Radiation Hydrodynamics、Vlasov、MHD |

## 工作流程

```
每日 UTC 01:00（北京时间 09:00）
        │
        ▼
  搜索 arXiv API（48h 内新论文，三方向并行）
        │
        ▼
  去重（跳过 seen_papers.txt 中已有 ID）
        │
        ▼
  10 分制评分筛选（≥ 7 分入选，目标 6-10 篇）
        │
        ▼
  生成中文摘要报告（Markdown 格式）
        │
        ▼
  提交到仓库（日报文件 + seen_papers.txt + run_log.md）
```

## 仓库文件说明

| 文件 | 说明 |
|------|------|
| `AI-for-PDE-日报-YYYYMMDD.md` | 每日论文摘要报告（自动生成） |
| `seen_papers.txt` | 已推送论文的 arXiv ID 列表，用于去重 |
| `run_log.md` | 每次运行记录（时间、检索数、入选数、异常） |

## 评分标准

每篇论文按三个维度打分，满分 10 分：

- **AI + PDE 相关度**（0–4 分）：与神经算子、PINN 等核心方向的契合程度
- **激光等离子体 / EUV 场景关联性**（0–3 分）：对课题方向的直接参考价值
- **创新性**（0–3 分）：是否提出新方法、新架构或新理论

## 触发方式

- **定时触发**：每日 UTC 01:00 自动运行
- **手动触发**：在 [Claude Code Scheduled](https://claude.ai/code/scheduled) 页面点击 Run now

## 技术栈

- **运行平台**：Anthropic Cloud（Claude Code Remote Agent）
- **模型**：claude-sonnet-4-6
- **数据来源**：[arXiv API](http://export.arxiv.org/api/query)
- **存储**：GitHub 仓库自动提交

---

## 历史日报摘要

<!-- DIGEST_START -->

### 第1期 · 2026-04-19 · [📄 查看完整日报](AI-for-PDE-日报-20260419.md)

**检索情况：** 13个关键词查询 → 约85篇去重论文（arXiv export API因403受限，改用 WebSearch 完成检索）

**入选7篇论文（评分≥7）：**

| # | arXiv ID | 标题摘要 | 方向 | 评分 |
|---|----------|---------|------|------|
| 1 | [2604.13447](https://arxiv.org/abs/2604.13447) | 无数据PINN求解漂移动力学方程（托卡马克NTV建模） | B/C | 10/10 |
| 2 | [2601.12614](https://arxiv.org/abs/2601.12614) | GNN代理模型加速全局混合Vlasov仿真（100×加速） | B/C | 10/10 |
| 3 | [2604.13919](https://arxiv.org/abs/2604.13919) | 嵌套FNO高效建模辐射传输方程 | C | 9/10 |
| 4 | [2604.04828](https://arxiv.org/abs/2604.04828) | 量子-经典混合FNO用于激光加工多物理场代理建模 | C | 9/10 |
| 5 | [2603.01102](https://arxiv.org/abs/2603.01102) | 结构保持随机神经网络精确求解MHD方程 | C | 9/10 |
| 6 | [2602.12706](https://arxiv.org/abs/2602.12706) | 物理信息Laplace神经算子（Karniadakis团队） | A | 7/10 |
| 7 | [2604.04061](https://arxiv.org/abs/2604.04061) | 几何感知算子学习框架处理变域界面问题 | A | 7/10 |

**本期最值得关注：** 2604.13447（无数据PINN求解动力学方程）和 2601.12614（Vlasov仿真GNN代理，100×加速），二者与激光等离子体/EUV动力学建模的核心需求高度契合。

<!-- DIGEST_END -->
