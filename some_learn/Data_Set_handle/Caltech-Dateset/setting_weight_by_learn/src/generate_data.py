# -*- coding: utf-8 -*-
# @Time    : 18-8-12 下午4:25
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : generate_data.py
# @Software: PyCharm Community Edition

import mxnet
from mxnet import ndarray as nd

def linreg(X1,X2,w1,w2,b1):
    # print X1, X2, w1, w2, b1
    #
    # print "nd.dot output : "
    # print  w1*X1 + w2*X2 + b1
    return w1*X1 + w2*X2 + b1


features1 = []
features2 = []

rf1 = open("/home/user/PycharmProjects/setting_weight_by_learn/basic_data/1_withgt_head.txt")
content1 = rf1.readline().strip("\n")
while content1:
    str1 = content1.split(" ")
    tmp1  = map(eval, str1[:])
    features1.append(tmp1)
    content1 = rf1.readline().strip("\n")

rf2 = open("/home/user/PycharmProjects/setting_weight_by_learn/basic_data/1_withgt_person.txt")
content2 = rf2.readline().strip("\n")
while content2:
    str2 = content2.split(" ")
    tmp2 = map(eval, str2[:])
    features2.append(tmp2)
    content2 = rf2.readline().strip("\n")

data1 = nd.array(features1)
data2 = nd.array(features2)

wf = open("/home/user/PycharmProjects/setting_weight_by_learn/basic_data/generate_data.txt", "w")

res = linreg(data1, data2, 0.5731586, 0.42243934, 0.00054808)

ans = res.asnumpy()

for i in ans:

    wf.write(str(i[0]))
    wf.write(" ")

    wf.write(str(i[1]))
    wf.write(" ")

    wf.write(str(i[2]))
    wf.write(" ")

    wf.write(str(i[3]))
    wf.write("\n")

