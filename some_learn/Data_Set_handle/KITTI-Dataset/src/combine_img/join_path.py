# -*- coding: utf-8 -*-
# @Time    : 18-12-6 上午11:05
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : join_path.py
# @Software: PyCharm

path_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/combine_img/path.txt", "r")

path_w = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/combine_img/final_path.txt", "w")
path_ = path_r.readline()

while path_:

    path_info = path_.strip('\n') + '/testing'
    path_w.write(path_info)
    path_w.write("\n")
    path_ = path_r.readline()

path_w.close()
path_r.close()