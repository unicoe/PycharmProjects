# -*- coding: utf-8 -*-
# @Time    : 19-1-3 上午10:34
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : comput_mean.py
# @Software: PyCharm

import os
import cv2
import numpy as np

path = '/home/user/Disk1.8T/data_set/citypersons/JPEGImages'


def compute(path):
    file_names = os.listdir(path)
    per_image_Rmean = []
    per_image_Gmean = []
    per_image_Bmean = []
    for file_name in file_names:
        img = cv2.imread(os.path.join(path, file_name), 1)
        per_image_Bmean.append(np.mean(img[:, :, 0]))
        per_image_Gmean.append(np.mean(img[:, :, 1]))
        per_image_Rmean.append(np.mean(img[:, :, 2]))
    R_mean = np.mean(per_image_Rmean)
    G_mean = np.mean(per_image_Gmean)
    B_mean = np.mean(per_image_Bmean)
    return R_mean, G_mean, B_mean


if __name__ == '__main__':
    R, G, B = compute(path)
    print(R, G, B)


"""
caltech img rgb mean

[106.6, 110.3, 107.7]
"""