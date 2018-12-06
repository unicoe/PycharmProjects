# -*- coding: utf-8 -*-
# @Time    : 18-12-5 下午4:02
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : sp_img_ls.py
# @Software: PyCharm

sp_im_read = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/kitti_visual/sp_img_ls.txt", "r")

sp_im_name = sp_im_read.readline()

sp_im_l = []

while sp_im_name:
    im_name = sp_im_name.strip("\n")
    sp_im_l.append(im_name)
    sp_im_name = sp_im_read.readline()

print sp_im_l