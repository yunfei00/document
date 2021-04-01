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

# 3 查看设备信息

```
udevadm info /dev/ttyUSB1
P: /devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0/ttyUSB1/tty/ttyUSB1
N: ttyUSB1
S: serial/by-id/usb-1a86_USB_Serial-if00-port0
S: serial/by-path/pci-0000:00:14.0-usb-0:7.2:1.0-port0
E: DEVLINKS=/dev/serial/by-path/pci-0000:00:14.0-usb-0:7.2:1.0-port0 /dev/serial/by-id/usb-1a86_USB_Serial-if00-port0
E: DEVNAME=/dev/ttyUSB1
E: DEVPATH=/devices/pci0000:00/0000:00:14.0/usb1/1-7/1-7.2/1-7.2:1.0/ttyUSB1/tty/ttyUSB1
E: ID_BUS=usb
E: ID_MM_CANDIDATE=1
E: ID_MODEL=USB_Serial
E: ID_MODEL_ENC=USB\x20Serial
E: ID_MODEL_FROM_DATABASE=HL-340 USB-Serial adapter
E: ID_MODEL_ID=7523
E: ID_PATH=pci-0000:00:14.0-usb-0:7.2:1.0
E: ID_PATH_TAG=pci-0000_00_14_0-usb-0_7_2_1_0
E: ID_PCI_CLASS_FROM_DATABASE=Serial bus controller
E: ID_PCI_INTERFACE_FROM_DATABASE=XHCI
E: ID_PCI_SUBCLASS_FROM_DATABASE=USB controller
E: ID_REVISION=0264
E: ID_SERIAL=1a86_USB_Serial
E: ID_TYPE=generic
E: ID_USB_CLASS_FROM_DATABASE=Vendor Specific Class
E: ID_USB_DRIVER=ch341
E: ID_USB_INTERFACES=:ff0102:
E: ID_USB_INTERFACE_NUM=00
E: ID_VENDOR=1a86
E: ID_VENDOR_ENC=1a86
E: ID_VENDOR_FROM_DATABASE=QinHeng Electronics
E: ID_VENDOR_ID=1a86
E: MAJOR=188
E: MINOR=1
E: SUBSYSTEM=tty
E: TAGS=:systemd:
E: USEC_INITIALIZED=61647867894

一下命令查看设备的详细信息
udevadm info -q all -a /dev/VF-device0
# 截取其中一段信息如下：
  looking at parent device '/devices/pci0000:00/0000:00:14.0/usb1/1-6':
    KERNELS=="1-6"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{idProduct}=="6001"
    ATTRS{idVendor}=="0403"
    ATTRS{product}=="FT232R USB UART"
```

# 4 udev 规则

udev规则定义了发现设备后会发生什么。udev规则至少包含一个条件和至少一个赋值（[规则语法](https://wiki.ubuntuusers.de/udev/#Regelsyntax)）。如果规则的所有条件都适用于设备，则将执行该规则的分配。这样，还会生成设备名称，然后在文件系统中可以使用该设备名称。可以将多个规则应用于同一设备。除了标准规则外，这还可以将您自己的规则应用于同一设备。各个规则文件以两位数开头，并按字母数字顺序处理。这样可以确保首先处理重要的规则。如果将多个规则写入规则文件，则它们会逐行分开。

# 5 标准规则

标准**规则**位于**/lib/udev/rules.d/中**。也可以在**/etc/udev/rules.d/**下找到某些系统**规则，例如**用于网卡的**规则**。


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MjE1ODg4MzcsLTE4MDM3OTg3MTksLT
IwNDc1Mzc1MjEsMTY2OTkwMTg0NSwtOTE0Mzc2MDM3LC0xNDYz
NTMxNzQxXX0=
-->