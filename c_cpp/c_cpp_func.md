# 目录

- <a href="#title1">1 帮助函数 getopt</a> 
- <a href="#title2">2 数组操作</a> 
- <a href="#title3">3 正则表达式匹配数字</a> 
- <a href="#title4">4 wait</a> 
<div STYLE="page-break-after: always;"></div>
 <h1 id="title1">1 帮助函数 getopt</h1>  
 ```
void parseOption(int argc, char *const argv[])
{	
	int opt;
	while ((opt = getopt(argc, argv, "hvtd")) != -1) {
```
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUyMTQ3NTU4OSwtMTE2MjIwMzI1Ml19
-->