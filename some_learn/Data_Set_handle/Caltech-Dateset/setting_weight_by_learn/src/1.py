# -*- coding: utf-8 -*-
# @Time    : 18-7-25 上午9:37
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : 1.py
# @Software: PyCharm Community Edition

import numpy as np

DEBUG = False

# save scores bboxes to dict1
rf1 = open("/home/user/PycharmProjects/setting_weight_by_learn/weight_add/source_bbox_gt/7_25_det_test_person.txt")
pic_dict1 = {}
content1 = rf1.readline()

while content1:

    tmp = content1.strip().split(" ")

    pic_name = tmp[0]
    pic_info = map(eval,tmp[1:])

    if pic_name in pic_dict1:
        pic_dict1[pic_name].append(pic_info)
    else:
        pic_dict1[pic_name] = [pic_info]

    content1 = rf1.readline()

if DEBUG:
    print pic_dict1
    print '1'

# save scores bboxes to dict2
rf2 = open("/home/user/PycharmProjects/setting_weight_by_learn/weight_add/source_bbox_gt/train1xnew_gt.txt")
pic_dict2 = {}
content2 = rf2.readline()

while content2:

    tmp1 = content2.strip().split(" ")

    pic_name1 = tmp1[0]
    pic_info1 = map(eval, tmp1[1:])

    if pic_name1 in pic_dict2:
        pic_dict2[pic_name1].append(pic_info1)
    else:
        pic_dict2[pic_name1] = [pic_info1]

    content2 = rf2.readline()

if DEBUG:
    print pic_dict2
    print '2'


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
    #print l1,l2
    return intersectionPercent

DEBUG = True

res_list = []

wf1 = open("/home/user/PycharmProjects/setting_weight_by_learn/weight_add/1_withgt_person.txt","w")
wf2 = open("/home/user/PycharmProjects/setting_weight_by_learn/weight_add/2_gt.txt","w")

def handle_weight1(idx_name,info1, info2):
    """
    handle a pic's bboxes , add weight for detection result
    :param info1: scores bboxes list
    :param info2: scores bboxes list
    :return: 
    """
    np_info1 = np.array(info1)
    np_info2 = np.array(info2)
    vis1 = np.zeros(len(np_info1))
    vis2 = np.zeros(len(np_info2))

    for idx in range(len(np_info1)):
        for idx2 in range(len(np_info2)):

            tmp_bbox1  = np_info1[idx][1:5]
            tmp_bbox2  = np_info2[idx2][1:5]
            tmp_score1 = np_info1[idx][0:1]
            tmp_score2 = np_info2[idx2][0:1]


            pro = 1
            if compute_IoU(tmp_bbox1.tolist(), tmp_bbox2.tolist()) > 0.5:
                if vis1[idx] != 1 and vis2[idx2] != 1:
                    #将匹配的结果保存，结果进行分别保存
                    wf1.write(str(tmp_bbox1[0]))
                    wf1.write(str(" "))
                    wf1.write(str(tmp_bbox1[1]))
                    wf1.write(str(" "))
                    wf1.write(str(tmp_bbox1[2]))
                    wf1.write(str(" "))
                    wf1.write(str(tmp_bbox1[3]))
                    wf1.write("\n")

                    wf2.write(str(tmp_bbox2[0]))
                    wf2.write(str(" "))
                    wf2.write(str(tmp_bbox2[1]))
                    wf2.write(str(" "))
                    wf2.write(str(tmp_bbox2[2]))
                    wf2.write(str(" "))
                    wf2.write(str(tmp_bbox2[3]))
                    wf2.write("\n")

                    vis1[idx] = 1
                    vis2[idx2] = 1

    if DEBUG:
        print vis1
        print vis2

    # for idx in range(len(np_info1)):
    #     if vis1[idx] == 0:
    #         res_str =  idx_name \
    #         + " " + str(np_info1[idx][0]) \
    #         + " " + str(np_info1[idx][1]) \
    #         + " " + str(np_info1[idx][2]) \
    #         + " " + str(np_info1[idx][3]) \
    #         + " " + str(np_info1[idx][4])
    #
    #         res_list.append(res_str)
    #
    # for idx2 in range(len(np_info2)):
    #     if vis2[idx2] == 0:
    #         res_str = idx_name \
    #               + " " + str(np_info2[idx2][0]) \
    #               + " " + str(np_info2[idx2][1]) \
    #               + " " + str(np_info2[idx2][2]) \
    #               + " " + str(np_info2[idx2][3]) \
    #               + " " + str(np_info2[idx2][4])
    #         res_list.append(res_str)




def write_result(res_list):
    wf = open("/home/user/PycharmProjects/handle_result/6_25(7_18)/weight_add/result/weight_handle_result1.0.txt", "w")

    for idx in res_list:
        wf.write(idx)
        wf.write("\n")

    wf.close()
    pass

#get the pic_dict1 pic_dict2,

#common pictures
com_list = []

for name in pic_dict1:
    if name in pic_dict2:
        com_list.append(name)

com_list.sort()

for idx in com_list:
    info1 = pic_dict1[idx]
    info2 = pic_dict2[idx]

    if DEBUG:
        print info1
        print info2

    handle_weight1(idx_name=idx, info1=info1, info2=info2)

# write_result(res_list)