# -*- coding: utf-8 -*-
# @Time    : 18-12-2 下午12:12
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : find_lst.py
# @Software: PyCharm

train_val_lst = []

rf1 = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/k_fold_cv/train_val_lst/tune_trainval_12_2.txt", "r")

content = rf1.readline()

while content:

    im_name = content.strip("\n")
    train_val_lst.append(im_name)

    content = rf1.readline()

train_lst = []

rf2 = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/mscnn/ImageSets/val.txt", "r")

content1 = rf2.readline()

while content1:

    im_name1 = content1.strip("\n")
    train_lst.append(im_name1)

    content1 = rf2.readline()


wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/k_fold_cv/train_val_lst/val_for_train.txt", "w")

for idx in train_val_lst:
    if idx in train_lst:
        wf.write(idx)
        wf.write("\n")
wf.close()