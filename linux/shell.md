# 目录

- <a href="#title1">1 判断文件或者文件夹是否存在</a> 
- <a href="#title2">2 数组操作</a> 
- <a href="#title3">3 正则表达式匹配数字</a> 
- <a href="#title4">4 wait</a> 
-  <a href="#title5">5 date</a> 

<div STYLE="page-break-after: always;"></div>
 
 <h1 id="title1">1 判断文件或者文件夹是否存在</h1>  
 
	```
	dir_name="./aa"
	if [ ! -d ${dir_path} ];then
	        mkdir ${dir_path}
	else
	        echo "file already exists."
	fi
	
	file_name="cc"
	if [ -f "${file_name}" ];then
		echo "file already exists."
	else
		echo "file is not exists."
	fi
	```
	文件比较符
	|     命令|解析|举例|
	|-----|------|----|
	| -e filename|  如果 filename存在，则为真 | [ -e /var/log/syslog ]
	| -d filename|  如果 filename为目录，则为真|  [ -d /tmp/mydir ]
	| -f filename  |如果 filename为常规文件，则为真 | [ -f /usr/bin/grep ]
	| -L filename  |如果 filename为符号链接，则为真 | [ -L /usr/bin/grep ]
	| -r filename  |如果 filename可读，则为真  |[ -r /var/log/syslog ]
	| -w filename | 如果 filename可写，则为真 | [ -w /var/mytmp.txt ]
	| -x filename | 如果 filename可执行，则为真 | [ -L /usr/bin/grep ]
	| filename1-nt filename2  |如果 filename1比 filename2新，则为真 | [ /tmp/install/etc/services -nt /etc/services ]
	| filename1-ot filename2 | 如果 filename1比 filename2旧，则为真 | [ /boot/bzImage -ot arch/i386/boot/bzImage ]

 <h1 id="title2">2 数组操作</h1>  

**说明： shell中只有一维数组**
1. 数组声明与查看
	```
	declare -a array_name        # 声明数组 也可不声明
	declare -a nums=(1 2 3 4)    # 声明数组并赋值
	unset array_name             # 删除数组
	# 显示数组元素
	echo ${nums[@]}
	1 2 3 4
	echo ${nums[*]}
	1 2 3 4
	unset nums[0]                # 删除数组元素
	echo ${nums[*]}
	2 3 4
	```
2. 数组定义
- 数组中的元素，必须以"空格"来隔开
- 字符串是SHELL中最重要的数据类型，其也可通过($str)来转成数组，操作起来非常方便
	```
	array0=(a1 a2 a3 a4)
	array1[0]=1
	array1[1]=2
	array1[2]=3
	array1[3]=4
	str="I am a good man"
	array2=($str)
	```
3. 数组长度
- 使用${array_name[@]} 或者 ${array_name[*]} 都可以全部显示数组中的元素.数组长度同理。
* 数组长度
	```
	array1=(a1 a2 a3 a4)
	echo ${#array1[@]}
	4
	echo ${#array1[*]}
	4
	```
* 元素长度
	```
	echo ${#array1[0]}
	```
4. 数组遍历
	```
	for ((i=0;i<${#nums[@]};i++)) do echo ${nums[i]};done
	1
	2
	3
	4

	for i in ${nums[@]}; do echo ${i};done
	1
	2
	3
	4
	```
5. 数组元素添加
	```
	declare -a nums=(1 2 3 4)
	nums[4]=5
	echo ${nums[@]}
	1 2 3 4 5

	new_nums=(${nums[@]} 6 7)
	echo ${new_nums[@]}
	1 2 3 4 5 6 7
	```
6. 数组切片

* 通用的格式${array[@]:起始位置:长度}，中间以":"隔开，如果第二项省略的话，就取后面所有的项
* 区别于Python之一:起始位置可以为负数，但必须以放在()中，长度不能为负数
	```
	array=(zero one two three four)
	echo ${array}
	zero
	echo ${array[0]}
	zero
	echo ${array[@]:1}
	one two three four
	echo ${array[@]:0:3}
	zero one two
	echo ${array[@]::4}
	zero one two three
	echo ${array[@]:(-2):2}
	three four
	echo ${array[@]:(-4):2}
	one two

	new_array=(${array[@]:1:4})
	echo ${new_array[*]}
	one two three four
	```

7. 元素切片，同字符切片相同

 <h1 id="title3"> 3 正则表达式匹配数字</h1>  
```
echo office365 | grep -P '\d+' -o
365
```
 <h1 id="title4"> 4 wait</h1>  
wait [作业指示或进程号]

1. 等待作业号或者进程号制定的进程退出，返回最后一个作业或进程的退出状态状态。如果没有制定参数，则等待所有子进程的退出，其退出状态为0.

2. 如果是shell中等待使用wait，则不会等待调用函数中子任务。在函数中使用wait，则只等待函数中启动的后台子任务。

3. 在shell中使用wait命令，相当于高级语言里的多线程同步。

**语法**
　　wait(参数)  使用 wait 是在等待上一批或上一个脚本执行完（即上一个的进程终止），再执行wait之后的命令。

**参数**

　　进程或作业标示：指定进程号或者作业号。

**实例**

1. 使用wait等待所有子任务结束
```
#!/bin/bash
sleep 10 &
sleep 5&
wait #等待10秒后，退出

#!/bin/bash
sleep 10 &
sleep 5&
wait $! #$!表示上个子进程的进程号，wait等待一个子进程，等待5秒后，退出
```
2. 在函数中使用wait
```
#!/bin/bash
fun(){
　　echo "fun is begin.timeNum:$timeNum"
　　local timeNum=$1
　　sleep $timeNum &
　　wait #这个只等待wait前面sleep
　　echo "fun is end.timeNum:$timeNum"
}
fun 10 &
fun 20 &
wait #如果fun里面没有wait，则整个脚本立刻退出，不会等待fun里面的sleep
echo "all is ending"
```
输出结果为：
```
fun is begin.timeNum:10
fun is begin.timeNum:20
fun is end.timeNum:10
fun is end.timeNum:20
all is ending
# 从输出结果，可以看到，整个脚本，等待了所有子任务的退出
```
3. 循环中使用
```
#!/bin/bash
for ((i=0;i<5;i++))
do
sleep 3;echo a
done
#运行需要15秒。

#!/bin/bash
for ((i=0;i<5;i++))
do
{
sleep 3;echo a
} &
done
wait
#打开5个子进程并行，运行只需要3秒。
```
 <h1 id="title5"> 5 date</h1>  

 1. 本月第一天
```
date +"%Y%m01"
20200801
```
 2. 本月最后一天
 
 ```
date -d"$(date -d"1 month" +%Y%m01) -1 day" +"%Y%m%d"
20200831
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI0NDUwNDQ4MCwtMTcyNTQ4MDM2NSw2MD
IxNDg0MjgsLTIzMTg5NiwyNjY0NDIxOTQsLTE3NzUxNDEwNDMs
LTE1NjEwNDQwMzEsMTkyODY3NDYyNV19
-->