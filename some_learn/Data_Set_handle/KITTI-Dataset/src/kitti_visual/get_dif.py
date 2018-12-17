# -*- coding: utf-8 -*-
# @Time    : 18-11-9 下午4:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : get_folder_name.py
# @Software: PyCharm


import os, sys

# 打开文件
path1 = "/home/user/Disk1.8T/draw_result/paper_result/cv1/adapted_R-FCN/VOC0712/JPEGImages/"
res1 = os.listdir( path1 )

# 输出所有文件和文件夹

path2 = "/home/user/Disk1.8T/draw_result/paper_result/cv/AVE-22k_nms_56-LAMR=4/VOC0712/JPEGImages/"
res2 = os.listdir( path2 )



for i2 in res1:
   if i2 not in res2:
      print i2