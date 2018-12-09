# -*- coding: utf-8 -*-
# @Time    : 18-12-7 下午4:45
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : split_train_val.py
# @Software: PyCharm

trainval_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/caltech1x_ls.txt","r")

trainval_ls = []

trainval_item = trainval_r.readline()

while trainval_item:

    item_tmp = trainval_item.strip("\n")
    trainval_ls.append(item_tmp)
    trainval_item = trainval_r.readline()


train_w = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/train.txt", "w")
val_w   = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/val.txt", "w")


for i in range(len(trainval_ls)):
    if i % 2 == 0:
        val_w.write(trainval_ls[i])
        val_w.write("\n")
    else:
        train_w.write(trainval_ls[i])
        train_w.write("\n")

val_w.close()
train_w.close()