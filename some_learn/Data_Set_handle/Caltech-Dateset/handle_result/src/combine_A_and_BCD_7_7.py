import os
import numpy as np
import cv2
import argparse
from matplotlib import  pyplot as plt

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

parser = argparse.ArgumentParser('create image pairs')
parser.add_argument('--fold_A',
                    dest='fold_A',
                    help='input directory for image A',
                    type=str,
                    default='')
args = parser.parse_args()




ls_a = [

'/home/user/Disk1.8T/draw_result/paper_result/select/2018_12_25_Tue_22_21_37_161/VOC0712/JPEGImages',

]

ls_b = [

'/home/user/Disk1.8T/draw_result/paper_result/select/2019_01_15_Tue_12_09_38_110/VOC0712/JPEGImages',

]

ls_c = [

'/home/user/Disk1.8T/draw_result/paper_result/select/2019_06_20_Thu_00_14_46_68/VOC0712/JPEGImages',

]

ls_d = [

'/home/user/Disk1.8T/draw_result/paper_result/select/2019_06_19_Wed_11_43_49_63/VOC0712/JPEGImages',

]




for i_a in ls_a:
    for i_b in ls_b:
        for i_c in ls_c:
            for i_d in ls_d:
                img_fold_A = os.path.join(i_a)
                img_fold_B = os.path.join(i_b)
                img_fold_C = os.path.join(i_c)
                img_fold_D = os.path.join(i_d)
                img_list = os.listdir(img_fold_D)

                num_imgs = min(1000000, len(img_list))

                # img_fold_AB = os.path.join()

                #if not os.path.isdir(img_fold_AB):
                #    os.makedirs(img_fold_AB)

                for n in range(num_imgs):
                    name_A = img_list[n]
                    path_A = os.path.join(img_fold_A, name_A)

                    name_B = name_A
                    path_B = os.path.join(img_fold_B, name_B)
                    path_C = os.path.join(img_fold_C, name_B)
                    path_D = os.path.join(img_fold_D, name_B)

                    if os.path.isfile(path_D) and os.path.isfile(path_A) is False \
                        and os.path.isfile(path_B) is False \
                        and os.path.isfile(path_C):
                        im_D = cv2.imread(path_D)
                        im_D = cv2.cvtColor(im_D, cv2.COLOR_BGR2RGB)

                        im_C = cv2.imread(path_C)
                        im_C = cv2.cvtColor(im_C, cv2.COLOR_BGR2RGB)

                        im_AB = np.hstack([im_C, im_D])
                        show = True
                        if show:
                            plt.figure(figsize=(64 * 4, 48))
                            plt.title(name_A)
                            # plt.imshow(im_A)
                            # plt.imshow(im_B)
                            plt.imshow(im_AB)
                            plt.show()

                    # if os.path.isfile(path_A)  and os.path.isfile(path_B)\
                    #         and os.path.isfile(path_C) and os.path.isfile(path_D):
                    #     name_AB = name_A
                    #     # mkdir(img_fold_AB)
                    #     # path_AB = os.path.join(img_fold_AB, name_AB)
                    #
                    #     im_A = cv2.imread(path_A)
                    #     im_B = cv2.imread(path_B)
                    #     im_C = cv2.imread(path_C)
                    #     im_D = cv2.imread(path_D)
                    #     im_A =  cv2.cvtColor(im_A, cv2.COLOR_BGR2RGB)
                    #     im_B =  cv2.cvtColor(im_B, cv2.COLOR_BGR2RGB)
                    #     im_C =  cv2.cvtColor(im_C, cv2.COLOR_BGR2RGB)
                    #     im_D =  cv2.cvtColor(im_D, cv2.COLOR_BGR2RGB)
                    #
                    #
                    #     im_AB = np.hstack([im_A, im_B, im_C, im_D])
                    #
                    #     show = True
                    #     if show:
                    #         plt.figure(figsize=(64*4, 48))
                    #         plt.title(name_A)
                    #         # plt.imshow(im_A)
                    #         # plt.imshow(im_B)
                    #         plt.imshow(im_AB)
                    #         plt.show()

                        # save img
                        # cv2.imwrite(path_AB, im_AB)
