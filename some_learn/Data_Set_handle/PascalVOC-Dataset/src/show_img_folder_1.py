import os
import matplotlib.pyplot as plt
import cv2
import  numpy as np
import scipy.misc as m
folder_name = [

#'/home/user/Disk1.8T/draw_result/augmentations/Expand',
#'/home/user/Disk1.8T/draw_result/augmentations/Expand_seglbl',
#'/home/user/Disk1.8T/draw_result/augmentations/Expand_seglbl_weak',
#'/home/user/Disk1.8T/draw_result/augmentations/RandomSampleCrop',
# '/home/user/Disk1.8T/draw_result/augmentations/RandomSampleCrop_seglbl',
# '/home/user/Disk1.8T/draw_result/augmentations/RandomSampleCrop_seglbl_weak',

'/home/user/Disk1.8T/draw_result/augmentations/seglbl_6_4_1'
]

for folder in folder_name:

    file_name = os.listdir(folder)
    for idx in file_name:

        img = m.imread(folder +"/"+ idx)
        plt.imshow(img)
        plt.show()
