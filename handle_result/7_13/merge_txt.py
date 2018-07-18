# -*- coding: utf-8 -*-
# @Time    : 18-6-18 下午4:12
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : merge_txt.py
# @Software: PyCharm Community Edition


rf = open("/home/user/PycharmProjects/handle_result/7_12/result/handle_7_12_det_test_head.txt")
wf = open("/home/user/PycharmProjects/handle_result/7_12/result/merge_result_7_12_det_test_person.txt","a+")

content = rf.readline()

while content:

    info = content.strip("\n").split(" ")

    for idx in info:
        wf.write(str(idx))
        wf.write(" ")
    wf.write("\n")
    content = rf.readline()

print "merge done~"