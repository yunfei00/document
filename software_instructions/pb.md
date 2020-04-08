# 1 PB 2.6.1 安装
1. 解压源码文件（本例文件名为protobuf-2.6.1.zip）
	```
	unzip protobuf-2.6.1.zip
	```
2. 编译安装
```
# wget https://github.com/google/protobuf/archive/v3.5.1.tar.gz
cd protobuf-2.6.1
./autogen.sh
./configure --prefix=/usr/local/protobuf

make -j8 && make install

ldconfig
————————————————
版权声明：本文为CSDN博主「nudt_qxx」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xiangxianghehe/java/article/details/78928629
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbODY5NjYxNzQyXX0=
-->