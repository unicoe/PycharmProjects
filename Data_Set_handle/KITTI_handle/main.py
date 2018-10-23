# -*- coding: utf-8 -*-
# @Time    : 18-10-21 下午8:59
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : main.py
# @Software: PyCharm Community Edition

import read_kitti

IMAGE_DIR = '/home/user/Disk1.8T/data_set/training/image_2/'
LABEL_DIR = '/home/user/Disk1.8T/data_set/training/label_2/'

imagelist = read_kitti.get_filelist(IMAGE_DIR,'.png')
bboxlist  = read_kitti.get_bboxlist(LABEL_DIR,imagelist)


