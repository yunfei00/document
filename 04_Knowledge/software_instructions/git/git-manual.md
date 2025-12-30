
# Git 使用指导手册（工程版 · 可落地）

> 适用：Windows / Linux / macOS，远端 GitHub / GitLab / 自建 Git 服务  
> 目标：快速定位状态、稳定提交、协作不翻车、安全回退、发布可追溯

---

## 1. 核心概念（必须懂）

### 1.1 三个区
- **工作区（Working Tree）**：你正在编辑的文件
- **暂存区（Index / Staging）**：`git add` 后准备提交的内容
- **提交区（Repository / HEAD）**：`git commit` 后形成的历史快照（`HEAD` 指向当前分支最新提交）

> 顺序：改代码 → add → commit → push

### 1.2 文件的三种常见状态
- **Untracked**：新文件，Git 还没跟踪
- **Modified**：被修改，但没 add
- **Staged**：已 add，等待 commit

---

## 2. 日常工作流（推荐你每天就用这套）

### 2.1 开始一天工作（先同步）
```bash
git status
git pull
```

### 2.2 开新分支（真实例子：修复“项目报告下载”）
假设你要修复一个 Bug：**项目维度的检测报告下载失败**。

1) 切到主分支并拉最新：
```bash
git switch main     # 或 git switch master
git pull
```

2) 从主分支创建并切换到新分支：
```bash
git switch -c fix/project-report-download
```

3) 在该分支上修改代码，然后提交：
```bash
git status
git add .
git commit -m "fix(report): project report download path"
```

4) 第一次把分支推到远端（让 PR/MR 能看到）：
```bash
git push -u origin fix/project-report-download
```

> 你可以把“分支”理解为一条独立轨道：你在分支里折腾，`main` 不会被你搞乱；做完再合回去。

---

## 3. PR / MR 是什么？

- **PR = Pull Request（GitHub）**
- **MR = Merge Request（GitLab）**

它们本质是同一件事：**把一个分支的改动合并到另一个分支**（通常是把 `feature/fix` 合回 `main/develop`），并提供：
- 变更记录（可追溯）
- 代码 Review（即使你一个人开发，也能当作“合并前检查清单”）
- CI 自动检查（未来可接入）

---

## 4. 常用查看命令（排错必用）

### 4.1 看当前状态
```bash
git status
```

### 4.2 看改了什么
```bash
git diff              # 工作区 vs 暂存区
git diff --staged     # 暂存区 vs HEAD
```

### 4.3 看提交历史
```bash
git log --oneline --graph --decorate --all
git show <commit_id>
```

### 4.4 查看某个文件的修改历史
```bash
git log -- <file>
git blame <file>
```

---

## 5. 撤销 / 回退（最常用也最容易搞错）

> 撤销前先 `git status`，看清楚改动在：工作区？暂存区？还是已经提交？

### 5.1 丢弃“所有未提交修改”（含已 add）
⚠️ **危险：改动直接丢失**（除非 IDE 本地历史能找回）
```bash
git reset --hard HEAD
```

### 5.2 只丢弃工作区修改（不动暂存区）
```bash
git restore .
```

### 5.3 取消暂存（把 add 撤回到工作区）
```bash
git restore --staged .
```

### 5.4 删除未跟踪文件（Untracked files）
```bash
git clean -fdn   # 先预览
git clean -fd    # 真删
```

### 5.5 先存起来（不想丢改动：WIP）
```bash
git stash push -m "wip"
git stash list
git stash pop
# git stash apply   # 取回但不删除 stash
```

### 5.6 误操作补救（找回丢失提交/分支）
```bash
git reflog
git reset --hard <commit_id>
```

---

## 6. 分支管理（协作核心）

### 6.1 查看分支
```bash
git branch
git branch -a
```

### 6.2 删除分支
```bash
git branch -d feature/x        # 已合并可删
git branch -D feature/x        # 强制删（慎用）
git push origin --delete feature/x
```

### 6.3 清理已删除的远端分支引用
```bash
git fetch --prune
git branch -vv
```

---

## 7. 同步远端（pull / fetch / rebase 的正确姿势）

### 7.1 pull 的本质
`git pull = git fetch + git merge`

### 7.2 更稳的方式（推荐）
```bash
git fetch origin
git merge origin/<branch>
```

### 7.3 rebase（让提交历史更干净：个人分支推荐）
```bash
git switch feature/x
git fetch origin
git rebase origin/main
```

冲突处理：
```bash
git add .
git rebase --continue
# 放弃：
git rebase --abort
```

> 公共分支慎用 rebase（会改历史，影响他人）。

---

## 8. 冲突处理（merge/rebase 常见）

### 8.1 冲突出现后
```bash
git status
```

### 8.2 标准流程
1) 打开冲突文件，处理冲突标记：
   - `<<<<<<<`
   - `=======`
   - `>>>>>>>`
2) 标记解决：
```bash
git add <file>
```
3) 继续：
- merge 场景：`git commit`
- rebase 场景：`git rebase --continue`

### 8.3 放弃本次 merge/rebase
```bash
git merge --abort
git rebase --abort
```

---

## 9. 远端与认证（GitHub 常见坑）

### 9.1 查看 remote
```bash
git remote -v
```

### 9.2 认证失败：账号密码不行了怎么办？
很多平台（尤其 GitHub）通常需要：
- **SSH Key（推荐）** 或
- **Personal Access Token（PAT）** 代替密码

#### 方案 A：SSH（长期最省事）
```bash
ssh-keygen -t ed25519 -C "your_email"
ssh -T git@github.com
git remote set-url origin git@github.com:yunfei00/document.git
```

#### 方案 B：PAT（受限环境也常用）
配置凭据缓存（减少重复输入）：
```bash
git config --global credential.helper store
# Windows 推荐：
git config --global credential.helper manager
```

---

## 10. .gitignore（工程必须配置）

详细说明与大量示例见：`./gitignore-examples.md`

> 注意：`.gitignore` **不会**自动移除已被跟踪的文件。  
> 需要用 `git rm --cached` 停止跟踪（文件会保留在本地）。

---

## 11. Tag / Release（交付与版本追溯）

### 11.1 打 tag（语义化版本）
```bash
git tag -a v1.1.0 -m "release v1.1.0"
git push origin v1.1.0
```

### 11.2 查看 tag
```bash
git tag
git show v1.1.0
```

---

## 12. 回滚策略（生产更安全）

### 12.1 推荐：revert（公共分支首选）
```bash
git revert <commit_id>
git push
```

### 12.2 reset（改历史：慎用公共分支）
```bash
git reset --hard <commit_id>
git push --force
```

---

## 13. 提交规范（建议统一：Conventional Commits）

格式：
```
<type>(<scope>): <subject>
```

type 推荐：
- `feat` `fix` `refactor` `perf` `docs` `test` `build` `ci` `chore` `revert`

scope 建议（按你项目模块）：`projects / images / repo / components / detection / report / notification / rbac / deployment / docs`

示例：
```bash
git commit -m "fix(report): project report download path"
git commit -m "feat(projects): add approval workflow entry"
git commit -m "docs(git): add branch model and release checklist"
```

---

## 14. 团队协作分支模型（轻量 GitFlow，适合商业交付）

### 14.1 分支角色
- **main（或 master）**：生产稳定分支（只通过 PR 合并，合并即发布）
- **develop（可选但推荐）**：集成分支（feature/fix 合到这里，稳定后再合 main）
- **feature/***：功能分支（从 develop 拉出，完成后合回）
- **hotfix/***：紧急修复（从 main 拉出，修复后合回 main + develop）
- **release/***（可选）：发布准备分支（集中修 bug、改版本号）

### 14.2 一句话规则
1) 任何开发都在 feature/fix 分支  
2) 通过 PR 合到 develop  
3) 到交付点合到 main 并打 tag  
4) main 出问题走 hotfix 发补丁版本

---

## 15. 最小命令集合（记住这 10 条就够用）

```bash
git status
git pull
git switch -c feature/x
git add .
git commit -m "msg"
git push
git fetch --all --prune
git log --oneline --graph --decorate --all
git reset --hard HEAD
git clean -fd
```
