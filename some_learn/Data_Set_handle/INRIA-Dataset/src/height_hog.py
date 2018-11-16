# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午6:57
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : height_hog.py
# @Software: PyCharm


from matplotlib import pyplot as plt
import numpy as np

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/h_lst.txt", "r")

h_lst = []

content = rf.readline()

while content:
    tmp_h = int(content)
    h_lst.append(tmp_h)
    content = rf.readline()

height = np.array(h_lst)

plt.hist(height, bins = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440,
            460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900])

plt.title("histogram")
plt.show()


"""
55 - 700
"""

# tmp_lst = []
#
# for i in xrange(0,920,20):
#    tmp_lst.append(i)
#
# print tmp_lst