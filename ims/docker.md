# docker 使用问题
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