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
	cv2.IMREAD_UNCHANGED 按原样返回加载的图像  -1
	cv2.IMREAD_GRAYSCALE 返回灰度格式的图像     0
	cv2.IMREAD_COLOR     以BGR颜色格式返回图像,这是默认标志   1
	cv2.IMREAD_ANYDEPTH  当输入具有相应的深度时，此标志用于返回16位/ 32位图像，否则将其转换为8位 2
	cv2.IMREAD_ANYCOLOR  返回任何可能的颜色格式的图像 4
	
return:This method returns the matrix of pixels which represent the given image. Pixel is nothing but the smallest unit of the image.
```

3. ds 




<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA1MDM3NjcyNCwtMTYzODc2MTQ1MSwxOT
AzMjEyNzM0LDE5MDQ3MzM3NywtMTIxMDgwNTE3NiwtNDk1NTUz
ODA0XX0=
-->