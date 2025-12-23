# 这里是新环境的配置


## 1. 安装docker

移除旧的 docker repo（如果之前添加过）
```
rm -f /etc/yum.repos.d/docker-ce.repo
```

使用阿里云的 Docker CE 镜像源

```
cat > /etc/yum.repos.d/docker-ce.repo << 'EOF'
[docker-ce-stable]
name=Docker CE Stable - $basearch - aliyun
baseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/$basearch/stable
enabled=1
gpgcheck=0

[docker-ce-stable-source]
name=Docker CE Stable - Sources - aliyun
baseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/source/stable
enabled=0
gpgcheck=0
EOF
```

清理缓存重新生成
```
yum clean all
yum makecache
```

安装 Docker（不会再卡了）
```
yum install -y docker-ce docker-ce-cli containerd.io
```

阿里云的镜像源非常稳定，不会出现 curl#35 中断问题。

如果你依然遇到问题，再尝试以下两个快速修复

```
[root@iZbp1bo9ai6t6ah3qqa0xbZ ~]# docker --version
Docker version 26.1.4, build 5650f9b
```

使用系统管理  拉起docker
```
systemctl start docker
```


## 2. 安装git 

```
sudo yum install -y git
git --version
```

## 3. 拷贝编译工具

需要有如下工具
```
[root@ims-builder ~]# cd /opt/tools/
[root@ims-builder tools]# ls
cosign-linux-amd64  docker  spotbugs-4.9.8
[root@ims-builder tools]#
```

## 4. 支持git 免密下载
参考git.md

## 5. docker 源配置
不配置下面命令会失败
```
docker pull python:3.11-slim


[root@ims-builder ~]# cat /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://dockerproxy.com",
    "https://docker.m.daocloud.io",
    "https://hub-mirror.c.163.com",
    "https://docker.xuanyuan.me"
  ],
"insecure-registries": ["49.7.180.245:31080"]
}
```

## 6. 上传文件
