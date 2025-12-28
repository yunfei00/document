# docker 使用问题

## 0. docker 常用命令汇总

1. 查看信息类
```
docker version          # 查看 Docker 版本
docker info             # 查看 Docker 整体信息
docker ps               # 查看正在运行的容器
docker ps -a            # 查看所有容器（包含已停止）
docker images           # 查看本地镜像
docker network ls       # 查看网络
docker volume ls        # 查看数据卷
```

2. 镜像（image）相关
```
# 查找镜像
docker search nginx                     # 从 Docker Hub 搜索镜像

# 拉取镜像
docker pull nginx                       # 拉取最新版本
docker pull nginx:1.27-alpine          # 拉取指定 tag

# 导出 / 导入 镜像（离线用得多）
docker save nginx:1.27-alpine -o nginx_1.27_alpine.tar
docker load -i nginx_1.27_alpine.tar

# 删除镜像
docker rmi nginx                        # 删除镜像
docker rmi nginx:1.27-alpine            # 删除指定 tag
docker image prune                      # 删除无用镜像（dangling）
docker image prune -a                   # 删除所有无容器使用的镜像（慎用）
```

3. 容器（container）生命周期
```
# 创建并运行一个容器（最常用）
docker run --name my-nginx -d -p 8080:80 nginx

# 常见参数说明：
# -d             后台运行
# --name         指定容器名字
# -p 宿主:容器    端口映射
# -v 宿主:容器    目录挂载
# --restart      重启策略（如 unless-stopped）

# 启动 / 停止 / 重启
docker start my-nginx
docker stop my-nginx
docker stop d37578585436
docker restart my-nginx

# 查看容器日志
docker logs my-nginx
docker logs -f my-nginx        # 实时滚动日志（类似 tail -f）
docker logs --tail 100 my-nginx

# 查看容器资源使用
docker top my-nginx
docker stats                   # 所有容器实时资源占用

# 进入容器（调试必备）
docker exec -it my-nginx /bin/bash     # bash
docker exec -it my-nginx /bin/sh       # 有的镜像只有 sh

# 文件复制
docker cp my-nginx:/etc/nginx/nginx.conf ./
docker cp ./local.conf my-nginx:/etc/nginx/conf.d/

# 容器改名
docker rename my-nginx nginx-web

# 导出 / 导入 容器（不太常用）
docker export my-nginx -o my-nginx.tar
cat my-nginx.tar | docker import - my-nginx-image:latest

# 删除容器
docker rm my-nginx            # 删除已停止容器
docker rm -f my-nginx         # 强制删除（包含正在运行）
docker container prune        # 清理所有已停止容器
```

4. 构建镜像（Dockerfile）
```
# 在当前目录的 Dockerfile 构建镜像
docker build -t myapp:1.0 .

# 指定 Dockerfile
docker build -f deploy/Dockerfile -t myapp:1.0 .

# 给镜像打标签
docker tag myapp:1.0 my-registry/myapp:1.0
```

5. 网络与端口
```
# 创建自定义网络（建议：一个系统建一个 bridge 网络）
docker network create ims-net

# 运行容器并加入自定义网络
docker run -d --name db --network ims-net mysql:8

# 将已有容器连接到网络
docker network connect ims-net my-nginx

# 查看容器网络信息
docker inspect my-nginx | grep -i ipaddress -n
docker network inspect ims-net
```

6. 数据卷（volume）与挂载
```
# 创建数据卷
docker volume create ims-db-data

# 使用数据卷（容器内部 /var/lib/mysql）
docker run -d --name db \
  -v ims-db-data:/var/lib/mysql \
  mysql:8

# 直接挂载宿主目录
docker run -d --name ims-app \
  -v /opt/ims_data/media:/app/media \
  -v /opt/ims_data/db:/app/db \
  ims-app:1.0

# 查看 / 删除数据卷
docker volume ls
docker volume inspect ims-db-data
docker volume rm ims-db-data
docker volume prune       # 清理无容器使用的数据卷
```

7. 查看&排错相关命令
```
# 查看容器详细信息（环境变量、挂载、网络等）
docker inspect my-nginx

# 查看容器内某个文件大小/结构
docker exec my-nginx ls -lh /etc/nginx/

# 在一条命令内执行临时容器调试
docker run --rm -it alpine:latest sh

# 清理系统垃圾（谨慎使用）
docker system df          # 查看占用
docker system prune       # 清理未用数据（有提示）
docker system prune -a    # 包含未用镜像（更狠）
```

8. Docker Compose（如果你在用的话）
```
# 启动（后台）
docker compose up -d

# 查看状态
docker compose ps

# 查看日志
docker compose logs
docker compose logs -f web     # 指定服务

# 停止 / 删除
docker compose stop
docker compose down            # 关闭并删除容器、网络等
docker compose down -v         # 同时删除卷（慎用）
```

## 1. 进入docker 镜像 
  ```
  docker exec -it ims-app bash
  ```

## 2. 看django 容器日志
  ```
  docker logs ims-app
  docker logs ims-app | tail -n 100
  docker logs --since 10m ims-app | tail -n 200


  docker logs ims-nginx | tail -n 50

  其他日志查看
  tail -n 200 /opt/ims/logs/nginx/error.log


  ```

## 3. 拷贝文件
  ```
  docker cp /usr/bin/docker ims-app:/usr/local/bin/docker
  ```

## 4. docker 重启服务
  ```
  docker restart ims-nginx

  ``` 

## 5. docker http支持

  ```
  sudo vim /etc/docker/daemon.json
  ```

  如果这个文件是空的，可以直接写成：

  ```
  {
    "insecure-registries": ["49.7.180.245:31080"]
  }
  ```


如果里面已经有内容（比如 registry-mirrors 之类），就合并一下，例如：
  ```
  {
    "registry-mirrors": [
      "https://your.mirror.com"
    ],
    "insecure-registries": [
      "49.7.180.245:31080"
    ]
  }
  ```

重启宿主机 docker 服务
```
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## 6. 删除docker 镜像

先停止并删除所有容器（否则镜像删不掉）
```
docker images -aq | xargs -r docker rmi -f
```

删除所有镜像
```
docker images -aq | xargs -r docker rmi -f
```

## 7. 离线安装docker compose

1. 在「有外网的机器」准备离线文件 下载 docker-compose v2 二进制（Linux x86_64 版本建议：v2.25.0（稳定、兼容 Docker 26）
  ```
  mkdir -p docker_compose_offline
  cd docker_compose_offline

  wget https://github.com/docker/compose/releases/download/v2.25.0/docker-compose-linux-x86_64
  ```
2. 重命名（这是 plugin 规范）
```
  mv docker-compose-linux-x86_64 docker-compose
  chmod +x docker-compose
  ```
3. 打包带走
```
tar czvf docker-compose-v2.25.0-linux-x86_64.tar.gz docker-compose
```

4. 在「离线服务器（CentOS 7.9）」安装
```
scp docker-compose-v2.25.0-linux-x86_64.tar.gz root@服务器:/opt/
```

5. 解压并安装到 Docker plugin 目录
```
cd /opt
tar zxvf docker-compose-v2.25.0-linux-x86_64.tar.gz

mkdir -p /usr/local/lib/docker/cli-plugins
mv docker-compose /usr/local/lib/docker/cli-plugins/
```

6. 验证
```
docker compose version
Docker Compose version v2.25.0
```

## 8. docker compose 启动程序

启动进程  需要当前路径下有 docker-compose.yml 文件
```
[root@ims-builder files]# docker compose up -d
[+] Running 4/4
 ✔ Container ims-redis   Running           0.0s
 ✔ Container ims-app     Started           0.6s
 ✔ Container ims-nginx   Running           0.0s
 ✔ Container ims-worker  Started           0.4s
```

1. 容器名称冲突

```
docker compose up
[+] Running 1/0
 ✔ Container ims-redis  Running                                                                                          0.0s
 ⠋ Container ims-app    Creating                                                                                         0.0s
Error response from daemon: Conflict. The container name "/ims-app" is already in use by container "d99e2be7047ed5bf6b70ba5e95e2ad403faf098f9db54c2e9ca8351eacfadce1". You have to remove (or rename) that container to be able to reuse that name.
```

docker-compose.yml 里指定了 container_name: ims-app，但宿主机上已经有一个同名容器 ims-app（ID 以 d99e2b… 开头）在占用

处理方案:
删掉旧的 ims-app 容器，再 compose up
```
docker ps -a --filter "name=^/ims-app$"
docker rm -f ims-app
docker compose up -d
```

2. 彻底清掉旧容器
```
docker rm -f ims-nginx ims-app ims-worker ims-redis
确认干净：
docker ps | grep ims
```

3. 删除旧的 ims-net 网络
```
docker network rm ims-net
```

