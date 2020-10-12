# 目录

<h3><a href="#title1">1 一组体成分数据</a> </h3>
<h3><a href="#title2">2 生物电阻抗分析</a> </h3>
<h3><a href="#title3">3 名词解释</a> </h3>
		<h4><ul><a href="#title3.1">3.1 有机化合物</a> </h4>
		<h4><ul><a href="#title3.2">3.2 无机化合物</a> </h4>
		<h4><ul><a href="#title3.3">3.3 无机盐</a> </h4>
		<h4><ul><a href="#title3.4">3.4 SEARCH 函数</a> </h4>
		<h4><ul><a href="#title3.5">3.5 SUBSTITUTE 函数</a> </h4>
		<h4><ul><a href="#title3.6">3.6 FIND 函数</a> </h4>
<div style="page-break-after:always"></div>

  <h1 id="title1">1 一组体成分数据</h1>  
 

1. 可以测量出的体成分有：人体总体液，细胞内外液，去脂体重，肌肉蛋白质，骨质和脂肪等。
2. 去脂体重主要成分是肌肉，骨质等，肌肉中以蛋白质和体液为主，体液占比70%以上。
3. 分子模型是研究中最常用的一种模型，它将人体分为两部分，一部分是脂肪物质（FM），一部分是非脂肪物质（FFM）。
4. 细胞是构成人体的基本单位，细胞模型在生理学评估中十分重要。该模型认为人体重量有三部分组成：细胞质量，细胞外液体，细胞外固体。其中脂肪细胞可以作为单独部分计算。
5. 体重=脂肪重量（FM）+细胞外液体+细胞外固体+体细胞质量（BCM） 体细胞质量可以通过测量钾的含量得到，细胞外液体可以通过稀释法测量，或通过稀释法测量身体总体液与通过钾含量得到的体细胞质量相减得到。

相关性关系：
6. 体重=体脂肪量+去脂体重；  
7. 体脂率=体脂肪量/体重；  
8. 去脂体重=肌肉量+无机盐；  
9. 肌肉量=蛋白质+身体总水分；  
10. 身体总水分=细胞外液+细胞内液体；  
11. 骨骼肌＜肌肉量；  
12. 体重控制=肌肉控制+脂肪控制；  
13. （左上肢肌肉+右上肢肌肉+躯干肌肉+左下肢肌肉+右下肢肌肉）≤肌肉量  
14. （左上肢脂肪+右上肢脂肪+躯干脂肪+左下肢脂肪+右下肢脂肪）≤体脂肪量  
15. 身体质量指数（BMI）=体重(单位kg)/（身高（单位m））²


说明：

ECF（extracellular fluid）指 细胞外液

ECW（extracellular water）指 细胞外的水

推测：

身体总重量（77.241791）=体脂肪 + 全身肌肉量 + 无机盐 + 所有ECF + 所有ECW = 9.583672 + 60.085647 + 4.286272 +1.922777 + 2.199524

所有ECF= 右上肢ECF + 左上肢ECF + 躯干ECF + 右下肢ECF + 左下肢ECF +浮肿指数ECF= 0.326951 + 0.326186 + 0.317950 + 0.313862 + 0.319133 + 0.318695= 1.922777

所有ECW = 右上肢ECW + 左上肢ECW + 躯干ECW + 右下肢ECW + 左下肢ECW + 浮肿指数ECW = 0.373420 + 0.372613 + 0.363941 + 0.359637 + 0.365187 + 0.364726 = 2.199524

全身肌肉量=四肢+躯干=4.362361 + 4.205561 + 31.487587 +10.022278 +10.007860 =60.085647 肌肉量是64.183746 有差别 暂时未知
```
/// TB0

float reserved_1; //1

float reserved_2; //2

float reserved_3; //3

float PBF; 12.407368 //4.体脂肪百分比 脂肪占体重的百分比 BFM/（BFM + FFM）×100 = 9.583672 / （67.658119+9.583672） ×100 = 12.407366

float reserved_4; //5

float FFM; 67.658119 //6.去脂体重 去掉脂肪的重量（kg） 体重=去脂体重+体脂肪 77.241791=67.658119+9.583672 （验证ok）

float BFM; 9.583672 //7.体脂肪 身体脂放重量（kg）

float LMRA; 4.362361 //8.右上肢肌肉量

float LMLA; 4.205561 //9.左上肢肌肉量

float LMTR; 31.487587 //10.躯干肌肉量

/// TB1

float LMRL; 10.022278 //11.右下肢肌肉量

float LMLL; 10.007860 //12.左下肢肌肉量

float reserved_5; //13

float LM; 64.183746 //14.肌肉量 （暂时不确定含义）

float reserved_6; //15

float TM; 4.286272 //16.无机盐

float reserved_7; //17

float ECFRA; 0.326951 //18.右上肢ECF

float ECFLA; 0.326186 //19.左上肢ECF

float ECFTR; 0.317950 //20.躯干ECF

/// TB2

float ECFRL; 0.313862 //21.右下肢ECF

float ECFLL; 0.319133 //22.左下肢ECF

float ECWRA; 0.373420 //23.右上肢ECW

float ECWLA; 0.372613 //24.左上肢ECW

float ECWTR; 0.363941 //25.躯干ECW

float ECWRL; 0.359637 //26.右下肢ECW

float ECWLL; 0.365187 //27.左下肢ECW

float ECWT; 0.364726 //28.浮肿指数ECW

float ECF; 0.318695 //29.浮肿指数ECF

float ICW; 31.584488 //30.细胞内水分

/// TB3

float ECW; 18.133390 //31.细胞外水分

float TBW; 49.717880 //32.总水分 总水分=细胞内水分 + 细胞外水分 = 31.584488 + 18.133390 = 49.717878

float PROTEIN; 13.653975 //33.蛋白质

float reserved_8; 39.190174 //34

float BCM; 45.238464 //35.细胞量

float reserved_9; 6.055309 //36

float reserved_10; 0.152884 //37

float reserved_11; 0.221679 //38

float reserved_12; 5.004560 //39

float reserved_13; 1.484752 //40

/// TB4

float reserved_14; //41 0 [1.466150]

float reserved_15; //42 1 [91.846764

float reserved_16; //43 2 [3.133394]

float reserved_17; //44 3 [3.126056]

float reserved_18; //45 4 [3.047126]

float reserved_19; //46 5 [3.007951]

float reserved_20; //47 6 [3.058462]

float reserved_21; //48 7 [9.899589]

float reserved_22; //49 8 [0.000000]

float reserved_23; //50 9 [0.000000]

/// TB5

float reserved_24; 0 [84.198906]//51

float reserved_25; 1 [99.528564]//52

float WHR; 2 [0.845977] //53.腰臀比

float VFA; 3 [34.854752]//54.内脏脂肪面积

float SCORE; 4 [90.738129]//55.评分 对身体的评分

float PBF_IVAL; 5 [15.000000]//56.体脂肪百分比（标准值） 体脂肪百分比标准范围 浮动±5

float BMI_IVAL; 6 [22.000000]//57.身体质量参数（标准值） 范围 18.5-24

float WHR_IVAL; 7 [0.850000] //58.腰臀比（标准值）

float WT_IVAL ; 8 [77.241791]//59.体重（标准值）

float BFM_IVAL; 9 [9.991080] //60.体脂肪（标准值）

/// TB6

float FFM_IVAL; 0 [56.616119] //61.去脂体重（标准值）

float BMR_IVAL; 1 [1592.908203]//62.基础代谢量（标准值）

float TM_IVAL ; 2 [3.849896] //63.无机盐（标准值）

float BMC_IVAL; 3 [3.170503] //64.细胞量（标准值）

float LM_IVAL ; 4 [53.445618] //65.肌肉量（标准值）

float TBW_IVAL; 5 [41.612850] //66.总水分（标准值）

float PROTEIN_IVAL;6 [11.153376] //67.蛋白质（标准值）

float ECW_IVAL; 7 [15.812882] //68.细胞外水分（标准值）

float ICW_IVAL; 8 [25.799967] //69.细胞内水分（标准值）

float reserved_26; 9 [31.647158] //70

/// TB7

float BCM_IVAL; 0 [36.953342] //71.细胞量（标准值）

float LMA_IVAL; 1 [3.169539] //72.左右上肢肌肉量（标准值）

float LMT_IVAL; 2 [25.287687] //73.躯干肌肉量（标准值）

float LML_IVAL; 3 [8.810190] //74.左右下肢肌肉量（标准值）

float BFMA_IVAL; 4 [0.599465] //75.左右上肢体脂肪（标准值）

float BFMT_IVAL; 5 [4.216236] //76.躯干体脂肪（标准值）

float BFML_IVAL; 6 [1.718466] //77.左右下肢体脂肪（标准值）

float PLMRA; 7 [132.029221] //78.右上肢肌肉量百分比

float PLMLA; 8 [127.283562] //79.左上肢肌肉量百分比

float PLMTR; 9 [119.538567] //80.躯干肌肉量百分比

/// TB8

float PLMRL; 0 [109.103218] //81.右下肢肌肉量百分比 这里的百分比是和标准值比较的

float PLMLL; 1 [108.946266] //82.左下肢肌肉量百分比

float PBFMRA; 2 [25.503374] //83.右上肢体脂肪百分比

float PBFMLA; 3 [36.979538] //84.左上肢体脂肪百分比

float PBFMTR; 4 [118.697365] //85.躯干体脂肪百分比

float PBFMRL; 5 [86.399834] //86.右下肢体脂肪百分比

float PBFMLL; 6 [85.317375] //87.左下肢体脂肪百分比

float CMT; 7 [0.000000] //88.体重控制

float CMM; 8 [0.000000] //89.肌肉控制

float CMF; 9 [0.000000] //90.脂肪控制

/// TB9

float BMR; 1831.415405 //91.基础代谢量

float reserved_27; //92

float reserved_28; //93

float reserved_29; //94

float reserved_30; //95

float reserved_31; //96

float reserved_32; //97

float reserved_33; //98

float reserved_34; //99

float reserved_35; //100
```


   <h1 id="title2">2 生物电阻抗分析</h1>  
   
**生物电阻抗分析**（**BIA**）是估算[身体成分](https://en.wikipedia.org/wiki/Body_composition "身体构成")（尤其是人体脂肪和肌肉质量）的常用方法。在BIA中，弱电流流经人体并测量电压，以计算人体的[阻抗](https://en.wikipedia.org/wiki/Electrical_impedance "电阻抗")（电阻）。人体大部分水分存储在肌肉中。因此，如果一个人肌肉发达，则很有可能该人也会有更多的体内水分，从而导致较低的阻抗。自从1980年代中期出现第一批可商购的设备以来，该方法由于其易用性和设备的便携性而变得流行。在消费者市场中，它是估算人体脂肪的简单工具。BIA [[1]](https://en.wikipedia.org/wiki/Bioelectrical_impedance_analysis#cite_note-1)实际上确定[电阻抗](https://en.wikipedia.org/wiki/Electrical_impedance "电阻抗")或与通过人体组织的电流相反，然后可用于估算[人体总水](https://en.wikipedia.org/wiki/Total_body_water "体内总水")（TBW），可用于估算无脂肪体重以及体重差异，[体内脂肪](https://en.wikipedia.org/wiki/Adiposity "肥胖")。

   <h2 id="title3.1">3.1 有机化合物</h1>  
   
[有机化合物](https://baike.baidu.com/item/%E6%9C%89%E6%9C%BA%E5%8C%96%E5%90%88%E7%89%A9/2950156)

   <h2 id="title3.2">3.2 无机化合物</h1>  
  
[无机化合物](https://baike.baidu.com/item/%E6%97%A0%E6%9C%BA%E5%8C%96%E5%90%88%E7%89%A9/10716655)

   <h2 id="title3.3">3.3 无机盐</h1>  
  
[无机盐](https://baike.baidu.com/item/%E6%97%A0%E6%9C%BA%E7%9B%90/2726998?fr=aladdin)

参考文档 [chrome-extension://bocbaocobfecmglnmeaeppambideimao/pdf/viewer.html?file=file%3A%2F%2F%2FC%3A%2FUsers%2FAdministrator%2FDesktop%2Ffat%2F%25E8%25BF%2590%25E5%258A%25A8%25E8%2590%25A5%25E5%2585%25BB%25E5%25AD%25A6%25E8%25AE%25B2%25E5%25BA%25A7%25E2%2580%2594%25E2%2580%2594%25E7%25AC%25AC%25E4%25BA%2594%25E8%25AE%25B2%2520%2520%25E6%259E%2584%25E6%2588%2590%25E4%25BA%25BA%25E4%25BD%2593%25E7%259A%2584%25E6%2597%25A0%25E6%259C%25BA%25E7%259B%2590%25E6%2588%2590%25E5%2588%2586%25E5%2592%258C%25E5%25BE%25AE%25E9%2587%258F%25E5%2585%2583%25E7%25B4%25A0.pdf]

<!--stackedit_data:
eyJoaXN0b3J5IjpbOTYzMTYxMzc2LC0xOTQ4MDQ2NTgzLC0xND
AwNzYxOTU5LC0xODgzNTU2NDksLTExMjYxNzAzMjJdfQ==
-->