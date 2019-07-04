import os
import matplotlib.pyplot as plt
import cv2
import  numpy as np
import scipy.misc as m

folder_name = [
'/home/user/Disk1.8T/unicoe/pytorch-ssd-2/data/VOCdevkit/VOC0712/JPEGImages/MOT17-11'
'/home/user/Disk1.8T/unicoe/pytorch-ssd-2/data/VOCdevkit/VOC0712/JPEGImages/MOT17-11'
]

wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/train_list.txt", "aw")

for folder in folder_name:

    file_name = os.listdir(folder)
    for idx in file_name:
        wf.write(folder.split("/")[-1] +'/'+ idx.split(".")[0])
        wf.write("\n")
