# 1 创建定时任务
```
crontab -ecrontab -e
```
# 2 查看该用户下的crontab服务是否创建成功
```
crontab -l
```
# 3 启动crontab服务
一般启动服务用 /sbin/service crond start 若是根用户的cron服务可以用 sudo service crond start， 不同版本**linux**系统启动的服务的命令也不同 ，像我的虚拟机里只需用 sudo service cron restart 即可，若是在根用下直接键入service cron start就能启动服务
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






0    12   *   *   *   mail dmtsai -s "at 12:00" < /home/dmtsai/.bashrc
#分  时   日   月  周  |《==============命令行=======================》|

代表意义    分钟    小时    日期    月份    周    命令
数字范围    0~59    0~23    1~31    1~12    0~7    就命令啊
*(星号) 代表任何时刻都接受的意思。举例来说，范例一内那个日、月、周都是*，就代表着不论何月、何日的礼拜几的12：00都执行后续命令的意思。
,(逗号) 代表分隔时段的意思。举例来说，如果要执行的工作是3：00与6：00时， 就会是：
0 3,6 * * * command   
时间还是有五列，不过第二列是 3,6 ，代表3与6都适用
-(减号)  代表一段时间范围内，举例来说，8点到12点之间的每小时的20分都进行一项工作：
20 8-12 * * * command
仔细看到第二列变成8-12.代表 8,9,10,11,12 都适用的意思
/n(斜线) 那个n代表数字，即是每隔n单位间隔的意思，例如每五分钟进行一次，则：
*/5 * * * * command
用*与/5来搭配，也可以写成0-59/5，意思相同
* * * * * flock -xn /tmp/get_fat_data.lock -c "sudo -u root /home/visbodyfit/yunfei/get_data/crontab.sh"
* 0-9 * * * flock -xn /tmp/get_fat_data.lock -c "sudo -u root /home/visbodyfit/yunfei/get_data/crontab.sh"
* 21-23 * * * flock -xn /tmp/get_fat_data.lock -c "sudo -u root /home/visbodyfit/yunfei/get_data/crontab.sh"


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

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjExODY4OTYxMSwtNTYxNjM3ODQwLC0xMj
QwODI2MjQ2LDExMDQ3NDU0MjJdfQ==
-->