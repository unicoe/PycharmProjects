# -*- coding: utf-8 -*-
# @Time    : 18-7-2 上午10:30
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : put_in_set.py
# @Software: PyCharm Community Edition

rf = open("/home/user/PycharmProjects/search_same_pictures/result.txt")

content = rf.readline()

ls = []

while content:
    ls.append(content)

    content = rf.readline()

res_set = set(ls)

wf = open("/home/user/PycharmProjects/search_same_pictures/set_res.txt", "w")

for idx in res_set:
    wf.write(idx)
wf.close()