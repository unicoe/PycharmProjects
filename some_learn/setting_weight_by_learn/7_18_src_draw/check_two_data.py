# -*- coding: utf-8 -*-
# @Time    : 18-7-18 上午10:15
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : check_two_data.py
# @Software: PyCharm Community Edition



"""
检验两个分布是否服从同一分布
"""

from scipy.stats import ks_2samp,kstest

import numpy as np
import matplotlib.pyplot as plt


rf1 = open("/home/user/PycharmProjects/handle_result/6_25/src_draw/score2.txt")

score1 = rf1.readline()
scores2 = []
while score1:

    scores2.append(float(score1))


    score1 = rf1.readline()


rf1.close()

rf = open("/home/user/PycharmProjects/handle_result/6_25/src_draw/score1.txt")

score = rf.readline()
scores1 = []
while score:

    scores1.append(float(score))
    score = rf.readline()

rf.close()


print scores1
print scores2


np_scores1 = np.array(scores1)
np_scores2 = np.array(scores2)

np_scores3 = np.array(scores1[10000:30000])
np_scores4 = np.array(scores1[30000:50000])

np_scores5 = np.array(scores2[0:100])
np_scores6 = np.array(scores2[5000:10000])


print ks_2samp(np_scores3, np_scores4)

print ks_2samp(np_scores1, np_scores3)

print ks_2samp(np_scores5, np_scores6)

print ks_2samp(np_scores1, np_scores2)


"""
Ks_2sampResult(statistic=0.005850000000000022, pvalue=0.8826216559688129)
Ks_2sampResult(statistic=0.0049534829990675044, pvalue=0.8364873288349566)
Ks_2sampResult(statistic=0.023399999999999976, pvalue=0.12766930748504676)
Ks_2sampResult(statistic=0.16876255358455894, pvalue=2.8786687938174e-262)


pvalue > 0.05就认为，两个分布是同一分布

ks检验，证明 两个结果是不同的分布

但是，对于ks检验，我还不是很懂
"""