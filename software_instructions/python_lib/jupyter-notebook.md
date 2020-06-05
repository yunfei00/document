# 1 配置远程访问
1. 检查配置文件是否存在
```
-   Windows:  `C:\Users\USERNAME\.jupyter\jupyter_notebook_config.py`
-   OS X:  `/Users/USERNAME/.jupyter/jupyter_notebook_config.py`
-   Linux:  `/home/USERNAME/.jupyter/jupyter_notebook_config.py`
```
2. 配置文件如果不存在，则创建
```
jupyter notebook --generate-config
```
3. 文件配置
```
 # 设置首次登陆禁止修改密码
 c.NotebookApp.allow_password_change = False
```
4. 设置远程登录密码
```
jupyter notebook password
```
5. 配置允许远程访问
```
vim jupyter_notebook_config.py
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 9999
c.NotebookApp.allow_remote_access = True
```
6. 运行jupyter
```
jupyter-notebook
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE2NjM3OTE3MCwyMTY5MDE3N119
-->
