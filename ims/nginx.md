# Nginx 配置使用相关

## 1. nginx 配置

```
[root@ims-builder files]# cat /opt/ims/nginx/nginx.conf
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;     # ★ 必须添加
    default_type  application/octet-stream;  # ★ 避免无类型时一律 text/plain

    upstream ims_app {
        server ims-app:8000;
    }

    sendfile on;
    client_max_body_size 2G;

    # 上传和响应的超时时间都放宽
    client_body_timeout   600s;
    send_timeout          600s;
    proxy_connect_timeout 600s;
    proxy_send_timeout    600s;
    proxy_read_timeout    600s;

    server {
        listen 80;
        server_name _;

        location / {
            proxy_pass http://ims_app;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /static/ {
            alias /data/static/;
            autoindex off;
        }

        location /media/ {
            alias /data/media/;
            autoindex off;
        }

        location /reports/ {
            alias /data/reports/;
            autoindex off;
        }

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;
    }
}
```
## 2. ngxin 默认超时时间

```
client_max_body_size：默认 1m
client_body_timeout：默认 60s
client_header_timeout：默认 60s
keepalive_timeout：默认 75s
send_timeout：默认 60s
proxy_read_timeout: 默认一般是 60s
proxy_send_timeout: 默认一般是 60s
proxy_connect_timeout：默认一般是 60s
```

## 3. nginx配置查看和加载

```
查看当前的配置文件详情(会打印配置文件信息)
docker exec -it ims-nginx nginx -T | sed -n '1,200p'
```