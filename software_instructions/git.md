# 目录

<h3><a href="#title1">1 mac 上git安装使用说明</a> </h3>
		<h4><ul><a href="#title1.1">1.1 git 安装</a> </h4>
		<h4><ul><a href="#title1.2">1.2 git 基本使用</a> </h4>
		<h4><ul><a href="#title1.3">1.3 git 连接github使用</a> </h4>
		<h4><ul><a href="#title1.4">1.4 创建与合并分支</a> </h4>
		<h4><ul><a href="#title1.5">1.5 分支冲突解决</a> </h4> 
		<h4><ul><a href="#title1.6">1.6 bug分支</a> </h4> 
		<h4><ul><a href="#title1.7">1.7 多人协作</a> </h4> 
		<h4><ul><a href="#title1.8">1.8 Git常用命令集</a> </h4> 
<h3><a href="#title2">2 ubuntu 上git保存用户名密码</a> </h3>
<h3><a href="#title3">3 Windows 上git 使用</a> </h3>

<div style="page-break-after:always"></div>

  <h1 id="title1">1 mac 上git安装使用说明</h1>  
   <h2 id="title1.1">1.1 git 安装</h2>  	
1. 下载git  [https://git-scm.com/download/mac](https://git-scm.com/download/mac). 
2. 双击安装,安装完成后查看版本
	```
	git --version
	git version 2.17.2 (Apple Git-113)
	```
   <h2 id="title1.2">1.2 git 基本使用</h2>  	
1. 创建版本库
		创建版本库github_test，并使用git init命令,git init 把这个目录变成git可以管理的仓库
	```
	mkdir github_test
	cd github_test
	git init
	```
2. 把文件添加到版本库中
		 创建文件test.txt,并写入内容11111，使用git add test.txt 命令添加到暂存区。然后使用git commit 提交到仓库。
	```
	echo "11111"  >test.txt
	git add test.txt
	git commit -m '提交文件test.txt'
	``` 
3. 查看文件状态
	使用git status命令查看，如下说明修改已经全部提交。
	```
	git status
	On branch master
	nothing to commit, working tree clean
	```  
	在文件test.txt中添加22222，然后使用git status再次查看，如下所示，表示修改内容未提交。
	```
	echo 22222 >>test.txt
	git status 
	On branch master
	Changes not staged for commit:
	(use "git add <file>..." to update what will be committed)
	(use "git checkout -- <file>..." to discard changes in working directory)
    modified:   test.txt
   no changes added to commit (use "git add" and/or "git commit -a")	
	```
4. 查看修改内容并修改文件
	 使用git diff test.txt 命令查看修改的内容，可见支增加了22222这一行。
	```
	git diff test.txt 
	diff --git a/test.txt b/test.txt
	index f7c6dd0..a5abd94 100644
	--- a/test.txt
	+++ b/test.txt
	@@ -1 +1,2 @@
	11111
	+22222
	```
	使用git add和git commit命令提交到仓库。
	```
	git add test.txt  
	git commit -m 'add 22222'
	```
5. 版本回退
	首先增加一行33333到文件test.txt中。
	```
	echo 33333 >>test.txt
	git add test.txt 
	git commit -m 'add 33333'
	```
    查询历史记录，使用git log命令
    ```
    git log
    ```
    回退到上个版本，操作如下：
    ```
    git reset --hard HEAD^ 
    ```
    再次恢复到最新的版本或指定版本，需要使用git reflog命令先查看版本记录，然后使用git reset命令恢复到指定的版本。
    ```
    git reflog
	6ed2943 (HEAD -> master) HEAD@{0}: reset: moving to HEAD^
	07d2bb9 HEAD@{1}: commit: add 33333
	6ed2943 (HEAD -> master) HEAD@{2}: commit: add 22222
	e0eeec2 HEAD@{3}: commit (initial): ttttttest.txt    

	git reset --hard 07d2bb9
    ```
6. 工作区与暂存区的区别
	工作区：就是你在电脑上看到的目录，比如目录下github_test里的文件(.git隐藏目录版本库除外)。或者以后需要再新建的目录文件等等都属于工作区范畴。

	版本库(Repository)：工作区有一个隐藏目录.git,这个不属于工作区，这是版本库。其中版本库里面存了很多东西，其中最重要的就是stage(暂存区)，还有Git为我们自动创建了第一个分支master,以及指向master的一个指针HEAD。
	在使用git add命令的时候，实际上是把文件添加到了暂存区，使用git commit命令提交，实际上是把暂存区的所有内容提交到当前分支上。
	我们在test.txt文件中，增加一行44444，并提交。
	```
	echo 44444 >>test.txt
	git add test.txt
	git commit -m 'add 44444'
	```
7. 撤销修改
		在文件test.txt中增加内容55555，但是发现增加的内容有误，需要恢复以前的版本，可以使用git reset --hard HEAD^命令恢复，也可以直接撤销，直接撤销命令如下：
	```
	echo 55555 >>test.txt
	git checkout -- test.txt		
	```
	git checkout -- test.txt意思就是，把test.txt文件在工作区做的修改全部撤销

8. 删除文件
	删除文件直接在本地删除，然后提交即可，如下进行删除并恢复。
	```
	rm test.txt
	git reflog
	1be7d44 (HEAD -> master) HEAD@{0}: commit: add 44444
	07d2bb9 HEAD@{1}: reset: moving to 07d2bb9
	6ed2943 HEAD@{2}: reset: moving to HEAD^
	07d2bb9 HEAD@{3}: commit: add 33333
	6ed2943 HEAD@{4}: commit: add 22222
	e0eeec2 HEAD@{5}: commit (initial): ttttttest.txt	

	git reset --hard 1be7d44
	```
	
   <h2 id="title1.3">1.3 git 连接github使用</h2>  	
1. 注册github账号 [https://github.com/](https://github.com/).  
2. 创建SSH Key，由于本地Git仓库和github仓库之间的传输是通过SSH加密的，所以需要进行设置。
	在用户主目录下，看看有没有.ssh目录，如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，如果有的话，直接跳过此如下命令，如果没有的话，打开命令行，输入如下命令：ssh-keygen -t rsa -b 4096 -C  "youremail@example.com"使用自己github注册时的邮箱地址。
	id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。
3. 登录github，添加ssh key
		登录后，点击右上角，进入Settings，单击“[SSH and GPG keys](https://github.com/settings/keys)，点击“New SSH key”,填写任意title，并粘贴id_rsa.pub中的内容。
4. 添加远程库
	现在的情景是：我们已经在本地创建了一个Git仓库后，又想在github创建一个Git仓库，并且希望这两个仓库进行远程同步，这样github的仓库可以作为备份，又可以其他人通过该仓库来协作。
	登录github,右上角十字单击后，找到“New repository”，填写仓库名称github_test，并单击Create repository创建远程仓库。
	目前，在GitHub上的这个'github_test'仓库还是空的，GitHub告诉我们，可以从这个仓库克隆出新的仓库，也可以把一个已有的本地仓库与之关联，然后，把本地仓库的内容推送到GitHub仓库。

	现在，我们根据GitHub的提示，在本地的'github_test'仓库下运行命令：
	```
	git remote add origin https://github.com/yunfei00/github_test.git
	git push -u origin master
	```
	从现在起，只要本地作了提交，就可以通过如下命令：
	```
	git push origin master
	```
	把本地master分支的最新修改推送到github上了，现在你就拥有了真正的分布式版本库了。
5. 从远程库克隆
	场景：远程库更新到本地，使用如下命令：
	```
	git clone https://github.com/yunfei00/github_test.git
	```
	从克隆的库中添加内容并提交，然后同步到远程库中
	```
	echo "66666"  >>test.txt 
	git add test.txt 
	git commit -m 'add 66666'
	git push origin master
	```
 <h2 id="title1.4">1.4 创建与合并分支</h2>  	
1. 简要说明
	 每次提交，Git都把它们串成一条时间线，这条时间线就是一个分支。截止到目前，只有一条时间线，在Git里，这个分支叫主分支，即master分支。HEAD严格来说不是指向提交，而是指向master，master才是指向提交的，所以，HEAD指向的就是当前分支。
2. 创建dev分支，并切换到dev分支，命令如下：
	```
	git checkout -b dev
	git branch
	``` 
	git checkout 命令加上 –b参数表示创建并切换，相当于如下2条命令
	git branch dev
	git checkout dev
	git branch查看分支，会列出所有的分支，当前分支前面会添加一个星号。
3. 在dev分支上添加77777，然后提交
	```
	echo 77777 >>test.txt
	git add test.txt
	git commit -m 'add 77777'
	```
4. 切换到master，并查看文件内容，发现并未修改
	```
	git checkout master
	cat test.txt
	```
5. 合并分支内容,git merge命令用于合并指定分支到当前分支上
	```
	git merge dev
	```
6. 删除dev分支
	```
	git branch -d dev
	```
 <h2 id="title1.5">1.5 分支冲突解决</h2>  	
1. 创建分支branch1，在test.txt中添加88888，然后提交
	```
	git checkout -b branch1  
	echo 88888 >> test.txt
	git add test.txt
	git commit -m 'add 88888'
	```
2. 切换到master分支，在test.txt中添加内容99999，然后提交
	```
	git checkout master
	echo 99999 >> test.txt
	git add test.txt
	git commit -m 'add 99999'
	```
3. 在master分支上合并branch1,报错后，查看状态，并重新查看文件
	```
	git merge branch1
	git status
	cat test.txt
	```
	Git用<<<<<<<，=======，>>>>>>>标记出不同分支的内容，其中<<<HEAD是指主分支修改的内容，>>>>> 是指branch1上修改的内容。
	找到问题所在，修改后提交
	```
	git add test.txt
	git commit -m 'conflict fixed'
	```
4. 分支管理策略(暂时未发现实际作用  仅做记录)
	通常合并分支时，git一般使用”Fast forward”模式，在这种模式下，删除分支后，会丢掉分支信息，现在我们来使用带参数 –no-ff来禁用”Fast forward”模式。首先我们来做demo演示下：

	创建一个dev分支。
	修改test.txt内容。
	添加到暂存区。
	切换回主分支(master)。
	合并dev分支，使用命令 git merge –no-ff  -m “注释” dev
	删除dev分支
	查看历史记录
	```
	git checkout -b dev
	echo 00000 >>test.txt 
	git add test.txt 
	git commit -m 'add 00000 in branch'
	git checkout master
	git merge --no-ff -m 'merge with no--ff'  dev
	git branch -d dev
	git branch
	git log --graph --pretty=oneline --abbrev-commit
	git branch -d branch1
	git log --graph --pretty=oneline --abbrev-commit
	```
	分支策略：首先master主分支应该是非常稳定的，也就是用来发布新版本，一般情况下不允许在上面干活，干活一般情况下在新建的dev分支上干活，干完后，比如上要发布，或者说dev分支代码稳定后可以合并到主分支master上来。
	
<h2 id="title1.6">1.6 bug分支</h2>  	
1. 场景说明：在分支dev上开发的时候，遇到一个紧急bug需要修复，那么需要暂停dev上的工作，新建一个分支fix-bug，修复后，在返回原来的分支继续工作。
2. 在master分支上，增加BBBBB到test.txt中
	```
	echo BBBBB >>test.txt 
	git add test.txt 
	git commit -m 'add BBBBB'
	```
3. 添加分支dev，并修改test.txt，添加aaaaa到test.txt中
	```
	git checkout -b dev
	echo aaaaa >>test.txt 
	```
4. 发现在master分支上有个bug，原来的BBBBB是错误的，应该添加的是bbbbb，使用git stash命令保存dev分支当前的状态，并切换到master分支，在master分支上建立fix-bug分支
	```
	git stash
	git checkout master
	git checkout -b fix-bug
	```
5.  修改错误后，提交文件，切换到master分支，合并修复的bug，然后删除fix-bug分支。
	```
	git add test.txt 
	git commit -m 'fix bug'
	git checkout master
	git merge --no-ff -m 'fix bug from fix-bug'  fix-bug
	cat test.txt 
	git branch -d fix-bug
	```
6. 切换到dev分支，并恢复当前的工作 
	```
	git checkout dev
	git status
	cat test.txt 
	git stash list
	git stash pop
	git status
	cat test.txt 
	git stash list
	```
<h2 id="title1.7">1.7 多人协作</h2>  	
1. 简要说明：当你从远程库克隆时候，实际上Git自动把本地的master分支和远程的master分支对应起来了，并且远程库的默认名称是origin。
要查看远程库的信息 使用 git remote
要查看远程库的详细信息 使用 git remote –v
	```
	git remote
	origin
	git remote -v
	origin  https://github.com/yunfei00/github_test.git (fetch)
	origin  https://github.com/yunfei00/github_test.git (push)
	```
2. 推送本地文件到远程仓库master分支
	```
	git push origin master
	```
3. 推送本地文件到远程仓库dev分支
	```
	git push origin dev
	```
	master分支是主分支，因此要时刻与远程同步。一些修复bug分支不需要推送到远程去，可以先合并到主分支上，然后把主分支master推送到远程去。
4. 同步远程仓库到本地
	```
	git pull
	```
5. 多人同时修改分支，比如当前两个目录下的git仓库分支dev，仓库1修改了test.txt文件，并添加提交，同步到远程仓库，仓库2也修改了test.txt文件，并添加提交，此时同步到远程库会存在冲突，应先下载最新的，然后解决冲突后再次提交。
	
	仓库1dev分支修改text.txt文件，并提交到远程库。
	```
	echo ddddd >>test.txt 
	git add test.txt 
	git commit -m 'add ddddd in dev1'
	git push origin dev
	```
		仓库2dev分支修改text.txt文件，并提交到远程库。
	```
	echo ddddd >>test.txt 
	git add test.txt 
	git commit -m 'add ddddd in dev2'
	git push origin dev
	```
	此时同时冲突，需要先更新最新到库到本地

	```
	git pull
	```
	更新后，查看冲突文件，并修改提交即可。
	```
	git add test.txt 
	git commit -m 'fix confict'
	git push origin dev
	```

<h2 id="title1.8">1.8 Git常用命令集</h2>  	

	```
	git init         把当前的目录变成可以管理的git仓库，生成隐藏.git文件。
	git add XX       把xx文件添加到暂存区去。
	git commit –m “XX”  提交文件 –m 后面的是注释。
	git status        查看仓库状态
	git diff  XX      查看XX文件修改了那些内容
	git log          查看历史记录
	git reset  --hard HEAD^ 或者 git reset  --hard HEAD~ 回退到上一个版本
	                     (如果想回退到100个版本，使用git reset –hard HEAD~100 )
	git reflog       查看历史记录的版本号id
	git checkout -- XX  把XX文件在工作区的修改全部撤销。
	git rm XX          删除XX文件
	git remote add origin https://github.com/tugenhua0707/testgit 关联一个远程库
	git push –u(第一次要用-u 以后不需要) origin master 把当前master分支推送到远程库
	git clone https://github.com/tugenhua0707/testgit  从远程库中克隆
	git checkout –b dev  创建dev分支 并切换到dev分支上
	git branch  查看当前所有的分支
	git checkout master 切换回master分支
	git merge dev    在当前的分支上合并dev分支
	git branch –d dev 删除dev分支
	git branch name  创建分支
	git stash 把当前的工作隐藏起来 等以后恢复现场后继续工作
	git stash list 查看所有被隐藏的文件列表
	git stash apply 恢复被隐藏的文件，但是内容不删除
	git stash drop 删除文件
	git stash pop 恢复文件的同时 也删除文件
	git remote 查看远程库的信息
	git remote –v 查看远程库的详细信息
	git push origin master  Git会把master分支推送到远程库对应的远程分支上
	```
 <h1 id="title2">2 ubuntu 上git保存用户名密码</h1>  
 
在使用Git 的时候，经常会遇到需要频繁输入密码的情况，每次git push 和 git pull 都要求输入用户名和密码，如果提交频繁的话就十分不方便。
## 解决方案
1. 进入Git 配置文件 
	```
	vim ~/.gitconfig
	```
2. 设置保存用户名密码，只有第一次需要输入
	```
	[credential]
		helper = store
	```
<h1 id="title3">3 Windows 上git 使用</h1>  

<h2 id="title3.1">3.1 安装</h2>  	

[git官网下载](https://git-scm.com/download/win)
[git  使用手册](https://git-scm.com/book/en/v2)

<h2 id="title3.2">3.2 建立本地工程</h2>  	

1. 下载git工程到本地，并建立debug分支
	```
	git clone XXX

	```
2. 使用vscode 进行代码查看

3. 合并代码后，到debug分支，然后提交给远程服务器

4. 下载代码到服务器，并进行编译

<!--stackedit_data:
eyJoaXN0b3J5IjpbMzAyOTI3MTMxLC0xNTYwNDY3OTYyLDE4Mz
I4ODIxNDUsMjAwODQ4NTI2OSwxODE2Nzg0Mzk1LC05MjE0MTE4
NTAsLTE3NzA2NzI5MTJdfQ==
-->