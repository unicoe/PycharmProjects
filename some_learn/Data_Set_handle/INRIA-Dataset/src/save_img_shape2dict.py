# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午5:20
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : save_img_shape2dict.py
# @Software: PyCharm


rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/img_shape.txt", "r")

shape_dict = {}

content = rf.readline()

while content:


    im_info = content.strip("\n").split(" ")
    shape_dict[im_info[0]] = [int(im_info[1]), int(im_info[2])]           # h w

    content = rf.readline()


print shape_dict