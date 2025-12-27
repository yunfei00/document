pip 安装原理
# 原理
pip安装软件是向第三方库管理网站（源）发起请求，并进行下载安装的。
默认第三方管理网站：[https://pypi.python.org/pypi](https://link.jianshu.com?t=https://pypi.python.org/pypi)  

默认安装到本地的python的安装目录(一般为($(python安装目录)\lib\site-packages))。

pip更多，请详看:[https://pip.pypa.io/en/latest/](https://link.jianshu.com?t=https://pip.pypa.io/en/latest/)

# 常用命令

* install 安装包.
* uninstall 卸载包.
* freeze 按着一定格式输出已安装包列表
* list 列出已安装包.
* show 显示包详细信息.
* search 搜索包，类似yum里的search.
* wheel Build weels from your requirements.
* help 当前帮助.

# 常见问题
1. 安装不了
如果安装不了软件包，一般是源的问题或者是dns问题。
dns更改需要在/etc/resolv.conf文件中修改DNS服务器。
例如：
```
nameserver 8.8.8.8
nameserver 114.114.114.114
nameserver 61.134.1.4

```

114.114.114.114是国内移动、电信bai和联通通用的DNS，解析成功率相对来说更高，国内用户使用的比较多，速度相对快、稳定，是国内用户上网常用的DNS。8.8.8.8是GOOGLE公司提供的DNS，该地址是全球通用的，相对来说，更适合国外以及访问国外网站的用户使用。
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU1Mzk5NTc3N119
-->