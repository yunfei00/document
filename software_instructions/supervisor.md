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

**子进程配置文件路径**：`/etc/supervisord.d/`

_注：默认子进程配置文件为ini格式，可在supervisor主配置文件中修改。_

<h1 id="title4">4 配置文件说明使用 </h1>

supervisor.conf配置文件说明：
```
[unix_http_server]
file=/tmp/supervisor.sock   ;UNIX socket 文件，supervisorctl 会使用
;chmod=0700                 ;socket文件的mode，默认是0700
;chown=nobody:nogroup       ;socket文件的owner，格式：uid:gid
 
;[inet_http_server]         ;HTTP服务器，提供web管理界面
;port=127.0.0.1:9001        ;Web管理后台运行的IP和端口，如果开放到公网，需要注意安全性
;username=user              ;登录管理后台的用户名
;password=123               ;登录管理后台的密码
 
[supervisord]
logfile=/tmp/supervisord.log ;日志文件，默认是 $CWD/supervisord.log
logfile_maxbytes=50MB        ;日志文件大小，超出会rotate，默认 50MB，如果设成0，表示不限制大小
logfile_backups=10           ;日志文件保留备份数量默认10，设为0表示不备份
loglevel=info                ;日志级别，默认info，其它: debug,warn,trace
pidfile=/tmp/supervisord.pid ;pid 文件
nodaemon=false               ;是否在前台启动，默认是false，即以 daemon 的方式启动
minfds=1024                  ;可以打开的文件描述符的最小值，默认 1024
minprocs=200                 ;可以打开的进程数的最小值，默认 200
 
[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ;通过UNIX socket连接supervisord，路径与unix_http_server部分的file一致
;serverurl=http://127.0.0.1:9001 ; 通过HTTP的方式连接supervisord
 
; [program:xx]是被管理的进程配置参数，xx是进程的名称
[program:xx]
directory=/home/visbodyfit/visfitdevice/hardwareServer  ;程序运行目录
command=/home/visbodyfit/visfitdevice/hardwareServer/hardware ; 程序启动命令
environment=        LD_LIBRARY_PATH=/home/visbodyfit/visfitdevice/hardwareServer/lib
autostart=true       ; 在supervisord启动的时候也自动启动
startsecs=10         ; 启动10秒后没有异常退出，就表示进程正常启动了，默认为1秒
autorestart=true     ; 程序退出后自动重启,可选值：[unexpected,true,false]，默认为unexpected，表示进程意外杀死后才重启
startretries=3       ; 启动失败自动重试次数，默认是3
user=root            ; 用哪个用户启动进程，默认是root
priority=10         ; 进程启动优先级，默认999，值小的优先启动
redirect_stderr=true ; 把stderr重定向到stdout，默认false
stdout_logfile_maxbytes=20MB  ; stdout 日志文件大小，默认50MB
stdout_logfile_backups = 20   ; stdout 日志文件备份数，默认是10
; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile=/home/visbodyfit/visfitdevice/hardwareServer/logs/hardware_out.log
stopasgroup=false     ;默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
killasgroup=false     ;默认为false，向进程组发送kill信号，包括子进程
 
;包含其它配置文件
[include]
files = relative/directory/*.ini    ;可以指定一个或多个以.ini结束的配置文件
```  

<h1 id="title5"> 5 supervisor命令说明 </h1>

```
supervisorctl status        //查看所有进程的状态
supervisorctl stop es       //停止es
supervisorctl start es      //启动es
supervisorctl restart       //重启es
supervisorctl update        //配置文件修改后使用该命令加载新的配置
supervisorctl reload        //重新启动配置中的所有程序
```

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
eyJoaXN0b3J5IjpbLTM1MDg5MTYzOCwxMzUxMjYzOTM5LDg3Mj
Y4ODU1NiwtNjQ3MTI0NjkxLDc0NTQ1Mzc5NCwxOTI0MzUyMjIz
LDg1MTQwMTY5NiwxMTkyMjExNjQ0LC00MTA4NzIzMTJdfQ==
-->