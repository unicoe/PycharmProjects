# -*- coding: utf-8 -*-
# @Time    : 18-11-12 下午9:24
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : copy2path.py
# @Software: PyCharm
import os
import shutil

file_lst =os.listdir("/home/user/py-R-FCN/data/VOCdevkit0712/VOC0712/JPEGImages")

file_name = [
    "set09_V004_I00419.jpg",
    "set09_V002_I01559.jpg",
    "set09_V009_I00029.jpg",
    "set10_V001_I01559.jpg",
    "set09_V009_I00149.jpg",
    "set10_V001_I00389.jpg",
    "set10_V009_I00629.jpg",
    "set10_V009_I00599.jpg",
    "set10_V009_I01559.jpg",
    "set10_V009_I01589.jpg",
    "set10_V011_I00629.jpg",
    "set10_V011_I00659.jpg",
    "set10_V010_I01499.jpg",
]

for i in file_lst:
    for j in file_name:
        if i == j:
            source_path= "/home/user/py-R-FCN/data/VOCdevkit0712/VOC0712/JPEGImages/" + str(i)
            des_path= "/home/user/Desktop/img_lst/" + str(i)
            shutil.copyfile(source_path,des_path)