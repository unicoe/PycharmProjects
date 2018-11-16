# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午9:34
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : save_im_name.py
# @Software: PyCharm

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/img_shape.txt", "r")

wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/img_name_lst.txt", "w")

content = rf.readline()

im_name_lst = []

while content:


    im_info = content.strip("\n").split(" ")

    im_name_lst.append(im_info[0])
    wf.write(im_info[0])
    wf.write("\n")

    content = rf.readline()

wf.close()