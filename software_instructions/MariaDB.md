# 1 MariaDB 说明
MariaDB数据库管理系统是MySQL的一个分支，主要由开源社区在维护，采用GPL授权许可 MariaDB的目的是完全兼容MySQL，包括API和命令行，使之能轻松成为MySQL的代替品。在存储引擎方面，使用XtraDB（英语：XtraDB）来代替MySQL的InnoDB。 MariaDB由MySQL的创始人Michael Widenius（英语：Michael Widenius）主导开发，他早前曾以10亿美元的价格，将自己创建的公司MySQL AB卖给了SUN，此后，随着SUN被甲骨文收购，MySQL的所有权也落入Oracle的手中。MariaDB名称来自Michael Widenius的女儿Maria的名字。

MariaDB基于[事务](https://baike.baidu.com/item/%E4%BA%8B%E5%8A%A1/5945882)的Maria[存储引擎](https://baike.baidu.com/item/%E5%AD%98%E5%82%A8%E5%BC%95%E6%93%8E/8969956)，替换了[MySQL](https://baike.baidu.com/item/MySQL)的[MyISAM](https://baike.baidu.com/item/MyISAM)存储引擎，它使用了Percona的 XtraDB，InnoDB的变体，分支的开发者希望提供访问即将到来的MySQL 5.4 InnoDB性能。这个版本还包括了 PrimeBase XT (PBXT) 和 FederatedX[存储引擎](https://baike.baidu.com/item/%E5%AD%98%E5%82%A8%E5%BC%95%E6%93%8E)。

# 2 在CentOS 7上安装MariaDB
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


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MTQyMzM2NDRdfQ==
-->