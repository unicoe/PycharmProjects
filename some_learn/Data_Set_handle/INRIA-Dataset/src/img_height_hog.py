# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午6:57
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : height_hog.py
# @Software: PyCharm


from matplotlib import pyplot as plt
import numpy as np

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/img_shape.txt", "r")

h_lst = []

content = rf.readline()

while content:
    tmp_h = int(content.strip("\n").split(" ")[2])
    h_lst.append(tmp_h)
    content = rf.readline()

height = np.array(h_lst)

plt.hist(height, bins =  [0, 100,  200,  300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600])

plt.title("histogram")
plt.show()

# tmp_lst = []
#
# for i in xrange(0,500,20):
#    tmp_lst.append(i)
#
# print tmp_lst