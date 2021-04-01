# 1 udev 简介
udev是linux系统管理设备设备事件的系统。

# 2 查看设备插拔信息 

```
udevadm monitor
monitor will print the received events for:
UDEV - the event which udev sends out after rule processing
KERNEL - the kernel uevent
# 当插拔设备时，会触发类似如下事件：
KERNEL[61642.638617] remove   /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0/ttyUSB1/tty/ttyUSB1 (tty)
KERNEL[61642.638655] remove   /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0/ttyUSB1 (usb-serial)
KERNEL[61642.638683] remove   /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0 (usb)
KERNEL[61642.639459] remove   /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2 (usb)
UDEV  [61642.639964] remove   /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0/ttyUSB1/tty/ttyUSB1 (tty)
UDEV  [61642.641728] remove   /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0/ttyUSB1 (usb-serial)
UDEV  [61642.642897] remove   /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0 (usb)
UDEV  [61642.644521] remove   /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2 (usb)
KERNEL[61646.817327] add      /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2 (usb)
KERNEL[61646.818418] add      /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0 (usb)
KERNEL[61646.818457] add      /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0/ttyUSB1 (usb-serial)
KERNEL[61646.819035] add      /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0/ttyUSB1/tty/ttyUSB1 (tty)
UDEV  [61646.838227] add      /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2 (usb)
UDEV  [61647.860485] add      /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0 (usb)
UDEV  [61647.860513] add      /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0/ttyUSB1 (usb-serial)
UDEV  [61647.868213] add      /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0/ttyUSB1/tty/ttyUSB1 (tty)

```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY2OTkwMTg0NSwtOTE0Mzc2MDM3LC0xND
YzNTMxNzQxXX0=
-->