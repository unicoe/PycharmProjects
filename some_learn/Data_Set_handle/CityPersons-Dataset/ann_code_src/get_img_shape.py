# -*- coding: utf-8 -*-
# @Time    : 18-11-9 下午4:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : get_folder_name.py
# @Software: PyCharm


import os, sys
import cv2
import numpy as np

# 遍历文件夹下的所有文件,获取图片的宽和高

def get_im_shape(path):
    cnt = 0
    wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/im_info_ls/img_shape.txt", "w")
    for (root, dirs, files) in os.walk(path):
        for filename in files:
            print(os.path.join(root,filename))
            cnt += 1

            img = cv2.imread(os.path.join(root, filename))
            im_shape = img.shape

            filename
            wf.write(filename.split(".")[0])
            wf.write(" ")
            wf.write(str(im_shape[0]))   # h
            wf.write(" ")
            wf.write(str(im_shape[1]))   # w
            wf.write("\n")
    wf.close()

    print("img nums: {:d}".format(cnt))


get_im_shape("/home/user/Disk1.8T/data_set/citypersons/JPEGImages")







