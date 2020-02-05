# 1 mysql install in mac
# 2 mac 上忘记mysql密码的处理
## 2.1 查询找到密码
1. 点击系统偏好设置中左下角的MySQL，并单击"Stop MySQL Server"。
2. 打开终端进入mysql安装路径，登录管理员权限
	```
	cd /usr/local/mysql/bin/
	sudo su
	``` 
3. 输入跳过mysql安全认证的命令 
	```
	./mysqld_safe --skip-grant-tables &
	```
	在第一步的mysql设置的画面中发现，关闭的mysql server 又重新变成running了。
4. 进入mysql ,并刷新权限
	```
	./mysql
	FLUSH PRIVILEGES;
	```
5. 查看用户名密码
	```
	mysql> select User,authentication_string from mysql.user;
	+---------------+-------------------------------------------+
	| User          | authentication_string                     |
	+---------------+-------------------------------------------+
	| root          | *94BDCEBE19083CE2A1F959FD02F964C7AF4CFC29 |
	| mysql.session | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
	| mysql.sys     | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
	+---------------+-------------------------------------------+
	3 rows in set (0.00 sec)
	```
	用户名为root，密码是经过md5加密的，可以在[md5在线解密](https://www.cmd5.com)网站进行解密查看。
	如果可以找到密码，那么就可以使用密码登录了。
	```
	mysql -u root -p
	```
## 2.2 找到密码后，重置密码
1. 进入安装目录,登录管理员权限
	```
	 cd /usr/local/mysql/bin/
	 sudo su 
	```
2. 登录mysql  
	```
	mysql -u root -p 输入密码 
	```

3. 修改密码
	```
	update mysql.user set authentication_string = PASSWORD('123456') where User = 'root';
	```
4. 刷新权限,再退出
	```
	FLUSH PRIVILEGES;
	quit 
	```

5. 重新登录 mysql ,输入密码 123456,登录成功
	```
	mysql -u root -p 
	```
## 2.3 不知道密码，重置密码

1. 停止mysql服务 
	```
	sudo /usr/local/mysql/support-files/mysql.server stop
	```
2. 进入安装目录 
	```
	cd /usr/local/mysql/bin
	```

3. 禁止mysql安全验证  
	```
	sudo ./mysqld_safe --skip-grant-tables &
	```
4. 登录mysql
```
./mysql
```

Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 2

Server version: 5.7.24 MySQL Community Server (GPL)

4.刷新权限  FLUSH PRIVILEGES;

5.修改密码 ALTER USER 'root'@'localhost' IDENTIFIED BY '888888';

6.退出mysql重新登录 quit

mysql -u root -p 输入刚刚更新的 888888，登录成功
————————————————
版权声明：本文为CSDN博主「猫七姑娘」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u013972652/article/details/87254950
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjQxODQ3NzMzLDI1Mjc5NTI1NCwtMTg1Mz
g0NjY4MywtNzE5MTI2NTgzLC0yMDM3NDk1ODIzLC0xNTUwODIy
MTgzLC0xODQyMzk2ODU0LDQ5MDUyNjQ5Ml19
-->