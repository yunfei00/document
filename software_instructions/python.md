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

# Create virtualenv using Python3
virtualenv -p python3 myenv

# 安装指定版本python虚拟环境
virtualenv venv --p	ython=python3.7

# Active your virtual environment:
source venv/bin/activate

# To deactivate:
deactivate
```

# 3. python 安装
Step 1: Update and Refresh Repository Lists
```
sudo apt update
```
Step 2: Install Supporting Software
```
sudo apt install software-properties-common
```
Step 3: Add Deadsnakes PPA
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```
Step 4: Install Python 3
```
sudo apt install python3.8
```

# 4 __init__.py

`__init__.py`该文件的作用就是相当于把自身整个文件夹当作一个包来管理，每当有外部`import`的时候，就会自动执行里面的函数。

# 5. python环境问题
1. 解决apt-get /var/lib/dpkg/lock-frontend 问题

```
sudo rm /var/lib/dpkg/lock-frontend
sudo rm /var/lib/dpkg/lock
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMzNTg4MDIwNSwxOTMwMDY4MTMzLDEwMD
cwMjc1NzYsMTg1OTY5NjYwOCwtOTAxMzE5MTYzLDExNzY1MTM2
MTIsMTI5Nzk0MjYsMTM5NjQyOTU2NSwtMjAwNjI3NjkzN119
-->