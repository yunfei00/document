**CRC校验**
CRC校验计算速度快，检错能力强，易于用编码器等硬件电路实现。从检错的正确率与速度、成本等方面，都比奇偶校验等校验方式具有优势。因而，CRC 成为计算机信息通信领域最为普遍的校验方式。常见应用有以太网/USB通信，压缩解压，视频编码，图像存储，磁盘读写等。

### CRC参数模型

不知道你是否遇到过这种情况，同样的CRC多项式，调用不同的CRC计算函数，得到的结果却不一样，而且和手算的结果也不一样，这就涉及到CRC的参数模型了。计算一个正确的CRC值，需要知道CRC的参数模型。

一个完整的CRC参数模型应该包含以下信息：WIDTH，POLY，INIT，REFIN，REFOUT，XOROUT。

-   NAME：参数模型名称。
-   WIDTH：宽度，即生成的CRC数据位宽，如CRC-8，生成的CRC为8位
-   POLY：十六进制多项式，省略最高位1，如 x8 + x2 + x + 1，二进制为1 0000 0111，省略最高位1，转换为十六进制为0x07。
-   INIT：CRC初始值，和WIDTH位宽一致,原始数据高width位和初始值进行异或运算
-   REFIN：true或false，在进行计算之前，原始数据是否翻转.如果REFIN为true，需要先对原始数据进行翻转,只是对每一个字节进行翻转，顺序不变
-   REFOUT：true或false，运算完成之后，得到的CRC值是否进行翻转，如计算得到的CRC值：0x97 = 1001 0111，如果REFOUT为true，进行翻转之后为11101001 = 0xE9。  
    
-   XOROUT：计算结果与此参数进行异或运算后得到最终的CRC值，和WIDTH位宽一致。  
    

通常如果只给了一个多项式，其他的没有说明则：INIT=0x00，REFIN=false，REFOUT=false，XOROUT=0x00。

![preview](https://pic2.zhimg.com/v2-91f148259b466e4a75a10c6607370855_r.jpg)

### CRC 计算流程如下

1.init 原始数据高width位和初始值进行异或运算
2.refin为TRUE，需要先对原始数据进行翻转：0011 0100 > 0010 1100,只是对每一个字节进行翻转，顺序不变
3.原始数据处理 把处理之后的数据和多项式进行模2除法，求得余数：
4.与xorout进行异或
5.refout为TRUE，对结果进行翻转得到最终的CRC


### CRC校验

上面通过笔算的方式，讲解了CRC计算的原理，下面来介绍一下如何进行校验。

按照上面CRC计算的结果，最终的数据帧：0011 0100 1101 1111 = 34DF，前8位0011 0100是原始数据，后8位1101 1111 是 CRC结果。

接收端的校验有两种方式，一种是和CRC计算一样，在本地把**接收到的数据和CRC分离**，然后在本地对数据进行CRC运算，得到的CRC值和接收到的CRC进行比较，如果一致，说明数据接收正确，如果不一致，说明数据有错误。

另一种方法是把整个数据帧进行CRC运算，因为是数据帧相当于把原始数据左移8位，然后加上余数，如果直接对整个数据帧进行CRC运算（除以多项式），那么余数应该为0，如果不为0说明数据出错。

而且，不同位出错，余数也不同，可以证明，余数与出错位数的对应关系只与CRC参数模型有关，而与原始数据无关。


### CRC python 实现
参考模型
CRC-16
```
POLY = 0x31 = 0011 0001(最高位1已经省略)
INIT = 0x00
XOROUT = 0x00
REFIN = TRUE
REFOUT = TRUE
```

###  位操作
```
x >> y # 返回 x 向右移 y 位得到的结果
x << y # 返回 x 向左移 y 位得到的结果
x & y # 且操作，返回结果的每一位是 x 和 y 中对应位做 and 运算的结果，只有 1 and 1 = 1，其他情况位0
x | y # 或操作，返回结果的每一位是 x 和 y 中对应位做 or 运算的结果，只有 0 or 0 = 0，其他情况位1
~x # 反转操作，对 x 求的每一位求补，只需记住结果是 -x - 1
x ^ y # 或非运算，如果 y 对应位是0，那么结果位取 x 的对应位，如果 y 对应位是1，取 x 对应位的补
```

### 代码实现
```
def crc_cal(data,width,poly,init,xorout,refin,refout):
    # CRC 计算流程如下
    # 1.init 原始数据高width位和初始值进行异或运算
    # 2.refin为TRUE，需要先对原始数据进行翻转：0011 0100 > 0010 1100,只是对每一个字节进行翻转，顺序不变
    # 3.原始数据处理 把处理之后的数据和多项式进行模2除法，求得余数：
    # 4.与xorout进行异或
    # 5.refout为TRUE，对结果进行翻转得到最终的CRC
    
    data_len = data.__len__()
    if not data_len:
        return None

    # print('init is ',init)
    # 1. init 处理
    if width == 8:
        data[0] = init & 0xFF ^ data[0]
    elif width == 16:
        if data_len < 2:  
            print('input lenth is so short for {},input is {}'.format(width,data))
            return None
        data[0] = init & 0xFF ^ data[0]
        data[1] = init & 0xFF ^ data[1]
    elif width == 32:
        if data_len < 4:  
            print('input lenth is so short for {},input is {}'.format(width,data))
            return None
        data[0] = init & 0xFF ^ data[0]
        data[1] = init & 0xFF ^ data[1]
        data[2] = init & 0xFF ^ data[2]
        data[3] = init & 0xFF ^ data[3]                  

    # 2. 翻转处理 
    data_in_ref = data
    if refin:
        data_in_ref = []
        for i in range(0,data_len):
            data_in_ref.append(int('{:08b}'.format(data[i])[::-1],2))


    # 3. 数据处理
    crc = 0
    for i in range(0,data_len):
        # print('{:08b}'.format(data_in_ref[i]))
        crc = crc ^ data_in_ref[i] 
        # print('crc left 8 is {:08b}'.format(crc))
        for i in range(0,8):
            if crc & pow(2,width-1):
                crc = (crc << 1 & (pow(2,width)-1)) ^ poly
            else:
                crc = crc << 1 & (pow(2,width)-1)
            # print('crc {} is {:08b}'.format(i,crc & (pow(2,width)-1)))


    # 上面的操作，最终左移位数为8,如果是16位，则需要修改为16，增加少的位数
    if width > 8:
        for i in range(0,width-8):
            if crc & pow(2,width-1):
                crc = (crc << 1 & (pow(2,width)-1)) ^ poly
            else:
                crc = crc << 1 & (pow(2,width)-1)
            # print('crc {} is {:08b}'.format(i,crc & (pow(2,width)-1)))
            
    
    # print('crc is {:08b}'.format(crc & (pow(2,width)-1)))

    # 4. xorout异或处理
    crc = crc ^ xorout
    
    # 5. 翻转处理
    if refout:
        # 反转
        crc_str = '{:0b}'.format(crc)
        if crc_str.__len__() < width:
            crc_str = '0' * (width-crc_str.__len__()) + crc_str 
        
        crc_str_reverse = crc_str[::-1]
        crc = int(crc_str_reverse,2)
        
    return crc
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4ODA3Mzg1NTksLTk5Nzg0MzU4MiwtNT
M3NDE3NzUwLC0xMTQ5MzY1NDQsLTEwMDg1MDMwODAsMTI3NDE0
MDgzMCwtNzQxMDA2OTQzLDEyNDYyNzQyNTcsMjExNzY2MzI5Mi
wtMTU0NzQ2MTAwMyw4ODQ3NTI4MTFdfQ==
-->