[参考链接](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)

# 1. 为什么要使用cmake

理论上说,任意一个C++程序都可以用g++来编译。但当程序规模越来越大时,一个工程可能有许多个文件夹和源文件,这时输入的编译命令将越来越长。通常一个小型Ｃ++项目可能含有十几个类，各类间还存在着复杂的依赖关系。其中一部分要编译成可执行文件，另一部分要编译成库文件。如果仅靠g++命令，我们需要输入大量的编译指令，整个编译过程会变得异常繁琐。因此，对于C++项目，使用一些工程管理工具会更加高效。历史上工程师们曾使用makefile进行自动编译，但cmake要比它更加方便。

在一个cmake工程中，我们会用cmake命令生成一个makefile文件，然后用make命令根据这个makefile文件的内容编译整个工程。

# 2.CMakeLists.txt文件的基本写法

1. 声明要求的cmake最低版本
``cmake_minimun_required( VERSION 2.8)``
2. 声明一个cmake工程，工程名为post_fusion
``project(post_fusion)``
3.  添加c++ 11标准支持
``set( CMAKE_CXX_FLAGS "-std=c++11" )``
如果程序中使用了C++11标准，则需要设置告诉编译器，没有可以不用写。
4. 设置编译器编译模式：
··set( CMAKE_BUILD_TYPE "Debug" )

对于编译用的Debug模式和调试用的Release模式，在Debug模式中，程序运行较慢，当可以在IDE中进行断点调试，而Release模式则速度较快，但没有调试信息。不设置默认是Debug模式。

# 添加引用的第三方头文件，例如添加Eigen头文件

include_directories( "/usr/include/eigen3" )

#编译生成库文件

add_library(irfusion comfunc.c post_sins_gnss.cpp)

这条命令告诉cmake，我们想把这些源文件编译成一个叫作“irfusion”的库。在linux中，库文件分为静态库和动态库两种，静态库以.a作为后缀名，共享库以.so结尾。所有库都是一些函数打包后的集合，差别在于静态库每次被调用都会生成一个副本，而共享库则只有一个副本，更省空间。如果想生成共享库而不是静态库，只需要使用以下语句即可

add_library(irfusion_shared SHARED  comfunc.c post_sins_gnss.cpp)

此时得到的文件就是irfusion_shared.so了。

然后，在CMakeList.txt中添加一个可执行程序的生成命令，链接到刚才使用的库上:

add_executable(irfusion main.cpp)
target_link_libraries(irfusion irfusion_shared)

通过这两行语句，irfusion程序就能顺利使用irfusion_shared库中的代码了。

整个工程中的代码结构：
# 1 find_package
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MzA0NTQ1NDMsLTMzMjUzMzU0NSwtMj
M4NjgwMzQ1XX0=
-->