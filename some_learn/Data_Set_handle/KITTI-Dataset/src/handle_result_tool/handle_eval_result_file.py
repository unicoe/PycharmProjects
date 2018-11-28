# -*- coding: utf-8 -*-
# @Time    : 18-11-1 上午10:11
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : handle_result_file.py
# @Software: PyCharm Community Edition

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/det_result/src/result.txt", "r")

content = rf.readline()

cnt = 1
while content:
    if cnt % 2 == 0:
        print "'" + content.strip("\n") + "',            0, clrs(" +str(cnt)+ ",:),  '--'"
    else:
        print "'" + content.strip("\n") + "',            0, clrs(" + str(cnt) + ",:),  '-'"
    cnt = cnt + 1
    content = rf.readline()