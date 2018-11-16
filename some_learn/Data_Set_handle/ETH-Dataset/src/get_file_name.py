# -*- coding: utf-8 -*-
# @Time    : 18-11-9 下午4:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : get_folder_name.py
# @Software: PyCharm


import os, sys

# 打开文件
path = "/home/user/Downloads/caltech_data_set/datasets/eth/images"
dirs = os.listdir( path )

# 输出所有文件和文件夹

wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/ETH-Dataset/lst/eth_test.txt", "w")

for file in dirs:
   file_name = file
   wf.write(file_name.split(".")[0])
   wf.write("\n")
   print file_name.split(".")[0]

