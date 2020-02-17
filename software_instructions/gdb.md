# 1 简介
GDB是一个由GNU开源组织发布的、UNIX/LINUX操作系统下的、基于命令行的、功能强大的程序调试工具。 对于一名Linux下工作的c++程序员，gdb是必不可少的工具。
# 2 启动gdb
1. 对C/C++程序的调试，需要在编译前就加上-g选项:
	```
	$g++ -g hello.cpp -o hello
	```
2. 调试可执行文件,program也就是你的执行文件，一般在当前目录下。
	```
	$gdb <program>
	```
3. 调试core文件(core是程序非法执行后core dump后产生的文件):

```$gdb <program> <core dump file>
$gdb program core.11127
调试服务程序:
$gdb <program> <PID>
$gdb hello 11127
如果你的程序是一个服务程序，那么你可以指定这个服务程序运行时的进程ID。gdb会自动attach上去，并调试他。program应该在PATH环境变量中搜索得到。


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg1Njc5MDgwN119
-->