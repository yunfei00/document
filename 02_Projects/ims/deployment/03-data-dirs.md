# 数据目录与权限（Volume 映射）

## 目录清单（建议）
- /opt/ims/data/db
- /opt/ims/data/media
- /opt/ims/data/static
- /opt/ims/data/reports
- /opt/ims/data/logs

## 权限建议
- 宿主机目录 owner/group
- 容器内用户（如使用非 root）
- 常见权限错误与修复命令

## 备份策略
- SQLite 文件备份点
- reports/media 备份点
- 全量与增量（可选）
