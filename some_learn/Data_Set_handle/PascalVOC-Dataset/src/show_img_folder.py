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

'/home/user/Disk1.8T/draw_result/augmentations/Expand_seglbl'
]

for folder in folder_name:

    file_name = os.listdir(folder)
    for idx in file_name:
        X = cv2.imread(folder + "/" + idx, cv2.IMREAD_UNCHANGED)
        #img = m.imread(folder +"/"+ idx)
        print(X.shape)
        #img_1 = m.imread("/home/user/Disk1.8T/unicoe/pytorch-ssd-2/data/VOCdevkit/VOC0712/JPEGImages/" + idx.split(".")[0] + ".jpg")
        #cv2.imwrite("/home/user/Disk1.8T/A_img/" + idx, img)
        #plt.figure(figsize=(12.8*2, 4.8*2))
        #plt.subplot(121)

        print(X.shape)
        Y_seg = X[:, :, 3]


        # save_img = random.randint(1, 10000)
        # print(type(Y_seg))

        # import pdb
        # pdb.set_trace()
        # print(Y_seg.shape)
        # print(Y_seg)
        # cv2.imwrite("/home/user/Disk1.8T/unicoe/ALFNet/output/save3/" + str(save_img) + ".png", Y_seg)
        # tmp_img = Y_seg.reshape(640,1280)
        # plt.image.imsave("/home/user/Disk1.8T/unicoe/ALFNet/output/save2/" + str(save_img) + ".png", tmp_img)
        X = X[:, :, 0:3]

        result_map = np.zeros((1,1024,2048, 2))

        # For np.where calculation.
        person = (Y_seg == 255)
        # car = (Y_seg == 26)
        # road = (Y_seg == 7)
        background = np.logical_not(person)

        result_map[:, :, :, 0] = np.where(background, 1, 0)
        result_map[:, :, :, 1] = np.where(person, 1, 0)

        plt.imshow(Y_seg)
        #plt.subplot(122)
        #plt.imshow(img_1)
        plt.show()