# 加签验签流程
生成密钥 → 构建镜像 → 推送镜像 → 签名镜像 → 验签镜像


## 1. install cosign 
1️. 确认系统架构
```
[root@ims-builder opt]# uname -m
x86_64
```
x86_64 → 用 amd64
aarch64 → 用 arm64

2. 下载 Cosign（二进制）

这里直接在浏览器中下载是最快的
```
curl -Lo cosign https://github.com/sigstore/cosign/releases/latest/download/cosign-linux-amd64

如果你是 ARM：
curl -Lo cosign https://github.com/sigstore/cosign/releases/latest/download/cosign-linux-arm64
```

3️. 安装到系统路径

```
chmod +x cosign
sudo mv cosign /usr/local/bin/
```

4. 验证安装
```

[root@ims-builder opt]# cosign version
  ______   ______        _______. __    _______ .__   __.
 /      | /  __  \      /       ||  |  /  _____||  \ |  |
|  ,----'|  |  |  |    |   (----`|  | |  |  __  |   \|  |
|  |     |  |  |  |     \   \    |  | |  | |_ | |  . `  |
|  `----.|  `--'  | .----)   |   |  | |  |__| | |  |\   |
 \______| \______/  |_______/    |__|  \______| |__| \__|
cosign: A tool for Container Signing, Verification and Storage in an OCI registry.

GitVersion:    v2.6.1
GitCommit:     634fabe54f9fbbab55d821a83ba93b2d25bdba5f
GitTreeState:  clean
BuildDate:     2025-09-26T17:24:36Z
GoVersion:     go1.25.1
Compiler:      gc
Platform:      linux/amd64

```

## 2. 生成密钥
可以不输入密码
```
[root@ims-builder cosing]# cosign generate-key-pair
Enter password for private key:
Enter password for private key again:
Private key written to cosign.key
Public key written to cosign.pub
```
私钥：用来“签名镜像”（谁持有私钥谁能签）
公钥：用来“验证签名”（给任何人都行，用来验证你签的东西）

## 3. 加载镜像包
```
docker load -i test1.tar
4f2f013f2287: Loading layer [==================================================>]  14.36MB/14.36MB
4237b4abe0c5: Loading layer [==================================================>]  32.77kB/32.77kB
2f068437f777: Loading layer [==================================================>]  8.192kB/8.192kB
f35b128e1c88: Loading layer [==================================================>]  3.584kB/3.584kB
a965522c57cf: Loading layer [==================================================>]  3.072kB/3.072kB
b46567e40b11: Loading layer [==================================================>]  14.97MB/14.97MB
a69f7245d083: Loading layer [==================================================>]  79.36kB/79.36kB
9813ceecf3fd: Loading layer [==================================================>]  8.843MB/8.843MB
893a4e4d1516: Loading layer [==================================================>]  33.79kB/33.79kB
Loaded image: 49.7.180.245:31080/basic/aa:V8
```

## 4. 打tag
```
如果 docker images 里已经有正确 repo:tag，你可以跳过这一段。
镜像 ID 打 tag
docker tag sha256:a4fe32dc8664f1b5e7bd409a84e3519a145d8702a1ef31abdc225d78e7c91c1b  49.7.180.245:31080/basic/aa:V100

[root@ims-builder cosing]# docker images|grep V100
49.7.180.245:31080/basic/aa   V100       a4fe32dc8664   7 weeks ago    36.5MB
```

## 5. login and push
这一步拿到digest
```
docker login 49.7.180.245:31080
docker push 49.7.180.245:31080/basic/aa:V100
The push refers to repository [49.7.180.245:31080/basic/aa]
893a4e4d1516: Layer already exists
9813ceecf3fd: Layer already exists
a69f7245d083: Layer already exists
b46567e40b11: Layer already exists
a965522c57cf: Layer already exists
f35b128e1c88: Layer already exists
2f068437f777: Layer already exists
4237b4abe0c5: Layer already exists
4f2f013f2287: Layer already exists
V100: digest: sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146 size: 2196
[root@ims-builder cosing]#
```

## 6. 使用digest 签名

[root@ims-builder aa]# cosign sign   --key cosign.key   --allow-insecure-registry   --allow-http-registry   --tlog-upload=false   49.7.180.245:31080/basic/a@sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146
Enter password for private key:
Pushing signature to: 49.7.180.245:31080/basic/a
[root@ims-builder aa]#
[root@ims-builder aa]# cosign sign   --key cosign.key   --allow-insecure-registry   --allow-http-registry   --tlog-upload=false   49.7.180.245:31080/basic/aa@sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146
Enter password for private key:
Pushing signature to: 49.7.180.245:31080/basic/aa
[root@ims-builder aa]

## 7. 验签
```
[root@ims-builder aa]# cosign verify   --key cosign.pub   --allow-insecure-registry   --allow-http-registry   --insecure-ignore-tlog   49.7.180.245:31080/basic/a@sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146
WARNING: Skipping tlog verification is an insecure practice that lacks transparency and auditability verification for the signature.

Verification for 49.7.180.245:31080/basic/a@sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146 --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - The signatures were verified against the specified public key

[{"critical":{"identity":{"docker-reference":"49.7.180.245:31080/basic/a"},"image":{"docker-manifest-digest":"sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146"},"type":"cosign container image signature"},"optional":null}]
[root@ims-builder aa]# cosign verify   --key cosign.pub   --allow-insecure-registry   --allow-http-registry   --insecure-ignore-tlog   49.7.180.245:31080/basic/aa@sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146
WARNING: Skipping tlog verification is an insecure practice that lacks transparency and auditability verification for the signature.

Verification for 49.7.180.245:31080/basic/aa@sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146 --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - The signatures were verified against the specified public key

[{"critical":{"identity":{"docker-reference":"49.7.180.245:31080/basic/aa"},"image":{"docker-manifest-digest":"sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146"},"type":"cosign container image signature"},"optional":null}]
[root@ims-builder aa]#
``` 

## 8. 列出签名（仓库可能不展示签名文件 看不到）
```

[root@ims-builder aa]# cosign tree   --allow-insecure-registry   --allow-http-registry   49.7.180.245:31080/basic/aa@sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146
📦 Supply Chain Security Related artifacts for an image: 49.7.180.245:31080/basic/aa@sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146
└── 🔐 Signatures for an image tag: 49.7.180.245:31080/basic/aa:sha256-a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146.sig
   ├── 🍒 sha256:9e0375bca6d927f2cc39a83a26a16e8df3b35879f035f68209d6a18bc1f16a0a
   └── 🍒 sha256:9e0375bca6d927f2cc39a83a26a16e8df3b35879f035f68209d6a18bc1f16a0a

[root@ims-builder aa]# cosign tree   --allow-insecure-registry   --allow-http-registry   49.7.180.245:31080/basic/a@sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146
📦 Supply Chain Security Related artifacts for an image: 49.7.180.245:31080/basic/a@sha256:a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146
└── 🔐 Signatures for an image tag: 49.7.180.245:31080/basic/a:sha256-a7d517b288030b8a904584ace91b3d5228c64b7e0a3cabadd1c6747190867146.sig
   ├── 🍒 sha256:80f13cf1921075217180a931b13319d0a15ca7af26a965cf9e20ee2b5a02c922
   └── 🍒 sha256:80f13cf1921075217180a931b13319d0a15ca7af26a965cf9e20ee2b5a02c922
[root@ims-builder aa]#
```





