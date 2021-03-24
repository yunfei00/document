# 目录
<h3><a href="#title1">1 安装</a> </h3>
<h3><a href="#title2">2 help document</a> </h3>
<h3><a href="#title3">3 OpenCV中的Gui功能</a> </h3>
<h4><a href="#title3.1">3.1 images</a> </h4>
		<h5><ul><a href="#title3.1.1">3.1.1 code </a> </h5>
		<h5><ul><a href="#title3.1.2">3.1.2 cv.imread </a> </h5>
		<h5><ul><a href="#title3.1.3">3.1.3 cv.imshow</a> </h5>
		<h5><ul><a href="#title3.1.4">3.1.4 cv.waitKey</a> </h5>
		<h5><ul><a href="#title3.1.5">3.1.5 cv.imwrite</a> </h5>
		<h5><ul><a href="#title3.1.6">3.1.6 cv.samples.findFile</a> </h5>
<h4><a href="#title3.2">3.2 videos</a> </h4>
		<h5><ul><a href="#title3.2.1">3.2.1 Capture Video from Camera </a> </h5>
		<h5><ul><a href="#title3.2.2">3.2.2 Playing Video from file</a> </h5>
		<h5><ul><a href="#title3.2.3">3.2.3 Saving a Video</a> </h5>
		<h5><ul><a href="#title3.2.4">3.2.4 cv.VideoCapture</a> </h5>
		<h5><ul><a href="#title3.2.5">3.2.5 cv.cvtColor</a> </h5>
		<h5><ul><a href="#title3.2.6">3.2.6 cv.VideoWriter_fourcc</a> </h5>
		<h5><ul><a href="#title3.2.7">3.2.7 cv.VideoWriter </a> </h5>  			
		<h5><ul><a href="#title3.2.8">3.2.8 cv.flip </a> </h5>
<h4><a href="#title3.3">3.3 Drawing Functions</a> </h4>
		<h5><ul><a href="#title3.3.1">3.3.1 cv.line </a> </h5>
		<h5><ul><a href="#title3.3.2">3.3.2 cv.rectangle</a> </h5>
		<h5><ul><a href="#title3.3.3">3.3.3 cv.circle</a> </h5>
		<h5><ul><a href="#title3.3.4">3.3.4 cv.ellipse</a> </h5>
		<h5><ul><a href="#title3.3.5">3.3.5 绘图多边形</a> </h5>
		<h5><ul><a href="#title3.3.6">3.3.6 向图像添加文本</a> </h5>
	<h4><a href="#title3.4">3.4 Mouse as a Paint-Brush</a> </h4>
		<h5><ul><a href="#title3.4.1">3.4.1 显示所有鼠标事件 </a> </h5>
		<h5><ul><a href="#title3.4.2">3.4.2 鼠标画圆</a> </h5>
		<h5><ul><a href="#title3.4.3">3.4.3 拖动鼠标画图 </a> </h5>
	<h4><a href="#title3.5">3.5 轨迹栏作为调色板</a> </h4>
		<h5><ul><a href="#title3.5.1">3.5.1 调色板程序 </a> </h5>
		<h5><ul><a href="#title3.5.2">3.5.2 cv.createTrackbar </a> </h5>
		<h5><ul><a href="#title3.5.3">3.5.3 cv.getTrackbarPos </a> </h5>
	<h3><a href="#title4">4 核心操作</a> </h3>
	<h4><a href="#title4.1">4.1 图像的基本操作</a> </h4>
		<h5><ul><a href="#title4.1.1">4.1.1 设置图像边框（边框填充） </a> </h5>
		<h5><ul><a href="#title4.1.2">4.1.2 cv.copyMakeBorder </a> </h5>
		<h5><ul><a href="#title4.1.3">4.1.3 Image ROI </a> </h5>
		<h5><ul><a href="#title4.1.4">4.1.4 分割和合并图像通道 </a> </h5>
		<h5><ul><a href="#title4.1.5">4.1.5 其他 </a> </h5>
	<h4><a href="#title4.2">4.2 图像算术运算</a> </h4>
		<h5><ul><a href="#title4.2.1">4.2.1 图像加法 </a> </h5>
		<h5><ul><a href="#title4.2.2">4.2.2 图像融合 </a> </h5>
		<h5><ul><a href="#title4.2.3">4.2.3 按位运算 </a> </h5>
	<h4><a href="#title4.3">4.3 性能度量和改进技术</a> </h4>
		<h5><ul><a href="#title4.3.1">4.3.1 运行时间计算 </a> </h5>
		<h5><ul><a href="#title4.3.2">4.3.2 OpenCV中的默认优化 </a> </h5>
		<h5><ul><a href="#title4.3.3">4.3.3 在IPython中评估性能 </a> </h5>
		<h5><ul><a href="#title4.3.4">4.3.4 性能优化技术 </a> </h5>

		
<div style="page-break-after:always"></div>

  <h1 id="title1">1 安装</h1>  

[安装参考](https://docs.opencv.org/3.4/d7/d9f/tutorial_linux_install.html)

 <h1 id="title2">2 help document </h1>  
 
[document](https://docs.opencv.org/master/d9/df8/tutorial_root.html)

<h1 id="title3">3 OpenCV学习 </h1>  
<h2 id="title3.1">3.1 Mat-基本图像容器 </h2>  

```
Mat本质上是具有两个数据部分的类：
矩阵头（包含诸如矩阵大小，用于存储的方法，用于存储矩阵的地址之类的信息，等等）和指向包含该矩阵的矩阵的指针像素值（根据选择的存储方法采用任何尺寸）。
矩阵标题的大小是恒定的，但是矩阵本身的大小可能因图像而异，通常会增加几个数量级。

通过不必要地复制(可能较大的图像)来提升程序速度。
```

```
Mat A, C; // 只创建头

A = imread(argv[1], [IMREAD_COLOR); // 分配矩阵
Mat B(A); // Use the copy constructor

C = A; // Assignment operator
```
以上A，B，C都指向同一数据块，但是头部不同。
矩阵数据的释放，使用引用计数器来进行，当引用计数器为0时，释放数据。

真实的拷贝如下：
```
Mat F = A.clone();
Mat G;
A.copyTo(G);
```

OpenCV函数的输出图像分配是自动的(除非另有说明)。
不需要考虑使用OpenCV的c++接口进行内存管理。

赋值操作符和复制构造函数只复制头文件。

图像的底层矩阵可以使用cv::Mat::clone()和cv::Mat::copyTo()函数进行复制。

<h3 id="title3.1.1">3.1.1 code </h3>  


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk5MDE2Mjk0OSwtMTMyNDg4NTc0NCwtMT
AzMzYzMTM4MSwyMzY5Mzk5MjksLTEzNTI4Mjg4MTBdfQ==
-->