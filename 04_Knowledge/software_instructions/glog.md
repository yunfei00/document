1. 下载安装：
拷贝svn上的glog进行编译安装
//git clone https://github.com/google/glog.git
sudo apt-get install autoconf automake libtool
cd glog
./autogen.sh  
./configure
make
sudo make install

2. 直接安装
```
sudo apt-get install -y libgoogle-glog-dev
```
3. 使用
g++ test.cpp -o test -lglog -lpthread



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM3MDczMzM0LC02Mjk3NzQ3NjgsNzMwOT
k4MTE2XX0=
-->