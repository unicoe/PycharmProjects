# -*- coding: utf-8 -*-
import os
import cv2
import matplotlib.pyplot as plt

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + 'ok')
        return True
    else:
        print(path + 'failed!')
        return False


def show_img(data_path):
    # data_path = "/home/unicoe/Desktop/train/MOT17-10"

    img_path = os.path.join(data_path)

    cnt = 0
    for i_im in os.listdir(img_path):

        im = cv2.imread(os.path.join(img_path, i_im))
        im_resize = cv2.resize(im,(1920, 1080))
        mkdir(os.path.join(img_path+'/tmp'))
        cv2.imwrite(os.path.join(img_path+"/tmp", i_im.split(".")[0]+'.png'), im_resize)

        # plt.imshow(im)
        # # plt.show()
        # mngr = plt.get_current_fig_manager()
        # # to put it into the upper left corner for example:
        # # mngr.window.setGeometry(500,200, 960, 540)
        #
        # plt.pause(1.0/2000.0)  # 该句显示图片*秒
        # plt.ioff()  # 显示完后一定要配合使用plt.ioff()关闭交互模式，否则可能出奇怪的问题
        #
        # plt.clf()  # 清空图片
        # # plt.close()

if __name__ == "__main__":

    path_ls = [
        "/home/user/Disk1.8T/unicoe/pytorch-fcn/experiments/8_9_0/visual/MOT17-02",
        "/home/user/Disk1.8T/unicoe/pytorch-fcn/experiments/8_9_0/visual/MOT17-04",
        #"/home/user/Disk1.8T/unicoe/pytorch-fcn/experiments/8_9_0/visual/MOT17-05",
        "/home/user/Disk1.8T/unicoe/pytorch-fcn/experiments/8_9_0/visual/MOT17-09",
        "/home/user/Disk1.8T/unicoe/pytorch-fcn/experiments/8_9_0/visual/MOT17-10",
        "/home/user/Disk1.8T/unicoe/pytorch-fcn/experiments/8_9_0/visual/MOT17-11",
        "/home/user/Disk1.8T/unicoe/pytorch-fcn/experiments/8_9_0/visual/MOT17-13",
    ]

    for i_p in path_ls:
        show_img(i_p)
