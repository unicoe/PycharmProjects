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
        print path + 'ok'
        return True
    else:

        print path + 'failed!'
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
            print bbox

        if cls in tmp_dict:
            tmp_dict[cls].append(bbox)
        else:
            tmp_dict[cls] = [bbox]
            cnt += 1
        content = rf.readline()
    rf.close()

    return tmp_dict

def compute_IoU(l1, l2):
    '''
    #the coordinate of this funcation is (x1,y1,x2,y2)
    :param l1: first rectangle coordinate 
    :param l2: second rectangle coordinate
    :return: yes or no IoU > 0.5(or x) 
    '''
    if(l1[0] > l2[0] + abs(l2[2]-l2[0])):
        return False
    if(l1[1] > l2[1] + abs(l2[3]-l2[1])):
        return False
    if(l1[0] + l1[2]-l1[0] < l2[0]):
        return False
    if(l1[1] + l1[3]-l1[1] < l2[1]):
        return False

    colInt = min(l1[0]+l1[2]-l1[0] , l2[0]+l2[2]-l2[0]) - max(l1[0], l2[0])
    rowInt = min(l1[1]+l1[3]-l1[1] , l2[1]+l2[3]-l2[1]) - max(l1[1], l2[1])

    intersection = colInt * rowInt
    area1 = (l1[2]-l1[0])*(l1[3]-l1[1])
    area2 = (l2[2]-l2[0])*(l2[3]-l2[1])

    intersectionPercent = intersection/(area1+area2-intersection + 0.0)
    print "IoU = " + str(intersectionPercent)
    return intersectionPercent

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

def show_IOU_gt_and_result(gt_dict, res_dict):
    cur_path = "/home/user/py-R-FCN/data/VOCdevkit0712/VOC0712/JPEGImages/"
    dirList = []
    fileList = []
    files = os.listdir(cur_path)

    for file in files:
        tmp_path = file.split('.')[0]
        dirList.append(tmp_path)

    for dir_ in dirList:
        if dir_ in gt_dict and dir_ in res_dict:
            tmp_list = []
            gtList = gt_dict[dir_]
            resList = res_dict[dir_]

            im_path = cur_path + dir_ + ".jpg"
            im = cv2.imread(im_path)

            for idx_gt in gtList:
                # [452.380659429031,167.729915560917,47.0928829915561,52.4969843184559]
                # [375.544632086852,172.740631992242,22.3884197828709,49.0229191797346]
                # '475 172 488 225'
                if dir_ == "set06_V002_I01499":
                    print idx_gt
                    print "check point"

                for idx_detail in idx_gt:
                    gt_detail = idx_detail.split(" ")
                    gt_x1 = int((gt_detail[0]))
                    gt_y1 = int((gt_detail[1]))
                    gt_x2 = int(((gt_detail[2])))
                    gt_y2 = int(((gt_detail[3])))
                    cv2.rectangle(im, (gt_x1, gt_y1), (gt_x2, gt_y2), (0, 255, 0), 1)
                    gt_l = []
                    gt_l.append(gt_x1)
                    gt_l.append(gt_y1)
                    gt_l.append(gt_x2)
                    gt_l.append(gt_y2)

                    for idx_res in resList:
                        if float(idx_res[0]) < 0.01:
                            continue
                        res_x1 = int(float(idx_res[1]))
                        res_y1 = int(float(idx_res[2]))
                        res_x2 = int(float(float(idx_res[3])))
                        res_y2 = int(float(float(idx_res[4])))
                        res_l = []
                        res_l.append(res_x1)
                        res_l.append(res_y1)
                        res_l.append(res_x2)
                        res_l.append(res_y2)

                        iou_res = round(compute_IoU(gt_l, res_l), 2)


                    # 这里还是有问题，画出结果不对
                        if iou_res > 0.5:
                            cv2.rectangle(im, (res_x1, res_y1), (res_x2, res_y2), (255, 255, 0), 1)

                            cv2.putText(im, str(str(iou_res) + " " + str(idx_res[0])), (int(res_x1), int(res_y1 - 6)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.4,
                                        (255, 255, 0))
                            if idx_res in tmp_list:
                                tmp_list.remove(idx_res)
                            resList.remove(idx_res)
                        else:
                            if idx_res in tmp_list:
                                if iou_res > idx_res[5]:
                                    idx_res[5] = iou_res
                            else:
                                idx_res.append(iou_res)
                                tmp_list.append(idx_res)

            for idx_tmp in tmp_list:
                if float(idx_tmp[0]) < 0.01:
                    continue
                res_x1 = int(float(idx_tmp[1]))
                res_y1 = int(float(idx_tmp[2]))
                res_x2 = int(float(float(idx_tmp[3])))
                res_y2 = int(float(float(idx_tmp[4])))
                res_l = []
                res_l.append(res_x1)
                res_l.append(res_y1)
                res_l.append(res_x2)
                res_l.append(res_y2)
                cv2.rectangle(im, (res_x1, res_y1), (res_x2, res_y2), (0, 0, 255), 1)

                cv2.putText(im, str(str(idx_tmp[5]) + " " + str(idx_tmp[0])), (int(res_x1), int(res_y1 - 6)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.4,
                            (0, 0, 255))
                tmp_list.remove(idx_tmp)

            mkdir('/home/user/Disk1.8T/draw_result/7_7/nms_handle_7_7_iter_10000_det_test_head/test/')
            cv2.imwrite('/home/user/Disk1.8T/draw_result/7_7/nms_handle_7_7_iter_10000_det_test_head/test/' + str(dir_ + ".jpg"),
                        im)

gt_dict = generate_gt_dict("/home/user/PycharmProjects/anaylsis_result/draw_result_in_new_anno/gt_file/test_gt.txt")
res_dict = generate_result("/home/user/PycharmProjects/handle_result/7_7/handle_result/nms_handle_7_7_iter_10000_det_test_head.txt")

show_IOU_gt_and_result(gt_dict, res_dict)