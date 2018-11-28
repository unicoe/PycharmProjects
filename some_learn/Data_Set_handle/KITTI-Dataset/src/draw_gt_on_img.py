#--coding:utf-8--

import os
import cv2

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok'
        return True
    else:

        print path + 'failed!'
        return False

def draw_gt(tmp_dict):
    cur_path = "/home/user/Disk1.8T/data_set/KITTI/training/image_2/"
    dirList = []
    fileList = []
    files = os.listdir(cur_path)

    for file in files:
        tmp_path = file.split('.')[0]
        dirList.append(tmp_path)

    for dir_ in dirList:
        if dir_ in tmp_dict:
            gtList = tmp_dict[dir_]
            im_path = cur_path+dir_+".png"
            im = cv2.imread(im_path)

            flag = 0  # 如果有框就进行画图
            for idx_gt in gtList:
                for idx_gb in idx_gt:

                    flag = 1
                    idx_bbx = "".join(idx_gb).split(' ')
                    x1 = int(float(idx_bbx[0]))
                    y1 = int(float(idx_bbx[1]))
                    x2 = int(float(idx_bbx[2]))
                    y2 = int(float(idx_bbx[3]))
                    cv2.rectangle(im,(x1,y1),(x2, y2) , (225, 255, 0), 1)
            if flag == 1:
                mkdir('/home/user/Disk1.8T/data_set/training/image_2_show_trun/')
                cv2.imwrite('/home/user/Disk1.8T/data_set/training/image_2_show_trun/' + str(dir_ + ".png"),im)
    pass

"""
数据返回的格式
set10_V011_I00329 [['508 171 559 284', '397 183 437 283']]
"""
def des_search(path):
    df = open(path)
    content1 = df.readline()
    tmp_dict2 = {}

    while content1:
        det = content1.replace("\n", "").split(",")
        cls1 = det[0]
        bbox = []
        for i in xrange(1, len(det), 1):
            if det[i] is not '':
                bbox.append(det[i].strip())

        if cls1 in tmp_dict2:
            tmp_dict2[cls1].append(bbox)
        else:
            tmp_dict2[cls1] = [bbox]

        content1 = df.readline()
    df.close()
    return tmp_dict2
    #--debug
    # for key_ in tmp_dict2:
    #      print key_,tmp_dict2[key_]

#读取标注信息，然后用来生成字典，然后从图片目录中读取图片名，然后对比在字典中有无当前的图片名，有的话，去生成ground truth.
file_dict = des_search("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/lst/trun_11_18.txt")
print file_dict
#
draw_gt(file_dict)



"""
通过read_kitti 得到有标注的文本，然后进行画图
"""

