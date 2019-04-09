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

parser = argparse.ArgumentParser('create image pairs')
parser.add_argument('--fold_A',
                    dest='fold_A',
                    help='input directory for image A',
                    type=str,
                    default='/home/user/Disk1.8T/data_set/seglabel_png_3_18_test/')
args = parser.parse_args()




ls_a = [

'/home/user/Disk1.8T/unicoe/pytorch-ssd-2/data/VOCdevkit/VOC0712/JPEGImages/',

]

ls_b = [

'/home/user/Disk1.8T/data_set/seglabel_png_3_18_test/',

]



# for arg in vars(args):
#     print('[%s] = ' % arg,  getattr(args, arg))

splits = os.listdir(args.fold_A)

for sp in splits:
    for i_b in ls_b:
        for i_a in ls_a:
            # if i_b in ls_a:
            img_fold_A = os.path.join(i_a)
            img_fold_B = os.path.join(i_b)
            img_list = os.listdir(img_fold_A)

            num_imgs = min(1000000, len(img_list))

            img_fold_AB_tmp = img_fold_B.split('seglabel_png_3_18_test/')
            img_fold_AB = os.path.join(img_fold_AB_tmp[0],'seglabel_png_3_18_test', 'combime')
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
                    mkdir(img_fold_AB)
                    path_AB = os.path.join(img_fold_AB, name_AB)

                    im_A = cv2.imread(path_A)
                    im_B = m.imread(path_B)

                    #im_AB = np.hstack([im_A, im_B])

                    show = True
                    if show:
                        plt.imshow(im_A)
                        plt.show()
                        plt.imshow(im_B)
                        #plt.imshow(im_AB)
                        plt.show()

                    # save img
                    print(path_AB)
                    # cv2.imwrite(path_AB, im_AB)
