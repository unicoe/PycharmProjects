import os
import matplotlib.pyplot as plt
import cv2
import  numpy as np
import scipy.misc as m

folder_name = [
'/home/user/Disk1.8T/lb_exp/PICTURE_DATA/Train/Annotation'
#'/home/user/Disk1.8T/lb_exp/PICTURE_DATA/Train/JPEGImage'
]

wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/ssd_train_list.txt", "aw")

for folder in folder_name:

    file_name = os.listdir(folder)
    for idx in file_name:
        wf.write(idx.split(".")[0])
        wf.write("\n")
