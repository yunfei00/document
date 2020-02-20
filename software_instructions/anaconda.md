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
	python                         3.7.2      haf84260_0  pkgs/main           
	python                         3.7.3      h359304d_0  pkgs/main           
	python                         3.7.4      h359304d_0  pkgs/main           
	python                         3.7.4      h359304d_1  pkgs/main           
	python                         3.7.5      h359304d_0  pkgs/main           
	python                         3.7.6      h359304d_2  pkgs/main           
	python                         3.8.0      h359304d_0  pkgs/main           
	python                         3.8.0      h359304d_1  pkgs/main           
	python                         3.8.0      h359304d_2  pkgs/main           
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

```
9. 删除虚拟环境
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAwNTczNTAyMl19
-->