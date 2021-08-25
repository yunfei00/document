1. 系统说明
系统使用的是ubuntu20.04的版本


2. 添加用户及用户组
    useradd yunfei
    useradd git
    
3. 软件安装
    tensorflow 安装
    pip3 install tensorflow

    jupyter-notebook安装
    apt update
    apt-get install jupyter-notebook
    jupyter notebook --generate-config
    vim /root/.jupyter/jupyter_notebook_config.py 
        主要配置内容：
        1. 允许远程访问
        2. 远程访问IP
        3. 远程访问端口
        4. 远程访问密码
        
    jupyter-notebook password
    jupyter-notebook  --allow-root
    
    gogs安装
    界面配置
    下载gogs包
    
    
    
  
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYyNDUyMzY5XX0=
-->