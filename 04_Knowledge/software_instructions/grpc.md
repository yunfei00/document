# 1 ubuntu 18.04 安装grpc

1. 按照官网安装说明进行安装
[参考链接](https://grpc.io/docs/languages/cpp/quickstart/)

2. 注意事项
cmake默认版本为3.10.0，版本较低，使用源码进行安装
下载安装包，cmake-3.20.2.tar.gz，然后进行解压安装，并加载

protobuf也不要搞成兼容的版本，不然以来有问题，使用源码进行安装

3. 安装完成后，错误信息

3.1 fatal error: absl/synchronization/mutex.h: No such file or directory

解决方案：
sudo cp -r  ~/.local/grpc/third_party/abseil-cpp/absl /usr/local/include/

# 2 python

# 3 c++
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTEyMzE4NjM2OSwtNDkxOTMxMDE3XX0=
-->