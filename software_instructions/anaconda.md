# 1 使用conda 创建虚拟环境
1. 检查conda版本
	```
	conda -V
	conda 4.8.2
	```
2. 升级conda
	```
	conda update conda
	```
3. 搜索可用的python版本
	```
	conda search "^python$"
	Loading channels: done
	# Name                       Version           Build  Channel             
	python                        2.7.13     h32f5f24_13  pkgs/main           
	...       
	python                        2.7.17      h97142e2_0  pkgs/main           
	python                         3.5.4     h4bd9b1b_18  pkgs/main           
	...       
	python                         3.7.0      hc167b69_0  pkgs/main           
	python                         3.7.1      haf84260_3  pkgs/main           
	python                         3.7.1      haf84260_7  pkgs/main           
	...         
	python                         3.8.1      h359304d_1  pkgs/main   
	
	```
4. 创建虚拟环境
	```
	#conda create -n yourenvname python=x.x anaconda
	conda create -n jupyter-env  python=3.7.1  anaconda
	```
5. 激活虚拟环境
	```
	source activate jupyter-env
	```
6. 安装虚拟环境软件包
	```
	pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --ignore-installed --upgrade   tensorflow "matplotlib<3" pandas sklearn scipy seaborn ipython==5.7 notebook
	```
7. 查询虚拟环境
	```
	conda info -e
	```
8. 退出虚拟环境
	```
	source deactivate
	```
9. 删除虚拟环境
	```
	conda remove -n yourenvname -all
	``` 
# 2 ubuntu 安装anaconda
## 1 检索最新版本的Anaconda
```
https://www.anaconda.com/distribution/
```
查找最新的Linux版本并复制安装程序bash脚本。
## 2 下载Anaconda Bash脚本
```
curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
```
## 3 运行Anaconda脚本
```
bash Anaconda3-2020.02-Linux-x86_64.sh
```
## 4 激活安装
```
source ~/.bashrc
```
## 5 测试安装
使用`conda`命令来测试安装和激活：
```
conda list
```
您将收到通过Anaconda安装可获得的所有软件包的输出
## 6 设置Anaconda环境
您可以使用以下`conda create`命令创建Anaconda环境。例如，`my_env`可以使用以下命令创建一个名为Python 3的环境：
```
conda create --name my_env python=3
```
激活新环境，如下所示：
```
conda activate my_env
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNDM5NDUzNTEsMjAwMTkwMjQxNF19
-->