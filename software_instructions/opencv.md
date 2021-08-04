# 目录
<h3><a href="#title1">1 opencv安装</a> </h3>
<h3><a href="#title2">2 mac上opencv开发环境配置</a> </h3>
<h3><a href="#title3">3 opencv学习</a> </h3>
		<h4><ul><a href="#title2.1">2.1 LEFT函数</a> </h4>
		<h4><ul><a href="#title2.2">2.2 RIGHT函数</a> </h4>
		
<div style="page-break-after:always"></div>

  <h1 id="title1">1 mac 上opencv安装</h1>  1 opencv安装

##  1.1 mac 上安装
与linux 安装类似

```
unzip 4.3.0.zip 
cd 4.3.0.zip 
cd opencv-4.3.0/
mkdir release
cd release/
cmake -D CMAKE_BUILD_TYPE=REALEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
sudo make install
```

opencv编译过程中，遇到问题，conda装过环境的，请参考：
https://github.com/JdeRobot/DetectionStudio/issues/99

其实，执行如下命令即可。然后删除所有文件，重新cmake
```
conda uninstall libtiff
```

## 1.2 windows 安装

[参考链接](https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html)
#  <h1 id="title1">2 mac上opencv开发环境配置</h1>  
参考 https://medium.com/@jaskaranvirdi/setting-up-opencv-and-c-development-environment-in-xcode-b6027728003

  <h1 id="title3">3 opencv学习</h1>  
  <h2 id="title3.1">3.1 VideoCapture </h2>  
  在opencv中关于视频的读操作是通过VideoCapture类来完成的；关于视频的写操作是通过VideoWriter类来实现的。
  
  [官网说明](https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a57c0e81e83e60f36c83027dc2a188e80)
  <h2 id="title3.1">3.2 cv::transpose</h2>  
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQzMjQ0MjQ3OCwxMDk3NDUxOTM2LC0xMT
k5MzcwMTY4LC02Njg4NTQ0NTYsLTE3MDU5NDk1NTZdfQ==
-->