# -*- coding: utf-8 -*-
# @Time    : 19-1-3 上午10:34
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : comput_mean.py
# @Software: PyCharm

import os
import cv2
import numpy as np

path = '/home/user/Disk1.8T/unicoe/pytorch-ssd-2/data/VOCdevkit/VOC0712/JPEGImages'


def compute(path):
    folder_names = os.listdir(path)
    per_image_Rmean = []
    per_image_Gmean = []
    per_image_Bmean = []
    for folder_name in folder_names:
        tmp_path = os.path.join(path, folder_name)
        file_names = os.listdir(tmp_path)
        for file_name in file_names:
            img = cv2.imread(os.path.join(tmp_path, file_name), 1)
            if img is not None:
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


citypersons
(72.43274907550811, 82.28064993314743, 71.83090366239547)
"""