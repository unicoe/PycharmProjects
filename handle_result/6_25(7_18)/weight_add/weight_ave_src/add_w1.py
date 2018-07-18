# -*- coding: utf-8 -*-
# @Time    : 18-7-18 下午3:48
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : add_w1.py
# @Software: PyCharm Community Edition

import numpy as np

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
    #print l1,l2
    return intersectionPercent

DEBUG = True

def handle_weight1(info1, info2):
    """
    handle a pic's bboxes , add weight for detection result
    :param info1: scores bboxes list
    :param info2: scores bboxes list
    :return: 
    """
    np_info1 = np.array(info1)
    np_info2 = np.array(info2)
    vis1 = np.zeros(len(np_info1))
    vis2 = np.zeros(len(np_info2))

    for idx in range(len(np_info1)):
        for idx2 in range(len(np_info2)):

            tmp_bbox1  = np_info1[idx][1:5]
            tmp_bbox2  = np_info2[idx2][1:5]
            tmp_score1 = np_info1[idx][0:1]
            tmp_score2 = np_info2[idx2][0:1]

            if compute_IoU(tmp_bbox1.tolist(), tmp_bbox2.tolist()) > 0.3:
                if vis1[idx] != 1 and vis2[idx2] != 1:
                    res_bbox = tmp_bbox1 * 0.6 + tmp_bbox2 * 0.4
                    res_scores = tmp_score1 * 0.6 + tmp_score2 * 0.4

                    vis1[idx] = 1
                    vis2[idx2] = 1

    if DEBUG:
        print vis1
        print vis2

    for idx in range(len(np_info1)):
        if vis1[idx] == 0:
            print np_info1[idx]
    for idx2 in range(len(np_info2)):
        if vis2[idx2] == 0:
            print np_info2[idx2]



"""
[[0.212, 122.3, 185.3, 147.3, 226.8], [0.005, 409.2, 179.7, 436.0, 235.5], [0.002, 255.7, 180.5, 273.5, 221.2], [0.001, 316.0, 175.6, 335.4, 206.3]]
[[0.065, 230.8, 178.8, 245.3, 212.228571429], [0.038, 222.6, 179.3, 237.1, 210.157142857], [0.015, 215.2, 179.4, 229.4, 208.828571429], [0.013, 168.2, 178.4, 182.2, 209.257142857], [0.003, 237.7, 184.8, 250.9, 212.514285714], [0.002, 246.3, 178.5, 260.1, 208.5], [0.001, 182.2, 177.5, 195.7, 208.071428571], [0.001, 462.9, 178.9, 476.1, 205.757142857], [0.0, 188.6, 177.7, 202.8, 209.985714286], [0.0, 163.5, 184.2, 174.7, 211.628571429], [0.0, 151.4, 199.0, 162.9, 225.0], [0.0, 197.8, 186.8, 210.7, 213.371428571], [0.0, 526.2, 170.1, 539.7, 198.385714286], [0.0, 470.6, 178.5, 484.2, 205.357142857], [0.0, 256.0, 184.9, 268.3, 210.9], [0.0, 454.1, 186.6, 468.0, 214.6], [0.0, 192.1, 198.7, 202.8, 222.128571429], [0.0, 447.1, 185.9, 460.3, 214.757142857], [0.0, 207.6, 186.8, 220.4, 212.228571429], [0.0, 263.4, 185.2, 276.0, 210.914285714]]
"""

info1 = [[0.212, 122.3, 185.3, 147.3, 226.8], [0.005, 409.2, 179.7, 436.0, 235.5], [0.002, 255.7, 180.5, 273.5, 221.2], [0.001, 316.0, 175.6, 335.4, 206.3]]
info2 = [[0.065, 230.8, 178.8, 245.3, 212.228571429], [0.038, 222.6, 179.3, 237.1, 210.157142857], [0.015, 215.2, 179.4, 229.4, 208.828571429], [0.013, 168.2, 178.4, 182.2, 209.257142857], [0.003, 237.7, 184.8, 250.9, 212.514285714], [0.002, 246.3, 178.5, 260.1, 208.5], [0.001, 182.2, 177.5, 195.7, 208.071428571], [0.001, 462.9, 178.9, 476.1, 205.757142857], [0.0, 188.6, 177.7, 202.8, 209.985714286], [0.0, 163.5, 184.2, 174.7, 211.628571429], [0.0, 151.4, 199.0, 162.9, 225.0], [0.0, 197.8, 186.8, 210.7, 213.371428571], [0.0, 526.2, 170.1, 539.7, 198.385714286], [0.0, 470.6, 178.5, 484.2, 205.357142857], [0.0, 256.0, 184.9, 268.3, 210.9], [0.0, 454.1, 186.6, 468.0, 214.6], [0.0, 192.1, 198.7, 202.8, 222.128571429], [0.0, 447.1, 185.9, 460.3, 214.757142857], [0.0, 207.6, 186.8, 220.4, 212.228571429], [0.0, 263.4, 185.2, 276.0, 210.914285714]]

handle_weight1(info1, info2)