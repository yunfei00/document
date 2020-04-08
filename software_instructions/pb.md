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
	make   # 编译库
	sudo make install   # 安装库
	sudo ldconfig   # 加载库
	```
3. 安装过程中的依赖库问题
	- ./autogen.sh: 38: ./autogen.sh: autoreconf: not found
	安装依赖库
	```
	sudo apt-get install autoconf
	```
	- Can't exec "libtoolize": No such file or directory at /usr/share/autoconf/Autom4te/FileUtils.pm line 345, <GEN7> line 6.
autoreconf: failed to run libtoolize: No such file or directory
autoreconf: libtoolize is needed because this package uses Libtool
	安装对应软件
	```
	sudo apt-get install libtool
	```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4ODc3NTMwOTFdfQ==
-->