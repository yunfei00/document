<h2>目录</h2>

<h3><a href="#title1">1 supervisor 介绍</a> </h3>
<h3><a href="#title2">2 在ubuntu 18.04 上安装</a> </h3>
<h3><a href="#title3">3 supervisor 使用</a> </h3>
		<h4><ul><a href="#title2.1">2.1 LEFT函数</a> </h4>

<h1 id="title1"> 1 supervisor 介绍</h1>

Supervisor是用Python开发的一套通用的进程管理程序，能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常退出时能自动重启。它是通过fork/exec的方式把这些被管理的进程当作supervisor的子进程来启动，这样只要在supervisor的配置文件中，把要管理的进程的可执行文件的路径写进去即可。也实现当子进程挂掉的时候，父进程可以准确获取子进程挂掉的信息的，可以选择是否自己启动和报警。supervisor还提供了一个功能，可以为supervisord或者每个子进程，设置一个非root的user，这个user就可以管理它对应的进程。


<h1 id="title2">2 在ubuntu 18.04 上安装 </h1>

```
sudo apt-get install supervisor
```
<h1 id="title3">3 supervisor 使用 </h1>

 **supervisor配置文件**：`/etc/supervisord.conf`

_注：supervisor的配置文件默认是不全的，不过在大部分默认的情况下，上面说的基本功能已经满足。_

##### 子进程配置文件路径：`/etc/supervisord.d/`

_注：默认子进程配置文件为ini格式，可在supervisor主配置文件中修改。_

  
  
作者：风吹我已散博客  
链接：https://www.jianshu.com/p/0b9054b33db3  
来源：简书  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




# supervisor常见报错
## 基本思路：
首先我们要明确问题出在supervisor上还是启动的程序上，可以用ps -ef | grep supervisord查看是否启动，在用ps查看自己的进程有没有启动；
确认下启动的supervisor配置文件是哪个，有的是/etc/supervisor/supervisord.conf，有的是/etc/supervisord.conf，以自己的为准，不要弄混；
推荐使用apt-get安装，其次是pip ，最后才是yum。不要问为什么，踩坑踩得。另外，尽量用supervisord 3.x以上的版本，2.x版本出问题概率大；
```
supervisord -v
3.3.1
```
supervisord的日志在 /var/log/supervisor/supervisord.log，启动失败一般能再这里找到有用的信息

## 常用命令
-   `启动守护进程：supervisord -c /etc/supervisor/supervisord.conf`
-   `重载配置：supervisorctl reload`

参考如下：
[https://blog.csdn.net/kkevinyang/article/details/80539940](https://blog.csdn.net/kkevinyang/article/details/80539940)

[https://www.jianshu.com/p/805977544d7f](https://www.jianshu.com/p/805977544d7f)

1. supervisor无法启动
```
# 以下命令无法查询到进程
ps -ef|grep supervisor
# 错误信息如下：
sudo supervisorctl 
[sudo] password for visbodyfit: 
unix:///var/run/supervisor.sock no such file
supervisor>

# 执行以下命令后恢复
sudo supervisord -c /etc/supervisor/supervisord.conf  # 启动守护进程
sudo supervisorctl reload  # 重载配置
```
#  supervisor 安装
1. contos install
```
yum install supervisor
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbNzQ1NDUzNzk0LDE5MjQzNTIyMjMsODUxND
AxNjk2LDExOTIyMTE2NDQsLTQxMDg3MjMxMl19
-->