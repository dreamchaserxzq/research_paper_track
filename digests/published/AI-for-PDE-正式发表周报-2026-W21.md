# AI for PDE 正式发表论文周报

日期范围：2023-05-24 至 2026-05-24 UTC。第 2 期，三年回溯检索。

## 本期概览

候选论文 16 篇，去重后 10 篇，正式发表状态明确 3 篇，新增入选 3 篇，arXiv 匹配 1 篇，待人工确认 1 篇。

## 本期重点

三年窗口内，高相关正式发表论文主要集中在 AI 天气和气候动力学代理模型、混合可微分物理求解器、生成式不确定性预报。最值得关注的是 NeuralGCM，它将传统物理动力学求解器与可学习物理参数化耦合，对 LPP-EUV 预脉冲辐射流体代理模型有直接方法启发。

## 方向 A：AI 求解 PDE / Scientific Machine Learning

### Neural general circulation models for weather and climate

- DOI：10.1038/s41586-024-07744-y
- Venue：Nature，2024-07-22，632:1060-1066
- 作者：Dmitrii Kochkov et al.
- 链接：https://www.nature.com/articles/s41586-024-07744-y
- 核心贡献：提出 NeuralGCM，将可微分大气动力学求解器与神经网络物理参数化结合，用于天气、集合预报和多年气候模拟。
- 方法要点：differentiable dynamical core + learned physics module + 端到端在线训练。
- 与课题关联：可迁移到 FLASH/ECOGEN 或辐射流体建模中，用神经网络替代电子热传导闭合、辐射输运近似、EOS/opacity 插值校正等高成本模块。
- 评分：10/10，AI+PDE 4/4，等离子体/EUV 迁移关联 3/3，创新与 venue 3/3。

## 方向 B：数据生成、代理模型与科学仿真 surrogate

### Accurate medium-range global weather forecasting with 3D neural networks

- DOI：10.1038/s41586-023-06185-3
- Venue：Nature，2023-07-05，619:533-538
- 作者：Kaifeng Bi et al.
- 链接：https://www.nature.com/articles/s41586-023-06185-3
- arXiv：2211.02556
- 核心贡献：提出 Pangu-Weather，用 3D Earth-specific Transformer 建模全球天气场演化，构建中期天气预报快速代理模型。
- 方法要点：三维变量编码和 hierarchical temporal aggregation，用于控制自回归误差累积。
- 与课题关联：可借鉴三维多变量场编码、分层时间推进和误差累积控制，用于靶材形态时序预测。
- 评分：9/10，AI+PDE 4/4，等离子体/EUV 迁移关联 2/3，创新与 venue 3/3。

### Probabilistic weather forecasting with machine learning

- DOI：10.1038/s41586-024-08252-9
- Venue：Nature，2024-12-04，637:84-90
- 作者：Ilan Price et al.
- 链接：https://www.nature.com/articles/s41586-024-08252-9
- 核心贡献：提出 GenCast，以条件生成式模型实现概率天气预报，从确定性 surrogate 扩展到可采样 ensemble。
- 方法要点：条件扩散模型生成未来天气状态，并自回归形成 15 天集合预报。
- 与课题关联：可迁移到 LPP-EUV 预脉冲不确定性量化，在不同激光、液滴、EOS/opacity 参数下生成分布式靶材形态预测。
- 评分：8/10，AI+PDE 3/4，等离子体/EUV 迁移关联 2/3，创新与 venue 3/3。

## 方向 C：激光等离子体 / EUV / 辐射流体 / Vlasov / MHD

本期未发现可确认三年窗口内正式发表状态、且满足评分与硬性约束的方向 C 新增论文。若干 radiation hydrodynamics surrogate、NLTE kinetics surrogate、ICF optimization、MHD neural operator 相关条目仍停留在 arXiv 或元数据不完整状态，未强行收录。

## 已有 arXiv 论文的正式发表状态更新

| arXiv ID | 标题 | DOI | 正式 venue | publication_date | 置信度 | 建议 |
|---|---|---|---|---|---|---|
| 2211.02556 | Pangu-Weather | 10.1038/s41586-023-06185-3 | Nature | 2023-07-05 | 1.0 | paper_registry.jsonl 不存在，暂不自动更新 |

## 待人工确认论文

| 标题 | 候选 DOI | 候选 venue | 问题 | 建议 |
|---|---|---|---|---|
| Learning skillful medium-range global weather forecasting | 10.1126/science.adi2336 | Science | Science.org 页面访问受限，未能直接确认 publisher 元数据 | 下期通过 Crossref/OpenAlex 或 publisher 页面再确认 |

## 未入选原因

主要原因包括：仅为 arXiv 预印本；缺少 DOI 或正式 venue；与 AI for PDE 或仿真代理关系不足；publisher 页面无法确认 publication_date。
