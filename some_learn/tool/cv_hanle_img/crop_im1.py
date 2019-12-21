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

# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/2019_10_10_Thu_01_58_01",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/2019_06_20_Thu_00_14_46",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/2019_06_19_Wed_11_43_49",

img_fold = "/home/user/Disk1.8T/draw_result/paper_result/submit1/2019_10_10_Thu_01_58_01/VOC0712/JPEGImages"

img_list = os.listdir(img_fold)

num_imgs = min(1000000, len(img_list))

for n in range(num_imgs):
    name = img_list[n]
    path = os.path.join(img_fold, name)
    save_path = "/home/user/Disk1.8T/draw_result/paper_result/submit1/2019_10_10_Thu_01_58_01/VOC0712/JPEGImages"
    mkdir(save_path)
    path1 = os.path.join(save_path, name)
    if os.path.isfile(path):

        im = cv2.imread(path)

        # show = True
        # if show:
        #     plt.imshow(im)
        #     plt.show()
        # caltech
        rect = np.array([int(97), int(65), int(725), int(537)])

        # calculate IoU (jaccard overlap) b/t the cropped and gt boxes

        # cut the crop from the image
        im = im[rect[1]:rect[3], rect[0]:rect[2],:]

        show = False
        if show:
            plt.imshow(im)
            plt.show()


        # save img
        cv2.imwrite(path1, im)