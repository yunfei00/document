<h2>目录</h2>

<h3><a href="#title1">1 seafile 说明</a></h3>
<h3><a href="#title2">2 seafile 服务器安装 </a></h3>
<h3><a href="#title3">3 seafile 客户端安装 </a></h3>

<h1 id="title1">1 seafile 说明 </h1>

Seafile 是一款开源的企业云盘，注重可靠性和性能。支持 Windows, Mac, Linux, iOS, Android 平台。支持文件同步或者直接挂载到本地访问。

<h1 id="title2">2 seafile 服务器安装 </h1>

<h1 id="title3">3 seafile 客户端安装 </h1>
<h2 id="title3.1">3.1 ubuntu安装</h2>

```
sudo add-apt-repository ppa:seafile/seafile-client
sudo apt-get update
sudo apt-get install seafile-cli
```
<h1 id="title4">4 seafile 客户端 使用 </h1>

```
# init 初始化seafile配置文件夹
seaf-cli init -d /home/yunfei/seafile

# start 启动seafile服务
seaf-cli start

# list-remote获取远程服务器的资料库列表，命令例子：(该命令可以查询到远程的Library ID)
seaf-cli list-remote -s [服务器地址] -u [用户名] -p [密码]
seaf-cli list-remote -s http://192.168.2.117:9000 -u XXX -p YYY

# list 获取本地已同步的文件夹，命令例子：
seaf-cli list

# download下载远程资料库，并且会默认的同步,命令例子：
seaf-cli download -l [Library ID] -s [服务器地址] -d /home/yunfei/seafile -u [用户名] -p [密码]

# status 查看状态
seaf-cli status

# stop 停止seafile服务
seaf-cli stop

# desync 解除同步，命令例子：
seaf-cli desync -d /home/yunfei/seafile

# create 创建远程资料库，命令例子：
seaf-cli create -n remote_directory -s [服务器地址] -u [用户名] -p [密码]

# sync把本地文件夹和远程资料库绑定同步,命令例子：
seaf-cli sync -l [Library ID] -s [服务器地址] -d l -u [用户名] -p [密码]

```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEwMTQzOTcwMSwtMTM2MjQzODE1NF19
-->