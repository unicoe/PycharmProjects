# -*- coding: utf-8 -*-
# @Time    : 18-7-1 下午8:29
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : show_pkl.py
# @Software: PyCharm Community Edition

import cPickle as pickle
f = open('/home/user/PycharmProjects/check_pkl/res/voc_2007_trainval_gt_roidb.pkl')
info = pickle.load(f)

wf = open("/home/user/PycharmProjects/check_pkl/res/head_body_pkl.txt", "w")
print len(info) # 4250, train1x

for idx in info:
    wf.write(str(idx))
    wf.write('\n')
wf.close()