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
1. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzEzNTUyODQsODUxNDAxNjk2LDExOTIyMT
E2NDQsLTQxMDg3MjMxMl19
-->