宏定义
SOH = b'\x01'
STX = b'\x02'
EOT = b'\x04'
ACK = b'\x06'
NAK = b'\x15'
CAN = b'\x18'
CRC = b'C'
1. ymodem协议由接收方发起字符C开始
2. 发送方在接收到C之后，开始发送数据
发送第一帧数据包，内容如下：
SOH 00 FF Foo.c NUL[123] CRC CRC
第1字节SOH:表示本包数据区大小有128字节。如果头为STX表示本包数据区大小为1024
第2字节00: 编号，第一包为00,第二包为01，第三包为02依次累加。到FF后继续从0循环递增。
第3字节FF: 编号的反码。 编号为00 对应FF，为01对应FE，以此类推。






<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY0MjE3NTQ1NywzMTg5Mzc3OF19
-->