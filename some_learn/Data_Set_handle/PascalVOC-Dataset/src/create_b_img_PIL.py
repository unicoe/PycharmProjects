# -*- coding: utf-8 -*-
# @Time    : 18-12-7 下午10:35
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : create_b_img_PIL.py
# @Software: PyCharm

import numpy as np
import PIL
import PIL.Image

#create a black use numpy,size is:512*512
#img = np.zeros((480,640,3), np.uint8)
#fill the image with white
#img.fill(0)

#cv2.imwrite("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/mask_img/b_img.png",img)

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok'
        return True
    else:

        print path + 'failed!'
        return False


img =  PIL.Image.new("P", (640,480))

im_ls_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/caltech1x_ls.txt","r")

im_ls = []

im_name = im_ls_r.readline()

while im_name:
    im_tmp = im_name.strip("\n")

    im_ls.append(im_tmp)

    im_name = im_ls_r.readline()


for i_im in im_ls:
    #cv2.imwrite("/home/user/Disk1.8T/data_set/seglabel_png/"+i_im+".png", img)
    mkdir("/home/user/Disk1.8T/data_set/seglabel_png1/")
    img.save("/home/user/Disk1.8T/data_set/seglabel_png1/"+i_im+".png", 'png')