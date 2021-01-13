# 目录

- <a href="#title1">1 帮助函数 getopt</a> 
- <a href="#title2">2 信号集 sigset_t</a> 
- <a href="#title3">3 json</a> 
- <a href="#title4">4 wait</a> 
<div STYLE="page-break-after: always;"></div>
 <h1 id="title1">1 帮助函数 getopt</h1>  

参考程序：
 ```
void parseOption(int argc, char *const argv[])
{	
	int opt;
	while ((opt = getopt(argc, argv, "hvtd")) != -1) {
        switch (opt) {
        case 'h':
            std::cout << argv[0] << std::endl
                      << "\t[v] - version" << std::endl
                      << "\t[h] - help" << std::endl;
            exit(0);
            break;
        case 'v':
            std::cout << "\n" << SOFTWARE_VERSION << "\n" << std::endl;
            exit(0);
            break;
        default:
            std::cout << "No such command" << std::endl;
            exit(0);
            break;
        }
    }
}
```

 [相关链接参考](https://www.cnblogs.com/water-moon/p/5983139.html)

 <h1 id="title2">2 信号集 sigset_t</h1>  

1. 信号集说明

	信号集被定义为一种数据类型
	```
	typedef struct {
	unsigned long sig[_NSIG_WORDS]；
	}  sigset_t
	```
	信号集用来描述信号的集合，每个信号占用一位（64位）。Linux所支持的所有信号可以全部或部分的出现在信号集中，主要与信号阻塞相关函数配合使用
	```
	sigemptyset(sigset_t *set)初始化由set指定的信号集，信号集里面的所有信号被清空，相当于64为置0；
	sigfillset(sigset_t *set)调用该函数后，set指向的信号集中将包含linux支持的64种信号，相当于64为都置1；
	sigaddset(sigset_t *set, int signum)在set指向的信号集中加入signum信号，相当于将给定信号所对应的位置1；
	sigdelset(sigset_t *set, int signum)在set指向的信号集中删除signum信号，相当于将给定信号所对应的位置0；
	sigismember(const sigset_t *set, int signum)判定信号signum是否在set指向的信号集中，相当于检查给定信号所对应的位是0还是1,异常返回-1。
	```
	```
	#include <stdio.h>
	#include <unistd.h>
	#include <stdlib.h>
	#include <signal.h>
	#include <sys/types.h>
	void print_sigset(sigset_t *set);
	int main(void)
	{
	    sigset_t myset;
	    sigemptyset(&myset);
	    sigaddset(&myset,SIGINT);
	    sigaddset(&myset,SIGQUIT);
	    sigaddset(&myset,SIGUSR1);
	    sigaddset(&myset,SIGRTMIN);
	    print_sigset(&myset);

	    return 0;

	}
	void print_sigset(sigset_t *set)
	{
	    int i;
	    for(i = 1; i < NSIG; ++i){
	        if(sigismember(set,i))
	            printf("1");
	        else
	            printf("0");
	    }
	    putchar('\n');
	}
	./a.out 
	0110000001000000000000000000000001000000000000000000000000000000
	```
2. 信号阻塞与未决

执行信号的处理动作称为信号递达（Delivery），信号从产生到递达之间的状态，称为信号未决（Pending）。进程可以选择阻塞（Block）某个信号。被阻塞的信号产生时将保持在未决状态，直到进程解除对此信号的阻塞，才执行递达的动作。注意，阻塞和忽略是不同的，只要信号被阻塞就不会递达，而忽略是在递达之后可选的一种处理动作。每个进程都有一个用来描述哪些信号递送到进程时将被阻塞的信号集，该信号集中的所有信号在递送到进程后都将被阻塞。
```
block集（阻塞集、屏蔽集）：一个进程所要屏蔽的信号，在对应要屏蔽的信号位置1
pending集（未决信号集）：如果某个信号在进程的阻塞集中，则也在未决集中对应位置1，表示该信号不能被递达，不会被处理
handler（信号处理函数集）：表示每个信号所对应的信号处理函数，当信号不在未决集中时，将被调用
以下是与信号阻塞及未决相关的函数操作：
#include <signal.h>
int sigprocmask(int how, const sigset_t *set, sigset_t *oldset))；
int sigpending(sigset_t *set));
int sigsuspend(const sigset_t *mask))；

sigprocmask()函数能够根据参数how来实现对信号集的操作，操作主要有三种：
-   SIG_BLOCK 在进程当前阻塞信号集中添加set指向信号集中的信号，相当于：mask=mask|set
-   SIG_UNBLOCK 如果进程阻塞信号集中包含set指向信号集中的信号，则解除对该信号的阻塞，相当于：mask=mask|~set
-   SIG_SETMASK 更新进程阻塞信号集为set指向的信号集，相当于mask=set

sigpending(sigset_t *set))获得当前已递送到进程，却被阻塞的所有信号，在set指向的信号集中返回结果。

sigsuspend(const sigset_t *mask))用于在接收到某个信号之前, 临时用mask替换进程的信号掩码, 并暂停进程执行，直到收到信号为止。

sigsuspend 返回后将恢复调用之前的信号掩码。信号处理函数完成后，进程将继续执行。该系统调用始终返回-1，并将errno设置为EINTR。
```

```
#include <unistd.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <fcntl.h>

#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <signal.h>


#define ERR_EXIT(m) \
    do \
    { \
        perror(m); \
        exit(EXIT_FAILURE); \
    } while(0)

void handler(int sig);
void printsigset(sigset_t *set)
{
    int i;
    for (i=1; i<NSIG; ++i)
    {
        if (sigismember(set, i))
            putchar('1');
        else
            putchar('0');
    }
    printf("\n");
}

int main(int argc, char *argv[])
{
    sigset_t pset;
    sigset_t bset;
    sigemptyset(&bset);   //清空信号集
    sigaddset(&bset, SIGINT);  //增加信号集（CTRL+C）
    // 注册信号处理
    if (signal(SIGINT, handler) == SIG_ERR)
        ERR_EXIT("signal error");
    
    if (signal(SIGQUIT, handler) == SIG_ERR)  //Ctrl + \
        ERR_EXIT("signal error");

    sigprocmask(SIG_BLOCK, &bset, NULL);//将信号加入进程阻塞集中
    for (;;)
    {
        sigpending(&pset);
        printsigset(&pset);
        sleep(1);
    }
    return 0;
}

void handler(int sig)
{
    if (sig == SIGINT)
        printf("recv a sig=%d\n", sig);
    else if (sig == SIGQUIT)
    {
        sigset_t uset;
        sigemptyset(&uset);
        sigaddset(&uset, SIGINT);
        sigprocmask(SIG_UNBLOCK, &uset, NULL);
    }
}
```
说明：程序首先将SIGINT信号加入进程阻塞集（屏蔽集）中，一开始并没有发送SIGINT信号，所以进程未决集中没有处于未决态的信号，当我们连续按下ctrl+c时，向进程发送SIGINT信号，由于SIGINT信号处于进程的阻塞集中，所以发送的SIGINT信号不能递达，也是就是处于未决状态，所以当我打印未决集合时发现SIGINT所对应的位为1，现在我们按下ctrl+\，发送SIGQUIT信号，由于此信号并没被进程阻塞，所以SIGQUIT信号直接递达，执行对应的处理函数，在该处理函数中解除进程对SIGINT信号的阻塞，所以之前发送的SIGINT信号递达了，执行对应的处理函数，但由于SIGINT信号是不可靠信号，不支持排队，所以最终只有一个信号递达。


3. 在终端输入`kill -l`可以查看各个信号对应的编号


 <h1 id="title1">3 json 解析</h1>  
 
 1. JSON for Modern C++
	 该库使用简单，适合做配置文件时使用。只需要包含头文件
	```
	#include <iostream>
	#include <fstream>
	#include <nlohmann/json.hpp>
	using json = nlohmann::json;

	int main()
	{
	    std::ifstream ifs("file.json");
	    json jf = json::parse(ifs);
	    std::cout << jf << std::endl;
	    std::cout << jf["a"] << std::endl;
	    return 0;
	}
	//编译
	g++ test.cpp -std=c++11
	//输出
	./a.out 
	{"a":123,"b":345}
	123
	```
2. 
 
 


<!--stackedit_data:
eyJoaXN0b3J5IjpbNjI4MDAyOTMzLC02Nzk0NTU2NTUsNjMxOT
AwMDcyLC05NTA0NTkwNyw1ODc4MTk5MDksMTI4MzAwMDM3Mywx
NDQ1MjgzNTU1LC01MDA1MDU1MzcsMTcxMjEwOTU3MCwtNTIxND
c1NTg5LC0xMTYyMjAzMjUyXX0=
-->