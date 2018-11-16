import os
import re

import cv2

root_path = '/home/peiyuyang/data/INRIA'
train_lst_file_path = '/home/peiyuyang/data/INRIA/Train/pos.lst'
anno_path = '/home/peiyuyang/data/INRIA/Train/annotations'
save_path = '/home/peiyuyang/data/INRIA/visualization'
pattern1 = '\(Xmin, Ymin\) - \(Xmax, Ymax\) : \(\d+, \d+\) - \(\d+, \d+\)'
pattern2 = '\d+'

pos_lst_file = open(train_lst_file_path)
pos_lst = pos_lst_file.readlines()
name_lst = []
for lst in pos_lst:
    name_lst.append(lst.split('/')[2].split('.')[0])
for lst in name_lst:
    anno_file_path = os.path.join(anno_path,lst + '.txt')
    anno_file = open(anno_file_path)
    anno_content = anno_file.read()
    bboxs_loc = re.findall(pattern1,anno_content)
    for bbox_loc in bboxs_loc:
        bbox_loc = re.findall(pattern2,bbox_loc)
        xmin = int(bbox_loc[0])
        ymin = int(bbox_loc[1])
        xmax = int(bbox_loc[2])
        ymax = int(bbox_loc[3])
        im_path = os.path.join('/home/peiyuyang/data/INRIA/Train/pos', lst + '.png')
        im = cv2.imread(im_path)
        cv2.rectangle(im, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 1)
        cv2.imwrite(save_path+'/'+lst+'.png', im)

        print

