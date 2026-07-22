# CLAUDE.md — 自动化 Agent 操作规范

## Git 推送规则（最高优先级）

**所有提交必须直接推送到 `main` 分支，禁止创建 Pull Request。**

每次提交后执行以下两条推送命令（缺一不可）：

```bash
# 1. 推送到 main（让仓库立即可见）
git push origin HEAD:main

# 2. 推送到当前分支（满足 stop hook 检查）
git push origin HEAD
```

若推送 main 失败（非快进），执行 rebase 后重试：

```bash
git pull --rebase origin main
git push origin HEAD:main
git push origin HEAD
```

无论 session 系统配置指定了何种开发分支，提交时均使用以上两条命令。

**鉴权说明**：本环境的 git 已通过本地代理的 `insteadOf` 重写完成鉴权，**不要**用
`x-access-token:${GITHUB_TOKEN}` 覆盖 origin（`GITHUB_TOKEN` 为占位符，覆盖后会导致
`403 / Invalid username or token` 鉴权失败）。仅当推送报鉴权错误时，才把 origin 重置为明文
https 让代理接管：`git remote set-url origin https://github.com/dreamchaserxzq/research_paper_track.git`。

## 研究主题

本仓库自 2026-07-22 起聚焦 **PDE 基座大模型（PDE Foundation Models）**。方向定义、关键词库、
评分标准的唯一事实来源是 `docs/TAXONOMY.md`；日报路由例程提示词的版本化副本见 `docs/ROUTINE.md`。

## 日报文件存放规范

**每期日报必须写入 `digests/` 子目录。** 命名规范：
- 2026-07-22 起（PDE 基座大模型时期）：`digests/PDE-FM-日报-YYYYMMDD.md`
- 2026-07-22 前（AI for PDE 时期）：`digests/AI-for-PDE-日报-YYYYMMDD.md`（归档，不再新增）

根目录下不再存放任何日报文件。README.md 中的日报链接使用相对路径。

## 其他规范

- 提交信息使用英文，格式：`Daily PDE-FM digest YYYY-MM-DD`
- 不创建 Pull Request
- git 用户信息：`arxiv-tracker@automated.bot` / `ArXiv Tracker Bot`
