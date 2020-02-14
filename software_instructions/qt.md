# 1 ubuntu 上Qt程序发布
# 1.1 常规发布（存在一些问题）
1 拷贝目标文件在指定目录
2 执行lib库拷贝脚本

#!/bin/sh

ExecName=$1

CUR_PATH=`pwd`

echo "parameters $# !"

if [ $# -ge 2 ]

then

dest=$2

else

echo "Input the dest path, please!"

exit 1

fi

echo "Package Name:${ExecName} Destination Directory:${dest}"

deplist=$(ldd ${ExecName} | awk '{if (match($3,"/")){ printf("%s "),$3 } }')

echo "copy base libraries !"

#clear garbage files

cd ${dest}

rm -rf *

cd ${CUR_PATH}

#begin to copy lib to dest

cp ${deplist} ${dest}

#copy source file to dest

#cp ExecName ${dest}

echo "copy done!"

#/opt/Qt5.9.1/5.9.1/gcc_64/plugins/platforms

#copy platforms libraries to dest directory

cp /opt/Qt5.9.1/5.9.1/gcc_64/plugins/platforms ./ -r

#cd platforms

#echo "Go in platforms"

#ExecName=libqxcb.so

#deplist=$(ldd ${ExecName} | awk '{if (match($3,"/")){ printf("%s "),$3 } }')

#cp ${deplist} ${dest}

echo "work done!"

3 设置环境变量 export QT_DEBUG_PLUGINS=1

加了这个环境变量，让我看到了QT程序加载的过程，看到了详细的报错信息。

4 在目标环境上查看是否可以运行 并根据提示修改问题

# 2 使用工具发布

1. 下载linuxdeployqt-6-x86_64.AppImage 网址：

https://github.com/probonopd/linuxdeployqt/releases

2. 使用Qt提供的qmake工具

export PATH=/home/visbodyfit/Qt5.9.1/5.9.1/gcc_64/bin:$PATH

qmake 查看一下 确保是可以运行的

qmake -v

QMake version 3.1

Using Qt version 5.9.1 in /home/visbodyfit/Qt5.9.1/5.9.1/gcc_64/lib

3. 修改权限 并发布

chmod a+x linuxdeployqt-6-x86_64.AppImage

./linuxdeployqt-6-x86_64.AppImage ~/smart_production/code/build-smart_production-Desktop_Qt_5_9_1_GCC_64bit-Release/smart_production

4. 打包发布

mkdir production

cd production/

cp ~/smart_production/code/build-smart_production-Desktop_Qt_5_9_1_GCC_64bit-Release/smart_production ./

cp ~/smart_production/code/build-smart_production-Desktop_Qt_5_9_1_GCC_64bit-Release/qt.conf ./

cp ~/smart_production/code/build-smart_production-Desktop_Qt_5_9_1_GCC_64bit-Release/plugins ./ -r

cp ~/smart_production/code/build-smart_production-Desktop_Qt_5_9_1_GCC_64bit-Release/translations/ ./ -r

cp ~/smart_production/code/build-smart_production-Desktop_Qt_5_9_1_GCC_64bit-Release/lib ./ -r

5. 在未安装Qt的环境下运行程序
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjExODM3MTEwM119
-->