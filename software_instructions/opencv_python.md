# 目录
<h3><a href="#title1">1 install</a> </h3>
<h3><a href="#title2">2 help document</a> </h3>
<h3><a href="#title3">3 images</a> </h3>
		<h4><ul><a href="#title3.1">3.1 code </a> </h4>
		<h4><ul><a href="#title3.2">3.2 cv.imread </a> </h4>
		<h4><ul><a href="#title3.3">3.3 cv.imshow</a> </h4>
		<h4><ul><a href="#title3.4">3.4 cv.waitKey</a> </h4>
		<h4><ul><a href="#title3.5">3.5 cv.imwrite</a> </h4>
		<h4><ul><a href="#title3.6">3.6 cv.samples.findFile</a> </h4>
<h3><a href="#title4">4 videos</a> </h3>
		<h4><ul><a href="#title4.1">3.1 cv.imread </a> </h4>
		<h4><ul><a href="#title4.2">3.2 cv.imshow</a> </h4>
		<h4><ul><a href="#title4.3">3.3 cv.waitKey</a> </h4>
		<h4><ul><a href="#title4.4">3.4 cv.imwrite</a> </h4>
		<h4><ul><a href="#title4.5">3.5 cv.samples.findFile</a> </h4>

		
<div style="page-break-after:always"></div>

  <h1 id="title1">1 install</h1>  

```
pip install opencv-python
```
 <h1 id="title2">2 help document </h1>  
 
[document](https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html)

<h1 id="title3">3 images </h1>  

**Learn to load an image, display it, and save it back**

<h2 id="title3.1">3.1 code </h2>  

```
import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("starry_night.jpg"))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
```

<h2 id="title3.2">3.2 cv.imread </h2>  

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

<h2 id="title3.3">3.3 cv.imshow </h2>  

```
imshow(winname, mat) -> None
para1:window name
para2:matrix image
打开了一个窗口以显示图像。窗口大小取决于图像的大小。如果窗口大小大于屏幕分辨率，则它将显示图像的缩放版本
```
<h2 id="title3.4">3.4 cv.waitKey</h2>  

```
waitKey([, delay]) -> retval
param: delay Delay in milliseconds. 0 is the special value that means "forever".
retval:key value

注意：只有在窗口模式下，才起作用。
```
<h2 id="title3.5">3.5 cv.imwrite</h2>  

```
imwrite(filename, img[, params]) -> retval
para1:filename
para2:img (Mat or vector of Mat) Image or Images to be saved.
para3:Format-specific parameters encoded as pairs (paramId_1, paramValue_1, paramId_2, paramValue_2, ... .) see cv::ImwriteFlags
	cv2::ImwriteFlags 暂不涉及，后期遇到查看
retval:It returns either True or False. Return `True` if the image is successfully saved otherwise return `False`.
```

<h2 id="title3.6">3.6 cv.samples.findFile </h2>  

```
findFile(relative_path[, required[, silentMode]])
找到则返回路径，否则返回空
```

<h1 id="title4">4 videos </h1>  

**Learn to play videos, capture videos from a camera, and write videos**
[参考链接](https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html)

<h2 id="title4.1">4.1 Capture Video from Camera </h2>  

```
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
```


<h2 id="title4.2">4.2 Playing Video from file </h2>  
<h2 id="title4.3">4.3 Saving a Video </h2>  

<h2 id="title4.4">4.4 cv.VideoCapture </h2>  

```
class VideoCapture(builtins.object)
cv2.VideoCapture(video_path or  device index  )
VideoCapture是一个对象，如果需要打开本地文件，则初始化参数需要本地的视频文件路径，如果是打开网络摄像头，则需要输入摄像头的编号.
编号如：/dev/video0，/dev/video1,/dev/video2

```

<h2 id="title4.5">4.5 cv.cvtColor </h2>  

```
cvtColor(src, code[, dst[, dstCn]]) -> dst
颜色转换，将图像的颜色从一种颜色空间更改为另一种颜色

BGR –>蓝绿色红色  
HSV –>色相饱和度值

**注意：**  
1）对于BGR，蓝色，绿色，红色的值范围是[0,255]  
2）对于HSV，色相的范围是[0,179]，饱和度范围是[0,255]，值范围是[0,255]。

convert_image  =  cv2.cvtColor(image,  cv2.COLOR_BGR2HSV)
```

<h2 id="title4.6">4.6 cv.VideoWriter_fourcc </h2>  

```
fourcc :four character code
是一种4字符代码，是一种视频流格式
```

<h2 id="title4.7">4.7 cv.VideoWriter </h2>  

[python 参考](https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html)
```
cv.VideoWriter()
cv.VideoWriter(filename, fourcc, fps, frameSize[, isColor])
cv.VideoWriter(filename, apiPreference, fourcc, fps, frameSize[, isColor])
```

<h2 id="title4.8">4.8 cv.flip </h2>  

```
flip(src, flipCode[, dst]) -> dst
翻转图片
@param src input array.
@param dst output array of the same size and type as src.
@param flipCode a flag to specify how to flip the array; 0 means
 flipping around the x-axis and positive value (for example, 1) means flipping around y-axis. Negative value (for example, -1) means flipping around both axes.
```






<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NjUxMjI3MDYsLTQ1NjU2MzMyNSwxOT
gzOTAwOTQxLC0yMDAyNzc5NTExLDIxMjcxMzI4NTcsLTMzMTA0
NDMxNiwtMTc5OTEwODU3OCwtMTY2MDEyNTAxNywtMTM4MDE2Mz
QwMCwtMTc4OTMxNzc1OCwtMTE0NDIzOTA1MywtNjkwNTU2NzUy
LC0xNzQxMzc1NTgwLDY3MDg3ODQxMiwtMTYzODc2MTQ1MSwxOT
AzMjEyNzM0LDE5MDQ3MzM3NywtMTIxMDgwNTE3NiwtNDk1NTUz
ODA0XX0=
-->