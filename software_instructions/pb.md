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
3. 增加库文件路径
	```
	到此步还没有安装完毕，在/etc/profile 或者用户目录 ~/.bashrc 
	添加下面内容
	####### add protobuf lib path ########
	#(动态库搜索路径) 程序加载运行期间查找动态链接库时指定除了系统默认路径之外的其他路径
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/protobuf/lib/
	#(静态库搜索路径) 程序编译期间查找动态链接库时指定查找共享库的路径
	export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/protobuf/lib/
	#执行程序搜索路径
	export PATH=$PATH:/usr/local/protobuf/bin/
	#c程序头文件搜索路径
	export C_INCLUDE_PATH=$C_INCLUDE_PATH:/usr/local/protobuf/include/
	#c++程序头文件搜索路径
	export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/local/protobuf/include/
	#pkg-config 路径
	export PKG_CONFIG_PATH=/usr/local/protobuf/lib/pkgconfig/
	```
4. 加载配置文件并查看版本
	```
	.  ~/.bashrc
	protoc --version   
	libprotoc 2.6.1
	```
5. 安装过程中的依赖库问题
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


# 2  同时安装多个版本的pb

此处以3.17.0和2.
```
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMDIxNTYxMjMsLTM5ODI5MTk4MCwxMz
g5NDk2MjEzLC0xODg3NzUzMDkxXX0=
-->