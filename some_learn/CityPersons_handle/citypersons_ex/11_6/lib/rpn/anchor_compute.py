# -*- coding: utf-8 -*-
# @Time    : 18-11-13 上午11:16
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : anchor_compute.py
# @Software: PyCharm

scale = [3.5, 4.41, 5.56, 7.0, 8.82, 11.12, 14.01, 17.65, 22.23, 28.02, 35.3]

# for i in range(len(scale)-1):
#     print scale[i+1] / scale[i]

base = 3.4

scale_lst = []

for i in range(11):
    scale_lst.append(round(base, 2))
    base = base * 1.25
    print round(base, 2)

print scale_lst
