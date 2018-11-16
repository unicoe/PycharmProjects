# -*- coding: utf-8 -*-
# @Time    : 18-10-21 下午8:59
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : read_kitti.py
# @Software: PyCharm Community Edition

import os
import numpy as np

# 获取指定后缀名的文件列表
def get_filelist(path,ext):
    filelist_temp  = os.listdir(path)
    filelist = []
    # 通过比较后缀，选中所有TXT标注文件
    for i in filelist_temp:
        if os.path.splitext(i)[1] == ext:
            filelist.append(os.path.splitext(i)[0])
    return filelist

# 批量获取标注文件的bounding box信息


def get_im_lst(lst_name):
    if lst_name == 'train':
        folder_path = "/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI_handle/mscnn/ImageSets/train.txt"
    elif lst_name == "val":
        folder_path = "/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI_handle/mscnn/ImageSets/val.txt"
    im_lst = []

    rf = open(folder_path, "r")

    content = rf.readline()

    while content:
        im_lst.append(content.strip("\n"))
        content = rf.readline()

    return im_lst

def get_bboxlist(rootpath,imagelist):
    cnt = 0
    wf_info = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI_handle/11_16.txt", "w")

    train_lst = get_im_lst("train")

    for file_idx in imagelist:
        filename = rootpath + file_idx + ".txt"
        if os.path.exists(filename):
            with open(filename) as fi:
                label_data = fi.readlines()

            if file_idx in train_lst:
                wf_info.write(str(file_idx))
                wf_info.write(",")
                for l in label_data:
                    data = l.split()

                    if data[0] in ['Pedestrian']:
                        #if data[2] in ['0', '1']:
                        if float(data[1]) <= 0.3 and data[2] in ['0', '1']:
                            if float(data[7]) > 40:
                                bbox_info = str(float(data[4])) + " " + str(float(data[5])) + " " + str(float(data[6])) + " " + str(float(data[7]))
                                # bbox_info = [float(data[4]),float(data[5]),float(data[6]),float(data[7])]
                                wf_info.write(bbox_info)
                                wf_info.write(",")
                                cnt = cnt + 1

                wf_info.write("\n")
    wf_info.close()
    print "write done!"
    print cnt
