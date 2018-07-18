# -*- coding: utf-8 -*-
# @Time    : 18-7-12 下午8:16
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : learn_timestamp.py
# @Software: PyCharm Community Edition

import time

time_tup = time.localtime(time.time())
print time_tup

format_time='%Y-%m-%d_%a_%H-%M-%S'

cur_time = time.strftime(format_time, time_tup)
print "test" + cur_time