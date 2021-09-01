
# 1 使用VISA控制仪器的流程
启动VISA（viOpenDefaultRM）--> 连接viOpen -->通讯Sx：viVPrintf Rx：viVScanf --> 断开viClose

# 2 启动Visa

样本程序ctrl_ext.vba. 中的90行处理VISA系统起动对话。VISA的viOpenDefaultRM功能对VISA系统进行初始化和起动。viOpenDefaultRM 功能必须在调用其它VISA功能之前执行，而这个功能的参数是起动信息（ctrl_ext.vba中的Defrm）。

## 语法

viOpenDefaultRM(param)

## 参数

参数

(param)

说明
起动信息（输出）
数据类型 长整型
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzQyNDIxMywxNzY0MzIyNjA0XX0=
-->