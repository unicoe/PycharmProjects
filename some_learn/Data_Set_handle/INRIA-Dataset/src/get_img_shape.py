# -*- coding: utf-8 -*-
# @Time    : 18-11-9 下午4:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : get_folder_name.py
# @Software: PyCharm


import os, sys
import cv2
import numpy as np

# 打开文件
path = "/home/user/Downloads/caltech_data_set/datasets/inria_test/images/set01/V000_copy"
dirs = os.listdir( path )

# 输出所有文件和文件夹

wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/test_img_shape.txt","w")

for file in dirs:
   img = cv2.imread(path + "/" + file)
   im_shape = img.shape
   wf.write(file.split(".")[0])
   wf.write(" ")
   wf.write(str(im_shape[0]))   # h
   wf.write(" ")
   wf.write(str(im_shape[1]))   # w
   wf.write("\n")
wf.close()







