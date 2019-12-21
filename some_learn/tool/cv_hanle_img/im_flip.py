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

img_fold = "/home/user/Disk1.8T/unicoe/pytorch-ssd-2-4/data/VOCdevkit/VOC0712/SegmentationClass_weak/MOT17-13"

img_list = os.listdir(img_fold)

num_imgs = min(1000000, len(img_list))

for n in range(num_imgs):
    name = img_list[n]
    path = os.path.join(img_fold, name)
    save_path = "/home/user/Disk1.8T/unicoe/pytorch-ssd-2-4/data/VOCdevkit/VOC0712/SegmentationClass_weak/MOT17-13"
    mkdir(save_path)
    path1 = os.path.join(save_path, name)
    if os.path.isfile(path):

        print(path)
        im_name_tmp = path[79:79+15]
        #'/home/user/Disk1.8T/unicoe/pytorch-fcn/data/VOC/VOCdevkit/VOC2012/JPEGImages__/MOT17-01/000226.jpg'
        # im_ls = [
        #     'MOT17-01/000014',
        #     'MOT17-01/000034',
        #     'MOT17-01/000046',
        #     'MOT17-01/000057',
        #     'MOT17-01/000120',
        #     'MOT17-01/000148',
        #     'MOT17-01/000226',
        #     'MOT17-01/000402',
        #     'MOT17-01/000425',
        #     'MOT17-01/000430',
        #     'MOT17-03/000171',
        #     'MOT17-03/000179',
        #     'MOT17-03/000270',
        #     'MOT17-03/000302',
        #     'MOT17-03/000363',
        #     'MOT17-03/000432',
        #     'MOT17-03/000437',
        #     'MOT17-03/000451',
        #     'MOT17-03/000557',
        #     'MOT17-03/000574',
        #     'MOT17-06/000006',
        #     'MOT17-06/000031',
        #     'MOT17-06/000266',
        #     'MOT17-06/000381',
        #     'MOT17-06/000478',
        #     'MOT17-06/000669',
        #     'MOT17-06/000869',
        #     'MOT17-06/000989',
        #     'MOT17-06/001063',
        #     'MOT17-06/001102',
        #     'MOT17-07/000072',
        #     'MOT17-07/000100',
        #     'MOT17-07/000105',
        #     'MOT17-07/000146',
        #     'MOT17-07/000156',
        #     'MOT17-07/000184',
        #     'MOT17-07/000212',
        #     'MOT17-07/000385',
        #     'MOT17-07/000394',
        #     'MOT17-07/000446',
        #     'MOT17-08/000171',
        #     'MOT17-08/000179',
        #     'MOT17-08/000270',
        #     'MOT17-08/000302',
        #     'MOT17-08/000432',
        #     'MOT17-08/000437',
        #     'MOT17-08/000451',
        #     'MOT17-08/000557',
        #     'MOT17-08/000574',
        #     'MOT17-12/000014',
        #     'MOT17-12/000148',
        #     'MOT17-12/000226',
        #     'MOT17-12/000430',
        #     'MOT17-12/000548',
        #     'MOT17-12/000571',
        #     'MOT17-12/000729',
        #     'MOT17-12/000788',
        #     'MOT17-12/000831',
        #     'MOT17-12/000849',
        #     'MOT17-12/000883',
        #     'MOT17-14/000004',
        #     'MOT17-14/000177',
        #     'MOT17-14/000180',
        #     'MOT17-14/000199',
        #     'MOT17-14/000200',
        #     'MOT17-14/000439',
        #     'MOT17-14/000505',
        #     'MOT17-14/000523',
        #     'MOT17-14/000600',
        #     'MOT17-14/000709',
        # ]
        # if im_name_tmp in im_ls:
        im = cv2.imread(path)


        # show = True
        # if show:
        #     plt.imshow(im)
        #     plt.show()
        #
        # import pdb
        # pdb.set_trace()
        im = cv2.flip(im, 1)

        show = False
        if show:
            plt.imshow(im)
            plt.show()


        # save img
        cv2.imwrite(path1, im)