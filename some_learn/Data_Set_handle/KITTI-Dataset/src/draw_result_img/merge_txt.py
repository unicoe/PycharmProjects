# -*- coding: utf-8 -*-
"""
画kitti 的结果图
该代码用来聚合各个结果的信息
"""

pcn_info    = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/det_result/kitti-eval/draw_kitti_result/pcn_pedestrian_detection.txt")
rpn_bf_info = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/det_result/kitti-eval/draw_kitti_result/rpn_bf_pedestrian_detection.txt")
deep_parts  = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/det_result/kitti-eval/draw_kitti_result/deepparts_pedestrian_detection.txt")
sdp_crc     = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/det_result/kitti-eval/draw_kitti_result/sdp_crc_pedestrian_detection.txt")
faster_rcnn = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/det_result/kitti-eval/draw_kitti_result/faster_rcnn_pedestrian_detection.txt")
dop3        = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/det_result/kitti-eval/draw_kitti_result/3dop_pedestrian_detection.txt")
ms_cnn      = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/det_result/kitti-eval/draw_kitti_result/ms_cnn_pedestrian_detection.txt")

ours_info = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/det_result/kitti-eval/draw_kitti_result/pedestrian_detection.txt")

res_info = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/det_result/kitti-eval/draw_kitti_result/draw_img_pedestrian_detection.txt", "w")

c_pcn = pcn_info.readline()
c_rpn_bf = rpn_bf_info.readline()
c_deep_parts = deep_parts.readline()
c_sdp_crc    = sdp_crc.readline()
c_faster_rcnn= faster_rcnn.readline()
c_dop3       = dop3.readline()
c_ms_cnn     = ms_cnn.readline()
c_ours = ours_info.readline()

while c_ours:

    tmp_pcn = c_pcn.strip("\n").split(" ")
    tmp_rpn_bf = c_rpn_bf.strip("\n").split(" ")
    tmp_ours = c_ours.strip("\n").split(" ")
    tmp_deep_parts   =  c_deep_parts.strip("\n").split(" ")
    tmp_sdp_crc      =     c_sdp_crc.strip("\n").split(" ")
    tmp_faster_rcnn  = c_faster_rcnn.strip("\n").split(" ")
    tmp_dop3         =        c_dop3.strip("\n").split(" ")
    tmp_ms_cnn       =      c_ms_cnn.strip("\n").split(" ")

    # print(tmp_ours)
    # print(tmp_rpn_bf)
    # print(tmp_pcn)

    # 聚合各个方法第二类的信息
    str_join =  tmp_ours[0]   + " " + \
                tmp_ours[2]   + " " + \
                tmp_pcn[2]    + " " + \
                tmp_rpn_bf[2] + " " + \
                tmp_deep_parts[2] + " " + \
                tmp_sdp_crc[2] + " " + \
                tmp_faster_rcnn[2] + " " + \
                tmp_dop3[2] + " " + \
                tmp_ms_cnn[2]

    # print(str_join)
    # break

    res_info.write(str_join)
    res_info.write("\n")

    c_pcn = pcn_info.readline()
    c_rpn_bf = rpn_bf_info.readline()
    c_ours = ours_info.readline()
    c_deep_parts = deep_parts.readline()
    c_sdp_crc    = sdp_crc.readline()
    c_faster_rcnn= faster_rcnn.readline()
    c_dop3       = dop3.readline()
    c_ms_cnn     = ms_cnn.readline()