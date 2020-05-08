# 1 mac 上opencv安装
与linux 安装类似
```
unzip 4.3.0.zip 
cd 4.3.0.zip 
cd opencv-4.3.0/
mkdir release
cd release/
cmake -D CMAKE_BUILD_TYPE=REALEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
sudo make install
```

# 2 mac上opencv开发环境配置
参考 https://medium.com/@jaskaranvirdi/setting-up-opencv-and-c-development-environment-in-xcode-b6027728003
