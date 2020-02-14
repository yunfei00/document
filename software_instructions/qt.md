# 1 ubuntu 上Qt程序发布
1. 下载linuxdeployqt-6-x86_64.AppImage 网址：
https://github.com/probonopd/linuxdeployqt/releases
2. 使用Qt提供的qmake工具
export PATH=/home/shuaige/Qt5.9.1/5.9.1/gcc_64/bin:$PATH
qmake 查看一下 确保是可以运行的
	```
	qmake -v
	QMake version 3.1
	Using Qt version 5.9.1 in /home/shuaige/Qt5.9.1/5.9.1/gcc_64/lib
	```
3. 修改权限 并发布
	```
	chmod a+x linuxdeployqt-6-x86_64.AppImage
	./linuxdeployqt-6-x86_64.AppImage test
	```
4. 打包发布
	```
	mkdir target
	cd target/
	cp ~/build-test-Desktop_Qt_5_9_1_GCC_64bit-Release/test ./
	cp ~/build-test-Desktop_Qt_5_9_1_GCC_64bit-Release/qt.conf ./
	cp ~/build-test-Desktop_Qt_5_9_1_GCC_64bit-Release/plugins ./ -r
	cp ~/build-test-Desktop_Qt_5_9_1_GCC_64bit-Release/translations/ ./ -r
	cp ~/build-test-Desktop_Qt_5_9_1_GCC_64bit-Release/lib ./ -r
	```
5. 在未安装Qt的环境下运行程序

# QT 常见问题
1.  error: cannot find -lGL
解决办法：

sudo apt-get install build-essential libgl1-mesa-dev

依赖库问题 安装完成后应该可以解决
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg0MzQ1MDg1NywxMTg4NTMwMTkwXX0=
-->