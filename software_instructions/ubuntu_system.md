# 1 无法安装ubuntu18.04系统

铂盛主机，CPU较新，安装的时候，安装失败，报错内容如下：

```
Unable to install GRUB in /dev/sda
Executing 'grub-install/dev/sda' failed.
This is a fatal error.
```

解决方案：尝试使用linux的系统修复工具进行修复。

```
sudo add-apt-repository ppa:yannubuntu/boot-repair
sudo apt-get update
sudo apt-get install boot-repair
```

# 2 无法进入系统，报错(initramfs)

1. exit 看哪个磁盘 比如/dev/sda1  
2. 修复磁盘fsck /dev/sda1 -y 其中 /dev/sda1 是步骤1中的磁盘号  
3. reboot重启即可
[参考链接](https://ostechnix.com/how-to-fix-busybox-initramfs-error-on-ubuntu/)


<!--stackedit_data:
eyJoaXN0b3J5IjpbOTk0NDkyMDQsLTEzMTIzODU1MzVdfQ==
-->