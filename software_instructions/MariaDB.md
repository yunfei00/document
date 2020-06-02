# 1 MariaDB 说明
MariaDB数据库管理系统是MySQL的一个分支，主要由开源社区在维护，采用GPL授权许可 MariaDB的目的是完全兼容MySQL，包括API和命令行，使之能轻松成为MySQL的代替品。在存储引擎方面，使用XtraDB（英语：XtraDB）来代替MySQL的InnoDB。 MariaDB由MySQL的创始人Michael Widenius（英语：Michael Widenius）主导开发，他早前曾以10亿美元的价格，将自己创建的公司MySQL AB卖给了SUN，此后，随着SUN被甲骨文收购，MySQL的所有权也落入Oracle的手中。MariaDB名称来自Michael Widenius的女儿Maria的名字。

MariaDB基于[事务](https://baike.baidu.com/item/%E4%BA%8B%E5%8A%A1/5945882)的Maria[存储引擎](https://baike.baidu.com/item/%E5%AD%98%E5%82%A8%E5%BC%95%E6%93%8E/8969956)，替换了[MySQL](https://baike.baidu.com/item/MySQL)的[MyISAM](https://baike.baidu.com/item/MyISAM)存储引擎，它使用了Percona的 XtraDB，InnoDB的变体，分支的开发者希望提供访问即将到来的MySQL 5.4 InnoDB性能。这个版本还包括了 PrimeBase XT (PBXT) 和 FederatedX[存储引擎](https://baike.baidu.com/item/%E5%AD%98%E5%82%A8%E5%BC%95%E6%93%8E)。

# 2 在CentOS 7上安装MariaDB
## 第1步-安装MariaDB
1. 将使用Yum安装MariaDB软件包
```
sudo yum install mariadb-server
```
2. 安装完成后，我们将使用以下命令启动守护程序
```
sudo systemctl start mariadb
```
3. `systemctl` 不会显示所有服务管理命令的结果，因此为确保成功，我们将使用以下命令
```
sudo systemctl status mariadb
# 如果MariaDB已成功启动，则输出应包含“ Active：活动（正在运行）
```
4. `systemctl enable`命令创建MariaDB，该命令将创建必要的符号链接，以确保MariaDB在启动时启动。
```
sudo systemctl enable mariadb
```
## 第2步-保护MariaDB服务器
MariaDB包含一个安全脚本，用于更改一些不太安全的默认选项，例如远程root登录和样本用户。使用此命令运行安全脚本:
```
sudo mysql_secure_installation
```
该脚本为每个步骤提供了详细的说明。第一个提示要求输入root密码（尚未设置），因此我们将按`ENTER`。接下来，将提示我们设置该根密码，我们将这样做。

然后，通过按`Y`，然后`ENTER`接受其余的提示，我们将接受所有安全建议，这将删除匿名用户，禁止远程root登录，删除测试数据库并重新加载特权表。

最后，既然我们已经确保了安装的安全，我们将验证其是否正常运行。

## 第3步-测试安装
我们可以通过连接该`mysqladmin`工具来验证我们的安装并获取有关该工具的信息，该工具可让您运行管理命令。使用以下命令以**root**（`-u root`）身份连接到MariaDB ，提示输入密码（`-p`），然后返回版本。
```
[root@VM_0_4_centos ~]# mysqladmin -u root -p version
Enter password: 
mysqladmin  Ver 9.0 Distrib 5.5.65-MariaDB, for Linux on x86_64
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Server version		5.5.65-MariaDB
Protocol version	10
Connection		Localhost via UNIX socket
UNIX socket		/var/lib/mysql/mysql.sock
Uptime:			58 min 41 sec

Threads: 1  Questions: 26  Slow queries: 0  Opens: 1  Flush tables: 2  Open tables: 27  Queries per second avg: 0.007

```
# 3 配置MariaDB进行远程客户端访问

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ1NjkxNzgyOCwtNzk5MzAwMDJdfQ==
-->