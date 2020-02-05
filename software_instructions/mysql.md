# 1 mysql install in mac
# 2 mac 上忘记mysql密码的处理
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
6. 如果密码解析不出来，或者想强制重置密码
	收到
	十多个
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MjU2NDU1ODAsLTIwMzc0OTU4MjMsLT
E1NTA4MjIxODMsLTE4NDIzOTY4NTQsNDkwNTI2NDkyXX0=
-->