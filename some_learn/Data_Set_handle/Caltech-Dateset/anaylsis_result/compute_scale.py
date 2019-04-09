# -*- coding: utf-8 -*-
# @Time    : 18-12-24 上午10:54
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : compute_scale.py
# @Software: PyCharm

min_s = 25
max_s = 400

ran = max_s - min_s

step = ran/6.0

print(step)

for i in range(25,450, int(step)):
    print i