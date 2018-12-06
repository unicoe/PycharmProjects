# -*- coding: utf-8 -*-
# @Time    : 18-11-9 下午4:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : get_folder_name.py
# @Software: PyCharm


import os, sys

# 打开文件
path = "/home/user/Downloads/caltech_data_set/datasets/inria_test/images/set01/V000"
dirs = os.listdir( path )

# 输出所有文件和文件夹
for file in dirs:
   file_name = "set01_V000_" + file
   print file_name.split(".")[0]


"""
HyperLearner
RepLoss
ACF++
DeepParts
SA-FastRCNN
LDCF++
F-DNN+SS
TA-CNN
Checkerboards
OR-CNN
MRFC+Semantic
CompACT-Deep
MS-CNN
RPN+BF
"""