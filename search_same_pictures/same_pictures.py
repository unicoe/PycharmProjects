# -*- conding:utf-8 -*-
__author__ = 'unicoe'
__date__ = '2018/7/2'
__time__ = '2:04'

import cv2
import numpy as np

import os

file1 = "1.png"
file2 = "3.png"

f1_list = os.listdir("/home/user/Disk1.8T/zl_folder/MobileNet_FPN_Prediction/")
f2_list = os.listdir("/home/user/Disk1.8T/zl_folder/pictures/")


print f1_list,f2_list

wf = open("/home/user/PycharmProjects/search_same_pictures/result.txt", "w")

for idx_1 in f1_list:
    image1 = cv2.imread("/home/user/Disk1.8T/zl_folder/MobileNet_FPN_Prediction/" + idx_1)
    im1_str = "/home/user/Disk1.8T/zl_folder/MobileNet_FPN_Prediction/" + idx_1
    image1.resize(300,300)
    for idx_2 in f2_list:
        image2 = cv2.imread("/home/user/Disk1.8T/zl_folder/pictures/" + idx_2)
        im2_str = "/home/user/Disk1.8T/zl_folder/pictures/" + idx_2
        image2.resize(300,300)
        if image1.size != image2.size:
            continue
        print image1.size, image2.size
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)

        print result

        if result is True:
            wf.write(im1_str)
            wf.write("\n")
wf.close()


# image1 = cv2.imread(file1)
# image2 = cv2.imread(file2)
# difference = cv2.subtract(image1, image2)
# result = not np.any(difference)  # if difference is all zeros it will return False
#
# if result is True:
#     print("same")
# else:
#     #cv2.imwrite("result.jpg", difference)
#     print ("not same")