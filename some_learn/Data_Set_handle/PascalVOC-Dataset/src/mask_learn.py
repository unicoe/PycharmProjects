# -*- coding: utf-8 -*-
# @Time    : 18-12-6 下午7:38
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : mask_learn.py
# @Software: PyCharm

import PIL
import PIL.Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

img_file = "/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/mask_img/2007_000129.png"
img = PIL.Image.open(img_file)

print(img.mode)

img1 = img.convert("P")



img = np.array(img, dtype=np.int32)
img[img == 255] = -1

print(img)

img = cv2.imread(img_file)

img = img[:, :, (2, 1, 0)] # bgr2rgb

print img.shape



#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # cv2默认为BGR顺序,其他的一般都为RGB img = img[:, :, (2, 1, 0)]

plt.imshow(img1)

plt.show()

