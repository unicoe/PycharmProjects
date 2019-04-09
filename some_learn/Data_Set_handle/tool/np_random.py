# -*- coding: utf-8 -*-
# @Time    : 19-1-13 下午7:59
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : np_random.py
# @Software: PyCharm

from numpy import random

random.seed(5)
print random.randint(2)

w = random.uniform(0.3 * 640, 640)
h = random.uniform(0.3 * 480, 480)

print(w,h)