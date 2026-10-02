# 研究知识库与交互工作台

[固定版本入口](index.html) · [PDE 论文工作台](2026-10-02/index.html) · [AI 与传统 PDE 方法工作台](2026-10-02-broader-horizons/index.html)

当前版本为 **2026-10-02**。先同步远程 main（`ca1125a6809e7a3998882a7d134e0c3c8e11c492`），再建立新版；两套 2026-09-19 目录保持原文件字节不变。新版的“本轮更新”分别说明登记变化、当轮原文核查、沿用证据、体系补读和检索缺口。

- PDE 语料包含456条主表身份，比旧版新增2条；补充参考与主表分开计数。43条原阅读记录沿用09-19核查范围，当轮记录见 `incremental_evidence.json`。
- 广角知识库保留原64个来源与访问日期，并补充 AI 与数值科学机制线索。图谱组织的是证据关联和有条件的类比，不是引用网络。
- 全部登记、选择性正文阅读、作者报告、独立复现与待验证假说是不同层次；本次没有运行科学实验或升级主表的历史阅读状态。

## 在电脑上打开

Windows PowerShell 执行后保持窗口开启：

```powershell
ssh -N -L 127.0.0.1:28765:127.0.0.1:8765 xzq@6.tcp.nas.cpolar.cn
```

- [固定知识库入口](http://127.0.0.1:28765/docs/research_synthesis/index.html)
- [2026-10-02 PDE 工作台](http://127.0.0.1:28765/docs/research_synthesis/2026-10-02/index.html)
- [2026-10-02 广角工作台](http://127.0.0.1:28765/docs/research_synthesis/2026-10-02-broader-horizons/index.html)

服务器端使用现有8765服务。若该服务尚未启动，在服务器项目根目录运行：

```bash
python -m http.server 8765 --bind 127.0.0.1 --directory /home/xzq/projects/research_paper_track
```

固定入口保留新旧版本链接；旧网址继续展示旧快照。页面没变化时按 Ctrl+F5。服务器端HTTP正常与Windows端转发是否成功是独立检查。

## 阅读与使用

两站均有本轮更新、嵌入综述、逐条来源、图谱与个人阅读清单。更新页支持检索本轮条目并回到原文核查详情；综述可使用章内目录、字号和继续阅读。广角还支持跨章节正文检索、图谱返回/前进、75%–175%缩放与居中。

在线入口 `index.html` 优先加载页面和压缩后的阅读数据，下载资料只在点击时传输，图谱、证据列表与搜索索引在使用时初始化。原网址保持不变。

需要离线阅读时，请点击侧栏或页尾的 **“下载完整离线版”**，保存 `offline.html`（下载文件名含工作台标识）。该单文件包含本站综述、公式字体、图谱和原始资料导出，离线时不请求外部资源；支持现代 Edge、Chrome、Firefox 和 Safari。在线入口文件本身不再是完整离线包。另一工作台、历史版本、原始论文网站和未内嵌的仓库文件仍需要相应目录或网络。

## 个人笔记与版本兼容

新版继续使用原有工作台的个人清单标识和存储键。在**同一浏览器、同一协议与主机端口**访问时，可读取旧版已有条目与笔记，也可导入旧版备份；无需重新收藏。切换端口、浏览器或从HTTP改为本地文件可能形成不同存储空间，先导出JSON备份。

清单仍只在当前浏览器保存，两套工作台分别管理；不会写回服务器、同步到其他电脑或改变来源证据等级。支持JSON/Markdown导出、校验预览后仅追加新ID的JSON导入、归档与撤销。重复ID保留当前笔记，不自动拼接或覆盖；若要合并同一条目的两份笔记，保留两份备份后手动整理。

如果其他标签页已经改过清单，本页检测到存储版本变化后停止写入，当前会话仍可导出。存储被禁止、损坏或配额不足时同样显示限制，不静默丢弃已有原始数据。旧版不认识新版新增ID，可能进入保护模式；请在新版编辑，并及时备份。

## 重建与验证

以下命令默认构建2026-10-02版本，不写旧目录，也不联网：

```bash
python scripts/build_research_graph.py
python scripts/build_research_site.py
python scripts/build_research_horizons.py
python scripts/build_research_graph.py --check
python scripts/build_research_site.py --check
python scripts/build_research_horizons.py --check
python scripts/papertrack.py check
python -m unittest discover -s tests -p 'test_research_*.py' -v
```

依赖 Python、Python-Markdown 和 Node.js（公式构建）；固定版本 KaTeX 随仓库保存，重建不联网。公式在构建时排版为 HTML 与 MathML。在线版的字体来自同站文件，仅在阅读公式时加载；离线版字体全部嵌入，二者均不依赖 CDN。行内公式与独立公式均可离线显示，较长公式在手机上可横向滚动；原始 Markdown 下载仍保留 LaTeX。图谱构建会记录当前主表、来源记录、日报及代码输入哈希；两站记录内嵌内容和构建输出哈希。旧版若需重建，应使用其原始构建代码与语料版本，不能用当前输入静默覆盖历史证据。

## 文件与证据

| 文件 | 含义 |
|---|---|
| `research_update.md` | 当轮变化、机制联系、阅读优先级和检索边界 |
| `update_manifest.json` | 更新页数据与新增/补充条目；不等于注册表 |
| `search_coverage.json` | 实际查询、访问日期、已读位置和覆盖限制 |
| PDE `remote_sync.json` | 同步前后提交、11次新增运行、登记变化 |
| PDE `corpus_manifest.json` / `paper_cards.jsonl` | 当前456身份与本地材料出处，不等于全部全文阅读 |
| PDE `incremental_evidence.json` | 当轮选择性原文核查，原43条记录分别沿用 |
| 广角 `*_evidence.json` / `evidence_catalog.json` | 来源、阅读位置、访问日期、支持点与局限 |
| `knowledge_graph.json` / `nodes.csv` / `edges.csv` | 有类型与证据边界的知识图谱 |
| `validation.json` | 当轮真实验证结果；UI检查不等于科学复现 |
| `math_validation.json` | 公式更新当时的页面哈希及验证；后续交付方式见性能报告 |
| `performance_validation.json` | 当前在线/离线文件哈希、同条件前后测量、公式与下载等回归验证 |

本次更新本地就绪后通过原有预览服务查看；未创建Git提交、未推送远程，也未修改外部日报调度。

## 首次加载优化验证

在本机 Chromium 中，以冷缓存、10 Mbps 下载带宽、100 ms 延迟和 4 倍 CPU 降速各测量一次：

| 页面 | 首次所需传输 | 交互就绪时间 |
|---|---|---|
| PDE | 19.39 MB → 0.56 MB | 约 17.4 s → 1.2 s |
| AI 与数值方法 | 2.08 MB → 0.31 MB | 约 2.4 s → 0.8 s |

这是同条件的本机模拟，不代表 Windows SSH 链路的实际耗时。两站的 `performance_validation.json` 保存完整测量、当前文件哈希与验证边界。已检查在线与独立离线文件、15 章 158 处公式、四种屏宽、28 项原始资料的下载字节、个人笔记保留、隐藏面板首次打开、断线重试以及缺少原生解压接口时的在线兼容路径。
