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

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + 'ok')
        return True
    else:
        print(path + 'failed!')
        return False

img_fold = "/home/user/Disk1.8T/draw_result/paper_result/mot_select/SSD_SEG_VIS/MOT17-01"

img_list = os.listdir(img_fold)

num_imgs = min(1000000, len(img_list))

for n in range(num_imgs):
    name = img_list[n]
    path = os.path.join(img_fold, name)
    save_path = "/home/user/Disk1.8T/draw_result/paper_result/mot_select/crop/SSD_SEG_VIS/MOT17-01/"
    mkdir(save_path)
    path1 = os.path.join(save_path, name)
    if os.path.isfile(path):

        im = cv2.imread(path)

        # show = True
        # if show:
        #     plt.imshow(im)
        #     plt.show()
        #
        # import pdb
        # pdb.set_trace()
        rect = np.array([int(97-25), int(123-25), int(750), int(475+25)])

        # calculate IoU (jaccard overlap) b/t the cropped and gt boxes

        # cut the crop from the image
        im = im[rect[1]:rect[3], rect[0]:rect[2],:]

        show = False
        if show:
            plt.imshow(im)
            plt.show()


        # save img
        cv2.imwrite(path1, im)