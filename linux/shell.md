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
	#echo "file is not exists."
	echo -e "\033[41;30m file is not exists. \033[0m"
	fi

	文件比较符
	-e filename  如果 filename存在，则为真  [ -e /var/log/syslog ]
	-d filename  如果 filename为目录，则为真  [ -d /tmp/mydir ]
	-f filename  如果 filename为常规文件，则为真  [ -f /usr/bin/grep ]
	-L filename  如果 filename为符号链接，则为真  [ -L /usr/bin/grep ]
	-r filename  如果 filename可读，则为真  [ -r /var/log/syslog ]
	-w filename  如果 filename可写，则为真  [ -w /var/mytmp.txt ]
	-x filename  如果 filename可执行，则为真  [ -L /usr/bin/grep ]
	filename1-nt filename2  如果 filename1比 filename2新，则为真  [ /tmp/install/etc/services -nt /etc/services ]
	filename1-ot filename2  如果 filename1比 filename2旧，则为真  [ /boot/bzImage -ot arch/i386/boot/bzImage ]
	```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMjQ5Nzc3NDldfQ==
-->