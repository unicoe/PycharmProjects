# -*- coding: utf-8 -*-
# @Time    : 18-12-17 下午10:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : crop_im.py
# @Software: PyCharm

import os
import cv2
from matplotlib import  pyplot as plt
import  numpy as np

img_fold = "/home/user/Disk1.8T/draw_result/paper_result/select/2019_06_19_Wed_11_43_49/VOC0712/JPEGImages"

img_list = os.listdir(img_fold)

num_imgs = min(1000000, len(img_list))

for n in range(num_imgs):
    name = img_list[n]
    path = os.path.join(img_fold, name)
    path1 = os.path.join("/home/user/Disk1.8T/draw_result/paper_result/select/2019_06_19_Wed_11_43_49/VOC0712/JPEGImages1", name)
    if os.path.isfile(path):

        im = cv2.imread(path)

        # plt.imshow(im)
        # plt.show()

        rect = np.array([int(101), int(70), int(716), int(527)])

        # calculate IoU (jaccard overlap) b/t the cropped and gt boxes

        # cut the crop from the image
        im = im[rect[1]:rect[3], rect[0]:rect[2],:]

        show = False
        if show:
            plt.imshow(im)
            plt.show()


        # save img
        cv2.imwrite(path1, im)