# 1 realsense D455 介绍
D455 是intel生产的一款相机。

# 2 相机内参
K = fx s x0 
      0 fy y0 
      0 0 1
      
fx,fy为焦距，一般情况下，二者相等。  
x0,y0为主坐标（相对于成像平面）。  
s为坐标轴倾斜参数，理想情况下为0。


# 3 示例错误

1. 编译的时候报错信息如下：
```
CMakeFiles/rs-color.dir/rs-color.c.o: In function `check_error':
rs-color.c:(.text+0x1c): undefined reference to `rs2_get_failed_args'
rs-color.c:(.text+0x2b): undefined reference to `rs2_get_failed_function'
rs-color.c:(.text+0x4e): undefined reference to `rs2_get_error_message'
CMakeFiles/rs-color.dir/rs-color.c.o: In function `print_device_info':
rs-color.c:(.text+0xac): undefined reference to `rs2_get_device_info'
rs-color.c:(.text+0xe1): undefined reference to `rs2_get_device_info'
rs-color.c:(.text+0x116): undefined reference to `rs2_get_device_info'
CMakeFiles/rs-color.dir/rs-color.c.o: In function `main':
rs-color.c:(.text+0x180): undefined reference to `rs2_create_context'
rs-color.c:(.text+0x1a3): undefined reference to `rs2_query_devices'
rs-color.c:(.text+0x1c6): undefined reference to `rs2_get_device_count'
rs-color.c:(.text+0x22c): undefined reference to `rs2_create_device'

```
说明，编译的时候，找不到对应的库
在Makelist文档汇总，修改如下：
```
find_package (realsense2)
target_link_libraries (rs-color  PRIVATE realsense2::realsense2)
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAzNzI2NDM1MSwxNTcyNDY4NDkzLC02Mj
Y5MDU2MzAsLTEyODY5MzQ2MDUsLTE1MzIwMjQ2NjRdfQ==
-->