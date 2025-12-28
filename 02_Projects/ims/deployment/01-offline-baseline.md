# 离线交付部署基线（Baseline）

## 一、宿主机前置条件
- Docker 版本要求
- 磁盘空间建议
- 端口规划（示例：32000/…）
- 时间同步/时区（如需）

## 二、目录规划（建议）
- /opt/ims/
  - data/（持久化数据）
  - images/（离线镜像包）
  - nginx/（nginx.conf）
  - compose/（compose.yml）

## 三、离线镜像导入流程
1. 拷贝镜像 tar 到 /opt/ims/images/
2. `docker load -i xxx.tar`
3. `docker images` 验证 tag 与版本

## 四、启动流程（compose）
- `docker compose up -d`
- 健康检查（curl / 访问登录页）
- 关键容器日志检查（app / worker / nginx / redis）

## 五、验收标准
- 能登录
- 核心页面可访问
- 能上传/下载（如有）
- 通知/审批入口正常（如有）
