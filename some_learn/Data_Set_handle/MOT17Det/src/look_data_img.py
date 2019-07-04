# -*- coding: utf-8 -*-
import os
import cv2
import matplotlib.pyplot as plt

def show_img(data_path):
    # data_path = "/home/unicoe/Desktop/train/MOT17-10"

    gt_path = os.path.join(data_path, "gt")
    img_path = os.path.join(data_path, "img1")

    print(gt_path, "\n", img_path)

    gt_info = open(os.path.join(gt_path,"gt.txt"), "r")

    gt_list = []

    for igt in gt_info.readlines():
        gt_list.append(igt)

    print(len(gt_list))

    """
    先遍历链表，对每一个框进行显示
    """
    im_bbox = {}

    for igt in gt_list:
        line_info = igt.strip("\n").split(",")
        if float(line_info[6]) in [1.0]  and float(line_info[7]) in [1.0,2.0] and float(line_info[8]) > 0.55:
            if line_info[0] in im_bbox:
                im_bbox[line_info[0]].append([line_info[2], line_info[3], line_info[4], line_info[5],])
            else:
                im_bbox[line_info[0]] = [[line_info[2], line_info[3], line_info[4], line_info[5],]]

    for i_im, i_bbox in im_bbox.items():
        #print(i_im, i_bbox)
        pre_zero = ""
        for izero in range(6 - len(i_im)):
            pre_zero += '0'

        im_name = pre_zero + i_im + '.jpg'

        #im = cv2.imread(os.path.join(img_path, im_name))
        im = plt.imread(os.path.join(img_path, im_name))

        # 将一张图片中所有的框集合起来，然后再画出来

        for i in i_bbox:
            x1 = int(i[0])
            y1 = int(i[1])
            w  = int(i[2])
            h  = int(i[3])
            if h > 40:
                print(w/(h+0.0))
                cv2.rectangle(im, (x1, y1), (x1 + w, y1 + h), (255, 0, 0), 3)

        plt.imshow(im)
        # plt.show()
        # mngr = plt.get_current_fig_manager()
        # # to put it into the upper left corner for example:
        # mngr.window.setGeometry(200,200, 960, 540)

        plt.pause(1.0/2000.0)  # 该句显示图片*秒
        plt.ioff()  # 显示完后一定要配合使用plt.ioff()关闭交互模式，否则可能出奇怪的问题

        plt.clf()  # 清空图片
        # plt.close()

if __name__ == "__main__":

    path_ls = [
        "/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-02",
        "/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-04",
        "/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-05",
        "/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-09",
        "/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-10",
        "/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-11",
        "/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-13",
    ]

    for i_p in path_ls:
        show_img(i_p)
