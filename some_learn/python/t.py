# -*- coding: utf-8 -*-
# @Time    : 19-3-6 下午3:59
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : t.py
# @Software: PyCharm

ls = [0,1,2,3,4,5,6,7,8,9]

for k in enumerate(ls[1::2], 2):
    print(k)


import time


fmt='%Y_%m_%d_%a_%H_%M_%S'
Date=time.strftime(fmt,time.localtime(time.time()))
print('获取当前的时间：',Date)