# 1 contOS svn 使用
1. 安装svn
	```
	yum -y install subversion
	```
	若需查看svn安装位置，可以用以下命令：
	```
	rpm -ql subversion
	```
2. 创建版本库目录
	```
	mkdir /home/yunfei/svn_server/
	svnadmin create /home/yunfei/svn_server/
	```
3. 编辑配置文件
	```
	cd /home/yunfei/svn_server/conf
	vim authz 

	[aliases]
	# joe = /C=XZ/ST=Dessert/L=Snake City/O=Snake Oil, Ltd./OU=Research Institute/CN=Joe Average

	[groups]
	# harry_and_sally = harry,sally
	# harry_sally_and_joe = harry,sally,&joe

	# [/foo/bar]
	# harry = rw
	# &joe = r
	# * =

	# [repository:/baz/fuz]
	# @harry_and_sally = rw
	# * = r
	#
	[/]
	yunfei = rw


	vim passwd 
	[users]
	# harry = harryssecret
	# sally = sallyssecret
	yunfei = 82865348


	vim svnserve.conf 
	### Visit http://subversion.apache.org/ for more information.

	[general]
	### The anon-access and auth-access options control access to the
	### repository for unauthenticated (a.k.a. anonymous) users and
	### authenticated users, respectively.
	### Valid values are "write", "read", and "none".
	### Setting the value to "none" prohibits both reading and writing;
	### "read" allows read-only access, and "write" allows complete 
	### read/write access to the repository.
	### The sample settings below are the defaults and specify that anonymous
	### users have read-only access to the repository, while authenticated
	### users have read and write access to the repository.
	anon-access = none
	auth-access = write
	### The password-db option controls the location of the password
	### database file.  Unless you specify a path starting with a /,
	### the file's location is relative to the directory containing
	### this configuration file.
	### If SASL is enabled (see below), this file will NOT be used.
	### Uncomment the line below to use the default password file.
	password-db = passwd
	### The authz-db option controls the location of the authorization
	### rules for path-based access control.  Unless you specify a path
	### starting with a /, the file's location is relative to the the
	### directory containing this file.  If you don't specify an
	### authz-db, no path-based access control is done.
	### Uncomment the line below to use the default authorization file.
	authz-db = authz
	### This option specifies the authentication realm of the repository.
	### If two repositories have the same authentication realm, they should
	### have the same password database, and vice versa.  The default realm
	### is repository's uuid.
	realm = /home/yunfei/svn_server
	### The force-username-case option causes svnserve to case-normalize
	### usernames before comparing them against the authorization rules in the
	### authz-db file configured above.  Valid values are "upper" (to upper-
	### case the usernames), "lower" (to lowercase the usernames), and
	### "none" (to compare usernames as-is without case conversion, which
	### is the default behavior).
	# force-username-case = none

	[sasl]
	### This option specifies whether you want to use the Cyrus SASL
	### library for authentication. Default is false.
	### This section will be ignored if svnserve is not built with Cyrus
	### SASL support; to check, run 'svnserve --version' and look for a line
	### reading 'Cyrus SASL authentication is available.'
	# use-sasl = true
	### These options specify the desired strength of the security layer
	### that you want SASL to provide. 0 means no encryption, 1 means
	### integrity-checking only, values larger than 1 are correlated
	### to the effective key length for encryption (e.g. 128 means 128-bit
	### encryption). The values below are the defaults.
	# min-encryption = 0
	# max-encryption = 256
	```
4. 启动svn
	```
	svnserve -d -r /home/yunfei/svn_server/
	```
5. 配置开机启动svn服务
	a. 安装好 svn 服务后，默认是没有随系统启动自动启动的， CentOS 7 的 /etc/rc.d/rc.local 是没有执行权限的， 系统建议创建 systemd service 启动服务
	于是查看 systemd 里 svn 的配置文件 /lib/systemd/system/svnserve.service,内容如下：
	```
	[Unit]
	Description=Subversion protocol daemon
	After=syslog.target network.target

	[Service]
	Type=forking
	EnvironmentFile=/etc/sysconfig/svnserve
	ExecStart=/usr/bin/svnserve --daemon --pid-file=/run/svnserve/svnserve.pid $OPTIONS

	[Install]
	WantedBy=multi-user.target
	```
	b. 找到 svn 的 service 配置文件 /etc/sysconfig/svnserve 编辑配置文件,将OPTIONS="-r /var/svn"改为svn库的目录，修改后如下：
	```
	# OPTIONS is used to pass command-line arguments to svnserve.
	# 
	# Specify the repository location in -r parameter:
	#OPTIONS="-r /var/svn"
	OPTIONS="-r /home/yunfei/svn_server"
	```
	c. 输入如下命令
	```
	systemctl enable svnserve.service  
	```
	d. 重启服务器，查看是否有svn服务
	```
	reboot
	ps -aux | grep 'svn'  
	```
	6. svn 迁移
# 2 mac 上svn使用
环境说明：
在Mac环境下，由于Mac自带了svn的服务器端和客户端功能，所以我们可以在不装任何第三方软件的前提下使用svn功能，不过还需做一下简单的配置。
我们首先来看下，如何在Mac环境下搭建svn服务器端环境。

## 2.1、创建代码仓库，用来存储客户端所上传的代码
我先在 /Users/j00226207 目录下新建一个svn目录，创建一个mycode仓库，输入指令：
```
svnadmin create /Users/j00226207/svn/mycode
```
指令执行成功后，会发现硬盘上多了个 /Users/j00226207/svn/mycode目录
## 2.2 配置svn的用户权限

1. 主要是修改/svn/mycode/conf目录下的三个文件,打开svnserve.conf，将下列配置项前面的#和空格都去掉
	```
	# anon-access = none
	# auth-access = write
	# password-db = passwd
	# authz-db = authz
	```
	anon-access = read代表匿名访问的时候是只读的，若改为anon-access = none代表禁止匿名访问，需要帐号密码才能访问
2. 打开passwd，在[users]下面添加帐号和密码
	```
	[users]
	test=123
	tmp = 456
	```
	帐号是test，密码是123
3. 打开authz，配置用户组和权限
	我们可以将在passwd里添加的用户分配到不同的用户组里，以后的话，就可以对不同用户组设置不同的权限，没有必要对每个用户进行单独设置权限。

	在[groups]下面添加组名和用户名，多个用户之间用逗号(,)隔开
	```
	[groups]
	testgroup = test,tmp
	```
	test和tmp都是属于testgroup这个组的，接下来再进行权限配置。
	使用[/]代表svn服务器中的所有资源库
	[/]
	@topgroup=rw上面的配置说明topgroup这个组中的所有用户对所有资源库都有读写(rw)权限，组名前面要用@
	如果是用户名，不用加@，比如mj这个用户有读写权限
	[/]
	mj=rw
	至于其他精细的权限控制，可以参考authz文件中的其他内容

4. 启动svn服务器
	```
	svnserve -d -r /Users/j00226207/svn/mycode/
	```
	没有任何提示就说明启动成功了

5. 关闭svn服务器
	如果你想要关闭svn服务器，最有效的办法是打开实用工具里面的“活动监视器”
	首次配置完先关闭svn服务器再进行数据的上传和下载操作。
## 2.3 使用svn客户端功能
1. 从本地导入代码到服务器(第一次初始化导入)
	```
	svn import /Users/j00226207/work/python svn://localhost/mycode/python --username=test --password=123  -m "初始化导入"
	```
	将/Users/j00226207/work/python svn://localhost/mycode/python中的所有内容，上传到服务器mycode仓库的python目录下，后面双引号中的"初始化导入"是注释
2. 从服务器端下载代码到客户端本地
	```
	svn checkout svn://localhost/mycode --username=test --password=123 /Users/j00226207/test/
	```
	将服务器中mycode仓库的内容下载到/Users/j00226207/test/目录中
 注：localhost（本地服务器IP地址）可以替换成你本地服务器的IP地址。当你和别人同用一个svn时，你可以输入你要进行数据请求的服务器的IP地址。
3. 提交更改过的代码到服务器，修改gui.py文件，然后提交
	```
	svn commit -m "修改了gui.py"
	```
4. 更新服务器端的代码到客户端
	```
	svn update
	```
## 2.4 svn 指令集
1. 将文件checkout到本地目录
	```
	svn checkout path（path是服务器上的目录）
	例如：svn checkout svn://192.168.1.1/pro/domain
	简写：svn co
	```
2. 往版本库中添加新的文件
	```
	svn add file
	例如：svn add test.PHP(添加test.php)
	svn add *.php(添加当前目录下所有的php文件)
	```
		svn add xxx@2x.png 文件时， 正常命令 svn add xxx@2x.png 会报 xxx not found
		需用 svn add xxx@2x.png@  来添加，也就是图片名字后面再添加一个@ 符号，
		这是因为 svn 命令最后需要用@符号来指定一个版本导致的
		遇到 xxx@2x.png文件时，如果用svn命令行添加到 版本库的话，只能手动一个一个添加，不能批量添加

3. 将改动的文件提交到版本库
	```
	svn commit -m “LogMessage“ [-N] [--no-unlock] PATH(如果选择了保持锁，就使用–no-unlock开关)
	例如：svn commit -m “add test file for my test“ test.php
	简写：svn ci
	```
4. 加锁/解锁
	```
	svn lock -m “LockMessage“ [--force] PATH
	例如：svn lock -m “lock test file“ test.php
	svn unlock PATH
	```
5. 更新到某个版本
	```
	svn update -r m path
	svn update如果后面没有目录，默认将当前目录以及子目录下的所有文件都更新到最新版本。
	svn update -r 200 test.php(将版本库中的文件test.php还原到版本200)
	简写：svn up
	```
6. 查看文件或者目录状态
	```
	svn status path（目录下的文件和子目录的状态，正常状态不显示）
	?：不在svn的控制中；M：内容被修改；C：发生冲突；A：预定加入到版本库；K：被锁定
	svn status -v path(显示文件和子目录状态)
	第一列保持相同z，第二列显示工作版本号，第三和第四列显示最后一次修改的版本号和修改人。
	注：svn status、svn diff和 svn revert这三条命令在没有网络的情况下也可以执行的，原因是svn在本地的.svn中保留了本地版本的原始拷贝。
	简写：svn st
	```
7. 删除文件
	```
	svn delete path -m “delete test fle“
	例如：svn delete svn://192.168.1.1/pro/domain/test.php -m “delete test file”
	或者直接svn delete test.php 然后再svn ci -m ‘delete test file‘，推荐使用这种
	简写：svn (del, remove, rm)
	```

8. 查看日志
	```
	svn log path
	例如：svn log test.php 显示这个文件的所有修改记录，及其版本号的变化
	```

9. 查看文件详细信息
	```
	svn info path
	例如：svn info test.php
	``` 
10. 比较差异
	```
	svn diff path(将修改的文件与基础版本比较)
	例如：svn diff test.php
	svn diff -r m:n path(对版本m和版本n比较差异)
	例如：svn diff -r 200:201 test.php
	简写：svn di
	```
11. 将两个版本之间的差异合并到当前文件
	```
	svn merge -r m:n path
	例如：svn merge -r 200:205 test.php（将版本200与205之间的差异合并到当前文件，但是一般都会产生冲突，需要处理一下）
	```
12. SVN 帮助
	```
	svn help
	svn help ci
	```
13. 版本库下的文件和目录列表
	```
	svn list path
	显示path目录下的所有属于版本库的文件和目录
	简写：svn ls
	```

14. 创建纳入版本控制下的新目录
	```
	svn mkdir 创建纳入版本控制下的新目录。
	```
15. 恢复本地修改
	```
	svn revert 恢复原始未改变的工作副本文件 (恢复大部份的本地修改)
	```
16. 代码库URL变更
	```
	svn switch (sw): 更新工作副本至不同的URL。
	```
17. 解决冲突
	```
	svn resolved: 移除工作副本的目录或文件的“冲突”状态。
	用法: resolved PATH…
	注意: 本子命令不会依语法来解决冲突或是移除冲突标记；它只是移除冲突的
	相关文件，然后让 PATH 可以再次提交。
	```
18. 输出指定文件或URL的内容。
	```
	svn cat 目标[@版本]…如果指定了版本，将从指定的版本开始查找。
	svn cat -r PREV filename > filename (PREV 是上一版本,也可以写具体版本号,这样输出结果是可以提交的)
	```
19. 配置忽略文件 vi ~/.subversion/config
```
找到 global-ignores 一行，去掉注释，编辑成
global-ignores = build *~.nib *.so *.pbxuser *.mode *.perspective*
找到 enable-auto-props = yes 把注释去掉，在[auto-props] Section声明以下文本文件

*.mode* = svn:mime-type=text/X-xcode
*.pbxuser = svn:mime-type=text/X-xcode
*.perspective* = svn:mime-type=text/X-xcode
*.pbxproj = svn:mime-type=text/X-xcode
```
## 2.5 svn 命令参数说明
1. svn 命令共同的选项
	```
	--targets list 读取list并将其解释为一个将要操作的参数列表
	--non-recurisive, –N 只操作单个目录，不处理子目录
	--verbose, –v 打印额外的信息
	--quiet, –q 打印的信息尽可能少
	--username,  name 指定在连接授权时使用的用户名
	--password, pawd 指定要使用的密码
	--no-auth-cache 不要缓存身份令牌
	--non-interactive 不要提示输入额外的信息
	--config-dir  dir  从dir读取用户配置
	--editor-cm cmd 使用cmd作为日志消息的编辑器
	```
2. svn add 
	```
	把文件及目录的名称添加给版本控制系统。他们会在下次提交时被添加到项目仓库
	svn add path
	--auto-props 在添加他们的时候自动设置文件的属性
	--no-auto-props 禁用自动属性设置
	```
3. svn blame
	```
	显示文件每行的版本及作者信息
	--revision, –r rev 如果指定的rev是单个版本，显示该版本作者信息。如果是范围rev1:rev2, 显示rev2版本作者的信息，但只检查版本到rev1.
	```
4. svn cat
	```
	输出指定文件或者URL的内容
	svn cat target…
	--revision, –r rev
	```
5. svn checkout
	```
	从项目仓库牵出一个工作拷贝
	svn checkout url…path
	如果没有指定path,签出的本地目录名使用URL的base name.
	```
6. svn cleanup
	```
	清理工作拷贝，移除锁，完成未完成的操作，等等。
	svn cleanup path…
	svn commit path
	把改动从你的工作拷贝发送到项目仓库
	--message, –m msg 使用msg作为提交日志消息。
	--file, –F file 使用file的内容作为提交日志消息。
	--no-unlock 不要在提交的时候释放锁。
	```
7. svn copy
	```
	在工作拷贝或者项目仓库中制造包括历史在内的复本
	svn copy src dest
	src和dest可以是工作拷贝(WC)的路径或者URL.
	src dest 效果……
	WC WC 拷贝并添加
	WC URL 立即提交WC的拷贝到URL
	URL WC 签出URL到WC, 添加
	URL URL 完全服务器端拷贝；用于制作分支和打标签
	--revision, –r rev要拷贝的src的版本。只在src是项目仓库的URL时才有意义。
	```
8. svn delete target
	```
	从项目仓库删除文件或者目录。如果target是工作拷贝中的文件或者目录，它被从工作拷贝中移除并且预计在下次提交时删除掉。如果target是项目仓库URL,通过一次立即的提交从项目仓库中删除。
	--message, –m msg
	--file, –F file
	```
9. svn diff  显示两个路径之间的差异
	```
	svn diff –r rev1:rev2 target…
	svn diff oldurl newurl
	```
10. svn export 创建一个无版本记录的拷贝.
	```
	svn export –r rev URL path
	从项目仓库的指定URL导出一个干净的目录树到path中，如果指定了rev参数，导出rev版本的，否则到处最新版本。
	```
11. svn import
	```
	提交一个无版本的文件或者树到项目仓库
	svn import path URL
	```
12. svn info 显示文件或者目录的信息。
13. svn list 列出项目仓库中的目录条数。
14. svn lock 锁住文件让其它用户不能提交改动。
	```
	svn lock target
	--message, –m msg 使用msg作为锁信息消息
	--force 强制加锁成功，通过从其他用户或者工作拷贝把锁给偷过来。
	```
15. svn log 显示一些版本或者文件的日志消息.
	```
	--stop-on-copy 在遍历历史的时候不要穿越拷贝（对于查找分支的起点很有用）
	```
16. svn merge 把两个来源的差异应用给工作拷贝路径。
	```
	svn merge –r rev1:rev2  source wcpath
	```
17. svn mkdir 创建版本控制下的新目录
	```
	svn mkdir target
	```
18. svn move src dest 移动或者重命名工作拷贝或者项目仓库中文件或者目录
	```
	--revision, –r rev使用版本rev作为源来执行这次移动。
	```
19. svn propdel 删除文件或者目录的属性
	```
	svn propdel propname path…
	```
20. svn propedit 编辑文件或者目录的属性
	```
	svn propedit propname path…
	```
21. svn propget 打印文件或者目录的属性值
	```
	svn propget propname path…
	--strict 禁用额外的换行和其它的美化措施（在把二进制属性重定向到文件时会有用处)
	```
22. svn proplist 列出文件或者目录的所有属性
	```
	--verbose
	--recursive
	--revision, –r rev 列出path在版本rev定义的属性
	```
23. svn propset(pset, ps)
	```
	svn propset propname propval path…
	--file, –F file 读取file的内容，使用它作为属性值.
	--recursive
	--encoding  enc 把值作为用enc编码的字符集
	```
24. svn resolved 移除工作拷贝文件或者目录的冲突状态
	```
	--recursive
	```
25. svn revert 恢复工作拷贝的文件（撤销最新的本地修改）
	```
	svn revert path 这个命令不需要网络连接
	--recursive
	```
26. svn status 打印工作拷贝中文件或者目录的状态
	```svn status path…
	--show-updates, –u 联系服务器显示更新信息
	--no-ignore 忽视默认设置和svn:ignore属性设置的忽略项
	--non-recursive, –N
	--verbose, –v
	```
27. svn switch 把工作拷贝转向到其他的URL
	```
	svn switch URL path
	更新工作拷贝让其使用项目仓库的新URL.这个行为类似svn update 而且是一种把工作拷贝转向到同一项目仓库中的分支或者标签的办法。
	--revision, –r rev 转向到版本rev
	--non-recursive, –N
	--diff3-cm 使用cmd作为合并命令
	```
28. svn unlock 解开工作拷贝文件或者项目仓库URL的锁
	```
	svn unlock target…
	--force 砸坏现有对target的锁，甚至它不是被当前工作拷贝所拥有的。
	```
29. svn update 把改动从项目仓库带到工作拷贝来。
	```
	svn update path…
	--revision, –r rev 更新到版本rev
	--non-recrusive, –N
	--diff3-cmd
	```
## 2.6 svn 出错信息总汇

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMwNTUwMDk3OCwxMTMyNDI0MDksLTE4Mj
AwMDY3NSwxNDc4MjUzNzY1LDQzODg2NTI5MywxMzMwMTkyODM2
LDk3ODg1MzE3OSwtMTM3MTk3NDE3MSwxOTU0Mzk3OTAzLDE2ND
U2NDg0NzAsMTY5NDQ4OTMxMiwtNjAzOTI2NjU3XX0=
-->