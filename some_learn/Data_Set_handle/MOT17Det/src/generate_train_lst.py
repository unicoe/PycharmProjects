# -*- coding: utf-8 -*-
import os
import cv2
import matplotlib.pyplot as plt

def show_img(data_path):
    # data_path = "/home/unicoe/Desktop/train/MOT17-10"

    img_path = os.path.join(data_path)
    wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/anno/lst/test_06.txt", "aw")
    cnt = 0
    for i_im in os.listdir(img_path):

        # 隔100张抽一张显示
        # if cnt % 100 != 2:
        #     cnt += 1
        #     continue
        # cnt = 0

        wf.write(data_path.split("/")[-1]+"/"+i_im.split(".")[0])
        wf.write("\n")


if __name__ == "__main__":

    path_ls = [
        # "/home/user/Disk1.8T/data_set/MOT17Det/test/MOT17-01",
        # "/home/user/Disk1.8T/data_set/MOT17Det/test/MOT17-03",
        # "/home/user/Disk1.8T/data_set/MOT17Det/test/MOT17-07",
        # "/home/user/Disk1.8T/data_set/MOT17Det/test/MOT17-08",
        # "/home/user/Disk1.8T/data_set/MOT17Det/test/MOT17-12",
        # "/home/user/Disk1.8T/data_set/MOT17Det/test/MOT17-14",

        "/home/user/Disk1.8T/data_set/MOT17Det/test/MOT17-06",
    ]

    for i_p in path_ls:
        show_img(i_p)
