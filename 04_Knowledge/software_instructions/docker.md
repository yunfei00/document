# Docker 通用使用说明（项目通用版）

> 适用于绝大多数基于 Docker / Docker Compose 的项目  
> 面向对象：开发 / 运维 / 测试 / 客户部署人员  
> 目标：**拿到项目即可照此文档完成部署、运维与排错**

---

## 0. 文档定位说明

### 本文档解决什么问题

- Docker 基础不熟？👉 **按步骤做即可**
- 不知道项目怎么启动？👉 **一条命令**
- 容器出问题？👉 **照排错章节查**
- 离线环境？👉 **有完整方案**

### 不解决什么

- 不讲 Docker 底层原理
- 不做镜像开发教程
- 不替代项目 README

---

## 1. 适用环境要求

- 操作系统（推荐）：
  - CentOS 7.9 / Rocky 8 / Ubuntu 20.04+
- Docker：≥ 24.x
- Docker Compose：v2.x（plugin 模式）

验证命令：

```bash
docker version
docker compose version
```

---

## 2. 项目启动（最常用 ⭐⭐⭐）

### 2.1 启动前检查

确保当前目录存在：

- `docker-compose.yml`

---

### 2.2 一条命令启动项目

```bash
docker compose up -d
```

---

### 2.3 查看运行状态

```bash
docker compose ps
docker ps
```

---

### 2.4 停止项目

```bash
docker compose down
```

---

## 3. 日常运维常用命令 ⭐⭐⭐

### 3.1 查看容器

```bash
docker ps
docker ps -a
```

---

### 3.2 查看日志（排错必备）

```bash
docker logs <容器名>
docker logs <容器名> --tail 200
docker logs -f <容器名>
```

---

### 3.3 进入容器调试

```bash
docker exec -it <容器名> bash
```

> 若无 bash，可使用 `/bin/sh`

---

### 3.4 重启服务

```bash
docker restart <容器名>
docker compose restart
```

---

## 4. 镜像（Image）常用操作

### 查看镜像

```bash
docker images
```

---

### 拉取镜像

```bash
docker pull nginx
docker pull nginx:1.27-alpine
```

---

### 构建镜像

```bash
docker build -t myapp:1.0 .
```

---

### 镜像导出 / 导入（离线）

```bash
docker save myapp:1.0 -o myapp_1.0.tar
docker load -i myapp_1.0.tar
```

---

## 5. 容器（Container）管理

### 创建并运行容器

```bash
docker run -d --name test -p 8080:80 nginx
```

---

### 删除容器

```bash
docker rm test
docker rm -f test
```

---

### 拷贝文件

```bash
docker cp test:/etc/nginx/nginx.conf ./
docker cp ./local.conf test:/etc/nginx/
```

---

## 6. 数据卷与目录挂载

### 使用数据卷

```bash
docker volume create mydata
docker run -d -v mydata:/data nginx
```

---

### 挂载宿主目录（推荐）

```bash
docker run -d -v /opt/app/data:/app/data myapp:1.0
```

---

## 7. 网络与端口

### 查看网络

```bash
docker network ls
```

---

### 创建自定义网络（推荐）

```bash
docker network create app-net
```

---

### 指定网络运行容器

```bash
docker run -d --network app-net nginx
```

---

## 8. Docker Compose 常用命令

```bash
docker compose up -d
docker compose ps
docker compose logs
docker compose logs -f web
docker compose down
docker compose down -v
```

---

## 9. 私有仓库 / HTTP 仓库支持

编辑 Docker 配置：

```bash
sudo vim /etc/docker/daemon.json
```

示例：

```json
{
  "insecure-registries": ["IP:PORT"]
}
```

重启 Docker：

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

## 10. 离线环境安装 Docker Compose ⭐⭐⭐

### 10.1 有外网机器下载

```bash
wget https://github.com/docker/compose/releases/download/v2.25.0/docker-compose-linux-x86_64
mv docker-compose-linux-x86_64 docker-compose
chmod +x docker-compose
tar czvf docker-compose-v2.25.0-linux-x86_64.tar.gz docker-compose
```

---

### 10.2 离线服务器安装

```bash
mkdir -p /usr/local/lib/docker/cli-plugins
tar zxvf docker-compose-v2.25.0-linux-x86_64.tar.gz
mv docker-compose /usr/local/lib/docker/cli-plugins/
```

验证：

```bash
docker compose version
```

---

## 11. 常见问题排查 ⭐⭐⭐

### Q1：端口打不开？

```bash
docker ps
docker logs <容器名>
```

---

### Q2：容器名冲突？

```bash
docker rm -f <容器名>
docker compose up -d
```

---

### Q3：容器不断重启？

```bash
docker logs <容器名>
```

---

## 12. ⚠ 危险操作（慎用）

> 以下操作 **不可逆**

### 清理未使用资源

```bash
docker container prune
docker image prune
```

### 清空 Docker（慎用）

```bash
docker system prune -a
```

---

## 13. 文档使用建议（非常重要）

### 推荐项目结构

```text
project/
├── docker-compose.yml
├── README.md
└── docs/
    └── Docker_通用使用说明.md
```

### README 中只做引用

```md
- Docker 使用说明：docs/Docker_通用使用说明.md
```

---

## 14. 结语

- 本文档 **可复制到任何项目直接使用**
- 建议作为 **团队统一 Docker 操作规范**
- 项目特殊内容请写入项目 README

