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
	Excel RIGHT函数从提供的文本字符串的右端提取给定数量的字符。例如，RIGHT(“apple”，3)返回“ple”。
### 返回值
	一个或多个字符。
#### 语法
	=RIGHT (text, [num_chars])
#### 参数
- **text** -要从中提取字符的文本。
- **num_chars** -[可选]要提取的字符数，从文本的左侧开始。默认= 1。

#### 示例
![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_right_1.png?itok=dzNv7l7-)

<h2 id="title2.3">2.3 MID函数</h2>  		

#### 概述
	Excel MID函数从提供的文本字符串的中间提取给定数量的字符。例如，=MID("apple"，2,3)返回"ppl"。
### 返回值
	提取的字符串。
#### 语法
	=MID (text, start_num, num_chars)
#### 参数
- **text** -要从中提取字符的文本。
- **start_num** -要提取的第一个字符的位置。
-  **num_chars** -要提取的字符数。

### 示例
![Excel MID function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_mid_1.png?itok=Um1z_8kh)

<h2 id="title2.4">2.4 SEARCH 函数</h2>  		

#### 概述
Excel SEARCH 函数返回一个文本字符串在另一个文本字符串中的位置。SEARCH返回find_text 在 within_text中第一个字符的位置。与查找不同，搜索允许使用通配符，而且不区分大小写。
### 返回值
表示find_text位置的数字。
#### 语法
	=SEARCH (find_text, within_text, [start_num])
#### 参数
- **find_text** -要查找的文本。
- **within_text** -要在其中搜索的文本。
-  **start_num** -[可选]在文本中搜索的起始位置。可选，默认为1。

### 示例
![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_search_1.png?itok=1YhJOWw1)
<h2 id="title2.4">2.4 SUBSTITUTE 函数</h2>  		

#### 概述
Excel SEARCH 函数返回一个文本字符串在另一个文本字符串中的位置。SEARCH返回find_text 在 within_text中第一个字符的位置。与查找不同，搜索允许使用通配符，而且不区分大小写。
### 返回值
表示find_text位置的数字。
#### 语法
	=SEARCH (find_text, within_text, [start_num])
#### 参数
- **find_text** -要查找的文本。
- **within_text** -要在其中搜索的文本。
-  **start_num** -[可选]在文本中搜索的起始位置。可选，默认为1。

### 示例
![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_search_1.png?itok=1YhJOWw1)


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwOTc3ODQ5MDgsMTYyNzY1OTI1NywtNz
Q3MjI0OTU4LDg5NzU1ODA4OF19
-->