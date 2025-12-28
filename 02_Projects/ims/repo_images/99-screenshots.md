# 镜像处理流程


## 1. 基础镜像上传流程

-   界面，用户选项为：仓库 名称 版本 文件  分类 描述
-   界面上传后，


## 2. 业务镜像上传流程

-   界面，用户选项为：项目 名称 版本 文件 仓库 分类 描述
-   

## 2. 镜像下载流程

## 3. 镜像加签


## 4. 镜像检测报告
镜像上传后，默认会生成报告 基础镜像和业务镜像相同

根据镜像关联的镜像仓库id,获取该仓库中的所有镜像信息
```
curl -H 'Content-Type: application/json' -H 'accept: application/json' -X POST -u 'xstest2:9Q{]ru2d)<K7gZ>S' http://49.7.180.245:31080/api/v1/artifact/repo/file/list -d '{"deleted": false,"repo_id":1495097876821574}'

{"code":"OK","body":{"pre":".","list":[{"dir":1,"name":"aa","path":"basic/aa"},{"dir":1,"name":"test","path":"basic/test"},{"dir":1,"name":"ubuntu","path":"basic/ubuntu"}]}}

```
获取镜像版本
```
curl -H 'Content-Type: application/json' -H 'accept: application/json' -X POST -u 'xstest2:9Q{]ru2d)<K7gZ>S' http://49.7.180.245:31080/api/v1/artifact/repo/file/list -d '{"deleted": false,"repo_id":1495097876821574,"path":"basic/aa"}'


{"code":"OK","body":{"pre":"basic","list":[{"dir":1,"name":"06","path":"basic/aa/06"},{"dir":1,"name":"100","path":"basic/aa/100"},{"dir":1,"name":"V5","path":"basic/aa/V5"},{"dir":1,"name":"V7","path":"basic/aa/V7"},{"dir":1,"name":"V8","path":"basic/aa/V8"},{"dir":1,"name":"aa01","path":"basic/aa/aa01"},{"dir":1,"name":"aa02","path":"basic/aa/aa02"},{"dir":1,"name":"aa03","path":"basic/aa/aa03"},{"dir":1,"name":"aa04","path":"basic/aa/aa04"},{"dir":1,"name":"aa05","path":"basic/aa/aa05"}]}}
[root@ims-builder opt]#
```
下载对应版本检测报告
```
curl -u 'xstest2:9Q{]ru2d)<K7gZ>S' "http://49.7.180.245:31080/api/v1/artifact/repo/file/scanreport?repo_id=1495097876821574&path=basic%aa%aa03%2Fmanifest.json" --output out.xlsx

获取检测报告失败：500 Server Error: Internal Server Error for url: http://49.7.180.245:31080/api/v1/artifact/repo/file/scanreport?repo_id=1495097876821574&path=basic%2Fubuntu%2FV1%2Fmanifest.json

curl -u 'xstest2:9Q{]ru2d)<K7gZ>S' "http://49.7.180.245:31080/api/v1/artifact/repo/file/scanreport?repo_id=1495097876821574&path=basic%2Fubuntu%2FV1%2Fmanifest.json" --output out.xlsx
```

总结，下载测试报告直接就可以请求一个地址查看
地址主要是四个参数:repo_id, repo_name, image_name, image_version，有时候没有生成，也要有对应的处理

