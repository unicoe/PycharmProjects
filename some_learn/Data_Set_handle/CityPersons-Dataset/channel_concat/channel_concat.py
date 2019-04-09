import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc as m
#org_img_path = "/home/user/Disk1.8T/data_set/cityspaces/leftImg8bit/train/aachen/aachen_000000_000019_leftImg8bit.png"

img = cv2.imread("/home/user/Disk1.8T/data_set/cityspaces/leftImg8bit/train/aachen/aachen_000000_000019_leftImg8bit.png")
label_img = cv2.imread("/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/aachen/aachen_labelIds/aachen_000000_000019_gtFine_labelIds.png", 0)

vis = False
if vis:

    plt.subplot(211)
    plt.imshow(img)
    plt.subplot(212)
    plt.imshow(label_img)

    plt.show()

np_img = np.array(img)
np_label_img = np.array(label_img)
np_label_img = np_label_img.reshape((1024, 2048, 1))
print(np_img.shape)
print(np_label_img.shape)

n_img = np.concatenate((np_img, np_label_img),2)
print(n_img.shape)

if vis:
    plt.imshow(n_img)
    plt.show()

cv2.imwrite("/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/channel_concat/test.png", n_img)