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
# 5 
https://www.cnblogs.com/mingforyou/p/3930636.html
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

定时任务立刻生效：
/etc/init.d/cron restart

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI4MTI2NjMxOSwtMTI0MDgyNjI0NiwxMT
A0NzQ1NDIyXX0=
-->