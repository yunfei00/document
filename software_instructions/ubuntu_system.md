# 1 无法安装ubuntu系统

铂盛主机，CPU较新，安装的时候，安装失败，报错内容如下：

```
Unable to install GRUB in /dev/sda
Executing 'grub-install/dev/sda' failed.
This is a fatal error.
```

解决方案：尝试使用linux的系统修复工具进行修复。

```
sudo add-apt-repository ppa:yannubuntu/boot-repair
sudo
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NjI5ODI0MDldfQ==
-->