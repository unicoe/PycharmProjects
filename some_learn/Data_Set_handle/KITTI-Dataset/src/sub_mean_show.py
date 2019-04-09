# -*- coding: utf-8 -*-
# @Time    : 19-1-3 上午10:34
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : comput_mean.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:43:29 2018
@author: Administrator
"""

import os
import cv2
import numpy as np

path = '/home/user/Disk1.8T/data_set/KITTI/training/image_2'


def compute(path):
    file_names = os.listdir(path)
    for file_name in file_names:
        img = cv2.imread(os.path.join(path, file_name), 1)
        img = img.astype(np.float32)
        img -= [93.8330908166208, 98.76049671976706, 95.8773930539917]
        # img -= [104,117,123]
        cv2.imshow("img", img)
        cv2.waitKey(0)


if __name__ == '__main__':
    R, G, B = compute(path)
    print(R, G, B)
