# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午9:21
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : source2target.py
# @Software: PyCharm
import copy
import numpy as np

# save img_shape to dict
def get_shape_dict():
    test_shape = open("/home/user/PycharmProjects/some_learn/Data_Set_handle"
              "/INRIA-Dataset/lst/test_img_shape.txt", "r")

    shape_dict = {}
    content = test_shape.readline()
    while content:


        im_info = content.strip("\n").split(" ")
        shape_dict[im_info[0]] = [int(im_info[1]), int(im_info[2])]           # h w

        content = test_shape.readline()

    return shape_dict

def get_source_dict(source_path):

    source_det = open(source_path, "r")

    content = source_det.readline()
    det_dict = {}
    while content:
        """
        set01_V000_I00280 0.266 256.2 84.5 394.1 417.3
        set01_V000_I00280 0.155 350.9 101.6 442.1 375.4
        
        0 set01_V000_I00280
        1 0.155
        2 3 4 5 bbox
        """
        det_info = content.strip("\n").split(" ")

        im_name = det_info[0]
        det_lst = []
        for idx in xrange(1,6):
            det_lst.append(float(det_info[idx]))

        if im_name in det_dict:
            det_dict[im_name].append(copy.copy(det_lst))
            pass
        else:

            det_dict[im_name] = [copy.copy(det_lst)]

        content = source_det.readline()
    return det_dict



def handle_det(det_dict):

    for im_idx in det_dict:
            im_w = 1242
            im_h = 375

            r1 = 2112.0 / im_w
            r2 = 640.0 / im_h

            for bbox_item in det_dict[im_idx]:
                x1 = bbox_item[1]
                y1 = bbox_item[2]
                x2 = bbox_item[3]
                y2 = bbox_item[4]

                t_x1 = x1 / r1
                t_y1 = y1 / r2

                t_x2 = x2 / r1
                t_y2 = y2 / r2

                bbox_item[1] = t_x1
                bbox_item[2] = t_y1
                bbox_item[3] = t_x2
                bbox_item[4] = t_y2
    return det_dict

def save_target(det_dict):

    save_name = "handle_" + target_idx.split("/")[-1]
    target_file = "/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/det_result/det/" + save_name

    save_target = open(target_file, "w")

    for im_idx in det_dict:
        for bbox_idx in det_dict[im_idx]:
            save_target.write(im_idx)
            for xy_i in bbox_idx:
                save_target.write(" ")
                save_target.write(str(round(xy_i,4)))

            save_target.write("\n")
    save_target.close()


target_lst = [

"/home/user/Disk1.8T/KITTI-experiments/det_result/1/2018_11_18_Sun_08_50_30_det_test_person.txt"

]

for target_idx in target_lst:

    source_dict = get_source_dict(target_idx)
    det_dict = handle_det(det_dict=source_dict)
    save_target(det_dict)
