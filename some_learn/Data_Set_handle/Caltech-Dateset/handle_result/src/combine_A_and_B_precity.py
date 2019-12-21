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
"/home/user/Disk1.8T/unicoe/pytorch-ssd-2-1/experments/6_180_seg_merge_base512/fcn_visual110000",


]

ls_b = [

'/home/user/Disk1.8T/unicoe/pytorch-ssd-2-1/experments/6_180_seg_merge_base512/visual120000/',

]

# ls_c = [
#
# '/home/user/Disk1.8T/unicoe/pytorch-ssd-2/experments/3_261_seg_merge_base512/visual110000',
#
# ]
#
# ls_d = [
#
# '/home/user/Disk1.8T/unicoe/pytorch-ssd-2/experments/3_261_seg_merge_base512/visual110000',
#
# ]




for i_a in ls_a:
    for i_b in ls_b:
        img_fold_A = os.path.join(i_a)
        img_fold_B = os.path.join(i_b)
        img_list = os.listdir(img_fold_A)

        num_imgs = min(1000000, len(img_list))

        # img_fold_AB = os.path.join()

        #if not os.path.isdir(img_fold_AB):
        #    os.makedirs(img_fold_AB)

        for n in range(num_imgs):
            name_A = img_list[n]
            path_A = os.path.join(img_fold_A, name_A)

            name_B = name_A
            path_B = os.path.join(img_fold_B, name_B)
            if os.path.isfile(path_A) and os.path.isfile(path_B):
                name_AB = name_A
                # mkdir(img_fold_AB)
                # path_AB = os.path.join(img_fold_AB, name_AB)
                path_AB = "/home/user/Disk1.8T/draw_result/ssd_fcn/combine_ab1/" + name_AB
                im_A = cv2.imread(path_A)
                im_B = cv2.imread(path_B)

                im_AB = np.vstack([im_A, im_B])

                show = False
                if show:
                    plt.figure(figsize=(12.8 * 2, 4.8 * 2))
                    plt.title(name_A)
                    plt.imshow(im_A)
                    plt.imshow(im_B)
                    plt.imshow(im_AB)
                    plt.show()

                # save img
                cv2.imwrite(path_AB, im_AB)
