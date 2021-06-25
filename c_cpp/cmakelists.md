[参考链接](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)

**一. 为什么要使用cmake**

理论上说,任意一个C++程序都可以用g++来编译。但当程序规模越来越大时,一个工程可能有许多个文件夹和源文件,这时输入的编译命令将越来越长。通常一个小型Ｃ++项目可能含有十几个类，各类间还存在着复杂的依赖关系。其中一部分要编译成可执行文件，另一部分要编译成库文件。如果仅靠g++命令，我们需要输入大量的编译指令，整个编译过程会变得异常繁琐。因此，对于C++项目，使用一些工程管理工具会更加高效。历史上工程师们曾使用makefile进行自动编译，但cmake要比它更加方便。

在一个cmake工程中，我们会用cmake命令生成一个makefile文件，然后用make命令根据这个makefile文件的内容编译整个工程。
# 1 find_package
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjExNTk3MzkyNywtMzMyNTMzNTQ1LC0yMz
g2ODAzNDVdfQ==
-->