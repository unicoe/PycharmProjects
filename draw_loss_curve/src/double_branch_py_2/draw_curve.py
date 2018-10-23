# -*- coding: utf-8 -*-
# @Time    : 18-6-20 下午3:48
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : draw_curve.py
# @Software: PyCharm Community Edition
"""
单分支 rpn loss

"""
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
train_all_loss_p2 = loadData_all_loss('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_all_loss_p2.txt')
train_accuracy_p2 = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_accuarcy_p2.txt')
train_loss_bbox_p2 = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_loss_bbox_p2.txt')
train_loss_cls_p2 = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_loss_cls_p2.txt')
train_rpn_cls_loss_p2 = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_rpn_cls_loss_p2.txt')
train_rpn_loss_bbox_p2 = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_rpn_loss_bbox_p2.txt')

# panads Series
draw_train_all_loss_p2 = pd.Series(train_all_loss_p2, index = range(0,len(train_all_loss_p2),1))
draw_train_accuracy_p2 = pd.Series(train_accuracy_p2, index = range(0,len(train_accuracy_p2),1))
draw_train_loss_bbox_p2 = pd.Series(train_loss_bbox_p2, index = range(0,len(train_loss_bbox_p2),1))
draw_train_loss_cls_p2 = pd.Series(train_loss_cls_p2, index = range(0,len(train_loss_cls_p2),1))
draw_train_rpn_cls_loss_p2 = pd.Series(train_rpn_cls_loss_p2, index = range(0,len(train_rpn_cls_loss_p2),1))
draw_train_rpn_loss_bbox_p2 = pd.Series(train_rpn_loss_bbox_p2, index = range(0,len(train_rpn_loss_bbox_p2),1))

#draw
fig = plt.figure()
w = 16
h = 10
fig.set_size_inches(w,h)

plt.subplot(231)
plt.plot(draw_train_all_loss_p2,'r')
plt.title(u"all loss")
#plt.legend((u'accuracy'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"loss")
# plt.show()

plt.subplot(232)
plt.plot(draw_train_accuracy_p2, 'g')
plt.title(u"accuracy")
#plt.legend((u'accuracy'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"accuracy")
# plt.show()

plt.subplot(233)
plt.plot(draw_train_loss_bbox_p2)
plt.title(u"loss_bbox")
#plt.legend((u'loss_bbox'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"loss_bbox")
# plt.show()

plt.subplot(234)
plt.plot(draw_train_loss_cls_p2,'y')
plt.title(u"loss_cls")
#plt.legend((u'loss_cls'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"loss_cls")
# plt.show()

plt.subplot(235)
plt.plot(draw_train_rpn_cls_loss_p2,'m')
plt.title(u"rpn_cls_loss")
#plt.legend((u'rpn_cls_loss'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"rpn_cls_loss")
# plt.show()

plt.subplot(236)
plt.plot(draw_train_rpn_loss_bbox_p2, 'c')
plt.title(u"rpn_loss_bbox")
#plt.legend((u'rpn_loss_bbox'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"rpn_loss_bbox")

plt.savefig("/home/user/PycharmProjects/draw_loss_curve/img/10_18_11_p2.png")
#save format maybe : format="eps"  or "pdf"


plt.show()


"""
23X

表示将整体区域分成　２＊３个区域，ｘ表示这些区域里的第几个
"""


train_all_loss_p3 = loadData_all_loss('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_all_loss_p3.txt')
train_accuracy_p3 = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_accuarcy_p3.txt')
train_loss_bbox_p3 = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_loss_bbox_p3.txt')
train_loss_cls_p3 = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_loss_cls_p3.txt')
train_rpn_cls_loss_p3 = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_rpn_cls_loss_p3.txt')
train_rpn_loss_bbox_p3 = loadData('/home/user/PycharmProjects/draw_loss_curve/logs/10_18_1/train_rpn_loss_bbox_p3.txt')

# panads Series
draw_train_all_loss_p3 = pd.Series(train_all_loss_p3, index = range(0,len(train_all_loss_p3),1))
draw_train_accuracy_p3 = pd.Series(train_accuracy_p3, index = range(0,len(train_accuracy_p3),1))
draw_train_loss_bbox_p3 = pd.Series(train_loss_bbox_p3, index = range(0,len(train_loss_bbox_p3),1))
draw_train_loss_cls_p3 = pd.Series(train_loss_cls_p3, index = range(0,len(train_loss_cls_p3),1))
draw_train_rpn_cls_loss_p3 = pd.Series(train_rpn_cls_loss_p3, index = range(0,len(train_rpn_cls_loss_p3),1))
draw_train_rpn_loss_bbox_p3 = pd.Series(train_rpn_loss_bbox_p3, index = range(0,len(train_rpn_loss_bbox_p3),1))

#draw
fig = plt.figure()
w = 16
h = 10
fig.set_size_inches(w,h)

plt.subplot(231)
plt.axis([0,150,0,10])
plt.plot(draw_train_all_loss_p3,'r')
plt.title(u"all loss")
#plt.legend((u'accuracy'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"loss")
# plt.show()

plt.subplot(232)
plt.plot(draw_train_accuracy_p3, 'g')
plt.title(u"accuracy")
#plt.legend((u'accuracy'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"accuracy")
# plt.show()

plt.subplot(233)
plt.plot(draw_train_loss_bbox_p3)
plt.title(u"loss_bbox")
#plt.legend((u'loss_bbox'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"loss_bbox")
# plt.show()

plt.subplot(234)
plt.plot(draw_train_loss_cls_p3,'y')
plt.title(u"loss_cls")
#plt.legend((u'loss_cls'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"loss_cls")
# plt.show()

plt.subplot(235)
plt.plot(draw_train_rpn_cls_loss_p3,'m')
plt.title(u"rpn_cls_loss")
#plt.legend((u'rpn_cls_loss'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"rpn_cls_loss")
# plt.show()

plt.subplot(236)
plt.plot(draw_train_rpn_loss_bbox_p3, 'c')
plt.title(u"rpn_loss_bbox")
#plt.legend((u'rpn_loss_bbox'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"rpn_loss_bbox")

plt.savefig("/home/user/PycharmProjects/draw_loss_curve/img/10_18_11_p3.png")
#save format maybe : format="eps"  or "pdf"


plt.show()
