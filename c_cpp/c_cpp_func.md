# 目录

- <a href="#title1">1 帮助函数 getopt</a> 
- <a href="#title2">2 数组操作</a> 
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





<!--stackedit_data:
eyJoaXN0b3J5IjpbNTgxNDk0NzY4LC01MDA1MDU1MzcsMTcxMj
EwOTU3MCwtNTIxNDc1NTg5LC0xMTYyMjAzMjUyXX0=
-->