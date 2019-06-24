# -*- coding: utf-8 -*-
# @Time    : 18-6-6 下午8:14
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : result_nms.py
# @Software: PyCharm Community Edition

import numpy as np
import nms

file_lst = [

'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/5_26/2019_05_27_Mon_10_35_11.txt',

]

for file_idx in file_lst:
    r_path = file_idx
    rf = open(r_path)

    content = rf.readline()
    result_dir = {}

    while content:

        res_list = content.strip("\n")
        # caltech inria eth
        pic_name = res_list[0:17]
        box_info = res_list[18:]

        #kitti

        # pic_name = res_list[0:6]
        # box_info = res_list[7:]

        #kitti test_
        # pic_name = res_list[0:11]
        # box_info = res_list[12:]

        if pic_name in result_dir :
            result_dir[pic_name].append(box_info)
        else:
            result_dir[pic_name] = []
            result_dir[pic_name].append(box_info)

        content = rf.readline()

    #test
    #print result_dir

    nms_lst = [0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54]

    for nms_num in nms_lst:
        w_path = r_path.strip("\n").split(".")[0] + "_nms_" + str(nms_num)[2:] +  ".txt"


        file_name = r_path.strip("\n").split(".")[0]
        tmp_name = r_path.strip("\n").split(".")[0].split("/")
        nms_name = "nms_" + str(nms_num)[2:] + "_" + tmp_name[-1]

        w_path = file_name[0:104] + nms_name +  ".txt"


        wf = open(w_path, "w")

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
            nms_res = nms.py_cpu_nms(tmp_np1, nms_num)
            print len(tmp_np1),len(nms_res)

            for nms_item in nms_res:
                wf.write(key)
                wf.write(" ")
                wf.write(boxes_info[nms_item])
                wf.write("\n")

        print "done."
