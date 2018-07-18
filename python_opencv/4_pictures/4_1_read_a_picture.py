# -*- coding: utf-8 -*-
# @Time    : 18-6-6 上午11:20
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : 4_1_read_a_picture.py
# @Software: PyCharm Community Edition

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/home/user/Pictures/python_opencv/1.jpeg",0)

#pre setting a window
#cv2.namedWindow("image", cv2.WINDOW_NORMAL)

#cv2.imshow('1.jpeg',img)
#cv2.imwrite("/home/user/Pictures/python_opencv/1.png",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# matplotlib

plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([]),plt.yticks([])
plt.show()