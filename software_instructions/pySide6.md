# 1 打包发布
1.  PySide6程序打包后无法运行 no Qt platform plugin could be initialized
显示的报错信息：
```
This application failed to start because no Qt platform plugin could 
be initialized. Reinstalling the application may fix this problem.
```

Pyinstaller打包的文件目录里缺少了Qt运行所需的一些文件。所以，我们需要手动复制这些文件到打包生成的目录（dist\hello_world\PySide6）。

查找PySide6安装路径
pip show PySide6

拷贝plugins、translations、qt.conf到发布路径即可。

2. 打包命令
```
pyinstaller -F -w mycode.py
-F 是打包成一个文件
-w 不带后台窗口
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQyNDc0ODEwMF19
-->