# -*- coding: utf-8 -*-
# @Time    : 18-12-7 下午4:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : mov_img2target.py
# @Software: PyCharm

import shutil

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok.'
        return True
    else:

        print path + ' path already exits.'
        return False


def get_im_ls():

    im_ls_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/kitti_visual/dif_ls/dif_ls.txt","r")
    im_ls = []
    im_name = im_ls_r.readline()

    while im_name:
        im_tmp = im_name.strip("\n")
        im_ls.append(im_tmp)
        im_name = im_ls_r.readline()
    return im_ls


source_path = "/home/user/Disk1.8T/draw_result/paper_result/cv/adapted_R-FCN/VOC0712/JPEGImages/"
dest_path = "/home/user/Disk1.8T/draw_result/paper_result/cv/adapted_R-FCN/dif/"
mkdir(dest_path)
im_ls = get_im_ls()

for i_im in im_ls:
    source_file = source_path + i_im
    shutil.copy(source_file, dest_path)