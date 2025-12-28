# Docker Compose 结构与职责划分

## 组件列表与职责
- ims-app：Django Web
- ims-worker：Celery Worker（异步任务）
- ims-nginx：反向代理/静态资源
- ims-redis：Broker/Backend（如启用）

## 网络与依赖
- depends_on 说明
- service name 作为 DNS（ims_app / ims_redis）

## 环境变量管理
- .env 内容说明（示例：DEBUG、ALLOWED_HOSTS、CSRF_TRUSTED_ORIGINS、DATA_DIR）
- 分环境策略（客户/测试/开发）

## 日志与持久化
- logs：挂载到 /opt/ims/data/logs
- media/static/reports：统一挂载到 /opt/ims/data/…

## 常见变体
- 不启用 worker 的最小部署
- 启用 worker+redis 的标准部署
