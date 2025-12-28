# IMS 离线部署与交付：总览

## 目标
- 在**无公网**环境完成安装、启动、升级、备份、故障恢复
- 交付物可复制、可追溯（版本号、镜像 digest、配置）

## 适用范围
- OS：CentOS 7.9（可扩展其他）
- 运行时：Docker / Docker Compose
- 数据库：SQLite（默认）/（可扩展 MySQL）

## 交付物清单（建议）
- docker 镜像包（ims-app / nginx / redis 等）
- docker-compose.yml
- .env（或 env.example）
- 数据目录结构（/opt/ims/data/…）
- 初始化脚本（可选）
- 校验文件（sha256sum）

## 关键原则
- 配置与数据分离（volume 映射）
- 镜像与版本固定（tag + digest）
- 可升级可回滚（数据备份 + 镜像留存）
