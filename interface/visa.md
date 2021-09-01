
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
数据类型      字符串型

参数              (param3)
说明              输出变量（输出）
数据类型      字符串型

## 第4步： 断开

280行处理断开对话。VISA的  viClose  功能将通信中断并使VISA系统终结，这个功能的参数是起动信息（ctrl_ext.vba中的Defrm）。

## 语法

viClose(param)

## Parameter

参数           (param)
说明           起动信息（输入）
数据类型   长整型


# 样本程序 
用来读出外围设备（仪器）产品信息

ctrl_ext.vba  是利用E5071C作为系统控制器时，控制通过USB/GPIB接口电缆连接的仪器的样本程序。这个VBA程序由下列程序模块组成。

对象名   模块类型
内容      mdlVisa
标准模块  读出外部仪器的产品信息。

模块1  
模块2
标准模块
利用VISA程序库的两个定义文件

-   当您由E5071C VBA来控制外围设备时，利用对仪器提供的GPIB命令经VISA进行通信。相反，当您由E5071C VBA来控制仪器本身时，则利用对仪器提供的COM对象进行通信。
    

### 90行到100行

对VISA系统进行初始化和起动，并将起动信息输出到Defrm变量。在这个过程期间，若发生差错，程序便转到错误处理程序（320行到360行）。

### 130行到140行

建立与经GPIB连接的外部仪器（GPIB地址：17）的连接，并将连接信息输出到Equip变量。在这个过程期间，若发生差错，程序便转到错误处理程序（320行到360行）。

### 170行到180行

查询利用VISA经USB/GPIB接口电缆连接的外部仪器的产品信息，在这个过程期间，若发生差错，程序便转到错误处理程序（320行到360行）。

### 210行到250行

通过VISA对产品信息进行检索，并将产品信息输出到Prod变量。在消息框中显示读出结果。在这个过程期间，若发生差错，程序便转到错误处理程序（320行到360行）。

### 280行

中断通信并使VISA系统终结。

### 320行到360行

若VISA功能发生差错，将显示错误的细节并使程序终结。

读出产品信息（ctrl_ext.vba）

```
10| Sub Main()

20|

30| Dim status As Long 'VISA function status return code

40| Dim Defrm As Long 'Session to Default Resource Manager

50| Dim Equip As Long 'Session to instrument

60| Dim Prod As String * 100 'String to receive the result

70|

80| ' Initializes the VISA system.

90| status = viOpenDefaultRM(Defrm)

100| If (status <> VI_SUCCESS) Then GoTo VisaErrorHandler

110|

120| ' Opens the session to the specified instrument.

130| status = viOpen(Defrm, "GPIB0::17::INSTR", 0, 0, Equip)

140| If (status <> VI_SUCCESS) Then GoTo VisaErrorHandler

150|

160| ' Asks for the instrument's product information.

170| status = viVPrintf(Equip, "*IDN?" & Chr$(10), 0)

180| If (status <> VI_SUCCESS) Then GoTo VisaErrorHandler

190|

200| ' Reads the result.

210| status = viVScanf(Equip, "%t", Prod)

220| If (status <> VI_SUCCESS) Then GoTo VisaErrorHandler

230|

240| ' Displays the result.

250| MsgBox Prod

260|

270| ' Closes the resource manager session (which closes everything)
280| Call viClose(Defrm)
290|
300| GoTo Prog_end
310|
320| VisaErrorHandler:
330| Dim VisaErr As String * 200
340| Call viStatusDesc(Defrm, status, VisaErr)
350| MsgBox "Error : " & VisaErr, vbExclamation
360| Exit Sub
370|
380| Prog_end:
390|
400| End Sub
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjU2MTI1MDQ5LDE0OTA3Mjc1MDksMTY1Nj
g1MTE3MiwxNzY0MzIyNjA0XX0=
-->