# 1 ubuntu 17.10之后版本网络管理
## 配置静态IP
参考网址 https://linuxize.com/post/how-to-configure-static-ip-address-on-ubuntu-18-04/
从17.10版本开始，Netplan是Ubuntu上的默认网络管理工具，它取代了/etc/network/interfaces以前用于在Ubuntu上配置网络的配置文件。
Netplan使用YAML语法的配置文件。要使用Netplan配置网络接口，您需要为该接口创建YAML描述，然后Netplan将为您选择的渲染器工具生成所需的配置文件。
### 使用配置文件修改
1. 确定要配置的以太网接口的名称
```
visbodyfit@server001:/etc/netplan$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp3s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 60:45:cb:88:5d:28 brd ff:ff:ff:ff:ff:ff
```
2. 打开/etc/netplan下面的yaml文件，并编辑内容
```
# Let NetworkManager manage all devices on this system
network:
  version: 2
  #  renderer: NetworkManager
  renderer: networkd
  ethernets:
    enp3s0:
      dhcp4: no
      addresses:
        - 192.168.0.8/24
      gateway4: 192.168.0.1
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
```
将DHCP设置为否 dhcp4: no
指定静态IP地址192.168.0.8/24。在下面addresses:可以添加一个或多个将分配给网络接口的IPv4或IPv6 IP地址。
指定网关 gateway4: 192.168.0.1
在下nameservers，设置名称服务器的IP地址addresses: [8.8.8.8, 1.1.1.1]
3. 保存并应用修改
```
sudo netplan apply
```
### 使用界面修改
1. 打开网络设置
2. 在"IPV4"方法部分中，选择"手动"，然后输入您的静态IP地址，网络掩码和网关。完成后，单击"应用"按钮。

# 2 ubuntu 16.04 安装中文输入法
1. 打开终端安装
	```
	sudo apt-get install fcitx fcitx-googlepinyin im-config
	```
	fcitx :小企鹅输入法，它是一个以 GPL 方式发布的输入法平台,可以通过安装引擎支持多种输入法，支持简入繁出，是在 Linux 操作系统中常用的中文输入法
	im-config:输入法配置
2. 配置输入法
	```
	im-config
	```
	回车进行配置，最后选择fcitx选项。然后重启系统。
3. 右上角有类似“Configure Input Method”的图标。可以使用ctrl+space进行输入法切换。

# 3 隐藏光标
1. 安装unclutter
	```
	sudo apt-get install unclutter
	```
2. 设置光标隐藏
	```
	unclutter -idle 3  # 3秒后消失
	```
3. 设置开机启动，参考4中设置

# 4 ubuntu18.04 设置开机执行脚本

## 原理说明
- Ubuntu18.04 不能像16.04 那样可以直接使用 /etc/rc.local 文件，需要自己创建
- systemd 默认读取 /etc/systemd/system 下的配置文件，该目录下的文件会链接/lib/systemd/system/下的文件。执行 ls /lib/systemd/system 你可以看到有很多启动脚本，其中就有我们需要的 rc.local.service
- 查看`rc.local.service`文件内容
	- 一般正常的启动文件主要分成三部分  
	`[Unit]` 段: 启动顺序与依赖关系  
	`[Service]` 段: 启动行为,如何启动，启动类型  
	`[Install]` 段: 定义如何安装这个配置文件，即怎样做到开机启动
1. 建立 rc-local.service 文件
	```
	sudo vim /etc/systemd/system/rc-local.service
	```
2. 复制下列内容到 rc-local.service 文件中
	```
	[Unit]
	Description=/etc/rc.local Compatibility
	ConditionPathExists=/etc/rc.local
	 
	[Service]
	Type=forking
	ExecStart=/etc/rc.local start
	TimeoutSec=0
	StandardOutput=tty
	RemainAfterExit=yes
	SysVStartPriority=99
	 
	[Install]
	WantedBy=multi-user.target
	```
3. 创建文件 rc.local
	```
	sudo vim /etc/rc.local
	```
4. 复制下列内容到 rc.local 文件中
	```
	#!/bin/sh -e
	#
	# rc.local
	#
	# This script is executed at the end of each multiuser runlevel.
	# Make sure that the script will "exit 0" on success or any other
	# value on error.
	#
	# In order to enable or disable this script just change the execution
	# bits.
	#
	# By default this script does nothing.
	echo "测试脚本执行成功" > /usr/local/test.log
	exit 0
	```
5. 给 rc.local 加上权限，启用服务
	```
	sudo chmod 755 /etc/rc.local    
	sudo systemctl enable rc-local
	```
6. 启动服务并检查状态
	```
	sudo systemctl start rc-local.service
	sudo systemctl status rc-local.service
	```
7. 重启后检查test.log文件是否已经存在

# 5 查看桌面环境版本

ubuntu 系统，没有找到显示桌面系统的方法，先安装软件进行查看。
```
sudo apt install screenfetch
直接输入screenfetch 进行查看，DE就是桌面环境
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMDI0MDYwMzIsMTk0NzA1OTIzMywxNT
U0OTcwOTQzLC0xNzQ1NzU2OTk4XX0=
-->