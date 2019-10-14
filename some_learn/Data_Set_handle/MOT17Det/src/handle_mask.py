import cv2
import math
import numpy as np

img_ls = [
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000001.jpg',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000001.png',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000002.jpg',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000002.png',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000003.jpg',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000003.png',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000005.jpg',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000005.png',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000020.jpg',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000020.png',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000052.jpg',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/visibale/000052.png',
]
for im in img_ls:
    tmp_im = cv2.imread(im)
    res = cv2.flip(tmp_im,1,dst=None)
    cv2.imwrite(im,res)