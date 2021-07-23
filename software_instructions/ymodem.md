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
4. 




<!--stackedit_data:
eyJoaXN0b3J5IjpbMjc1MDgyNTYxLDMxODkzNzc4XX0=
-->