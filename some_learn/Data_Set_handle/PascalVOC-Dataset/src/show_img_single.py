# -*- coding: utf-8 -*-
# @Time    : 19-3-18 下午4:55
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : show_img.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 18-12-6 下午9:55
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : create_seg_im.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import PIL
from PIL import Image, ImageDraw
import scipy.misc as m

import cv2

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok'
        return True
    else:

        print path + 'failed!'
        return False

def get_im_ls():

    im_ls_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/person_1_5_vis0.3_h20_w10.txt","r")
    im_ls = []
    im_name = im_ls_r.readline()

    while im_name:
        im_tmp = im_name.strip("\n")
        im_ls.append(im_tmp)
        im_name = im_ls_r.readline()
    return im_ls


def get_gt_info():
    gt_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/gt_info_20_10_0.3_zss.txt", "r")
    gt_dict = {}
    gt_info = gt_r.readline()

    while gt_info:
        gt_info_tmp = gt_info.strip("\n").strip(" ").split(" ")
        if len(gt_info_tmp) > 1:
            gt_dict[gt_info_tmp[0]] = []
            for i in range(1,len(gt_info_tmp)):
                gt_dict[gt_info_tmp[0]].append(gt_info_tmp[i])

        gt_info = gt_r.readline()

    return gt_dict

def str2int(str):

    str_tmp = str.split(",")
    result_ls = []
    for i in str_tmp:
        result_ls.append(int(i))

    return result_ls

im_ls = get_im_ls()
gt_dict = get_gt_info()



for i_im in im_ls:
    bbox_tmp = []
    if i_im in gt_dict:

        #img = PIL.Image.new("P", (640, 480),color=0)
        #img = PIL.Image.open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/set00_V000_I00035.png")
        #img = m.imread("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/set00_V000_I00035.png")

        #img = img.convert("P")
        #print(img.mode)

        #img = cv2.imread("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/set00_V000_I00035.png")
        _seglbl_weak = "/home/user/Disk1.8T/data_set/seglabel_png_3_18_test/combime/"
        tmp_im = i_im + ".jpg"
        print(i_im)
        print(tmp_im)
        img = m.imread(_seglbl_weak + tmp_im)
        #img = PIL.Image.open("")

        plt.title(tmp_im)
        plt.imshow(img)

        plt.show()


