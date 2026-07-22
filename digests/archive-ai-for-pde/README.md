# 归档 · AI for PDE 时期追踪成果（2026-04-19 ~ 2026-07-22）

本文件夹保存**旧研究方向**时期自动追踪的全部成果。2026-07-22 起本仓库转向
**PDE 基座大模型（PDE Foundation Models）**，此前内容整体归档于此，不再新增、不再重写。

## 旧研究方向

计算物理 × 科学机器学习交叉领域，三个追踪方向：

| 方向 | 覆盖 |
|------|------|
| A：AI 求解 PDE | Neural Operator、PINN、DeepONet、Operator Learning |
| B：数据生成与代理模型 | Surrogate Model、Generative Model、Active Learning |
| C：激光等离子体 / EUV 计算 | Laser-Plasma ML、EUV、Radiation Hydrodynamics、Vlasov、MHD |

> 注：其中"A：AI 求解 PDE"方向在新体系中作为 **方向 D** 继续保留追踪，
> 详见根目录 `docs/TAXONOMY.md`。

## 目录结构

| 路径 | 说明 |
|------|------|
| `daily/AI-for-PDE-日报-YYYYMMDD.md` | 每日论文摘要日报（共 68 期） |
| `published/AI-for-PDE-正式发表周报-2026-Wxx.md` | 正式发表论文周报（W21 ~ W30） |
| `历史日报摘要.md` | 从主 README 迁出的历史日报摘要索引 |

去重集 `seen_papers.txt`、论文注册表 `metadata/*.jsonl` 与运行日志 `run_log*.md`
跨主题连续保留在仓库根目录，未随本次归档迁移。
