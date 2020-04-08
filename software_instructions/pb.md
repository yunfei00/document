# 1 ubuntu 16.04 安装PB 2.6.1 
1. 解压源码文件（本例文件名为protobuf-2.6.1.zip）
	```
	unzip protobuf-2.6.1.zip
	```
2. 编译安装
	```
	# wget https://github.com/google/protobuf/archive/v3.5.1.tar.gz
	cd protobuf-2.6.1
	./autogen.sh                    # 自动配置
	./configure --prefix=/usr/local/protobuf   # 安装到指定路径
	make -j8 && make install   编译安装库
	ldconfig   # 加载库
	```
3. 安装过程中的依赖库问题
	

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUzMDEyMjI1XX0=
-->