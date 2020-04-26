1. 判断文件或者文件夹是否存在
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
# 2 数组操作

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
--------------------------------------------
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


5 数组添加
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ declare -a nums=(1 2 3 4)
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ nums[4]=5
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${nums[@]}
1 2 3 4 5


new_nums=(${nums[@]} 6 7)
echo ${new_nums[@]}
1 2 3 4 5 6 7

6 数组切片

1 通用的格式${array[@]:起始位置:长度}，中间以":"隔开，如果第二项省略的话，就取后面所有的项
3) 区别于Python之一:起始位置可以为负数，但必须以放在()中，长度不能为负数

jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ array=(zero one two three four)
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${array}
zero
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${array[0]}
zero
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${array[@]:1}
one two three four
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${array[@]:0:3}
zero one two
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${array[@]::4}
zero one two three
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${array[@]:(-2):}

jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${array[@]:(-2):2}
three four
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${array[@]:(-4):2}
one two
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${array[@]:(-2)::}
-bash: array[@]: :: syntax error: operand expected (error token is ":")
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${array[@]:(-2):2}
three four
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ new_array=(${array[@]}:1:4)
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${new_array[*]}
zero one two three four:1:4
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ new_array=(${array[@]:1:4})
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${new_array[*]}
one two three four
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ new_array=(${array[@]:1:3})
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ echo ${new_array[*]}
one two three
jiayunfei@suanier-All-Series:~/after_sales_service/visbodyfit_D/get_log/log_files$ history 

7 元素切片，同字符切片相同

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk3ODYwODIzMiwxOTI4Njc0NjI1XX0=
-->