import os
import re

import cv2

from xmlFormat import generate_xml

root_path = '/home/peiyuyang/data/INRIA'
test_lst_file_path = '/home/peiyuyang/data/INRIA/Test/pos.lst'
anno_path = '/home/peiyuyang/data/INRIA/Test/annotations'

pattern1 = '\(Xmin, Ymin\) - \(Xmax, Ymax\) : \(\d+, \d+\) - \(\d+, \d+\)'
pattern2 = '\d+'

pos_lst_file = open(test_lst_file_path)
pos_lst = pos_lst_file.readlines()
name_lst = []
for lst in pos_lst:
    name_lst.append(lst.split('/')[2].split('.')[0])
for lst in name_lst:
    anno_file_path = os.path.join(anno_path,lst + '.txt')
    anno_file = open(anno_file_path)
    anno_content = anno_file.read()
    bboxs_loc = re.findall(pattern1,anno_content)

    info_list = []

    for bbox_loc in bboxs_loc:

        info_dict = {'file_name': '', 'class': '', 'xmin': '', 'ymin': '', 'xmax': '', 'ymax': ''}

        bbox_loc = re.findall(pattern2,bbox_loc)
        xmin = bbox_loc[0]
        ymin = bbox_loc[1]
        xmax = bbox_loc[2]
        ymax = bbox_loc[3]

        info_dict['class'] = 'person'
        info_dict['xmin'] = xmin
        info_dict['ymin'] = ymin
        info_dict['xmax'] = xmax
        info_dict['ymax'] = ymax
        info_list.append(info_dict)

        floder = 'Annotations_xml'
        file_name = lst
        save_path = os.path.join(root_path, floder, file_name + '.xml')
        #judgeDir(os.path.join(xml_path, set_path))
        #judgeDir(os.path.join(xml_path, set_path, v_path))
        generate_xml(floder, file_name + '.jpg', save_path, info_list)
