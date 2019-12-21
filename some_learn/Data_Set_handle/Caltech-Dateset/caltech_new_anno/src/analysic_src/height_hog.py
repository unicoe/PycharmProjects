# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午6:57
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : height_hog.py
# @Software: PyCharm


from matplotlib import pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import FuncFormatter

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/caltech_new_anno/src/analysic_src/h_info.txt", "r")

h_lst = []

content = rf.readline()

while content:
    tmp_h = int(content)
    h_lst.append(tmp_h)
    content = rf.readline()

height = np.array(h_lst)

plt.hist(height, bins = [0, 50, 100,
                          150,
                          200,
                          250,
                          300,
                          350,
                          400,
                          450,],normed=True,color='#1E90FF')
font = FontProperties(fname=r"/home/user/PycharmProjects/SIMSUN.TTC", size=20)
plt.title(u"Caltech行人数据集", fontproperties=font)


def to_percent(temp, position):
    # print temp/len(h_lst)
    return '%1.0f' % (5000*temp) + '%'


plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.xlabel(u"行人的高度" , fontproperties=font)
plt.ylabel(u"行人数量百分比" , fontproperties=font)
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