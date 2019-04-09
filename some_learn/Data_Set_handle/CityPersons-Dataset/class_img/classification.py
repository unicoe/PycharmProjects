# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import cv2
import scipy.misc as m
import shutil

folder_name = [

# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/aachen',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/bochum',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/bremen',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/cologne',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/darmstadt',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/dusseldorf',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/erfurt',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/hamburg',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/hanover',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/jena',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/krefeld',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/monchengladbach',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/strasbourg',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/stuttgart',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/tubingen',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/ulm',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/weimar',
# '/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/train/zurich',

'/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/val/munster',
'/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/val/lindau',
'/home/user/Disk1.8T/data_set/cityspaces/gtFine_copy/val/frankfurt',


]

# 将各个文件夹下的文件进行分类

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok.'
        return True
    else:

        print path + ' path already exits.'
        return False

for folder in folder_name:
    print(folder)
    city_name = folder.split("/")[-1]
    print(city_name)

    #创建子文件夹
    color_f       = folder+ '/' + city_name +'_color'
    polygons_f    = folder+ '/' + city_name +'_polygons'
    labelIds_f    = folder+ '/' + city_name +'_labelIds'
    instanceIds_f = folder+ '/' + city_name +'_instanceIds'

    mkdir(color_f)
    mkdir(polygons_f)
    mkdir(labelIds_f)
    mkdir(instanceIds_f)

    #列出所有文件夹\文件,进行筛选
    file_name = os.listdir(folder)
    for idx in file_name:
        idx_info = idx.split(".")
        print(idx_info)

        if os.path.isdir(folder+"/"+idx):
            continue

        if(idx_info[1] == "json"):
            print(idx_info[1])
            shutil.move(folder+'/'+idx, polygons_f)
        else:
            cls_info = idx_info[0].split("_")[-1]
            print(idx_info[0])
            print(cls_info)
            if(cls_info == "color"):
                shutil.move(folder + '/' + idx, color_f)
            elif(cls_info == "instanceIds"):
                shutil.move(folder + '/' + idx, instanceIds_f)
            elif(cls_info == "labelIds"):
                shutil.move(folder + '/' + idx, labelIds_f)


# color 是三通道图像
# instanceIds 和 labelIds 都是单通道的

# 组合使用原图和labelIds和instanceIds做实验,看效果.