# -*- coding: utf-8 -*-
# @Time    : 18-11-9 下午4:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : get_folder_name.py
# @Software: PyCharm


import os, sys

# 打开文件
path1 = "/home/user/Disk1.8T/draw_result/kitti/2018_12_07_Fri_23_36_43_det_test_person/testing/image_2"
res1 = os.listdir( path1 )

# 输出所有文件和文件夹

path2 = "/home/user/Disk1.8T/draw_result/kitti/2018_12_07_Fri_22_56_43_det_test_person/testing/image_2"
res2 = os.listdir( path2 )



for i2 in res2:
   if i2 not in res1:
      print i2