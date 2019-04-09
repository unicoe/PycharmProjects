import os
import matplotlib.pyplot as plt
import cv2
import scipy.misc as m
folder_name = [

#'/home/user/Disk1.8T/draw_result/augmentations/Expand',
#'/home/user/Disk1.8T/draw_result/augmentations/Expand_seglbl',
#'/home/user/Disk1.8T/draw_result/augmentations/Expand_seglbl_weak',
#'/home/user/Disk1.8T/draw_result/augmentations/RandomSampleCrop',
# '/home/user/Disk1.8T/draw_result/augmentations/RandomSampleCrop_seglbl',
# '/home/user/Disk1.8T/draw_result/augmentations/RandomSampleCrop_seglbl_weak',

'/home/user/Disk1.8T/data_set/cityspaces/concat_channel/bochum'
]

for folder in folder_name:

    file_name = os.listdir(folder)
    for idx in file_name:
        #img = cv2.imread(folder+ '/' + idx)
        img = m.imread(folder +"/"+ idx)
        #img_1 = m.imread("/home/user/Disk1.8T/unicoe/pytorch-ssd-2/data/VOCdevkit/VOC0712/JPEGImages/" + idx.split(".")[0] + ".jpg")
        #cv2.imwrite("/home/user/Disk1.8T/A_img/" + idx, img)
        #plt.figure(figsize=(12.8*2, 4.8*2))
        #plt.subplot(121)
        plt.imshow(img)
        #plt.subplot(122)
        #plt.imshow(img_1)
        plt.show()
