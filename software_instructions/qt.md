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
# 2 快捷键
 |说明|快捷键|
 |-----|----|
 |注释 |ctrl + /
|运行 |ctrl + r
|编译 |ctrl + b
|字体缩放 |ctrl + 鼠标滚轮
|查找 |chtl + f
|整行移动 |ctrl + shift +  &uarr; 或者 &darr;
|帮助文档 |F1|
|自动对齐 |ctrl + i|
|同名之前的.h和.cpp切换| F4
 
# 3 QT 常见问题
1.  error: cannot find -lGL
	解决办法：
	```
	sudo apt-get install build-essential libgl1-mesa-dev
	```
	 依赖库问题 安装完成后应该可以解决
2. Qt realease 版本不输出自带日志行号等信息
	原因是：文件信息、行数等信息在Release版本默认舍弃。我们只要在.pro文件定义一个宏
	```
	DEFINES += QT_MESSAGELOGCONTEXT
	```
# 4 学习笔记
## 4.1. QString与QByteArray互相转换的方法
1. QString转QByteArray方法
	```
	QString str("hello");
	QByteArray bytes = str.toUtf8(); // QString转QByteArray方法1
	QString str("hello");
	QByteArray bytes = str.toLatin1(); // QString转QByteArray方法2
	```
2. QByteArray转QString方法
	```
	//Qt5.3.2
	QByteArray bytes("hello world");
	QString string = bytes; // QByteArray转QString方法1
	QByteArray bytes("hello world");
	QString string;
	string.prepend(bytes);// QByteArray转QString方法2
	qDebug() << string;
	```
3. QByteArray不以\0为结束符，和数组一样。
4. char arr 转QByteArray

## 4.2 QlineEdit常用操作
1. 设置光标
	```
	ui->le_cal_weight_result->setFocus();
	```
2. 清空按钮
void setClearButtonEnabled(bool); //是否设置一个清空按钮.点击这个清空按钮后，就会自动删除行编辑框内的所有内容,类似于clear().
3. 设置行编辑框内文本的显示模式.
void setEchoMode(QLineEdit::EchoMode); //设置行编辑框内文本的显示模式.
如图两种显示模式是最常用的模式.分别为:QLineEdit::Normal,QLineEdit::Password.默认为QLineEdit::Normal.
4. void setAlignent(Qt::Alignment flag); //设置文本输入的位置.
5. void setValidator(QVaildator*); //设置输入验证器.(很重要!!)
6. void setPlaceText(QString); //设置占位符.
7. void setText(QString); //设置行编辑框内的文本.
8. void setReadOnly(bool); //把该行编辑框设置为只读模式，无法进行编辑.

8.void setEnabled(bool); //设置是否激活行编辑框，作用和7类似.

9.void setContextMenuPolicy(Qt::NoContextMenu). //设置该行编辑框内不会出现菜单.(密码输入里必用).

10.void setDragEnabled(bool); //设置行编辑框内的被选择的文本能否被拖拽，默认不能被拖拽.

11.void setAcceptDrops(bool); //设置行编辑框能否被拖拽进来文本.

12.bool isModified(); //判断文本是否被修改.

13.void selectAll(); //选中框内所有文本.

14.QString displayText(); //返回显示的文本.

15.QString selectedText(); //返回被选中的文本.

信号:

1.void cursorPositionChanged(int old, int new); //光标位置改变就发现信号.

2.void returnPressed(); //光标在行编辑框内时，点击回车即发出信号.

3.void selectionChanged() //选择的文本发生变化时，发出信号.

4.void textChanged(const QString & text) //只要文本内容发生改变，则发出信号.

5.void textEdited(const QString &text); //当文本被编辑后发出信号,注意!程序中调用的setText()方法并不会触发该信号.

# 4 QT 全屏问题

```

int height = this->height();

int weight = this->width();

QString disp = "修改前分辨率:" + QString::number(weight) + "X" + QString::number(height);

qInfo() << disp;

//ui->textBrowser->append(QString::number(height) + QString::number(weight));

static bool flag = false;

flag = !flag;

if (flag){

this->showFullScreen();

} else {

this->showNormal();

}

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg0MjEzMDc2NywtMTc1ODI4NDMwNyw5ND
I0NzQ5MjQsLTIwMDA0MDY3MzAsMTE4ODUzMDE5MF19
-->