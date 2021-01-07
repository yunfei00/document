# 1 CentOS python3安装
1. python3 install (源码安装)

	安装必要工具 yum-utils ，它的功能是管理repository及扩展包的工具 (主要是针对repository)
    ```
    yum install yum-utils
    yum install libffi-devel -y
    yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make
    ```
   使用yum-builddep为Python3构建环境,安装缺失的软件依赖,使用下面的命令会自动处理.
    ```
    yum-builddep python
    ```
    [官网获取源码](https://www.python.org/downloads/release/python-381/)后，执行以下命令进行安装，并查看版本
    ```
    tar xf Python-3.8.1.tgz
    cd Python-3.8.1/
    ./configure 
    make
    make install
    python3 -V
    ```
# 2 安装虚拟环境

```
sudo pip3 install virtualenv 

# Now create a virtual environment
virtualenv venv 

# you can use any name insted of **venv**
virtualenv -p /usr/bin/python2.7 venv

# Active your virtual environment:
source venv/bin/activate



```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU1MjMzMjYxLDEyOTc5NDI2LDEzOTY0Mj
k1NjUsLTIwMDYyNzY5MzddfQ==
-->