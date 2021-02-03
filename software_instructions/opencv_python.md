# 目录
<h3><a href="#title1">1 install</a> </h3>
<h3><a href="#title2">2 help document</a> </h3>
<h3><a href="#title3">3 参考函数</a> </h3>
		<h4><ul><a href="#title3.1">3.1 cv.imread </a> </h4>
		<h4><ul><a href="#title3.2">2.2 RIGHT函数</a> </h4>
		
<div style="page-break-after:always"></div>

  <h1 id="title1">1 install</h1>  

```
pip install opencv-python
```
 <h1 id="title2">2 help document </h1>  
 
[document](https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html)

<h1 id="title3">3 参考函数 </h1>  

<h2 id="title3.1">3.1 cv.imread </h2>  

```
cv2.imread(filename[,flags])
para1:filename
para2:cv::ImreadModes
	cv2.IMREAD_UNCHANGED 按原样返回加载的图像  -1
	cv2.IMREAD_GRAYSCALE 返回灰度格式的图像     0
	cv2.IMREAD_COLOR     以BGR颜色格式返回图像,这是默认标志   1
	cv2.IMREAD_ANYDEPTH  当输入具有相应的深度时，此标志用于返回16位/ 32位图像，否则将其转换为8位 2
	cv2.IMREAD_ANYCOLOR  返回任何可能的颜色格式的图像 4
	cv2.IMREAD_LOAD_GDAL 用于gdal驱动程序以加载图像 8
	cv2.IMREAD_REDUCED_GRAYSCALE_2 返回灰度格式的图像，并且图像尺寸减小为原始图像尺寸的1/2 16
	cv2.IMREAD_REDUCED_COLOR_2 以BGR颜色格式返回图像，并且图像尺寸减小为原始图像尺寸的1/2 17
	cv2.IMREAD_REDUCED_GRAYSCALE_4 返回灰度格式的图像，并且图像大小减小为原始图像大小的1/4 32
	cv2.IMREAD_REDUCED_COLOR_4 以BGR颜色格式返回图像，并且图像尺寸减小为原始图像尺寸的1/4 33
	cv2.IMREAD_REDUCED_GRAYSCALE_8 返回灰度格式的图像，并且图像尺寸减小到原始图像尺寸的1/8 64
	cv2.IMREAD_REDUCED_COLOR_8 以BGR颜色格式返回图像，并且图像尺寸减小为原始图像尺寸的1/8 65
	
return:This method returns the matrix of pixels which represent the given image. if error,return NULL.

example:
import cv2
file = 'starry_night.jpg'
image = cv2.imread(file)
image.shape
(1200, 1920, 3)

image = cv2.imread('error_file')
if image is None:
	print('None')
None

Color Channel:
imread() takes the image as input and decodes into a matrix with the color channels stored in the order of Blue, Green, Red, and A respectively.  
image[:,:,0] represents Blue channel  
image[:,:,1] represents Green channel  
image[:,:,2] represents Red channel  
image[:,:,3] represents Transparency channel  透明通道
```
<h2 id="title3.X">3.X cv.samples.findFile </h2>  

```
findFile(relative_path[, required[, silentMode]])
找到则返回路径，否则返回空
```







<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM2MTY2NjUxNiwtMTc0MTM3NTU4MCw2Nz
A4Nzg0MTIsLTE2Mzg3NjE0NTEsMTkwMzIxMjczNCwxOTA0NzMz
NzcsLTEyMTA4MDUxNzYsLTQ5NTU1MzgwNF19
-->