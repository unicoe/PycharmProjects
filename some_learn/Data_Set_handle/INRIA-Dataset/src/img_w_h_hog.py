# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午6:57
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : height_hog.py
# @Software: PyCharm


from matplotlib import pyplot as plt
import numpy as np
#
rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/img_w_h_lst.txt", "r")

h_lst = []

content = rf.readline()

while content:
    tmp_h = float(content)
    h_lst.append(tmp_h)
    content = rf.readline()

height = np.array(h_lst)

plt.hist(height, bins = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
                         1.0, 1.1, 1.2, 1.3, 1.4,1.5, 1.6, 1.7, 1.8, 1.9, 2.0])

plt.title("histogram")
plt.show()

# tmp_lst = []
#
# for i in xrange(0,300,10):
#    tmp_lst.append(i/100.0)
#
# print tmp_lst