# 1 Django install
要求已经提前安装好了python3,如果还未安装python3，则参考[python安装](https://github.com/yunfei00/document/blob/master/software_instructions/python.md)
```
python3 -m pip install Django
python3
Python 3.8.1 (default, Jan 28 2020, 20:48:28) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.
import django
print(django.get_version())
3.0.2
```
# 2 config django
1. creat project
	```
	django-admin startproject test
	```
2. start project
    ```
    python3 manage.py  runserver
    ```
    
# 3 遇到问题
1. Centos7 虚拟环境安装Django 出现SQLite版本问题
	```
    raise ImproperlyConfigured('SQLite 3.8.3 or later is required (found %s).' %Database.sqlite_version)
    ```
    ## 解决方案：升级SQLite
	  1. Centos系统自带的sqlite3版本偏低，在上面的错误提示中要求需要SQLite 3.8.3 or later，那么就需要去升级 SQlite 的版本了。
    2. 更新SQLite 3  [官网路径](https://www.sqlite.org/download.html)
	```
	wget https://www.sqlite.org/2020/sqlite-amalgamation-3310100.zip
	tar xf sqlite-autoconf-3310100.tar.gz
	cd sqlite-autoconf-3310100/
	./configure
	make
	make install
	```
    3. 备份旧的sqlite3
	```
	mv /usr/bin/sqlite3  /usr/bin/sqlite3_old
	软链接将新的sqlite3设置到/usr/bin目录下
	ln -s /usr/local/bin/sqlite3   /usr/bin/sqlite3
	```
	  4. 将路径传递给共享库
	   设置开机自启动执行，可以将下面的export语句写入 ~/.bashrc 文件中，如果如果你想立即生效，可以执行source ~/.bashrc 将在每次启动终端时执行
	```
	export LD_LIBRARY_PATH="/usr/local/lib"
	```
    4. 查看python环境中sqlite3 是否已经更新
	```
	[root@VM_0_4_centos ~]# python3
	Python 3.8.1 (default, Jan 28 2020, 20:48:28) 
	[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import sqlite3
	>>> sqlite3.sqlite_version
	'3.31.1'
	```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5Nzc3MTkwNzAsMjM5NjUyMzc3LDEyMT
Y4ODMxNTFdfQ==
-->