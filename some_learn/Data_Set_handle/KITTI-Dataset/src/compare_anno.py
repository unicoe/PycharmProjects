# -*- coding: utf-8 -*-
# @Time    : 18-11-16 下午10:17
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : compare_anno.py
# @Software: PyCharm

def get_im_lst(folder_path):

    im_lst = []

    rf = open(folder_path, "r")

    content = rf.readline()

    while content:
        im_lst.append(content.strip("\n"))
        content = rf.readline()

    return im_lst

l1 = get_im_lst("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/lst/anno_lst.txt")
l2 = get_im_lst("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/anno/person_11_16.txt")


l1.sort()
l2.sort()

for idx in l1:
    if idx in l2:
        pass
    else:
        print idx

"""
001987
002933
003556
003861
004358
004837
006814
007156
"""