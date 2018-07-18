# -*- coding: utf-8 -*-
# @Time    : 18-6-19 下午8:47
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : test_random.py
# @Software: PyCharm Community Edition

import random
import time

random.seed(time.time())

cnt1 = 0
cnt2 = 0
i = 10000000
while i:
    if random.random() >= 0.7:
        cnt1 += 1
    else:
        cnt2 += 1
    i -= 1

print cnt1,cnt2

#test

"""
/home/user/anaconda2/bin/python /home/user/PycharmProjects/handle_result/union_iou/test_random.py
>0.5
4999990 5000010

事实证明，最后的结果不会相差很多，

>0.7
2998981 7001019
Process finished with exit code 0
"""