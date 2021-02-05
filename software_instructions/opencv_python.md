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
		<h4><ul><a href="#title4.1">4.1 Capture Video from Camera </a> </h4>
		<h4><ul><a href="#title4.2">4.2 Playing Video from file</a> </h4>
		<h4><ul><a href="#title4.3">4.3 Saving a Video</a> </h4>
		<h4><ul><a href="#title4.4">4.4 cv.VideoCapture</a> </h4>
		<h4><ul><a href="#title4.5">4.5 cv.cvtColor</a> </h4>
		<h4><ul><a href="#title4.6">4.6 cv.VideoWriter_fourcc</a> </h4>
		<h4><ul><a href="#title4.7">4.7 cv.VideoWriter </a> </h4>  			
		<h4><ul><a href="#title4.8">4.8 cv.flip </a> </h4>
<h3><a href="#title5">5 Drawing Functions</a> </h3>
		<h4><ul><a href="#title5.1">5.1 cv.line </a> </h4>
		<h4><ul><a href="#title5.2">5.2 cv.rectangle</a> </h4>
		<h4><ul><a href="#title5.3">5.3 cv.circle</a> </h4>
		<h4><ul><a href="#title5.4">5.4 cv.ellipse</a> </h4>
		<h4><ul><a href="#title5.5">5.5 绘图多边形</a> </h4>
		<h4><ul><a href="#title5.6">5.6 向图像添加文本</a> </h4>
	<h3><a href="#title6">6 Mouse as a Paint-Brush</a> </h3>
		<h4><ul><a href="#title6.1">6.1 显示所有鼠标事件 </a> </h4>
		<h4><ul><a href="#title6.2">6.2 鼠标画圆</a> </h4>
		<h4><ul><a href="#title6.3">6.3 拖动鼠标画图 </a> </h4>
	<h3><a href="#title7">7 轨迹栏作为调色板</a> </h3>
		<h4><ul><a href="#title7.1">7.1 调色板程序 </a> </h4>
		<h4><ul><a href="#title7.2">7.2 cv.createTrackbar </a> </h4>
		<h4><ul><a href="#title7.3">7.3 cv.getTrackbarPos </a> </h4>
	<h3><a href="#title8">8 图像的基本操作</a> </h3>
		<h4><ul><a href="#title8.1">8.1 设置图像边框（边框填充） </a> </h4>
		<h4><ul><a href="#title8.2">8.2 cv.copyMakeBorder </a> </h4>
		<h4><ul><a href="#title8.3">8.3 Image ROI </a> </h4>
		<h4><ul><a href="#title8.4">8.4 分割和合并图像通道 </a> </h4>
		<h4><ul><a href="#title8.5">8.5 其他 </a> </h4>

		
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

```
import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
```
<h2 id="title4.3">4.3 Saving a Video </h2>  

```
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 0)
    # write the flipped frame
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
```

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
cv.VideoWriter_fourcc(*'XVID') 
相当于cv.VideoWriter_fourcc('X','V','I','D') ,其中*号相当于是一个解包器
```

关于python中 *的更多知识面参考如下:
[python中*号的使用](https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558)

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

<h1 id="title5">5 Drawing Functions</h1>  

**Goal**
* Learn to draw different geometric shapes with OpenCV
* You will learn these functions : cv.line(), cv.circle() , cv.rectangle(), cv.ellipse(), cv.putText() etc.
[参考链接](https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html)

<h2 id="title5.1">5.1 cv.line </h2>  

```
import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)

line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
thickness:厚度
要绘制一条直线，您需要传递直线的起点和终点。
```
<h2 id="title5.2">5.2 cv.rectangle </h2>  

```
要绘制矩形，您需要矩形的左上角和右下角
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
参数和line类似
```
<h2 id="title5.3">5.3 cv.circle </h2>  

```
要绘制一个圆，需要其中心坐标和半径。我们将在上面绘制的矩形内绘制一个圆。
cv.circle(img,(447,63), 63, (0,0,255), -1)
circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img
@param thickness 负值，代表填充图形。

```

<h2 id="title5.4">5.4 cv.ellipse </h2>  

```
要绘制椭圆，我们需要传递几个参数。一个参数是中心位置（x，y）。下一个参数是轴长度（长轴长度，短轴长度）。angle是椭圆沿逆时针方向旋转的角度。startAngle和endAngle表示从主轴沿顺时针方向测量的椭圆弧的起点和终点
cv.ellipse（img，（256,256），（100,50），0,0,180,255，-1）
cv.ellipse（img，（256,256），（100,50），0,0,180,(0,255,0)，-1）
ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) -> img
@param thickness 负值，代表填充图形。

```

<h2 id="title5.5">5.5 绘图多边形 </h2>  

要绘制多边形，首先需要顶点的坐标。将这些点设置为ROWSx1x2形状的数组，其中ROWS是顶点数，并且其类型应为int32。

```
polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) -> img
pts = np.array（[[10,5]，[20,30]，[70,20]，[50,10]]，np.int32）
pts = pts.reshape（（-1,1,2））
cv.polylines（img，[pts]，True，（0,255,255））
如果第三个参数为False，您将获得一条连接所有点的折线，而不是闭合形状

```

<h2 id="title5.6">5.6 向图像添加文本 </h2>  

要将文本放入图像中，需要指定以下内容。
* 您要写入的文字数据
* 您要放置它的位置坐标（即数据开始的左下角）。
* 字体类型（检查cv.putText（）文档以获取受支持的字体）
* 字体比例（指定字体大小）
* 常规的颜色，厚度，线型等内容。为了获得更好的外观，建议使用线型= cv.LINE_AA。
```
putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

```

<h1 id="title6">6 Mouse as a Paint-Brush </h1>  

[参考链接](https://docs.opencv.org/master/db/d5b/tutorial_py_mouse_handling.html)

<h2 id="title6.1">6.1 显示所有鼠标事件 </h2>  

```
import cv2 as cv
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )

['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 
'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 
'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 
'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 
'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 
'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

event： 
EVENT_LBUTTONDBLCLK = 7  左键双击 
EVENT_LBUTTONDOWN = 1 左键点击 
EVENT_LBUTTONUP = 4 左键释放 
EVENT_MBUTTONDBLCLK = 9 中间释放 
EVENT_MBUTTONDOWN = 3 中间点击 
EVENT_MBUTTONUP = 6 中间释放 
EVENT_MOUSEHWHEEL = 11 滚轮事件 
EVENT_MOUSEMOVE = 0 滑动
EVENT_MOUSEWHEEL = 10 滚轮事件 
EVENT_RBUTTONDBLCLK = 8 右键双击 
EVENT_RBUTTONDOWN = 2 右键点击 
EVENT_RBUTTONUP = 5 右键释放 

flags:  
EVENT_FLAG_ALTKEY = 32 按Alt不放事件 
EVENT_FLAG_CTRLKEY = 8 按Ctrl不放事件 
EVENT_FLAG_LBUTTON = 1 左键拖拽 
EVENT_FLAG_MBUTTON = 4 中键拖拽 
EVENT_FLAG_RBUTTON = 2 右键拖拽 
EVENT_FLAG_SHIFTKEY = 16 按Shift不放事件
```

<h2 id="title6.2">6.2 鼠标画圆 </h2> 

```
import numpy as np
import cv2 as cv
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),-1)
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()

鼠标事件回调函数说明
setMouseCallback(windowName, onMouse [, param]) -> None
鼠标回调函数，使用固定格式
# mouse callback function

def draw_circle(event,x,y,flags,param)
# x y为此时的坐标位置
```

<h2 id="title6.3">6.3 拖动鼠标画图 </h2> 

```
import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)
            
            
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()            
```

<h1 id="title7">7 轨迹栏作为调色板 </h1>  

**目标**
* 了解将轨迹栏绑定到OpenCV窗口
* 您将学习以下功能：cv.getTrackbarPos（），cv.createTrackbar（）等。

[参考链接](https://docs.opencv.org/master/d9/dc8/tutorial_py_trackbar.html)

<h2 id="title7.1">7.1 调色板程序 </h2>  

```
import numpy as np
import cv2 as cv
def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv.destroyAllWindows()
```

<h2 id="title7.2">7.2 cv.createTrackbar </h2>  

```
createTrackbar(trackbarName, windowName, value, count, onChange) -> None

value 默认值
count 最大值
onChange 为回调函数
```
<h2 id="title7.3">7.3 cv.getTrackbarPos </h2>  

```
getTrackbarPos(trackbarname, winname) -> retval
返回当前数值
```



<h1 id="title8">8 图像的基本操作 </h1>  

学习读取和编辑像素值，以及如何使用图像ROI和其他基本操作。

**目标**
学会：
-   访问像素值并对其进行修改
-   访问图像属性
-   设置感兴趣区域（ROI）
-   分割并合并图像

[参考链接](https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html)

<h2 id="title8.1">8.1 设置图像边框（边框填充） </h2>  

```
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv.imread('opencv-logo.png')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
```
<h2 id="title8.2">8.2 cv.copyMakeBorder </h2>  

```
copyMakeBorder(src, top, bottom, left, right, borderType[, dst[, value]]) -> dst
边框填充函数
src：要处理的原图
top, bottom, left, right：上下左右要扩展的像素数
borderType：边框类型，这个就是需要关注的填充方式
	其中默认方式和固定值方式最常用，我们详细说明一下
	固定值填充:(统一都填充0也称为zero padding)   
	img2 = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
	默认边框类型(其实是取镜像对称的像素填充)
	default = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
	一般情况下默认方式更加合理，因为边界的像素值更加接近，当然应视场合而定。
具体的填充，在后面使用的时候，再进一步研究。


如果要在图像周围创建边框（如相框），则可以使用cv.copyMakeBorder（）。但是它在卷积运算，零填充等方面有更多应用。此函数采用以下参数：

src-输入图像
顶部，底部，左侧，右侧边界的宽度，以相应方向上的像素数为单位
borderType-定义要添加哪种边框的标志。它可以是以下类型：
cv.BORDER_CONSTANT-添加恒定的彩色边框。该值应作为下一个参数给出。
cv.BORDER_REFLECT-边框将是边框元素的镜像，如下所示： fedcba | abcdefgh | hgfedcb
cv.BORDER_REFLECT_101或cv.BORDER_DEFAULT-与上述相同，但略有变化，例如： gfedcb | abcdefgh | gfedcba
cv.BORDER_REPLICATE-最后一个元素被复制，像这样： aaaaaa | abcdefgh | hhhhhhh
cv.BORDER_WRAP-无法解释，它看起来像这样： cdefgh | abcdefgh | abcdefg
value-边框颜色，如果边框类型为cv.BORDER_CONSTANT
```
<h2 id="title8.3">8.3 Image ROI </h2>  

使用Numpy索引次获得ROI(**region of interest**,即感兴趣的区域)。
比如你搜索眼睛，只需要在脸部区域，缩小了搜索范围，就可以提高效率。
在这里，我要选择球并将其复制到图像中的另一个区域：

```
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
```

<h2 id="title8.4">8.4 分割和合并图像通道 </h2>  

有时您需要在图像的B，G，R通道上单独工作。在这种情况下，您需要将BGR图像拆分为单个通道。在其他情况下，您可能需要加入这些单独的渠道来创建BGR图像。您可以通过以下方式简单地做到这一点：
```
b,g,r = cv.split(img)
img = cv.merge((b,g,r))
or
b = img[:,:,0]
假设您要将所有红色像素都设置为零-您不需要先拆分通道。numpy索引更快：
img[:,:,2] = 0

```
**警告**
cv.split（）是一项昂贵的操作（就时间而言）。因此，仅在必要时使用它。否则请进行Numpy索引。
<h2 id="title8.5">8.5 其他 </h2>  

```
像素值读取：
img.item(10,10,2)

像素值设置：
img.itemset((10,10,2),100)

形状：
print(img.shape)
(342, 548, 3)

大小:
print(img.size)
562248

数据类型:
print( img.dtype )
uint8
```
<h1 id="title9">9 图像算术运算 </h1>  

**目标**
- 学习图像的几种算术运算，例如加法，减法，按位运算等。
- 了解以下功能：cv.add(), cv.addWeighted()等。

[参考链接](https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html)

<h2 id="title9.1">9.1 图像加法 </h2>  

opencv的 cv.add()和numpy的res = img1 + img2都可以进行运算。
但是有区别，opencv是按照饱和度计算，numpy是按照取模计算，cv.add更加合理。

```
>>> x = np.uint8([250])
>>> y = np.uint8([10])
>>> print( cv.add(x,y) ) # 250+10 = 260 => 255
[[255]]
>>> print( x+y )          # 250+10 = 260 % 256 = 4
[4]

add(src1, src2[, dst[, mask[, dtype]]]) -> dst
```
<h2 id="title9.2">9.2 图像融合 </h2>  
图像融合也是也是图像加法，但是对图像赋予不同的权重，以使其具有融合或透明的感觉。

```
融合公式：（下标无法表示，所以看起来是这样的）
g(x)=(1−α)f0(x)+αf1(x)

addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) -> dst
dst = src1*alpha + src2*beta + gamma

img1 = cv.imread('ml.png')
img2 = cv.imread('opencv-logo.png')
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
```
<h2 id="title9.3">9.3 按位运算 </h2>  

这包括按位AND，OR，NOT和XOR操作。在提取图像的任何部分（如我们将在后续章节中看到），定义和使用非矩形ROI等方面，它们将非常有用。下面我们将看到一个如何更改图像特定区域的示例。 。

我想将OpenCV徽标放在图像上方。如果添加两个图像，它将改变颜色。如果将它们混合，则会获得透明效果。但我希望它不透明。如果是矩形区域，则可以像上一章一样使用ROI。但是OpenCV徽标不是矩形。因此，您可以按如下所示进行按位操作：

```
# Load two images
img1 = cv.imread('messi5.jpg')
img2 = cv.imread('opencv-logo-white.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
```

相关函数使用说明如下：
```



cv.threshold
```

灰度图：
一幅完整的图像，是由红色、绿色、蓝色三个通道组成的。红色、绿色、蓝色三个通道的缩览图都是以灰度显示的。用不同的灰度色阶来表示“ 红，绿，蓝”在图像中的比重。

我们可以通过下面几种方法，将其转换为灰度：
1.浮点算法：Gray=R*0.3+G*0.59+B*0.11
2.整数方法：Gray=(R*30+G*59+B*11)/100
3.移位方法：Gray =(R*76+G*151+B*28)>>8;
4.平均值法：Gray=（R+G+B）/3;
5.仅取绿色：Gray=G；
通过上述任一种方法求得Gray后，将原来的RGB(R,G,B)中的R,G,B统一用Gray替换，形成新的颜色RGB(Gray,Gray,Gray)，用它替换原来的RGB(R,G,B)就是灰度图了。
性能度量和改进技术

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzODYxMzU4NjYsLTE4OTAxOTY2Nyw0OD
Q4ODU1NDgsLTY2NTg1NjgwNSwxNjM3NjkxMDE5LDcxNTQ2Mzg5
MSwtMTM3MTE5OTc1NSwtOTAyNzYyNTg5LDExMzMwOTk5MDUsNT
E0MTQzNTI1LC0xMDMxMTMwODg1LDE1MjQyMTY0NTYsMTY3NDE1
NjQ0MSwxMzA4NTgxODM5LC01NDI3Mzg5NjIsMTM1MTAyNTEwNC
wtMTk2MjE4ODkwOSwxNzc2Mjg4MzA4LC0yMTI0NTk2MTExLDgx
NjY0MTQ5N119
-->