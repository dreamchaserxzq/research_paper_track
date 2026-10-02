# AI × PDE 数值科学：2026-09-19 广角研究快照

直接阅读 [总综述](RESEARCH_HORIZONS.zh-CN.md)；交互入口为 [index.html](index.html)。内容包括 AI 的表示/生成与推理/行动两份专题、传统 PDE 数值方法、九项跨域研究问题、学习路线及逐项证据。

## 打开方式

`index.html` 把七篇阅读章节、来源清单与完整图谱内嵌在一个文件里。把该文件下载到自己的电脑后，可直接用浏览器打开，无需启动服务或联网加载正文；JSON/CSV 导出也可离线使用。论文原文链接仍需要联网。公式以可复制的 TeX 显示。

完整综述页支持跨七篇正文搜索、命中片段定位、本章目录、字号调节与上一篇/下一篇。离开正文查看图谱后，点击“完整综述”可回到原阅读位置；首页“继续阅读”可恢复当前浏览器保存的章节进度。该进度是个人浏览位置，不代表新的文献阅读证据；本地存储被禁用时仍可正常使用阅读器。

若使用远程工作区，服务器上的绝对文件路径不等于你电脑上的浏览器网址。可通过开发工具的文件下载功能取得 `index.html`，或在**自己电脑的终端**运行以下命令，将占位的 SSH 别名替换为平时连接这台服务器所用的别名：

```bash
scp 你的服务器SSH别名:/home/xzq/projects/research_paper_track/docs/research_synthesis/2026-09-19-broader-horizons/index.html ./research-horizons.html
```

也可以复用本任务此前的本地 HTTP 服务和 SSH 转发。服务器侧文件服务端口为8765；若本机已转发到18765，直接打开[广角综述工作台](http://127.0.0.1:18765/docs/research_synthesis/2026-09-19-broader-horizons/index.html)。顶部可切换到 [PDE 论文图谱](http://127.0.0.1:18765/docs/research_synthesis/2026-09-19/index.html)。PDE 入口此前已由用户确认可访问；每次使用仍需保持 SSH 转发和服务器服务运行。

## 证据边界

64个唯一来源包括论文、作者书籍/讲义和官方材料。阅读等级分别为56项正文相关章节、2项书籍部分章节、3项摘要、3项官方文档或目录。没有把来源数量称为全文精读数量，没有执行科学复现。

图谱共138节点（65概念、64来源、9假说）、296关系。关系包含阅读支持的概括与综述推断；不是自动提取的引用网。九项假说有效性和新颖性均未确立。

## 文件与重建

| 文件 | 用途 |
|---|---|
| `RESEARCH_HORIZONS.zh-CN.md` | 总体地图、发展逻辑与研究判断 |
| `ai_foundations.md` / `ai_reasoning_systems.md` | 广义 AI 的两个专题 |
| `pde_numerics.md` | 传统数值方法的独立体系 |
| `cross_domain.md` / `learning_roadmap.md` | 创新假说与持续学习路径 |
| 四份 `*_evidence.json` | 手工整理的来源、概念与关系输入 |
| `coverage.md` / `evidence_catalog.json` | 自动汇总的阅读边界与完整账本 |
| `knowledge_graph.json` / `nodes.csv` / `edges.csv` | 图谱交换文件 |
| `index.html` | 单文件交互阅读器，包含全部正文 |
| `build_manifest.json` | 输入/输出哈希、源仓库提交与数量 |
| `validation.json` | 实际执行的内容与浏览器检查结果 |

在仓库根目录运行：

```bash
python scripts/build_research_horizons.py
python scripts/build_research_horizons.py --check
python scripts/papertrack.py check
```

构建需要 Python 和 Python-Markdown（本次使用3.3.4），不发起网络请求。构建器面向固定日期快照；更新研究应另建日期目录并保存旧证据，而不是把旧阅读日期改成今天。HTML 本身无需这些构建依赖。

本次仅生成与核验本地成果，没有提交、推送、公开部署，也没有更改现有 A/B/C/D 例程、注册表或外部调度器。
