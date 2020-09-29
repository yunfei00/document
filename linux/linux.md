<h3><a href="#title1">1 nohup</a> </h3>
<h3><a href="#title2">2 scp</a> </h3>
<h3><a href="#title3">3 svn 安装</a> </h3>
<h3><a href="#title4">4 命令行控制颜色</a> </h3>
<h3><a href="#title5">5 Ubuntu用户操作</a> </h3>
<h3><a href="#title6">6 远程执行命令 带窗口</a> </h3>
<h3><a href="#title7">7 内核版本与系统版本查看</a> </h3>
<h3><a href="#title8">8 英伟达显卡安装卸载</a> </h3>
<h3><a href="#title9">9 tar命令</a> </h3>
<h3><a href="#title10">10 时间同步</a> </h3>
<h3><a href="#title11">11 date 命令</a> </h3>
<h3><a href="#title12">12 ubuntu修改静态IP</a> </h3>
<h3><a href="#title13">4 命令行控制颜色</a> </h3>
<h3><a href="#title14">4 命令行控制颜色</a> </h3>
<h3><a href="#title15">4 命令行控制颜色</a> </h3>
<h3><a href="#title16">4 命令行控制颜色</a> </h3>
<h3><a href="#title17">4 命令行控制颜色</a> </h3>
<h3><a href="#title18">4 命令行控制颜色</a> </h3>
<h3><a href="#title19">4 命令行控制颜色</a> </h3>
<h3><a href="#title20">4 命令行控制颜色</a> </h3>
<h3><a href="#title21">4 命令行控制颜色</a> </h3>
<h3><a href="#title22">4 命令行控制颜色</a> </h3>
<h3><a href="#title23">4 命令行控制颜色</a> </h3>
<div style="page-break-after:always"></div>
<h1 id="title1">1 nohup</h1>  

```
nohup ./01_st.sh >/dev/null 2>&1 &
```
<h1 id="title1">2 scp</h1>  

```
scp visbodyfit@192.168.0.10:/home/yunfei/test.get_value.c ./
scp hardware  visbodyfit@192.168.0.10:/home/visbodyfit/yunfei
```
<h1 id="title3">3 svn 安装</h1>  
```
sudo apt-get install subversion  
```
<h1 id="title4">4 命令行控制颜色</h1>  

```
#!/bin/bash

#下面是字体输出颜色及终端格式控制
#字体色30-37
echo -e "\033[30m黑色字\033[0m"
echo -e "\033[31m红色字\033[0m"
echo -e "\033[32m绿色字\033[0m"
echo -e "\033[33m黄色字\033[0m"
echo -e "\033[34m蓝色字\033[0m"
echo -e "\033[35m紫色字\033[0m"
echo -e "\033[36m天蓝字\033[0m"
echo -e "\033[37m白色字\033[0m"
#字背景颜色范围:40-47
echo -e "\033[40;37m黑底白字\033[0m"
echo -e "\033[41;30m红底黑字\033[0m"
echo -e "\033[42;34m绿底蓝字\033[0m"
echo -e "\033[43;34m黄底蓝字\033[0m"
echo -e "\033[44;30m蓝底黑字\033[0m"
echo -e "\033[45;30m紫底黑字\033[0m"
echo -e "\033[46;30m天蓝底黑字\033[0m"
echo -e "\033[47;34m白底蓝字\033[0m"
#.....

#控制选项说明
#\033[0m关闭所有属性
#\033[1m设置高亮度
#\033[4m下划线
echo -e "\033[4;31m下划线红字\033[0m"
#闪烁
echo -e "\033[5;34m红字在闪烁\033[0m"
#反影
echo -e "\033[8m消隐\033[0m "


#\033[30m-\033[37m设置前景色
#\033[40m-\033[47m设置背景色
#\033[nA光标上移n行
#\033[nB光标下移n行
echo -e "\033[4A光标上移4行\033[0m"
#\033[nC光标右移n行
#\033[nD光标左移n行
#\033[y;xH设置光标位置
#\033[2J清屏
#\033[K清除从光标到行尾的内容
echo -e "\033[K清除光标到行尾的内容\033[0m"
#\033[s保存光标位置
#\033[u恢复光标位置
#\033[?25|隐藏光标
#\033[?25h显示光标
echo -e "\033[?25l隐藏光标\033[0m"
echo -e "\033[?25h显示光标\033[0m"
```
```
#下面的这个例子是字体不停的闪烁。
#!/bin/bash

a=30
b=41
while true
do
echo -e "\033[${a}m光辉女郎\033[0m"
echo -e "\033[${a}m的吗西亚\033[0m"
echo -e "\033[${a}m洛克萨斯\033[0m"
a=$(($(($a%7))+30))
b=$(($(($b%7))+40))
#每次让字体颜色在30-37转换
#每次让背景颜色在40-47转换
echo -e "\033[4A\033[0m"
done
```

<h1 id="title5">5 Ubuntu用户操作</h1>  

查询用户组
添加用户组
```
sudo groupadd -g 1055 visbodyfit
```
删除用户组
修改用户组
为用户组添加用户
添加用户
```
sudo useradd visbodyfit  -u 998 -g 1055
sudo passwd visbodyfit
afei
suanier@521
```

<h1 id="title6">6 远程执行命令  带窗口</h1>  

```
sshpass -p "afei"  ssh -X visbodyfit@192.168.0.10 /home/visbodyfit/visfitdevice/hardwareServer/tool/hardware_test/hardware_test

```

<h1 id="title7">7 内核版本与系统版本查看</h1>  

```
    uname -a
```
    
x.系统版本
```
    cat /etc/issue
```

<h1 id="title8">8 英伟达显卡安装卸载</h1>  

https://www.geforce.cn/drivers
卸载
```
sudo ./NVIDIA-Linux-x86_64-384.98.run --uninstall
sudo ./NVIDIA-Linux-x86_64-384.98.run --no-x-check --no-nouveau-check --no-opengl-files
```

查看是否安装OK
nvidia-smi

<h1 id="title9">9 tar命令</h1>  

解压到目标文件夹
tar xf 20190714-20190718.tar.gz  -C 0714-0718/

<h1 id="title10">10 时间同步</h1>  

ubuntu 设备 默认服务器同步时间：
/var/log
grep 'step time server'  *
grep 'step time server'  /var/log/*
syslog:Nov 26 16:35:06 localhost ntpdate[22813]: step time server 91.189.89.199 offset -29052.487788 sec
其中 91.189.89.199为时间服务器
也可以手工使用：sudo ntpdate cn.pool.ntp.org
sudo ntpdate cn.pool.ntp.org
26 Nov 17:51:30 ntpdate[30566]: adjust time server 84.16.73.33 offset 0.020134 sec
或者sudo ntpdate 91.189.89.199

<h1 id="title11">11 date 命令</h1>  


1. 时间戳解析成指定格式
date --date='@1575447167' "+%Y%m%d"
20191204

2. 时间向前24H：
date --date="@$(expr  $(date +%s) - 86400)" "+%Y%m%d"
20191208

3. 时间精确到微妙
date "+%Y-%m-%d %H:%M:%S-$(expr $(date +%N) / 1000)"
2019-12-09 14:14:06-938178

4. 格式化 
date --date="2/24/17 16:13:27"
2017年 02月 24日 星期五 16:13:27 CST
date --date="2/24/17"
2017年 02月 24日 星期五 00:00:00 CST
date --date='Dec 27 11:26:07' "+%Y%m%d"
20191227

5. 比较两个时间差值
expr $(date +%s) - $(date --date='Dec 27 11:26:07' +%s)
6. 两个日期之间的所有时间
	```
	# 说明：20200225到20200301之间所有时间列表
	begin_time=20200225
	end_time=20200301
	declare -a datas
	count=$(expr $(expr $(date --date="${end_time}" "+%s") - $(date --date="${begin_time}" "+%s")) / 3600 / 24 + 1)
	echo  "datas count is ${count}"
	# datas count is 6
	current_data="${begin_time}"
	for  ((i=0;i<  ${count};i++))
	do
	datas[i]=${current_data}
	current_data=$(date --date=@$(expr $(date --date="${current_data}" "+%s") + 3600 \* 24) "+%Y%m%d")
	done
	
	echo "${datas[@]}"
	# 20200225 20200226 20200227 20200228 20200229 20200301
	```
<h1 id="title12">12 ubuntu修改静态IP</h1>  

1 打开目标文件
sudo gedit /etc/network/interfaces // gedit 是用gedit进行编译打开，也可以用其他编译器打开

2 修改文件内容

auto enp7s0
iface enp7s0 inet static
address 10.0.208.222
netmask 255.255.240.0
gateway 10.0.208.1
dns-nameservers 10.0.208.1

3 文件内容说明：

auto enp7s0 // 使用的网络接口，之前查询接口是为了这里
iface enp7s0 inet static // enp7s0这个接口，使用静态ip设置
address 10.0.208.222 // 设置ip地址
netmask 255.255.240.0 // 设置子网掩码
gateway 10.0.208.1 // 设置网关
dns-nameservers 10.0.208.1 // 设置dns服务器地址

4 重启设备

5 参考网址：

https://www.jianshu.com/p/d69a95aa1ed7


<h1 id="title13">13 linux 根目录结构</h1>  

/boot
存放系统启动的相关文件，比如内核

/dev
设备文件

块(block)设备
可存储或持有数据 (store or hold data)，可随机访问
举例：软盘，硬盘，CD—ROM驱动

字符(character)设备
可传输或转移数据 (transmit or transfer data) 线性访问，以字符为单位
举例：鼠标，显示屏

/etc
配置文件

/home
用户的家目录

/lib
库文件

/lib/modules
内核模块文件

静态库 (static libraries)
后缀为 *.a, 代表 ‘archive’，编译时使用，便于管理单个程序

动态库 (dynamic libraries)
后缀为 *.so, 代表 ‘shared object’, 程序运行时共享同一个实例，节约内存

/media
挂载点目录，比如移动设备

/mnt
文件系统或者设备的通用挂载点

/opt
第三方程序安装目录

/proc
虚拟文件系统，内核映射文件，存储运行时系统的信息，比如系统内存，设别挂在，硬件配置等，可以看作是内核的控制与信息中心

/sys
内核的接口(interface)，包含跟硬件设备相关属性的映射文件

/tmp
存放临时文件

/var
存放可变化文件

/var/run 进程
/var/cache 缓存
/var/log 日志
/var/mail 邮件
/var/lock 锁文件
/var/tmp 临时文件
/bin
可执行二进制文件，系统相关的

/sbin
管理命令

/usr
universal shared read-only

/usr/bin 普通用户二进制程序
/usr/sbin centos中/sbin指向此处
/usr/lib centos中/lib指向此处
/usr/local 第三方软件
/usr/local/bin
/usr/local/sbin
/usr/local/lib


<h1 id="title14">14 文件及基本操作</h1>  

使用 ls 指令查看目录中文件的信息
使用 ls -l 命令列举当前目录下的文件

-rwxr-xr-x   1 root   wheel      33888  3 23 07:55 zfgrep
12           3  4       5          6        7        8
1
2
1.文件类型
( - ) 普通文件
( d ) 目标文件
( b ) 块设备文件
( l ) 符号链接文件
( p ) 套接字文件
( s ) 命令管道文件
2.文件权限
共九位，三位为一组，三组分别为root，普通用户，客人对应的权限，rwx(读，写，执行)，例: ‘rwxr-xr-x’

3.文件硬链接次数
与源文件同时指向相同的物理地址

4.文件的属主
5.文件的属组
6.文件的字节数
7.文件的最近修改时间
文件的时间戳
access 访问时间
modify 修改文件具体内容时间
change 改变文件基本信息时间，比如文件名
8.文件名
文件名命名规范
长度不超255
不使用 ‘/’ 作为文件名
严格区分大小写
> ls 指令的其他参数
-h 将文件大小转换为根更清晰的格式
-a 显示以.开头的隐藏文件
-d 显示目录自身属性
-r 逆序显示文件
-i 显示结点号
-R 递归显示
> 使用 mkdir 命令
作用
创建目录，支持如下写法： mkdir {a,b}{c,d} (= mkdir ac ad bc bd)

> 使用 cd 命令
作用
在目录之间跳转

> 使用 pwd 命令
作用
显示当前位置的绝对路径

> 使用 touch 命令
作用
更新(修改)文件的时间戳，创建文件

参数使用
-c 若文件不存在则不创建文件
-t 自定义时间(格式：[[CC]YY]MMDDhhmm[.ss]]， 比如 199706231223.34)
-a 只修改access时间
-m 只修改modify时间
> 使用 stat 命令
作用
查看文件(目录)信息

参数使用
-f 显示目录信息
> 使用 rm 命令
作用
删除文件(目录)

参数使用
-i 在删除前询问是否删除
-f force
-r 递归删除，用于删除目录及其下面的所有文件与子目录，与 -f 合用最佳
> 使用 cp 命令
作用
复制文件(目录)

参数使用
-r 复制目录及其下的所有文件与子目录
-f 如果存在目标文件无法打开，则删除它并在此尝试
-p 不修改文件的基本属性
-a 文档(archive)复制，常用于备份
> 使用 mv 命令
作用
移动(重命名)文件

<h1 id="title15">15 trap</h1>  

1. 运行格式
trap命令的参数分为两部分，前一部分是接收到指定信号时将要采取的行动，后一部分是要处理的信号名。
```
trap command signal
```
2. 它有三种形式分别对应三种不同的信号回应方式。
	1. 当脚本收到signal-list清单内列出的信号时，trap命令执行双引号中的命令
	```
	trap "commands" signal-list
	```
	2. trap不指定任何命令，接受信号的默认操作，默认操作是结束进程的运行
	```
	trap signal-list
	```
	3. trap命令指定一个空命令串，允许忽视信号
	```
	trap " " signal-list
	```
3. 脚本程序通常是以从上到下的顺序解释执行的，所以必须在你想保护的那部分代码以前指定trap命令。
4. 信号量详细列表可以trap -l即可显示

| 名称 | 默认动作 | 说明 |
|------|------------|------|
|SIGHUP| 终止进程| 终端线路挂断|
SIGINT| 终止进程| 中断进程
SIGQUIT | 建立CORE文件 终止进程，并且生成core文件
SIGILL| 建立CORE文件| 非法指令
SIGTRAP| 建立CORE文件| 跟踪自陷
SIGBUS| 建立CORE文件| 总线错误
SIGSEGV| 建立CORE文件| 段非法错误
SIGFPE |建立CORE文件| 浮点异常
SIGIOT| 建立CORE文件 |执行I/O自陷
SIGKILL |终止进程| 杀死进程
SIGPIPE |终止进程 |向一个没有读进程的管道写数据
SIGALARM| 终止进程| 计时器到时
SIGTERM |终止进程| 软件终止信号
SIGSTOP| 停止进程 |非终端来的停止信号
SIGTSTP |停止进程 |终端来的停止信号
SIGCONT| 忽略信号 |继续执行一个停止的进程
SIGURG |忽略信号 |I/O紧急信号
SIGIO |忽略信号 |描述符上可以进行I/O
SIGCHLD| 忽略信号| 当子进程停止或退出时通知父进程
SIGTTOU| 停止进程 |后台进程写终端
SIGTTIN |停止进程 |后台进程读终端
SIGXGPU |终止进程 |CPU时限超时
SIGXFSZ |终止进程 |文件长度过长
SIGWINCH| 忽略信号 |窗口大小发生变化
SIGPROF |终止进程 |统计分布图用计时器到时
SIGUSR1 |终止进程 |用户定义信号1
SIGUSR2 |终止进程 |用户定义信号2
SIGVTALRM |终止进程| 虚拟计时器到时

<h1 id="title16">16 shell 命名管道操作</h1>  

1. 管道建立
	```
	mkfifo /tmp/testpipe 
	mknod /tmp/testpipe p
	visbodyfit@visfit:~/yunfei$ ls -al 
	prw-rw-r--  1 visbodyfit visbodyfit    0 4月  17 17:21 testpipe|
	```
2. 读取管道内容
	```
	#!/bin/bash
	pipe=/tmp/testpipe
	trap "rm -f $pipe" EXIT
	if [[ ! -p $pipe ]]; then
	    mkfifo $pipe
	fi
	while true
	do
	    if read line <$pipe; then
	        if [[ "$line" == 'quit' ]]; then
	            break
	        fi
	        echo $line
	    fi
	done
	echo "Reader exiting"
	```
3. 写管道
	```
	#!/bin/bash
	pipe=/tmp/testpipe
	if [[ ! -p $pipe ]]; then
	   echo "Reader not running"
	   exit 1
	fi

	if [[ "$1" ]]; then
	   echo "$1" >$pipe
	else
	   echo "Hello from $$" >$pipe
	fi
	```


<h1 id="title17">17 seq 用法</h1>  


1. seq 说明
squeue 是一个序列的缩写，主要用来输出序列化的东西
	```
	用法：seq [选项]... 尾数
	　或：seq [选项]... 首数 尾数
	　或：seq [选项]... 首数 增量 尾数
	以指定增量从首数开始打印数字到尾数
	 -f, --format=格式      使用printf 样式的浮点格式
	 -s, --separator=字符串 使用指定字符串分隔数字(默认使用：\n)
	 -w, --equal-width     在列前添加0 使得宽度相同【自动补位】
	     --help            显示此帮助信息并退出
	     --version         显示版本信息并退出
	```
2. seq 使用方法
	* 生成序列化数字1到100
	```
	seq 100
	```
	* 指定分隔符，横着输出
	```
	seq -s '#' 5
	1#2#3#4#5
	```
	* 以空格作为分格，且输出单数
	```
	seq -s ' ' 1 2 10
	1 3 5 7 9
	```
	* 默认补位操作
	```
	seq  -w -s " "  10
	01 02 03 04 05 06 07 08 09 10
	```
	* 格式化补齐输出 （通过%后添加0替代空格补足空位）
	```
	seq  -f "%04g"  -s  " "  10
	0001 0002 0003 0004 0005 0006 0007 0008 0009 0010
	```
<h1 id="title18">18 history 格式设置</h1>  

	```
	HISTFILESIZE=2000
	HISTSIZE=2000
	HISTTIMEFORMAT="%Y%m%d-%H%M%S: "  或者HISTTIMEFORMAT="%Y%m%d %T "或者HISTTIMEFORMAT="%F %T "
	export HISTTIMEFORMAT
	```
<h1 id="title19">19 service服务</h1>  

service命令用于对系统服务进行管理，比如启动（start）、停止（stop）、重启（restart）、查看状态（status）等。
	service命令本身是一个shell脚本，它在/etc/init.d/目录查找指定的服务脚本，然后调用该服务脚本来完成任务。
```
sudo service supervisor restart
```
<h1 id="title20">20 shell正则表达式</h1>  

- 基本的正则表达式（Basic Regular Expression 又叫Basic RegEx 简称BREs）
- 扩展的正则表达式（Extended Regular Expression 又叫Extended RegEx 简称EREs）
- Perl的正则表达式（Perl Regular Expression 又叫Perl RegEx 简称PREs）

	带有正则表达式的一些常用命令是tr，sed，vi和grep。下面列出了一些基本的正则表达式。

|符号 |内容描述
|----|--
|.| 替换任何字符
|^|匹配字符串的开头
|$|匹配字符串的结尾
|*|匹配之前的项零次或多次
|\\ |转义字符
|()|分组正则表达式
|?|完全匹配一个字符

[参考链接](https://man.linuxde.net/docs/shell_regex.html)

示例：
1. 匹配年
	``` 
	echo 2020-05-25|sed 's/^\(....\).*\(..\).*\(..\)/\1/'
	2020
	echo 20200525|sed 's/^\(....\).*\(..\).*\(..\)/\1\/\2\/\3/'
	2020/05/25
	```

	<h1 id="title21">21 Centos postfix 邮箱服务器搭建</h1>  
	
	### 步骤1：检查和删除Sendmail（仅在安装了Sendmail时才需要）
	```
	rpm -qa | grep sendmail
	# 如果有，则执行如下命令删除
	sudo yum remove sendmail*
	```
	### 步骤2：安装Postfix
	运行以下命令，检查是否已安装sendmail：
	```
	rpm -qa | grep postfix
	# 如果没有，则安装
	sudo yum install postfix
	```
	### 步骤3：配置Postfix
	```
	vim /etc/postfix/main.cf
	```
	
	<h1 id="title22">22 ubuntu 内核日志错误码</h1>  
		
	1. ubuntu内核日志错误码，可以在文件/usr/include/asm-generic/errno.h中查看。
	2. 内核日志中，可以搜索error，查看错误
	3. 错误码110说明
		设备启动后，内核日志显示错误码110，#define	ETIMEDOUT	110	/* Connection timed out */，连接超时，初步怀疑可能是某个USB口短路或异常导致，待排查。
		
	<h1 id="title23">23 饭</h1>  
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjQyMjQ3MjUxLC0zMjc2OTA3NDYsLTY3NT
c4NDc1OSwxMTUyMzAxNDQ4LDE2MzYwMzIxMjYsMTYzNjAzMjEy
NiwtMTkzNjc3MTE2MCwtMTczMTgyNTg0MCwyMTA5Njg3OTYwLC
0xMjAxMjQyOTkyLDM5ODM2NjgxOCwxMDEzMDUxMjY0LDg4OTU4
MDMzOCw1NDIwNjMyMTEsLTEzNjc4NDkxMTddfQ==
-->