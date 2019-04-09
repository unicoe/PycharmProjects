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
        folder_path = "/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/mscnn/ImageSets/train.txt"
    elif lst_name == "val":
        folder_path = "/home/user/PycharmProjects/some_learn/Data_Set_handle/kITTI-Dataset/mscnn/ImageSets/val.txt"
    im_lst = []

    rf = open(folder_path, "r")

    content = rf.readline()

    while content:
        im_lst.append(content.strip("\n"))
        content = rf.readline()

    return im_lst

def get_bboxlist(rootpath,imagelist):
    cnt = 0
    wf_info = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/lst/gt_info_20_19_1_16.txt", "w")


    train_lst = get_im_lst("train")

    rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/lst/img_shape.txt", "r")
    shape_dict = {}
    content = rf.readline()
    while content:
        im_info = content.strip("\n").split(" ")
        shape_dict[im_info[0]] = [int(im_info[1]), int(im_info[2])]  # h w
        content = rf.readline()


    for file_idx in imagelist:
        filename = rootpath + file_idx + ".txt"
        if os.path.exists(filename):
            with open(filename) as fi:
                label_data = fi.readlines()

            if file_idx in train_lst:

                img_h = shape_dict[file_idx][0]
                img_w = shape_dict[file_idx][1]

                wf_info.write(str(file_idx))
                wf_info.write(" ")
                for l in label_data:
                    data = l.split()
                    if (data[0] in ['Pedestrian']) and (float(data[1]) <= 0.3) and (data[2] in ['0', '1']):
                        #if data[2] in ['0', '1']:
                        xmin = str(max(0, int(float(data[4]))))
                        ymin = str(max(0, int(float(data[5]))))
                        xmax = str(min(int(float(data[6])), img_w))
                        ymax = str(min(int(float(data[7])), img_h))
                        w = int(xmax) - int(xmin)
                        h = int(ymax) - int(ymin)

                        if (int(xmin) < 0) or (int(xmax) < 0) or (int(ymin) < 0) or (int(ymax) < 0):
                            print xmin
                            print ymin
                            print xmax
                            print ymax

                        if ((int(ymax) - int(ymin)) < 0) or ((int(xmax) - int(xmin)) < 0):
                            print xmin
                            print ymin
                            print xmax
                            print ymax

                        float(data[7])
                        if h >= 20:

                            bbox_info = str(float(data[4])) + "," + str(float(data[5])) + "," + str(float(data[6])) + "," + str(float(data[7]))
                            # bbox_info = [float(data[4]),float(data[5]),float(data[6]),float(data[7])]
                            wf_info.write(bbox_info)
                            wf_info.write(" ")
                            cnt = cnt + 1

                wf_info.write("\n")
    wf_info.close()
    print "write done!"
    print cnt

IMAGE_DIR = '/home/user/Disk1.8T/data_set/KITTI/training/image_2/'
LABEL_DIR = '/home/user/Disk1.8T/data_set/KITTI/training/label_2/'

imagelist = get_filelist(IMAGE_DIR, '.png')
bboxlist  = get_bboxlist(LABEL_DIR, imagelist)