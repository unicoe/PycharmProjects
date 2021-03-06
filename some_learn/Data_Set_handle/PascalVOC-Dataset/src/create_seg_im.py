# -*- coding: utf-8 -*-
# @Time    : 18-12-6 下午9:55
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : create_seg_im.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import cv2

def get_im_ls():

    im_ls_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/caltech1x_ls.txt","r")
    im_ls = []
    im_name = im_ls_r.readline()

    while im_name:
        im_tmp = im_name.strip("\n")
        im_ls.append(im_tmp)
        im_name = im_ls_r.readline()
    return im_ls


def get_gt_info():
    gt_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/gt_info.txt", "r")
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

        img = cv2.imread("/home/user/Disk1.8T/data_set/seglabel_png/" + i_im + ".png")

        for i_bbox in gt_dict[i_im]:

            tmp = str2int(i_bbox)

            bbox_tmp.append(str2int(i_bbox))

            cv2.rectangle(img, (tmp[0],tmp[1]),(tmp[2],tmp[3]),(255,255,255),thickness=2)
            cv2.rectangle(img, (tmp[0]+1, tmp[1]+1), (tmp[2]-1, tmp[3]-1), (128, 128, 192), -1)

            # img = img[:,:,(2,1,0)]
            # debug 2018-12-06 22:12:56
            # plt.imshow(img)
            # plt.show()
        cv2.imwrite("/home/user/Disk1.8T/data_set/seglabel_png1/" + i_im + ".png", img)