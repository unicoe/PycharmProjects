# -*- coding: utf-8 -*-
# @Time    : 18-10-18 上午11:09
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : handle_py_result.py
# @Software: PyCharm Community Edition
import pdb
import matplotlib.pyplot as plt


rf = open("/home/user/PycharmProjects/handle_result/10_17/comp4_2336f4bc-b790-4a4c-8870-068fd783f067_det_test_person.txt", 'r')

content = rf.readline()


"""
set10/V007/60 0.012 3.7 177.0 32.9 238.1
set10/V007/60 0.001 11.2 171.7 25.3 209.6
"""

scores = []
areas  = []

while content:
    res = content.strip('\n').split(' ')

    for i in range(1,6):
        res[i] = float(res[i])

    score = res[1]
    area  = (res[5]-res[3]) * (res[4]-res[2])

    if score > 0.001:
        scores.append(score)
        areas.append(area)
    content = rf.readline()
    #pdb.set_trace()

plt.plot(areas, scores,  'ro')
plt.axis([0,30000,0,1.1])
plt.plot((650,650),(0,1),'g-')
plt.plot((4000,4000),(0,1),'g-')
plt.plot((8000,8000),(0,1),'g-')
plt.savefig("/home/user/PycharmProjects/handle_result/10_17/check_area_10_18_2336f4bc.png")
plt.show()