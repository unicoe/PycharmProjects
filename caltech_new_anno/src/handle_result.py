# -*- coding: utf-8 -*-
# @Time    : 18-6-6 下午8:03
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : handle_result.py
# @Software: PyCharm Community Edition

rf = open("/home/user/PycharmProjects/handle_result/result_detection/tmp_det_test_upper.txt")
wf = open("/home/user/PycharmProjects/caltech_new_anno/result/handle_0.01_6_6_det_test_upper2.txt","w")

content = rf.readline()


while content:

    info = content.strip("\n").split(" ")
    if (float(info[1])-0.01) < 0:
        content = rf.readline()
        continue

    for idx in info:
        wf.write(str(idx))
        wf.write(" ")
    wf.write("\n")
    content = rf.readline()
