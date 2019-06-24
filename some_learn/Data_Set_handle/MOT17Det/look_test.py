# -*- coding: utf-8 -*-
import os
import cv2
import matplotlib.pyplot as plt

def show_img(data_path):
    # data_path = "/home/unicoe/Desktop/train/MOT17-10"

    img_path = os.path.join(data_path, "img1")

    cnt = 0
    for i_im in os.listdir(img_path):

        # 隔100张抽一张显示
        if cnt % 100 != 2:
            cnt += 1
            continue
        cnt = 0

        im = plt.imread(os.path.join(img_path, i_im))

        plt.imshow(im)
        # plt.show()
        mngr = plt.get_current_fig_manager()
        # to put it into the upper left corner for example:
        mngr.window.setGeometry(500,200, 960, 540)

        plt.pause(1.0/2000.0)  # 该句显示图片*秒
        plt.ioff()  # 显示完后一定要配合使用plt.ioff()关闭交互模式，否则可能出奇怪的问题

        plt.clf()  # 清空图片
        # plt.close()

if __name__ == "__main__":

    path_ls = [
        "/home/unicoe/Desktop/test/MOT17-01",
        "/home/unicoe/Desktop/test/MOT17-03",
        "/home/unicoe/Desktop/test/MOT17-06",
        "/home/unicoe/Desktop/test/MOT17-07",
        "/home/unicoe/Desktop/test/MOT17-08",
        "/home/unicoe/Desktop/test/MOT17-12",
        "/home/unicoe/Desktop/test/MOT17-14",
    ]

    for i_p in path_ls:
        show_img(i_p)
