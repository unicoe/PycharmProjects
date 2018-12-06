# -*- coding: utf-8 -*-
# @Time    : 18-11-6 下午10:32
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : crop_img.py
# @Software: PyCharm

import cv2
import argparse


# 加载图像并显示
image = cv2.imread("/home/user/PycharmProjects/some_learn/CityPersons_handle/crop_img/bremen_000103_000019_leftImg8bit.png")
# cv2.imshow("Original", image)

print image.shape


img_part = image[0:1024,1024:2048]
# cv2.imshow("img_part", img_part)

cv2.imwrite("/home/user/PycharmProjects/some_learn/CityPersons_handle/crop_img/crop_img1.png", img_part)


