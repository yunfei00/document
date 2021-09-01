
参考地址 https://documentation.help/E5071C-zh/Programming_with_VISA.htm#Overview
# 1 使用VISA控制仪器的流程
启动VISA（viOpenDefaultRM）--> 连接viOpen -->通讯Sx：viVPrintf Rx：viVScanf --> 断开viClose

# 2 启动Visa

样本程序ctrl_ext.vba. 中的90行处理VISA系统起动对话。VISA的viOpenDefaultRM功能对VISA系统进行初始化和起动。viOpenDefaultRM 功能必须在调用其它VISA功能之前执行，而这个功能的参数是起动信息（ctrl_ext.vba中的Defrm）。

## 语法

viOpenDefaultRM(param)

## 参数

参数         (param)
说明         起动信息（输出）
数据类型 长整型

## 第2步：连接

130行处理连接对话。VISA的viOpen功能进行与规定仪器的连接。viOpen功能返回某个值，使得VISA功能可以将其应用于规定仪器，这个功能的参数是起动信息（Defrm）、规定仪器的地址信息（ctrl_ext.vba中的“GPIB：：17：：INSTR”）、接入方式（ctrl_ext.vba中的0）、超时（ctrl_ext.vba中的0）和连接信息（ctrl_ext.vba中的Equip）。

## 语法

viOpen(param1,  param2,  param3, param4, param5)

## 参数

参数            (param1)
说明            起动信息（输入）
数据类型    长整型

参数           (param2)
说明           规定仪器的地址信息（输入）
数据类型    字符串型
语法           "GPIB0::gpib address::INSTR"
					"USB0::manufacturer ID::model code::serial number::0::INSTR"  
					(ex. "USB0::2391::2312::MY12345678::0::INSTR")
					"TCPIP0::IP address::inst0::INSTR"

参数          (param3)
说明          接入方式（输入0）

参数          (param4)
说明          超时（输入0）

参数          (param5)
说明          连接信息（输出）
数据类型   长整型


## 第3步. 通信

170行进行通信对话。VISA的viVPrintf功能将程序消息（GPIB命令）发送到规定仪器。这个功能的参数是连接信息（Equip）、程序消息（*EDN?）和待格式化变量（ctrl_ext.vba中的0）。

-   为了输入/输出GPIB命令，主要是利用viVPrintf  功能和viVScanf功能信息，但也可以利用其它VISA功能。欲知详情，请参考visa.hlp  （VISA程序库的在线帮助）。
    

## 语法

viVPrintf(param1, param2, param3)

## 参数

参数           (param1)
说明           连接信息（输出）
数据类型   长整型

参数           (param2)
说明           发送GPIB命令的程序消息时的程序消息，消息结束处要求一个消息终结符（ctrl_ext.vba中的Chr$（10））
数据类型    字符串型

参数         (param3)
说明         变量待格式化，若不可应用，则输入0。
数据类型  规定的数据类型

210行控制接收对话。VISA的viVScanf  功能接收来自规定仪器的结果，并将其存储在输出变量中。这个功能的参数是连接信息（ctrl_ext.vba中的Equip）、输出变量的格式参数（ctrl_ext.vba中的%t）和输出变量（ctrl_ext.vba中的Prod）。

## 语法

viVScanf(param1, param2, param3)

## 参数

参数            (param1)
说明            连接信息（输入）
数据类型    长整型

参数             (param2)
说明             输出变量的格式参数
数据类型

字符串型

参数

(param3)

说明

输出变量（输出）

数据类型

字符串型
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAzMTYwMTk2OCwxNzY0MzIyNjA0XX0=
-->