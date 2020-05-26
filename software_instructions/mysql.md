# 1 mysql install in mac
mac 下载安装包并点击下一步安装，即可完成。
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
1. 进入mysql
	```
	mysql -u root -p
	```
2. 查看所有的数据库,以下两条语句作用相同
	```
	show databases;
	select schema_name from information_schema.schemata;
	```
3. 创建数据库 `CREATE DATABASE 数据库名;`
4. 删除数据库 `drop database <数据库名>;`
5. 查看mysql数据库的运行状态  `status;`
6. 选择数据库 例如 `use information_schema`
7. 查看数据库中的表 `show tables;`
8. 创建数据表 `CREATE TABLE table_name (column_name column_type);`
9. 删除数据表 `DROP TABLE table_name ;`
10. 插入数据 
	```
	INSERT INTO table_name ( field1, field2,...fieldN )
	                       VALUES
	                       ( value1, value2,...valueN );
	```
11. 显示数据表的详细索引信息，包括PRIMARY KEY（主键）
	```
	SHOW INDEX FROM runoob_tbl;
	```
12. 显示数据表的属性，属性类型，主键信息 ，是否为 NULL，默认值等其他信息：
	```
	show columns from table_name;
	```
13. 查看表结构 `desc table_name;`
14. 查看表状态 `show table status from db like 条件`
可以查看engine数据库引擎，version，row、index等信息
15. 小技巧，当多行命令输入，发现错误后，用\c结束。
16.  查询数据库连接
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
17. 查看端口号 `show global variables like 'port';` 
# 3 msyql 常见问题处理
1. mac 中文乱码问题
	解决方案：
	在创建数据库的时候应该将数据库的字符编码设置成utf8
	```
	create database customer_gl character set utf8;
	```
# 4 mysql 数据类型
MySQL支持多种类型，大致可以分为三类：数值、日期/时间和字符串(字符)类型。
##  数值类型
类型

大小

范围（有符号）

范围（无符号）

用途

TINYINT

1 byte

(-128，127)

(0，255)

小整数值

SMALLINT

2 bytes

(-32 768，32 767)

(0，65 535)

大整数值

MEDIUMINT

3 bytes

(-8 388 608，8 388 607)

(0，16 777 215)

大整数值

INT或INTEGER

4 bytes

(-2 147 483 648，2 147 483 647)

(0，4 294 967 295)

大整数值

BIGINT

8 bytes

(-9,223,372,036,854,775,808，9 223 372 036 854 775 807)

(0，18 446 744 073 709 551 615)

极大整数值

FLOAT

4 bytes

(-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38)

0，(1.175 494 351 E-38，3.402 823 466 E+38)

单精度  
浮点数值

DOUBLE

8 bytes

(-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)

0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)

双精度  
浮点数值

DECIMAL

对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2

依赖于M和D的值

依赖于M和D的值

小数值
## 日期和时间类型

## 字符串类型


	 

 
	 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyNTI1NzU3OCwxNzE2MDYwOTI2LC0xNj
A1MjM2OTg3LC05OTY3NDk4OTUsMTAzNTc2Mjc5NywyMDI3MzE0
MzgxLDE5ODk0NjQ1NDksMjQxODQ3NzMzLDI1Mjc5NTI1NCwtMT
g1Mzg0NjY4MywtNzE5MTI2NTgzLC0yMDM3NDk1ODIzLC0xNTUw
ODIyMTgzLC0xODQyMzk2ODU0LDQ5MDUyNjQ5Ml19
-->