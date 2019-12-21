# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
import argparse
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import torchvision.transforms as transforms
from torch.autograd import Variable

import sys
sys.path.append('/home/user/Disk1.8T/unicoe/pytorch-ssd-2')

import torch.utils.data as data
import time
import skimage.io
import numpy as np
import pdb
from .fcn_visual_utils import visualize_segmentation,get_tile_image
from .mkdir import mkdir
import cv2


def tes_net():
    # dump predictions and assoc. ground truth to text file for now
    # pdb.set_trace()
    img = cv2.imread("/home/user/Disk1.8T/submit_teacher/anno/000197.jpg")
    lbl_pred = cv2.imread("/home/user/Disk1.8T/submit_teacher/anno/000197.png")


    # 转换成功
    # TODO 引入图片seg_gt,进行结果可视化 19/1/6 21:48
    img = img

    # print(img.shape)
    # print("img shape: before visual")
    print(lbl_pred)
    lbl_pred = lbl_pred[0, :, :]
    print(lbl_pred)


    #print(img.shape)
    visualizations=[]
    viz = visualize_segmentation(
        lbl_pred=lbl_pred,
        img=img,
        n_class=20,
        label_names= np.array(['background','person',])
    )
    visualizations.append(viz)


    # viz = get_tile_image(visualizations)
    # skimage.io.imsave('/home/user/Disk1.8T/unicoe/pytorch-ssd-2/experments/8_220_seg_merge_base512/visual/viz_evaluate.png', viz)
    # 替换保存方式,将所有语义分割的测试结果都保存,然后看效果,
    mkdir("/home/user/Disk1.8T/unicoe/pytorch-ssd-2/experments/8_220_seg_merge_base512/visual" + get_model_id)

    for i_vis in range(len(visualizations)):
        skimage.io.imsave(
            "/home/user/Disk1.8T/unicoe/pytorch-ssd-2/experments/8_220_seg_merge_base512/visual" + get_model_id + "/" + str(
            i_vis) + ".png", visualizations[i_vis])


tes_net()