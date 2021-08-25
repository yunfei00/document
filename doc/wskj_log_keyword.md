[toc]
# 1 classic
## 1.1 单个关键字
测量结果： SCAN_STATUS_RESPONSE
按键弹起：EVENT_ALL_BUTTON_UP
按键按下：EVENT_ALL_BUTTON_DOWN
    开始测量：START_SCAN_REQUEST
上人      ：EVENT_PERSON
下人       :EVENT_PERSON_LEAVE
转盘传感器事件：tb action
急停按钮按下：EMERGENCY_BUTTON_DOWN
急停弹起事件：EMERGENCY_BUTTON_UP


# 2 Air
## 2.1 单个关键字
设备自检：     DEVICE_SELF_TEST_REQUEST
开始扫描：     START_SCAN_REQUEST
体重板重启:    体重板关闭
体成分超时：   上报体脂板数据读取异常
导轨底部传感器事件：EVENT_RAIL_BOTTOM_SENSER_INTERRUPT
导轨顶部传感器事件：EVENT_RAIL_TOP_SENSER_INTERRUPT
转盘事件：EVENT_TABLE_4_4TH_SERNSER_INTERRPUT
急停按下事件：EVENT_EMERGENCY_BUTTON_DOWN
急停弹起事件：EVENT_EMERGENCY_BUTTON_UP
导轨反转事件：RAIL_REVERSE_RESPONSE
开机事件：VisbodyFit 
    体重测量事件：BODY_INFO_REQUEST
    测出体重：上报体重
单片机程序重启：EVENT_MCU_IS_REBOOTED
体脂板标定结束：< EWP03W >
开机关键字：VisbodyFit-Air



## 2.2 体重测量与上报

## 2.3 扫描流程
```
START_SCAN_REQUEST|< CC >|< TB9 >
```
## 2.4 同一个客户体重不准
```
上报体重|BODY_INFO_REQUEST|userID is 
```
客户同一天测试，体重相差2.5kg，未提供电话。需要过滤信息。
## 2.5 体脂板校验失败3
```
VisbodyFit-Air|体脂板数据校验失败3
```
## 2.6 测量失败
上报体重|BODY_INFO_REQUEST|userID is |VisbodyFit-Air|START_SCAN_REQUEST|< CC >|< TB9 >|

# 3 现象说明
## 3.1 E1错误

体脂测量 左边脚掌或者左手四指松开 会在第三个SP包之后报错
右边脚掌或者右手四指松开 则直接报错 不返回SP信息

krDf5y5P

grep '硬件返回异常类型' *
egrep '上报体重|BODY_INFO_REQUEST|userID is |VisbodyFit-Air|START_SCAN_REQUEST|< CC >|< TB0 >|< TB9 >|100%|上报体脂板测量异常|上报' *
EVENT_RAIL_BOTTOM_SENSER_INTERRUPT|EVENT_RAIL_TOP_SENSER_INTERRUPT|EVENT_RAIL_TOP_SENSER_INTERRUPT|VisbodyFit-Air

3 V-R 关键字
上报电阻数据|





VD:
校准文件打印关键字
Raw50kg :



<!--stackedit_data:
eyJoaXN0b3J5IjpbOTM1MjgwMTE4XX0=
-->