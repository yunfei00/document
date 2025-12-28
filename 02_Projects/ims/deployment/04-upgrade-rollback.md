# 升级与回滚

## 升级前必做
- 记录当前版本：镜像 tag / digest
- 备份数据目录（db/media/reports）
- 导出当前配置（compose.yml/.env/nginx.conf）

## 升级流程（推荐）
1. `docker compose down`
2. 导入新镜像（docker load）
3. 更新 compose image tag
4. `docker compose up -d`
5. 数据迁移/初始化（如有）
6. 验证（登录、核心流程、任务）

## 回滚流程
- 回滚镜像 tag
- 还原数据备份
- 启动旧版本并验证

## 风险点
- 数据库迁移不兼容
- 静态资源不一致
- 配置项缺失
