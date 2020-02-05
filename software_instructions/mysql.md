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
4. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcyMTAzNDk2MCw0OTA1MjY0OTJdfQ==
-->