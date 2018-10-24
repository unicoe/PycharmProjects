# -*- coding: utf-8 -*-
# @Time    : 18-7-2 上午10:34
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : img_show.py
# @Software: PyCharm Community Edition
import cv2
from matplotlib import pyplot as plt


r_name = open("/home/user/PycharmProjects/search_same_pictures/set_res.txt")

im_name = r_name.readline()

while im_name:
    im_name = im_name.strip('\n')
    im = cv2.imread(im_name,0)
    plt.imshow(im, cmap='gray', interpolation='bicubic')
    plt.show()
    im_name = r_name.readline()