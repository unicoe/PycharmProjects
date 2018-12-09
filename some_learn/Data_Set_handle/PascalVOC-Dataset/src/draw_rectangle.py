# -*- coding: utf-8 -*-
# @Time    : 18-12-6 下午10:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : draw_rectangle.py
# @Software: PyCharm

import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8") #3

blue = (255, 0, 0) #18
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1) #19
cv2.imshow("Canvas", canvas) #20
cv2.waitKey(0) #21
