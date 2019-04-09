# -*- coding: utf-8 -*-
# @Time    : 19-1-3 上午10:34
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : comput_mean.py
# @Software: PyCharm

import os
import cv2
import numpy as np

path = '/home/user/Disk1.8T/data_set/KITTI/training/image_2'


def compute_rgb_mean(path):            #含子文件夹
    per_image_Rmean = []
    per_image_Gmean = []
    per_image_Bmean = []
    for (root, dirs, files) in os.walk(path):
        for file_name in files:
            print(os.path.join(root,file_name))
            img = cv2.imread(os.path.join(root, file_name), 1)
            per_image_Bmean.append(np.mean(img[:, :, 0]))
            per_image_Gmean.append(np.mean(img[:, :, 1]))
            per_image_Rmean.append(np.mean(img[:, :, 2]))
    R_mean = np.mean(per_image_Rmean)
    G_mean = np.mean(per_image_Gmean)
    B_mean = np.mean(per_image_Bmean)
    return R_mean, G_mean, B_mean


if __name__ == '__main__':
    R, G, B = compute_rgb_mean(path)
    print(R, G, B)


"""
kitti

rgb mean

(93.8330908166208, 98.76049671976706, 95.8773930539917)
"""