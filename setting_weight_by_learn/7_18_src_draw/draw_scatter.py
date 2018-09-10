# -*- coding: utf-8 -*-
# @Time    : 18-7-18 上午9:48
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : draw_scatter.py
# @Software: PyCharm Community Edition

import numpy as np
import matplotlib.pyplot as plt

rf = open("/home/user/PycharmProjects/handle_result/6_25/src_draw/score1.txt")

score = rf.readline()
scores1 = []
while score:

    scores1.append(float(score))
    if len(scores1) >= 12379:
        break
    score = rf.readline()

rf.close()


rf1 = open("/home/user/PycharmProjects/handle_result/6_25/src_draw/score2.txt")

score1 = rf1.readline()
scores2 = []
while score1:

    scores2.append(float(score1))

    score1 = rf1.readline()

rf1.close()


print scores1
print scores2



np_scores1 = np.array(scores1)
np_scores2 = np.array(scores2)

np_x1 = np.arange(0, len(scores1))
np_x2 = np.arange(0, len(scores2))


print type(np_scores1)
print type(np_scores2)


f1 = plt.figure()


plt.scatter(np_x1, np_scores1, alpha=0.6, marker='o')
plt.scatter(np_x2, np_scores2, alpha=0.6, marker='v')

plt.savefig("/home/user/PycharmProjects/handle_result/6_25/src_draw/1.png")

plt.show()