# -*- coding: utf-8 -*-
# @Time    : 18-6-20 下午3:48
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : draw_curve.py
# @Software: PyCharm Community Edition

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def loadData_all_loss(file):
    dataMat = []
    fr = open(file)
    for line in fr.readlines():
        lineA = line.strip("\n").split(" ")

        dataMat.append(float(lineA[3]))
    return dataMat

def loadData(file):
    dataMat = []
    fr = open(file)
    for line in fr.readlines():
        lineA = line.strip("\n").split(" ")

        dataMat.append(float(lineA[6]))
    return dataMat

#loda data
train_all_loss = loadData_all_loss('/home/user/PycharmProjects/draw_loss_curve/logs/ssd_5_11/train_all_loss.txt')
train_mbox_loss = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/ssd_5_11/train_mbox_loss.txt')


# panads Series
draw_train_all_loss = pd.Series(train_all_loss, index = range(0,len(train_all_loss),1))
draw_train_mbox_loss = pd.Series(train_mbox_loss, index = range(0,len(train_mbox_loss),1))

#draw
fig = plt.figure()
w = 16
h = 10
fig.set_size_inches(w,h)


plt.subplot(211)
plt.plot(draw_train_all_loss,'r')
plt.title(u"all loss")
#plt.legend((u'accuracy'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"loss")
# plt.show()

plt.subplot(212)
plt.plot(draw_train_mbox_loss)
plt.title(u"mbox_loss")
#plt.legend((u'mbox_loss'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"mbox_loss")
# plt.show()

plt.savefig("/home/user/PycharmProjects/draw_loss_curve/img/5_291.eps", format="eps")
plt.show()

"""
23X

表示将整体区域分成　２＊３个区域，ｘ表示这些区域里的第几个
"""
