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
4. 登录mysql，刷新权限
	```
	./mysql
	FLUSH PRIVILEGES;
	```
5. 修改密码 
	```
	ALTER USER 'root'@'localhost' IDENTIFIED BY 'test';
	```

6. 退出mysql重新登录 
	```
	quit
	mysql -u root -p
	```
	 输入刚刚更新的 test，登录成功
# 3 常用的mysql命令
1. 查看所有的数据库,以下两条语句作用相同
	```
	show databases;
	select schema_name from information_schema.schemata;
	```
2. 查看mysql数据库的运行状态  `status;`
3. use 命令选择数据库 例如 `use information_schema`
4. 查看数据库中的表 `show tables;`
5. 查看表结构 `desc table_name;`
6. 查看表状态 `show table status from db like 条件`
可以查看engine数据库引擎，version，row、index等信息
7. 小技巧，当多行命令输入，发现错误后，用\c结束。
8.  查询数据库连接
	```
	show full  processlist;
	show status like '%Max_used_connections%';
	show status like '%Threads_connected%';#当前连接数
	show status like '%table_lock%';#表锁定
	show status like 'innodb_row_lock%';#行锁定
	show status like '%qcache%'; #查询缓存情况
	show variables like "%query_cache%";
	SHOW STATUS LIKE 'Qcache%';
	show variables like "%binlog%";
	show status like 'Aborted_clients';#由于客户没有正确关闭连接已经死掉，已经放弃的连接数量
	show variables like '%max_connections%';//查看最大连接数量
	show variables like '%timeout%';#查看超时时间
	show variables like 'log_%'; #查看日志是否启动
	```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAzNTc2Mjc5NywyMDI3MzE0MzgxLDE5OD
k0NjQ1NDksMjQxODQ3NzMzLDI1Mjc5NTI1NCwtMTg1Mzg0NjY4
MywtNzE5MTI2NTgzLC0yMDM3NDk1ODIzLC0xNTUwODIyMTgzLC
0xODQyMzk2ODU0LDQ5MDUyNjQ5Ml19
-->