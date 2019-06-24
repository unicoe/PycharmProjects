#--coding:utf-8--
import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc as m
import os
import PIL
from PIL import Image, ImageDraw

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok.'
        return True
    else:
        print path + ' path already exits.'
        return False


org_img_path = "/home/user/Disk1.8T/data_set/city_new_data_1"
# /aachen/aachen_000000_000019_leftImg8bit.png

label_img_path = "/home/user/Disk1.8T/data_set/city_seglabel_png_5_71"
# /aachen/aachen_labelIds/aachen_000000_000019_gtFine_labelIds.png

org_img_folder = os.listdir(org_img_path)

print(org_img_folder)
for city_name in org_img_folder:
    org_img_path_city = org_img_path + "/" + city_name
    label_img_path_city = label_img_path + "/" + city_name
    # print(org_img_path_city)
    # print(label_img_path_city)

    img_ls = os.listdir(org_img_path_city)
    #print(img_ls)

    for it in img_ls:
        print(it)

        org_img = org_img_path_city+"/"+it
        org_img_it = cv2.imread(org_img)

        #img_name = it[:-16] + "_gtFine_labelIds.png"
        #label_img = label_img_path_city+"/"+city_name+"_labelIds"+"/"+img_name
        label_img = label_img_path_city + "/" + it
        # print(label_img)
        label_img_it = cv2.imread(label_img, 0)

        vis = False
        if vis:
            plt.subplot(211)
            plt.imshow(org_img_it)
            plt.subplot(212)
            plt.imshow(label_img_it)
            plt.show()

        np_img = np.array(org_img_it)

        if label_img_it == None:
            label_img_it = PIL.Image.new("P", (2048, 1024), color=0)

        np_label_img = np.array(label_img_it)
        np_label_img = np_label_img.reshape((1024, 2048, 1))
        # print(np_img.shape)
        # print(np_label_img.shape)

        n_img = np.concatenate((np_img, np_label_img),2)
        # print(n_img.shape)

        vis = False
        if vis:
            plt.imshow(n_img)
            plt.show()

        save_folder = "/home/user/Disk1.8T/data_set/cityspaces/weak3_concat_channel/train/" + city_name
        mkdir(save_folder)
        cv2.imwrite(save_folder+"/"+it, n_img)