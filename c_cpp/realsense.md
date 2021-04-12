# 目录
<h3><a href="#title1">1 说明</a> </h3>
<h3><a href="#title2">2 rs-hello-realsense</a> </h3>
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

  <h1 id="title1">1 说明</h1>  

本文档主要针对C++版本中的realsense库进行学习记录。

 <h1 id="title2">2 rs-hello-realsense </h1>  
 
```
#include <librealsense2/rs.hpp> // Include RealSense Cross Platform API
#include <iostream>             // for cout

// Hello RealSense example demonstrates the basics of connecting to a RealSense device
// and taking advantage of depth data
int main(int argc, char * argv[]) try
{
    // Create a Pipeline - this serves as a top-level API for streaming and processing frames
    rs2::pipeline p;

    // Configure and start the pipeline
    p.start();

    while (true)
    {
        // Block program until frames arrive
        rs2::frameset frames = p.wait_for_frames();

        // Try to get a frame of a depth image
        rs2::depth_frame depth = frames.get_depth_frame();

        // Get the depth frame's dimensions
        float width = depth.get_width();
        float height = depth.get_height();

        // Query the distance from the camera to the object in the center of the image
        float dist_to_center = depth.get_distance(width / 2, height / 2);

        // Print the distance
        std::cout << "The camera is facing an object " << dist_to_center << " meters away \r";
    }

    return EXIT_SUCCESS;
}
catch (const rs2::error & e)
{
    std::cerr << "RealSense error calling " << e.get_failed_function() << "(" << e.get_failed_args() << "):\n    " << e.what() << std::endl;
    return EXIT_FAILURE;
}
catch (const std::exception& e)
{
    std::cerr << e.what() << std::endl;
    return EXIT_FAILURE;
}

```
<h1 id="title3">3 OpenCV学习 </h1>  
<h2 id="title3.1">3.1 Mat-基本图像容器 </h2>  

```
Mat本质上是具有两个数据部分的类：
矩阵头（包含诸如矩阵大小，用于存储的方法，用于存储矩阵的地址之类的信息，等等）和指向包含该矩阵的矩阵的指针像素值（根据选择的存储方法采用任何尺寸）。
矩阵标题的大小是恒定的，但是矩阵本身的大小可能因图像而异，通常会增加几个数量级。

通过不必要地复制(可能较大的图像)来提升程序速度。
```

<h1 id="title_reference">参考 </h1>  

1. [rs2::context](http://docs.ros.org/en/kinetic/api/librealsense2/html/classrs2_1_1context.html)

	常见用法：用于查询设备
	```
	if (ctx.query_devices().size() == 0) {
		EXIT_PROGRAM("No realsense device connected.");
	} else {
	std::cout << "realsense device count is " << ctx.query_devices().size() << std::endl;
	}
	```
2. [rs2::config](http://docs.ros.org/en/kinetic/api/librealsense2/html/classrs2_1_1config.html)
该配置允许管道用户为管道流以及设备选择和配置请求过滤器。这是管道创建中的可选步骤，因为管道在内部解析其流设备。Config为用户提供了一种设置过滤器并测试是否与设备的管道要求没有冲突的方法。它还允许用户找到配置过滤器和管道的匹配设备，以便显式选择设备，并在流开始之前修改其控件。
	```
	cfg.enable_stream(RS2_STREAM_COLOR, -1, 1280, 720, RS2_FORMAT_BGR8, 30);
	```
3. [rs2::pipeline](http://docs.ros.org/en/kinetic/api/librealsense2/html/classrs2_1_1pipeline.html)
管道用于采集视频流
	```
	rs2::pipeline pipe;
	pipe.start(cfg);
	pipe.start(cfg);
	```

4. [rs2::align](http://docs.ros.org/en/kinetic/api/librealsense2/html/classrs2_1_1align.html)

	```
	rs2::align align_to_color(RS2_STREAM_DEPTH);
	data = align_to_color.process(data);
	```
5. [rs2::pipeline_profile](http://docs.ros.org/en/kinetic/api/librealsense2/html/classrs2_1_1pipeline__profile.html)

	管道配置文件包括设备和具有特定配置文件的活动流的选择。该概要文件是在管道定义的过滤器和条件下对上述内容的选择。流可能属于该设备的多个传感器。
	```
	rs2::pipeline_profile profile;
	profile = pipe.start(cfg);
	auto sensor = profile.get_device().first<rs2::depth_sensor>();
	sensor.set_option(RS2_OPTION_LASER_POWER, 100.0);
	auto  device_name = sensor.get_info(RS2_CAMERA_INFO_NAME);
	std::cout << "Intel Realsense " << device_name << " " << 					sensor.get_info(RS2_CAMERA_INFO_SERIAL_NUMBER) << " is connected." << std::endl;
	```
6. [rs2::sensor](http://docs.ros.org/en/kinetic/api/librealsense2/html/classrs2_1_1sensor.html)

7. [rs2::depth_sensor]() 

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxOTgxOTAxMSwxMjY3ODc3OCwtMTIxMj
g5Nzk1NSwtNTAwNDU4NDI0LC0xMDM0OTAxNzIsNTQ1NjE3NTI5
LDEwODc0NzY3OSwtNjcwMTUzODcwLDM1Nzg0NDMzOSw5Nzk5Nz
MyMzZdfQ==
-->