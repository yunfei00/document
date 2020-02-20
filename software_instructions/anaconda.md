# 1 使用conda 创建虚拟环境
1. 检查conda版本
	```
	conda -V
	conda 4.8.2
	```
2. 升级conda
	```
	conda update conda
	```
3. 搜索可用的python版本
	```
	conda search "^python$"
	conda search "^python$"
Loading channels: done
# Name                       Version           Build  Channel             
python                        2.7.13     h32f5f24_13  pkgs/main           
python                        2.7.13     h89fad4f_16  pkgs/main           
python                        2.7.13     hdada7c8_15  pkgs/main           
python                        2.7.14     h001abdc_23  pkgs/main           
python                        2.7.14     h138c1fe_30  pkgs/main           
python                        2.7.14     h138c1fe_31  pkgs/main           
python                        2.7.14     h50fefbe_18  pkgs/main           
python                        2.7.14     ha6acbcf_22  pkgs/main           
python                        2.7.14     ha7e29e4_26  pkgs/main           
python                        2.7.14     hd74e306_15  pkgs/main           
python                        2.7.14     hde5916a_29  pkgs/main           
python                        2.7.14     he768d2d_19  pkgs/main           
python                        2.7.14     hed931fe_16  pkgs/main           
python                        2.7.15      h138c1fe_0  pkgs/main           
python                        2.7.15      h8f8e585_2  pkgs/main           
python                        2.7.15      h8f8e585_4  pkgs/main           
python                        2.7.15      h8f8e585_6  pkgs/main           
python                        2.7.16      h97142e2_0  pkgs/main           
python                        2.7.16      h97142e2_1  pkgs/main           
python                        2.7.16      h97142e2_2  pkgs/main           
python                        2.7.16      h97142e2_3  pkgs/main           
python                        2.7.16      h97142e2_4  pkgs/main           
python                        2.7.16      h97142e2_5  pkgs/main           
python                        2.7.16      h97142e2_6  pkgs/main           
python                        2.7.16      h97142e2_7  pkgs/main           
python                        2.7.17      h97142e2_0  pkgs/main           
python                         3.5.4     h4bd9b1b_18  pkgs/main           
python                         3.5.4     h821eb87_14  pkgs/main           
python                         3.5.4     h8f450c2_22  pkgs/main           
python                         3.5.4     hb8880cc_19  pkgs/main           
python                         3.5.4     hc167b69_27  pkgs/main           
python                         3.5.4     hdd9bdb2_21  pkgs/main           
python                         3.5.4     he1de2d4_12  pkgs/main           
python                         3.5.4     he720263_23  pkgs/main           
python                         3.5.4     hf91e954_15  pkgs/main           
python                         3.5.5      h0a44026_3  pkgs/main           
python                         3.5.5      hc167b69_0  pkgs/main           
python                         3.5.5      hc167b69_1  pkgs/main           
python                         3.5.6      hc167b69_0  pkgs/main           
python                         3.6.2     h26d10c0_12  pkgs/main           
python                         3.6.2     h9e63aee_14  pkgs/main           
python                         3.6.2     ha11d96e_18  pkgs/main           
python                         3.6.2     hd04bb42_19  pkgs/main           
python                         3.6.2     hd0bf7f1_15  pkgs/main           
python                         3.6.3      h47c878a_7  pkgs/main           
python                         3.6.3      h5ce8c04_4  pkgs/main           
python                         3.6.3      h6804ab2_0  pkgs/main           
python                         3.6.3      h794556d_2  pkgs/main           
python                         3.6.3      hc655967_3  pkgs/main           
python                         3.6.4      hc167b69_0  pkgs/main           
python                         3.6.4      hc167b69_1  pkgs/main           
python                         3.6.4      hc167b69_3  pkgs/main           
python                         3.6.5      hc167b69_0  pkgs/main           
python                         3.6.5      hc167b69_1  pkgs/main           
python                         3.6.6      hc167b69_0  pkgs/main           
python                         3.6.7      haf84260_0  pkgs/main           
python                         3.6.8      haf84260_0  pkgs/main           
python                         3.6.9      h359304d_0  pkgs/main           
python                        3.6.10      h359304d_0  pkgs/main           
python                         3.7.0      hc167b69_0  pkgs/main           
python                         3.7.1      haf84260_3  pkgs/main           
python                         3.7.1      haf84260_7  pkgs/main           
python                         3.7.2      haf84260_0  pkgs/main           
python                         3.7.3      h359304d_0  pkgs/main           
python                         3.7.4      h359304d_0  pkgs/main           
python                         3.7.4      h359304d_1  pkgs/main           
python                         3.7.5      h359304d_0  pkgs/main           
python                         3.7.6      h359304d_2  pkgs/main           
python                         3.8.0      h359304d_0  pkgs/main           
python                         3.8.0      h359304d_1  pkgs/main           
python                         3.8.0      h359304d_2  pkgs/main           
python                         3.8.1      h359304d_1  pkgs/main   
	
	```
4. 创建虚拟环境
	```
	conda create -n yourenvname python=x.x anaconda
	```
5. 激活虚拟环境
6. 安装虚拟环境软件包
7. 退出虚拟环境
8. 删除虚拟环境
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDA0NjQyMDcyXX0=
-->