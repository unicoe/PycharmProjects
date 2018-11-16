# -*- coding: utf-8 -*-
# @Time    : 18-6-11 下午8:59
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : new_Visualization_6_11.py
# @Software: PyCharm Community Edition

#--coding:utf-8--
import os
import cv2

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

def generate_result(resource_path):
    """
    :param path: 
    :return: 
    """
    rf = open(resource_path)

    content = rf.readline()
    cnt = 0
    tmp_dict = {}

    while content:
        #print content

        res = content.replace("\n", "").split(" ")
        cls  = str(res[0:1][0])
        bbox = res[1:6]

        if cls in tmp_dict:
            tmp_dict[cls].append(bbox)
        else:
            tmp_dict[cls] = [bbox]
            cnt += 1

        content = rf.readline()
    rf.close()
    return tmp_dict

def generate_gt_dict(resource_path):
    """
    :param path: 
    :return: image dict
    """
    rf = open(resource_path)
    content = rf.readline()
    cnt = 0
    tmp_dict = {}

    while content:
        #print content
        res = content.replace("\n", "").split(",")

        cls  = str(res[0:1][0])
        bbox = res[1:]

        #--test--
        if cls == "set06_V002_I01499":
            print(bbox)

        if cls in tmp_dict:
            tmp_dict[cls].append(bbox)
        else:
            tmp_dict[cls] = [bbox]
            cnt += 1
        content = rf.readline()
    rf.close()

    return tmp_dict


def str2float_in_list(str_list):
    """
    this funcation transform strlist to floatlist
    :param str_list: 
    :return:float_list 
    """
    import re
    float_reg = re.compile(r'^\d+\.\d+$')
    float_list = [float(f) for f in str_list if float_reg.match(f)]

    return float_list

def show_gt(gt_dict):
    cur_path = "/home/user/Disk1.8T/data_set/citypersons/JPEGImages/"
    dirList = []
    fileList = []


    for im_idx in gt_dict:
        dirList.append(im_idx)


    for dir_ in dirList:
        if dir_ in gt_dict:
            tmp_list = []
            gtList = gt_dict[dir_]

            im_path = cur_path + dir_ + ".png"
            im = cv2.imread(im_path)

            for idx_gt in gtList:
                # [452.380659429031,167.729915560917,47.0928829915561,52.4969843184559]
                # [375.544632086852,172.740631992242,22.3884197828709,49.0229191797346]
                # '475 172 488 225'
                if dir_ == "set06_V002_I01499":
                    print(idx_gt)
                    print("check point")

                # todo 可视化代码有待改进
                for idx_detail in idx_gt:
                    gt_detail = idx_detail.split(" ")
                    gt_x1 = int((gt_detail[0]))
                    gt_y1 = int((gt_detail[1]))
                    gt_x2 = int(((gt_detail[2]))) + int((gt_detail[0]))
                    gt_y2 = int(((gt_detail[3]))) + int((gt_detail[1]))
                    cv2.rectangle(im, (gt_x1, gt_y1), (gt_x2, gt_y2), (0, 255, 0), 1)

            save_path = '/home/user/Disk1.8T/draw_citypersons_gt/11_6/train_gt/'+dir_.split("/")[0]+ "/"
            mkdir(save_path)
            cv2.imwrite(save_path + str(dir_.split("/")[1]+ ".png"), im)

gt_dict = generate_gt_dict("/home/user/PycharmProjects/some_learn/CityPersons_handle/ann_code_src/train_gt_list.txt")

show_gt(gt_dict)