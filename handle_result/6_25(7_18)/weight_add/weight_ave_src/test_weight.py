# -*- coding: utf-8 -*-
# @Time    : 18-7-18 下午4:49
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : test_weight.py
# @Software: PyCharm Community Edition

import numpy as np

l1 = [255.7, 180.5, 273.5, 221.2]
l2 = [256.0, 184.9, 268.3, 210.9]

np_l1 = np.array(l1)
np_l2 = np.array(l2)

np_l1 = np_l1*0.6
np_l2 = np_l2*0.4

np_res = np_l1 + np_l2

print l1
print l2
print np_res

def compute_IoU(l1, l2):
    '''
    #the coordinate of this funcation is (x1,y1,x2,y2)
    :param l1: first rectangle coordinate 
    :param l2: second rectangle coordinate
    :return: yes or no IoU > 0.5(or x) 
    '''

    if(l1[0] > l2[0] + abs(l2[2]-l2[0])):
        return False
    if(l1[1] > l2[1] + abs(l2[3]-l2[1])):
        return False
    if(l1[0] + l1[2]-l1[0] < l2[0]):
        return False
    if(l1[1] + l1[3]-l1[1] < l2[1]):
        return False

    colInt = min(l1[0]+l1[2]-l1[0] , l2[0]+l2[2]-l2[0]) - max(l1[0], l2[0])
    rowInt = min(l1[1]+l1[3]-l1[1] , l2[1]+l2[3]-l2[1]) - max(l1[1], l2[1])

    intersection = colInt * rowInt
    area1 = (l1[2]-l1[0])*(l1[3]-l1[1])
    area2 = (l2[2]-l2[0])*(l2[3]-l2[1])

    intersectionPercent = intersection/(area1+area2-intersection + 0.0)
    print "IoU = " + str(intersectionPercent)
    print l1,l2
    return intersectionPercent

compute_IoU(np_res.tolist(), l1)
compute_IoU(np_res.tolist(), l2)


"""
numpy 真好用
"""