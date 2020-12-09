# 目录

<h3><a href="#title1">1 ubuntu 系统通过USB无线网卡上网</a> </h3>
		<h4><ul><a href="#title1.1">1.1 问题说明</a> </h4>
		<h4><ul><a href="#title1.2">1.2  无线网卡规格</a> </h4>
		<h4><ul><a href="#title1.3">1.3  驱动下载安装</a> </h4>
		<h4><ul><a href="#title1.4">2.4 SEARCH 函数</a> </h4>
<h3><a href="#title2">2 Excel中分列相关函数</a> </h3>

		<h4><ul><a href="#title2.5">2.5 SUBSTITUTE 函数</a> </h4>
		<h4><ul><a href="#title2.6">2.6 FIND 函数</a> </h4>

<div style="page-break-after:always"></div>

  <h1 id="title1">1 ubuntu 系统通过USB无线网卡上网</h1>  
  
<h2 id="title1.1">1.1 问题说明</h2>  

台式机ubuntu系统，需要通过USB无线网卡上网。需要购买USB无线网卡，并进行配置，测试。

<h2 id="title1.2">1.2  无线网卡规格</h2>  

选用EP-AC1670 1300M双频无线网卡。

<h2 id="title1.3">1.3  驱动下载安装</h2>  

[驱动下载git网址](https://github.com/RinCat/RTL88x2BU-Linux-Driver)
安装方法
```
unzip  RTL88x2BU-Linux-Driver-master.zip
cd RTL88x2BU-Linux-Driver-master
make
sudo make install
```
<h2 id="title1.4">1.4 网络连接</h2>  

手工在界面连接5G网络和2.4G网络。

<h2 id="title1.5">1.5  传输速度测试</h2>  

1. 测试工具下载
[iperf下载网址](https://iperf.fr/iperf-download.php)
根据系统下载不同的版本。

2. 工具测试
使用电脑，通过网线连接路由器，另一台插有无限网卡的电脑通过wifi连接。


服务器端使用如下命令：
```
iperf -s -p 6666
```

客户端使用如下命令：
```
iperf -c 192.168.0.44 -p 6666 -f M -t 10 -i 1
```

查看测试的结果即可。
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkwMDQ1MDMyNCwxMTk2NDAxNDcsLTE0Mz
Q2MjMwNzFdfQ==
-->