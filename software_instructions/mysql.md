# 1 mysql install in mac
# 2 mac 上忘记mysql密码的恢复
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
	
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyODkwOTk4MjcsNDkwNTI2NDkyXX0=
-->