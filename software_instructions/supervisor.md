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



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQyMjk4ODkwMl19
-->