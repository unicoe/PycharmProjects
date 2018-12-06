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
    cur_path = "/home/user/py-R-FCN/data/VOCdevkit0712/VOC0712/JPEGImages/"
    dirList = []
    fileList = []
    files = os.listdir(cur_path)

    for file in files:
        tmp_path = file.split('.')[0]
        dirList.append(tmp_path)

    for dir_ in dirList:
        if dir_ in tmp_dict:
            gtList = tmp_dict[dir_]
            im_path = cur_path+dir_+".jpg"
            im = cv2.imread(im_path)
            # im = im[:, :, (2, 1, 0)]
            # fig, ax = plt.subplots(figsize=(1, 1))
            # ax.imshow(im, aspect='equal')

            for idx_gt in gtList:
                for idx_gb in idx_gt:
                    #'475 172 488 225'  是 x1 y1 x2 y2的格式
                    idx_bbx = "".join(idx_gb).split(' ')

                    x1 = int(idx_bbx[0])
                    y1 = int(idx_bbx[1])
                    x2 = int(idx_bbx[2])
                    y2 = int(idx_bbx[3])

                    w = x2 - x1
                    h = y2 - y1

                    """
                    将gt划分区域
                    #line(img, pt1, pt2, co lor, thickness=None, lineType=None, shift=None)
                    """
                    #--debug
                    # cv2.line(im,(x1+w/2,y1),(x1+w/2, y1+h) , (225, 255, 0), 1)
                    # cv2.line(im,(x1,y1+h/3),(x1+w, y1+h/3) , (225, 255, 0), 1)
                    # cv2.line(im,(x1,y1+h*2/3),(x1+w, y1+h*2/3) , (225, 255, 0), 1)


                    #--等距离划分
                    # divide_num_x = 5
                    # for i in xrange(1,divide_num_x):
                    #     cv2.line(im, (x1 + i*w / divide_num_x, y1), (x1 + i*w / divide_num_x, y1 + h), (225, 255, 0), 1)
                    #
                    # divide_num_y = 5
                    # for i in xrange(1,divide_num_y):
                    #     cv2.line(im, (x1, y1 + i*h / divide_num_y), (x1 + w, y1 + i*h / divide_num_y), (225, 255, 0), 1)
                    #
                    # cv2.rectangle(im,(x1,y1),(x2, y2) , (225, 255, 0), 1)
                    #

                    #--debug尝试的划分方法
                    # cv2.line(im, (x1 + w / 5, y1 + h/4), (x1 + w / 5, y1 + h), (225, 255, 0), 1)
                    # cv2.line(im, (x1 + w*4 / 5, y1 + h / 4), (x1 + w*4 / 5, y1 + h), (225, 255, 0), 1)
                    # cv2.line(im, (x1 + w / 5, y1 + h / 4), (x1 + w * 4 / 5, y1 + h/4), (225, 255, 0), 1)
                    #
                    # cv2.line(im,(x1,y1+h/3),(x1+w, y1+h/3) , (225, 255, 0), 1)
                    # cv2.line(im,(x1,y1+h*2/3),(x1+w, y1+h*2/3) , (225, 255, 0), 1)

                    divide_num_x = 2
                    for i in xrange(1,divide_num_x):
                        cv2.line(im, (x1 + i*w / divide_num_x, y1), (x1 + i*w / divide_num_x, y1 + h), (225, 255, 0), 1)

                    # divide_num_y = 4
                    # for i in xrange(1,divide_num_y):
                    #     cv2.line(im, (x1, y1 + i*h / divide_num_y), (x1 + w, y1 + i*h / divide_num_y), (225, 255, 0), 1)

                    cv2.rectangle(im,(x1,y1),(x2, y2) , (225, 255, 0), 1)




            mkdir('/home/user/Disk1.8T/draw_train_and_test/1_1_2/')
            cv2.imwrite('/home/user/Disk1.8T/draw_train_and_test/1_1_2/' + str(dir_ + ".jpg"),im)

    pass


def des_search(path):
    df = open(path)
    content1 = df.readline()
    tmp_dict2 = {}

    while content1:
        #print content1
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

        #break

        content1 = df.readline()
    df.close()
    return tmp_dict2
    #--debug
    # for key_ in tmp_dict2:
    #     print key_,tmp_dict2[key_]

#从生成的　annotations-set06/V000 这样的文本文档中，读取标注信息，然后用来生成字典，然后从图片目录中读取图片名，然后对比在字典中有无当前的图片名，有的话，去生成ground truth.
file_dict = des_search("/home/user/PycharmProjects/anaylsis_result/draw_result_in_new_anno/gt_file/train_gt.txt")
print file_dict
#
draw_gt(file_dict)