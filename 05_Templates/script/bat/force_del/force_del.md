
# windows 无法删除文件，提示找不到该项目

解决方案：

新建bat文件，并将以下两条命令拷贝到新建到bat文件中，然后将无法删除的文件拖入到bat文件中。

DEL /F /A /Q \\?\%1 　　

RD /S /Q \\?\%1

[脚本文件](https://github.com/yunfei00/document/blob/master/script/bat/force_del/force_del.bat)

脚本解析：

C:\Users\Administrator>help del

删除一个或数个文件。

DEL [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names

ERASE [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names

names 指定一个或多个文件或者目录列表。

通配符可用来删除多个文件。

如果指定了一个目录，该目录中的所

有文件都会被删除。

/P 删除每一个文件之前提示确认。

/F 强制删除只读文件。

/S 删除所有子目录中的指定的文件。

/Q 安静模式。删除全局通配符时，不要求确认

/A 根据属性选择要删除的文件

属性 R 只读文件 S 系统文件

H 隐藏文件 A 存档文件

I 无内容索引文件 L 重分析点

- 表示“否”的前缀

如果命令扩展被启用，DEL 和 ERASE 更改如下:

/S 开关的显示句法会颠倒，即只显示已经

删除的文件，而不显示找不到的文件。

C:\Users\Administrator>help RD

删除一个目录。

RMDIR [/S] [/Q] [drive:]path

RD [/S] [/Q] [drive:]path

/S 除目录本身外，还将删除指定目录下的所有子目录和

文件。用于删除目录树。

/Q 安静模式，带 /S 删除目录树时不要求确认

Windows下的通配符主要就2个：
*代替任意个任意字符
?代替1个任意字符主要用在文件/文件夹名上，当然也有一些配置域、IP等高级命令会用到*，但是那是属于网络协议规范的范畴了。
例子：比如您想查windows下的所有exe文件：dir c:\windows\*.exe如果您只想查windows下文件名有2个字符的exe文件：dir c:\windows\??.exe*和？也可以和固定字符混用，比如"新建文件夹*"，“exp_201312??.log”，“backup_?_*.txt”等
