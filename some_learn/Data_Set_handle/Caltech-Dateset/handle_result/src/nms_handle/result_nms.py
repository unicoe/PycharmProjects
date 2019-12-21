# -*- coding: utf-8 -*-
# @Time    : 18-6-6 下午8:14
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : result_nms.py
# @Software: PyCharm Community Edition

import numpy as np
import nms

file_lst = [

#"/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/640480_basic/2019_10_17_Thu_11_55_26.txt",
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_03_40_12.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_04_09_36.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_04_39_00.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_05_08_20.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_05_37_36.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_06_07_12.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_06_36_32.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_06_45_09.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_07_03_15.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_07_16_52.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_07_19_50.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/300500/500/2019_10_25_Fri_07_20_50.txt',

]

for file_idx in file_lst:
    r_path = file_idx
    rf = open(r_path)

    content = rf.readline()
    result_dir = {}

    while content:

        res_list = content.strip("\n")
        # MOT
        # pic_name = res_list[0:15]
        # box_info = res_list[16:]

        # caltech
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

    nms_lst = [0.55]
    #nms_lst = [0.55]

    for nms_num in nms_lst:
        w_path = r_path.strip("\n").split(".")[0] + "_nms_" + str(nms_num)[2:] +  ".txt"


        file_name = r_path.strip("\n").split(".")[0]
        tmp_name = r_path.strip("\n").split(".")[0].split("/")
        nms_name = "nms_" + str(nms_num)[2:] + "_" + tmp_name[-1]

        w_path = file_name[0:120] + nms_name +  ".txt"


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
            #print len(tmp_np1),len(nms_res)

            for nms_item in nms_res:
                wf.write(key)
                wf.write(" ")
                wf.write(boxes_info[nms_item])
                wf.write("\n")

        print "done."
