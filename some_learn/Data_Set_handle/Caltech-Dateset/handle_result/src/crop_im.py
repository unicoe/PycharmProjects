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

img_fold = "/media/user/LOG/60"

img_list = os.listdir(img_fold)

num_imgs = min(1000000, len(img_list))

for n in range(num_imgs):
    name = img_list[n]
    path = os.path.join(img_fold, name)
    path1 = os.path.join("/media/user/LOG/601/", name)
    if os.path.isfile(path):

        im = cv2.imread(path)

        rect = np.array([int(82), int(60), int(574), int(426)])

        # calculate IoU (jaccard overlap) b/t the cropped and gt boxes

        # cut the crop from the image
        im = im[rect[1]:rect[3], rect[0]:rect[2],:]

        show = False
        if show:
            plt.imshow(im)
            plt.show()


        # save img
        cv2.imwrite(path1, im)