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

## 其他规范

- 提交信息使用英文，格式：`Daily paper digest YYYY-MM-DD`
- 不创建 Pull Request
- git 用户信息：`arxiv-tracker@automated.bot` / `ArXiv Tracker Bot`
