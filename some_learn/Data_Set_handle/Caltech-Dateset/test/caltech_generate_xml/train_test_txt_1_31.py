import os
import random

trainval_percent = 1
train_percent = 0.9
xmlfilepath = '/home/user/Downloads/caltech_data_set/Caltech2VOC/trainval/annotations'
txtsavepath = '/home/user/Downloads/caltech_data_set/Caltech2VOC/trainval/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('/home/user/Downloads/caltech_data_set/Caltech2VOC/trainval/ImageSets/Main/trainval.txt', 'a+')
ftest = open('/home/user/Downloads/caltech_data_set/Caltech2VOC/trainval/ImageSets/Main/test.txt', 'a+')
ftrain = open('/home/user/Downloads/caltech_data_set/Caltech2VOC/trainval/ImageSets/Main/train.txt', 'a+')
fval = open('/home/user/Downloads/caltech_data_set/Caltech2VOC/trainval/ImageSets/Main/val.txt', 'a+')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()