import os
import numpy as np
import cv2
import argparse
from matplotlib import  pyplot as plt
import scipy.misc as m

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + ' create successful.'
        return True
    else:

        print path + ' path already exists.'
        return False


ls_a = [

'/home/user/Disk1.8T/draw_result/augmentations/seglbl_visible_6_4/',

]

ls_b = [

'/home/user/Disk1.8T/draw_result/augmentations/seglbl_6_4/',

]

for i_b in ls_b:
    for i_a in ls_a:
        img_fold_A = os.path.join(i_a)
        img_fold_B = os.path.join(i_b)
        img_list = os.listdir(img_fold_A)

        num_imgs = min(1000000, len(img_list))

        # img_fold_AB_tmp = img_fold_B.split('seglabel_png_3_18_test/')
        # img_fold_AB = os.path.join(img_fold_AB_tmp[0],'seglabel_png_3_18_test', 'combime')
        #img_fold_AB =
        #if not os.path.isdir(img_fold_AB):
        #    os.makedirs(img_fold_AB)

        for n in range(num_imgs):
            name_A = img_list[n]
            path_A = os.path.join(img_fold_A, name_A)

            name_B = name_A.split(".")[0]+".png"
            path_B = os.path.join(img_fold_B, name_B)
            if os.path.isfile(path_A) and os.path.isfile(path_B):
                name_AB = name_A
                # mkdir(img_fold_AB)
                # path_AB = os.path.join(img_fold_AB, name_AB)

                im_A = cv2.imread(path_A)
                im_B = cv2.imread(path_B)

                # com_AB = 1*im_A + 1*im_B

                im_AB = np.hstack([im_A[:,:,0], im_B[:,:,0]])

                show = True
                if show:
                    #plt.subplot(121)
                    #plt.imshow(im_A)
                    #plt.subplot(122)
                    #plt.imshow(com_AB)
                    plt.imshow(im_AB)
                    plt.show()

                # save img
                # print(path_AB)
                # cv2.imwrite(path_AB, im_AB)
