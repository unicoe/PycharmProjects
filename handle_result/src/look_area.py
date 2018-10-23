# -*- coding: utf-8 -*-
# @Time    : 18-10-18 上午10:40
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : look_area.py
# @Software: PyCharm Community Edition

import pdb
import matplotlib.pyplot as plt

rf = open("/home/user/PycharmProjects/handle_result/10_17/check_area.txt", 'r')

content = rf.readline()

scores = []
areas  = []

while content:
    res = content.strip('\n').split(' ')
    scores.append(float(res[0]))
    areas.append(float(res[1]))
    content = rf.readline()

    # pdb.set_trace()

plt.plot(areas, scores,  'ro')
plt.axis([0,10000,0,1.1])
plt.savefig("/home/user/PycharmProjects/handle_result/10_17/check_area_u.png")
plt.show()