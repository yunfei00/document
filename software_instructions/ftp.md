# 1 ubuntu下ftp服务器搭建
ubuntu下ftp服务器搭建：
概念：
    FTP服务器（File Transfer Protocol Server）是在互联网上提供文件存储和访问服务的计算机，它们依照FTP协议提供服务。
    FTP是File Transfer Protocol(文件传输协议)。顾名思义，就是专门用来传输文件的协议。简单地说，支持FTP协议的服务器就是FTP服务器。
搭建ftp服务器，首先要选择ftp服务器软件。
FileZilla
是一款经典的开源FTP解决方案，包括FileZilla客户端和FileZillaServer。其中，FileZillaServer的功能比起商业软件FTP Serv-U毫不逊色。无论是传输速度还是安全性方面，都是非常优秀的一款。
VsFTP
VSFTP是一个基于GPL发布的类Unix系统上使用的FTP服务器软件，它的全称是Very Secure FTP 从此名称可以看出来，编制者的初衷是代码的安全。
安全性是编写VSFTP的初衷，除了这与生俱来的安全特性以外，高速与高稳定性也是VSFTP的两个重要特点。
在速度方面，使用ASCII代码的模式下载数据时，VSFTP的速度是Wu-FTP的两倍，如果Linux主机使用2.4.*的内核，在千兆以太网上的下载速度可达86MB/S。
在稳定方面，VSFTP就更加的出色，VSFTP在单机（非集群）上支持4000个以上的并发用户同时连接，根据Red Hat的Ftp服务器的数据，VSFTP服务器可以支持15000个并发用户.

下面具体讲述一下ubuntu下vsftpd软件
1. 下载vsftpd软件
	```
	sudo apt-get install vsftpd
	vsftpd -v  //查看版本
	```
2. 配置vsftpd.conf文件，具体的可以看里面的说明。这里采用默认配置。
	```
	sudo vim /etc/vsftpd.conf
	```
3. 添加FTP用户
	```
	//建立ftp文件夹
	sudo useradd -d /home/ubuntu/ftp -s /bin/bash username
	//设置密码（username为用户名）
	sudo passwd username
	//如果需要删除用户,可以使用如下命令：
	userdel username
	```
4. 启动ftp服务
	```
	sudo service vsftpd start
	```
5. 访问ftp服务器
访问ftp服务器需要有ftp客户端软件：
windows下访问，可以使用FileZilla
如果遇到
ftp: connect: Connection refused
则使用如下命令删除并重新安装：
	```
	sudo apt-get remove --purge vsftpd
	sudo apt-get install vsftpd
	```
	linux下也可以直接使用ftp命令进行访问。当然还要学习一些ftp命令。
	关于适用shell脚本调用ftp服务，后期推出脚本。

# 2 在Centos下搭建Ftp服务

1. 检查是否安装 了vsftpd，如果未安装 则安装vsftpd。
```
查看系统中是否安装了vsftpd rpm -qa | grep vsftpd

2）如果没有安装 vsftpd，则安装 ：yum -y install vsftpd
```
2、创建ftp用户，比如ftp_test。命令：useradd -s /sbin/nologin -d /home/ftp_test ftp_test
useradd -s /sbin/nologin -d /home/ftp_server ftp_user
注意：

1）目录尽量不要选择根目录下，这里是/home/ftp_test，并且ftp_test这个目录不要手动创建，否则权限会有问题，执行命令的时候会自动创建

2）注意目录的权限，如果有需要，应该设置相应的权限

3、为ftp_test用户创建密码。命令：passwd ftp_test
密码 a82865348

执行之后输入2次密码确认就设置好了密码。

4、编辑vsftpd配置文件，命令:vim /etc/vsftpd/vsftpd.conf

找到anonymous_enable这个配置项，默认是YES，修改成NO，表示不允许匿名用户登录。

5、启动vsftp服务，命令：systemctl start vsftpd.service

6、查看ftp服务的状态，命令：systemctl status vsftpd.service

7、用ftp客户端进行连接访问。

 

参考：https://www.cnblogs.com/freeweb/p/6518257.html

ftp服务的开启与关闭命令：

开启：# service vsftpd start

关闭：# service vsftpd stop

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNDkzNDQ5MDhdfQ==
-->