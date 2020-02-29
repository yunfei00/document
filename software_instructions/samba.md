# 1 ubuntu 安装samba
1. 安装samba
	```
	sudo apt-get install samba
	```
2. 版本查看
	```
	samba -V
	Version 4.3.11-Ubuntu
	```
3. 备份 smb.conf
	```
	sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak
	```
4. 配置smb.conf
在smb.conf最后加入以下配置并保存，然后退出
	```
	[work]
	comment = samba home directory
	path = /home/user/
	public = yes
	browseable = yes
	public = yes
	read only = no
	valid users = user
	create mask = 0777
	directory mask = 0777
	force user = nobody
	force group = nogroup
	available = yes
	```
5. 增加samba用户, 一定要操作这一步，否则windows上访问时输入用户名和密码会不对，访问不了
	```
	sudo smbpasswd -a user
	Failed to add entry for user user
	```
	解决办法:
	这是因为没有加相应的系统账号，所以会提示Failed to add entry for user user的错误，只需增加相应的系统账号user就可以了:
	```
	sudo groupadd user -g 6000
	sudo useradd user -u 6000 -g 6000 -s /sbin/nologin -d /dev/null
	```
	这时就可以用smbpasswd -a user增加user这个samba账号了!为了增加系统的安全性，所以加的系统账号不要给shell它，也不给它指定目录，到时在/home目录给user账号建个文件夹，该文件夹只有user有读写权限即可!
	例如:
	```
	sudo mkdir /home/user
	sudo chown -R user:user /home/user
	sudo chmod 777 /home/user
	```
	若不想让另人访问，只让user用户可以访问，只需执行命令:
	```
	chmod u+rwx,g+rwx,o-rwx /home/user
	```
	这时可以用smbpasswd命令增加samba账号user了
	```
	sudo smbpasswd -a user
	New SMB password:
	Retype new SMB password:
	Added user user.
	```
6. 重启samba
	```
	sudo service smbd restart
	```
7. windows 访问
	```
	\\192.168.0.20 即可访问
	```
# 2 centOS 安装samba

1. 使用yum方式安装samba，如果并不确定是否有安装samba，可以使用下面命令查看：
	```
	rpm -qa | grep samba
	```
	如果如图所示为空，则说明未安装samba相关程序
	```
	yum install samba -y
	```
	看到 Complete! 字样就算安装完成了。

2. 安装完成之后可以查看安装情况以及配置文件的位置
	```
	rpm -qa | grep samba
	rpm -qc samba samba-common
	```
3. 修改配置文件（修改前可以备份一份以备以后查用）
	```
	cp /etc/samba/smb.conf /etc/samba/smb.conf_bak
	ll /etc/samba/smb.conf*
	修改配置文件：
	vim /etc/samba/smb.conf 或 vi /etc/samba/smb.conf
	```
	本次参考提示写入一些最基本的信息，其他默认内容可以删除

	```
	Global parameters
	[global]
		printcap name = cups
		security = USER
		workgroup = SAMBA   ---用户组
		idmap config * : backend = tdb
		cups options = raw
	[samba]----共享目录名称
		comment = Home Directories
		inherit acls = Yes
		path = /home/samba_user ---共享目录位置
		read only = No
		valid users = samba_user  ---可以查看的用户
	```
5. 测试一下刚才的配置文件是否正确
	```
	testparm
	```
	出现Loaded services file OK.就说明没有问题。

6. 添加用户组
	```
	groupadd SAMBA
	```
7. 添加用户samba_user到SAMBA用户组
	```
	useradd samba_user -G SAMBA
	```
7. 设置用户密码
	```
	passwd samba_user
	```
8. 启动samba服务，并设置开机启动~
	```
	systemctl start smb
	systemctl enable smb
	```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NDY0Mzk1MzIsNjUxNjM3MDA2XX0=
-->