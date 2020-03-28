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
