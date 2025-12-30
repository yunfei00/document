
# Git 专题（入口）

这里是 **Git 使用指导手册 + 协作规范模板 + 发布清单** 的归档目录。

> 建议用法：
> - **学习/查阅**：直接看本目录文档
> - **在项目仓库生效**：把模板文件复制到项目仓库规定位置（见下方“落地到项目仓库”）

## 目录

- [Git 使用指导手册](./git-manual.md)
- [PR 模板（归档版）](./PULL_REQUEST_TEMPLATE.md)
- [Issue 模板：Bug（归档版）](./ISSUE_TEMPLATE_bug.yml)
- [Issue 模板：Feature（归档版）](./ISSUE_TEMPLATE_feature.yml)
- [发布清单（Release Checklist）](./release-checklist.md)
- [.gitignore 详细说明与示例](./gitignore-examples.md)
- [CHANGELOG 模板（可选）](./changelog-template.md)

## 落地到项目仓库（让模板“自动出现”）

> 下面是 **GitHub** 的常见识别路径（你商业版 IMS 项目仓库建议按这个放置）。

### PR 模板（任选其一）
- `PULL_REQUEST_TEMPLATE.md`（仓库根目录）
- `.github/pull_request_template.md`

### Issue 模板（必须放这个目录）
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`

### 发布清单
- `RELEASE_CHECKLIST.md`（仓库根目录）
  - 或放到 `docs/release/`，但建议根目录保留一份入口链接

## 备注
- 本目录下的模板文件用于**归档与复用**；复制到项目仓库后才会对 GitHub 界面产生作用。
