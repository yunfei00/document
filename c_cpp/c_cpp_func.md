# 目录

- <a href="#title1">1 帮助函数 getopt</a> 
- <a href="#title2">2 信号集 sigset_t</a> 
- <a href="#title3">3 正则表达式匹配数字</a> 
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

```





<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYwNTA2NTQ1MCwxMjgzMDAwMzczLDE0ND
UyODM1NTUsLTUwMDUwNTUzNywxNzEyMTA5NTcwLC01MjE0NzU1
ODksLTExNjIyMDMyNTJdfQ==
-->