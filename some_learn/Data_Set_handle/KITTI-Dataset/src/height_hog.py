# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午6:57
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : height_hog.py
# @Software: PyCharm


from matplotlib import pyplot as plt
import numpy as np

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/lst/h_lst.txt", "r")

h_lst = []

content = rf.readline()

while content:
    tmp_h = int(content)
    h_lst.append(tmp_h)
    content = rf.readline()

height = np.array(h_lst)

plt.hist(height, bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250,260])

plt.title("histogram")
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