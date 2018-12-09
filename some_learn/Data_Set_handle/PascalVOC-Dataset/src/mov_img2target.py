# -*- coding: utf-8 -*-
# @Time    : 18-12-7 下午4:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : mov_img2target.py
# @Software: PyCharm

import shutil

def get_im_ls():

    im_ls_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/caltech1x_ls.txt","r")
    im_ls = []
    im_name = im_ls_r.readline()

    while im_name:
        im_tmp = im_name.strip("\n")
        im_ls.append(im_tmp)
        im_name = im_ls_r.readline()
    return im_ls


source_path = "/home/user/py-R-FCN/data/VOCdevkit0712/VOC0712/copy_img/"
dest_path = "/home/user/Disk1.8T/data_set/data/VOC/VOCdevkit/VOC2012/JPEGImages"

im_ls = get_im_ls()

for i_im in im_ls:
    source_file = source_path + i_im + ".jpg"
    shutil.copy(source_file, dest_path)