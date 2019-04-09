# -*- coding: utf-8 -*-
# @Time    : 18-7-1 下午8:29
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : show_pkl.py
# @Software: PyCharm Community Edition

import cPickle as pickle
f = open('/home/user/PycharmProjects/some_learn/Data_Set_handle/tool/check_pkl/res/train')
info = pickle.load(f)

wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/tool/check_pkl/res/pkl_4_9.txt", "w")
print len(info) # 4250, train1x

for idx in info:
    wf.write(str(idx))
    wf.write('\n')
wf.close()