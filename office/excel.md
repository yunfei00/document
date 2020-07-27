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
   1. LEFT 

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, LEFT("apple",3) returns "app".

Purpose

Extract text from the left of a string

Return value

One or more characters.

Syntax

=LEFT (text, [num_chars])

Arguments

-   **text**  - The text from which to extract characters.
-   **num_chars**  - [optional] The number of characters to extract, starting on the left side of text. Default = 1.

Usage notes

-   Use the LEFT function when you want to extract characters starting at the left side of  **text**.
-   **num_chars**  is optional and defaults to 1.
-   LEFT will extract digits from numbers as well.
-   Number formatting (i.e. the currency symbol $) is not part of a number so is not counted or extracted.


<!--stackedit_data:
eyJoaXN0b3J5IjpbNDYyNjY5Mjg0LDE2Mjc2NTkyNTcsLTc0Nz
IyNDk1OCw4OTc1NTgwODhdfQ==
-->