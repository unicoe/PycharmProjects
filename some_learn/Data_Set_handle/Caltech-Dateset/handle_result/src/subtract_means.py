# -*- coding: utf-8 -*-
# @Time    : 19-1-3 上午10:23
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : subtract_means.py
# @Software: PyCharm
import torch
from torchvision import transforms
import cv2
import numpy as np
import types
from numpy import random


class SubtractMeans(object):
    def __init__(self, mean):
        self.mean = np.array(mean, dtype=np.float32)

    def __call__(self, image, boxes=None, labels=None):
        image = image.astype(np.float32)
        image -= self.mean
        return image.astype(np.float32), boxes, labels


def sub_means():

    pass


img = cv2.imread("/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/test/caltech_learn_annoations/set06_V001_I00029.jpg")
# cv2.imshow("img",img)
# cv2.waitKey (0)
img = img.astype(np.float32)

mean = img.mean()
print mean
# cv2.imshow("img",img)
# cv2.waitKey (0)

#img -= [104,117,123]
img -= [106.6, 110.3, 107.7]

cv2.imshow("img",img)
cv2.waitKey (0)
# print(1)

