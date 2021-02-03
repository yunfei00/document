# 目录
<h3><a href="#title1">1 install</a> </h3>
<h3><a href="#title2">2 help document</a> </h3>
<h3><a href="#title3">3 opencv学习</a> </h3>
		<h4><ul><a href="#title2.1">2.1 LEFT函数</a> </h4>
		<h4><ul><a href="#title2.2">2.2 RIGHT函数</a> </h4>
		
<div style="page-break-after:always"></div>

  <h1 id="title1">1 install</h1>  

```
pip install opencv-python
```
 <h1 id="title2">2 help document </h1>  
 
[document](https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html)

<h1 id="title3">read,write,show image </h1>  

1.  cv.imread

```
cv2.imread(filename[,flags])
para1:filename
para2:cv::ImreadModes
	cv2.IMREAD_UNCHANGED 按原样返回加载的图像
	cv2.IMREAD_GRAYSCALE 返回灰度格式的图像。或者，我们可以为此标志传递整数值0。
return:This method returns the matrix of pixels which represent the given image. Pixel is nothing but the smallest unit of the image.
```

3. ds 




<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY0ODgyNTYsLTE2Mzg3NjE0NTEsMTkwMz
IxMjczNCwxOTA0NzMzNzcsLTEyMTA4MDUxNzYsLTQ5NTU1Mzgw
NF19
-->