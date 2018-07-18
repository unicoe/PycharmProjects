# -*- coding: utf-8 -*-
# @Time    : 18-6-6 下午8:14
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : result_nms.py
# @Software: PyCharm Community Edition

rf = open("/home/user/PycharmProjects/handle_result/6_16/handle_result/merge_result.txt")

content = rf.readline()

result_dir = {}

while content:

    res_list = content.strip("\n")
    pic_name = res_list[0:17]
    box_info = res_list[18:]
    if pic_name in result_dir :
        result_dir[pic_name].append(box_info)
    else:

        result_dir[pic_name] = []
        result_dir[pic_name].append(box_info)

    content = rf.readline()

#test
#print result_dir

wf = open("/home/user/PycharmProjects/handle_result/6_16/handle_result/nms_merge_result.txt", "w")


import numpy as np
import nms


for key in result_dir.iterkeys():
    tmp_np = np.array([0, 0, 0, 0, 0])

    boxes_info = result_dir[key]
    len_box  = len(boxes_info)
    info = []
    for b_item in boxes_info:
        tmp_info = b_item.strip(" ").split(" ")
        tf_info = []
        for t_idx in tmp_info:
            tf_info.append(float(t_idx))
        info.append(tf_info)
    tmp_np1 = np.array(info)
    nms_res = nms.py_cpu_nms(tmp_np1, 0.4)
    print len(tmp_np1),len(nms_res)

    for nms_item in nms_res:
        wf.write(key)
        wf.write(" ")
        wf.write(boxes_info[nms_item])
        wf.write("\n")

print 1
