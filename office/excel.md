# 目录

- <a href="#title1">1 Excel中时间戳转化成指定格式的时间</a> 
- <a href="#title2">2 Excel中分列相关函数</a> 

<div STYLE="page-break-after: always;"></div>
  <h1 id="title1">1 Excel中时间戳转化成指定格式的时间</h1>  

1. Excel默认不支持Unix格式时间戳，这在导入数据时十分不便。可以用以下公式将时间戳转换成Excel格式的时间，excel格式设置为yyyy-mm-dd hh:mm:ss：
	```
	=(x+8*3600)/86400+70*365+19
	```
2. 公式说明
	```
	x      时间戳的单元格
	8*3600 8为中国的时区 
	```
3. 原理介绍
	
	Excel的日期实际上是序列值，它以1900-1-1为1，每过一天序列值加1。
	Unix时间戳是从1970-1-1 0:00:00 UTC开始到现在经过的秒数。
	```
	用x表示时间戳，可得到换算公式：
	x+8*3600 当前时区的时间(秒)
	(x+8*3600)/86400 转换单位为天
	(x+8*3600)/86400+70*365 加上1900到1970这七十年
	(x+8*3600)/86400+70*365+19 闰年多出来的天数
	```
	1900年到1970年共是17个闰年，考虑到Excel将1900-1-1当作1，那么公式最后应该加18才对，为什么要加19？这是Excel中的一个bug——1900年也被当作闰年，因此应当再多加一天。
   <h1 id="title2">2 Excel中常用函数</h1>  
   <h2 id="title2.1">2.1 LEFT函数</h2>  		
 #### 概述
	LEFT函数从提供的文本字符串的左侧提取给定数量的字符。
### 返回值
	一个或多个字符。
#### 语法
	=LEFT (text, [num_chars])
#### 参数
	- **text** -要从中提取字符的文本。
	- **num_chars** -[可选]要提取的字符数，从文本的左侧开始。默认= 1。
#### 示例
![Excel LEFT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_left.png?itok=94fFaJe2)
   <h2 id="title2.2">2.2 RIGHT函数</h2>  		

#### 概述
	Excel右函数从提供的文本字符串的右端提取给定数量的字符。例如，RIGHT(“apple”，3)返回“ple”。
### 返回值
	一个或多个字符。
#### 语法
	=RIGHT (text, [num_chars])
#### 参数
	- **text** -要从中提取字符的文本。
	- **num_chars** -[可选]要提取的字符数，从文本的左侧开始。默认= 1。


![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_right_1.png?itok=dzNv7l7-)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQxMTE3OTUzMSwxNjI3NjU5MjU3LC03ND
cyMjQ5NTgsODk3NTU4MDg4XX0=
-->