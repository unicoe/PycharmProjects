# -*- coding: utf-8 -*-
# @Time    : 18-12-2 上午10:58
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : k_fold_cv.py
# @Software: PyCharm

trainval_lst = []

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/mscnn/ImageSets/trainval.txt", "r")

content = rf.readline()

while content:

    im_name = content.strip("\n")
    trainval_lst.append(im_name)
    content = rf.readline()


print trainval_lst


train_w = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/k_fold_cv/train_val_lst/train2.txt","w")
val_w   = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/k_fold_cv/train_val_lst/val2.txt","w")


k = 2

for i in range(len(trainval_lst)):

    if i % 5 == 0 and i != 0:
        k = k + 5

    if i == k :
        print k
        val_w.write(trainval_lst[i])
        val_w.write("\n")
    else:
        train_w.write(trainval_lst[i])
        train_w.write("\n")

train_w.close()
val_w.close()