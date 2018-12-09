# -*- coding: utf-8 -*-
# @Time    : 18-12-6 下午9:42
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : careate_b_img.py
# @Software: PyCharm

import numpy as np
import cv2
#create a black use numpy,size is:512*512
img = np.zeros((480,640,3), np.uint8)
#fill the image with white
img.fill(0)

cv2.imwrite("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/mask_img/b_img.png",img)


im_ls_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/caltech1x_ls.txt","r")

im_ls = []

im_name = im_ls_r.readline()

while im_name:
    im_tmp = im_name.strip("\n")

    im_ls.append(im_tmp)

    im_name = im_ls_r.readline()


for i_im in im_ls:
    cv2.imwrite("/home/user/Disk1.8T/data_set/seglabel_png/"+i_im+".png", img)
