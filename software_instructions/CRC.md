**CRC校验**
CRC校验计算速度快，检错能力强，易于用编码器等硬件电路实现。从检错的正确率与速度、成本等方面，都比奇偶校验等校验方式具有优势。因而，CRC 成为计算机信息通信领域最为普遍的校验方式。常见应用有以太网/USB通信，压缩解压，视频编码，图像存储，磁盘读写等。

### CRC参数模型

不知道你是否遇到过这种情况，同样的CRC多项式，调用不同的CRC计算函数，得到的结果却不一样，而且和手算的结果也不一样，这就涉及到CRC的参数模型了。计算一个正确的CRC值，需要知道CRC的参数模型。

一个完整的CRC参数模型应该包含以下信息：WIDTH，POLY，INIT，REFIN，REFOUT，XOROUT。

-   NAME：参数模型名称。
-   WIDTH：宽度，即生成的CRC数据位宽，如CRC-8，生成的CRC为8位
-   POLY：十六进制多项式，省略最高位1，如 x8 + x2 + x + 1，二进制为1 0000 0111，省略最高位1，转换为十六进制为0x07。
-   INIT：CRC初始值，和WIDTH位宽一致。
-   REFIN：true或false，在进行计算之前，原始数据是否翻转，如原始数据：0x34 = 0011 0100，如果REFIN为true，进行翻转之后为0010 1100 = 0x2c
-   REFOUT：true或false，运算完成之后，得到的CRC值是否进行翻转，如计算得到的CRC值：0x97 = 1001 0111，如果REFOUT为true，进行翻转之后为11101001 = 0xE9。  
    
-   XOROUT：计算结果与此参数进行异或运算后得到最终的CRC值，和WIDTH位宽一致。  
    

通常如果只给了一个多项式，其他的没有说明则：INIT=0x00，REFIN=false，REFOUT=false，XOROUT=0x00。
<!--stackedit_data:
eyJoaXN0b3J5IjpbODg0NzUyODExXX0=
-->