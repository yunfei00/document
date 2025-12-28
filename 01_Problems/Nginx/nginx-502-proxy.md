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

## 3. 查看当前的配置文件详情(会打印配置文件信息)
```
docker exec -it ims-nginx nginx -T | sed -n '1,200p'
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
# configuration file /etc/nginx/nginx.conf:
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


# configuration file /etc/nginx/mime.types:

types {
    text/html                                        html htm shtml;
    text/css                                         css;
    text/xml                                         xml;
    image/gif                                        gif;
    image/jpeg                                       jpeg jpg;
    application/javascript                           js;
    application/atom+xml                             atom;
    application/rss+xml                              rss;

    text/mathml                                      mml;
    text/plain                                       txt;
    text/vnd.sun.j2me.app-descriptor                 jad;
    text/vnd.wap.wml                                 wml;
    text/x-component                                 htc;

    image/avif                                       avif;
    image/png                                        png;
    image/svg+xml                                    svg svgz;
    image/tiff                                       tif tiff;
    image/vnd.wap.wbmp                               wbmp;
    image/webp                                       webp;
    image/x-icon                                     ico;
    image/x-jng                                      jng;
    image/x-ms-bmp                                   bmp;

    font/woff                                        woff;
    font/woff2                                       woff2;

    application/java-archive                         jar war ear;
    application/json                                 json;
    application/mac-binhex40                         hqx;
    application/msword                               doc;
    application/pdf                                  pdf;
    application/postscript                           ps eps ai;
    application/rtf                                  rtf;
    application/vnd.apple.mpegurl                    m3u8;
    application/vnd.google-earth.kml+xml             kml;
    application/vnd.google-earth.kmz                 kmz;
    application/vnd.ms-excel                         xls;
    application/vnd.ms-fontobject                    eot;
    application/vnd.ms-powerpoint                    ppt;
    application/vnd.oasis.opendocument.graphics      odg;
    application/vnd.oasis.opendocument.presentation  odp;
    application/vnd.oasis.opendocument.spreadsheet   ods;
    application/vnd.oasis.opendocument.text          odt;
    application/vnd.openxmlformats-officedocument.presentationml.presentation
                                                     pptx;
    application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
                                                     xlsx;
    application/vnd.openxmlformats-officedocument.wordprocessingml.document
                                                     docx;
    application/vnd.wap.wmlc                         wmlc;
    application/wasm                                 wasm;
    application/x-7z-compressed                      7z;
    application/x-cocoa                              cco;
    application/x-java-archive-diff                  jardiff;
    application/x-java-jnlp-file                     jnlp;
    application/x-makeself                           run;
    application/x-perl                               pl pm;
    application/x-pilot                              prc pdb;
    application/x-rar-compressed                     rar;
    application/x-redhat-package-manager             rpm;
    application/x-sea                                sea;
    application/x-shockwave-flash                    swf;
    application/x-stuffit                            sit;
    application/x-tcl                                tcl tk;
    application/x-x509-ca-cert                       der pem crt;
    application/x-xpinstall                          xpi;
    application/xhtml+xml                            xhtml;
    application/xspf+xml                             xspf;
    application/zip                                  zip;

    application/octet-stream                         bin exe dll;
    application/octet-stream                         deb;
    application/octet-stream                         dmg;
    application/octet-stream                         iso img;
    application/octet-stream                         msi msp msm;

    audio/midi                                       mid midi kar;
    audio/mpeg                                       mp3;
    audio/ogg                                        ogg;
    audio/x-m4a                                      m4a;
    audio/x-realaudio                                ra;

    video/3gpp                                       3gpp 3gp;
    video/mp2t                                       ts;
    video/mp4                                        mp4;
    video/mpeg                                       mpeg mpg;
    video/quicktime                                  mov;
    video/webm                                       webm;
    video/x-flv                                      flv;
    video/x-m4v                                      m4v;
    video/x-mng                                      mng;
    video/x-ms-asf                                   asx asf;
    video/x-ms-wmv                                   wmv;
    video/x-msvideo                                  avi;
}
```

## 4. 检查nginx配置和加载
```
[root@ims-builder files]# docker exec -it ims-nginx nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
[root@ims-builder files]# docker exec -it ims-nginx nginx -s reload
```
