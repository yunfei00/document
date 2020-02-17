# 1 创建定时任务
```
crontab -ecrontab -e
```
# 2 查看该用户下的crontab服务是否创建成功
```
crontab -l
```
# 3 启动crontab服务
|命令 |      说明
|----------------------|----
|service crond start|启动服务
|service crond stop|关闭服务
|service crond restart|重启服务
|service crond reload|重新载入配置
|service crond status|查看crontab服务状态
|service crond start|手动启动crontab服务

# 4 查看服务是否已经运行用
```
ps -ax | grep cron
```
# 5 crontab 命令解析

cron服务提供crontab命令来设定cron服务的，以下是这个命令的一些参数与说明:
	
|  命令参数  |含义|
|-----------|---|
|crontab -u |设定某个用户的cron服务，一般root用户在执行这个命令的时候需要此参数  |
|crontab -l |列出某个用户cron服务的详细内容  |
|crontab -r |删除某个用户的cron服务  |
|crontab -e |编辑某个用户的cron服务  |

举例：
1. root查看自己的cron设置:
	```
	crontab -u root -l 
	``` 
2. root想删除fred的cron设置
	```
	crontab -u fred -r
	```  
# 6 定时任务原理说明
crond 是**linux**用来定期执行程序的命令。当安装完成操作系统之后，默认便会启动此任务调度命令。crond命令每分钟会定期检查是否有要执行的工作，如果有要执行的工作便会自动执行该工作。

# 7 cron文件语法

|分|小时|日 |月| 星期 |命令|
|--|-----|----|---|-------|----|
|0-59| 0-23 |1-31| 1-12| 0-6| command (取值范围,0表示周日一般一行对应一个任务)

记住几个特殊符号的含义:
“*”代表取值范围内的数字,  
“/”代表”每”,  
“-”代表从某个数字到某个数字,  
“,”分开几个离散的数字

举例：
|分|小时|日 |月| 星期 |命令|含义|
|--|-----|----|---|-------|----|---|
|0-59|0-23|1-31|1-12|0-6|command|
|*   |*   |*   |*   |*  |ls     |每分钟执行ls命令
|5   |*   |*   |*   |*  |ls     |每5分钟执行ls命令  指定每天的 5:30 执行ls命令 
|7   |8   |*   |*   |*  |ls     |指定每天8：07分执行ls命令
|5   |8   |6   |*   |*  |ls     |指定每月6号8:07分执行ls命令    指定每年的6月8日
|30  |3   |10,20| * |*  |ls     |每月10号及20号的3：30执行ls命令
|25  |8-11|*   |*   |*  |ls     |每天8-11点的第25分钟执行ls命令
|*/15|*   |*   |*   |*  |ls     |每15分钟执行一次ls命令

脚本实例：
1. 使用root账户，每分钟执行一次`test.sh` ，加锁test.lock，如果程序未执行完，则本次不继续执行
	```
	* * * * * flock -xn /tmp/test.lock -c "sudo -u root test.sh" 
	```
2. 每分钟执行`test.sh`
```
	* * * * * /usr/bin/bash  /home/yunfei/svn_client_code/project/get_res_data/test.sh air "$(/usr/bin/date --date=@$(/usr/bin/expr $(/usr/bin/date +\%s) - 25 \* 3600) +\%Y\%m\%d)"   > /dev/null 2>&1 &``
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NDE2NjA1ODgsLTY4Njg3MjQ4OSwtND
YyNDk1MTIzLDIxMTg2ODk2MTEsLTU2MTYzNzg0MCwtMTI0MDgy
NjI0NiwxMTA0NzQ1NDIyXX0=
-->