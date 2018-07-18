# -*- coding: utf-8 -*-
# @Time    : 18-6-6 下午8:03
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : handle_result.py
# @Software: PyCharm Community Edition

rf = open("/home/user/PycharmProjects/handle_result/6_15/handle_result/nms_merge_det_result.txt")
wf = open("/home/user/PycharmProjects/handle_result/6_15/handle_result/6_15_0.01_nms_merge_det_result.txt","w")

content = rf.readline()

while content:

    info = content.strip("\n").split(" ")
    # if (float(info[5]) - float(info[3]) < 50):
    #     content = rf.readline()
    #     continue

    if (float(info[1])-0.01) < 0:
        content = rf.readline()
        continue

    for idx in info:
        wf.write(str(idx))
        wf.write(" ")
    wf.write("\n")
    content = rf.readline()
