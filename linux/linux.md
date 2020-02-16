# 1 nohup不产生日志文件
```
nohup ./01_st.sh >/dev/null 2>&1 &
```
# 2 远程拷贝
```
scp   visbodyfit@192.168.0.10:/home/visbodyfit/yunfei/test.get_value.c ./
scp hardware  visbodyfit@192.168.0.10:/home/visbodyfit/yunfei
```
# 3 svn 安装
```
sudo apt-get install subversion  
```
# 4 命令行控制颜色
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


# 5 Ubuntu用户操作
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

# 6 远程执行命令  带窗口
```
sshpass -p "afei"  ssh -X visbodyfit@192.168.0.10 /home/visbodyfit/visfitdevice/hardwareServer/tool/hardware_test/hardware_test

```

# 7 内核版本与系统版本查看
```
    uname -a
```
    
x.系统版本
```
    cat /etc/issue
```

# 8 英伟达显卡安装卸载
https://www.geforce.cn/drivers
卸载
```
sudo ./NVIDIA-Linux-x86_64-384.98.run --uninstall
sudo ./NVIDIA-Linux-x86_64-384.98.run --no-x-check --no-nouveau-check --no-opengl-files
```

查看是否安装OK
nvidia-smi

# 9 tar命令
解压到目标文件夹
tar xf 20190714-20190718.tar.gz  -C 0714-0718/

# 10 时间同步
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

# 11 date 命令
时间戳解析成指定格式
date --date='@1575447167' "+%Y%m%d"
20191204

时间向前24H：
date --date="@$(expr  $(date +%s) - 86400)" "+%Y%m%d"
20191208

时间精确到微妙
date "+%Y-%m-%d %H:%M:%S-$(expr $(date +%N) / 1000)"
2019-12-09 14:14:06-938178

date --date='Dec 27 11:26:07' "+%Y%m%d"
20191227

比较两个时间差值
expr $(date +%s) - $(date --date='Dec 27 11:26:07' +%s)


# 12 ubuntu修改静态IP
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





<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNjc4NDkxMTddfQ==
-->