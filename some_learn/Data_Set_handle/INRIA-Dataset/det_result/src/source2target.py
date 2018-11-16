# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午9:21
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : source2target.py
# @Software: PyCharm
import copy
import numpy as np

# save img_shape to dict
rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle"
          "/INRIA-Dataset/lst/test_img_shape.txt", "r")

shape_dict = {}
content = rf.readline()
while content:


    im_info = content.strip("\n").split(" ")
    shape_dict[im_info[0]] = [int(im_info[1]), int(im_info[2])]           # h w

    content = rf.readline()


rf1 = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/det_result/det/2018_11_15_Thu_22_08_24_det_test_person.txt", "r")

content = rf1.readline()
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

    content = rf1.readline()


rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/"
          "INRIA-Dataset/lst/test_img_shape.txt", "r")

content = rf.readline()
im_name_lst = []
while content:
    im_info = content.strip("\n").split(" ")
    im_name_lst.append(im_info[0])
    content = rf.readline()


for im_idx in im_name_lst:
    if im_idx in det_dict:
        cur_shape = shape_dict[im_idx]
        im_w = cur_shape[1]
        im_h = cur_shape[0]

        min_size = min(im_w, im_h)
        max_size = max(im_w, im_h)

        """
        # Each scale is the pixel size of an image's shortest side
        __C.TEST.SCALES = (960,)

        # Max pixel size of the longest side of a scaled input image
        __C.TEST.MAX_SIZE = 1280
        """
        im_scale = float(960) / float(min_size)
        # Prevent the biggest axis from being more than MAX_SIZE
        if np.round(im_scale * max_size) > 1280:
            im_scale = float(1280) / float(max_size)

        sw = im_w * im_scale
        sh = im_h * im_scale

        r1 = 1280.0 / sw
        r2 = 960.0 / sh

        for bbox_item in det_dict[im_idx]:
            x1 = bbox_item[1]
            y1 = bbox_item[2]
            x2 = bbox_item[3]
            y2 = bbox_item[4]

            # tw = bbox_item[3] - bbox_item[1]
            # th = bbox_item[4] - bbox_item[2]
            #
            #
            #
            # b_w = min(tw, th)
            # b_h = max(tw, th)

            b_w = bbox_item[3] - bbox_item[1]
            b_h = bbox_item[4] - bbox_item[2]

            tmp_b_w = b_w/r1
            tmp_b_h = b_h/r2

            x_c = x1 + b_w/2.0
            y_c = y1 + b_h/2.0
            t_xc = x_c / r1
            t_yc = y_c / r2

            # t_x1 = t_xc - b_w/2.0
            # t_y1 = t_yc - b_h/2.0
            #
            # t_x2 = t_xc + b_w / 2.0
            # t_y2 = t_yc + b_h / 2.0

            t_x1 = t_xc - tmp_b_w / 2.0
            t_y1 = t_yc - tmp_b_h / 2.0

            t_x2 = t_xc + tmp_b_w / 2.0
            t_y2 = t_yc + tmp_b_h / 2.0

            bbox_item[1] = t_x1
            bbox_item[2] = t_y1
            bbox_item[3] = t_x2
            bbox_item[4] = t_y2

wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/det_result/det/handle_2018_11_15_Thu_22_08_24_det_test_person.txt", "w")

for im_idx in im_name_lst:
    if im_idx in det_dict:
        for bbox_idx in det_dict[im_idx]:
            wf.write(im_idx)
            for xy_i in bbox_idx:
                wf.write(" ")
                wf.write(str(round(xy_i,4)))

            wf.write("\n")
wf.close()


