# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午6:57
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : height_hog.py
# @Software: PyCharm


from matplotlib import pyplot as plt
import numpy as np

from matplotlib.font_manager import FontProperties

def show_hog(path):
    rf = open(path, "r")

    h_lst = []

    content = rf.readline()

    while content:
        tmp_h = int(content)
        h_lst.append(tmp_h)
        content = rf.readline()

    height = np.array(h_lst)

    plt.hist(height, bins = [0,100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100], color='#1E90FF')
    font = FontProperties(fname=r"/home/user/PycharmProjects/SIMSUN.TTC", size=20)
    plt.title(u"MOT2017Det行人数据集", fontproperties=font)
    plt.xlabel(u"行人的高度" , fontproperties=font)
    plt.ylabel(u"行人的数量" , fontproperties=font)
    #plt.title("")from matplotlib.font_manager import FontProperties
    plt.show()


"""
55 - 700
"""
#
# tmp_lst = []
#
# for i in xrange(0,260,10):
#    tmp_lst.append(i)
#
# print tmp_lst

ls = [

# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/train_h02.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/train_h04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/train_h05.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/train_h09.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/train_h10.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/train_h11.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/train_h13.txt',
"/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/train_h.txt"
]

for i_path in ls:
    show_hog(i_path)