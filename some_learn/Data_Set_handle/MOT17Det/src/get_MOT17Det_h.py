# -*- coding: utf-8 -*-
import os
import cv2
import matplotlib.pyplot as plt

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + 'ok')
        return True
    else:
        print(path + 'failed!')
        return False

def generate_xml(file_root, file_info, obj, width, height,):

    from lxml.etree import Element, SubElement, tostring
    import pprint
    from xml.dom.minidom import parseString
    import os
    try:
        node_root = Element('annotation')
        node_folder = SubElement(node_root, 'folder')
        node_folder.text = file_info[0]
    except:
        print "error"
    node_filename = SubElement(node_root, 'filename')
    node_filename.text = file_info[1]

    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = str(width)

    node_height = SubElement(node_size, 'height')
    node_height.text = str(height)

    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '3'

    for obj_i in obj:
        print obj_i
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        #node_name.text = 'mouse'
        node_name.text = 'person'

        node_name = SubElement(node_object, 'difficult')
        # node_name.text = 'mouse'
        node_name.text = '0'

        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        #node_xmin.text = '99'
        node_xmin.text = obj_i['xmin']

        node_ymin = SubElement(node_bndbox, 'ymin')
        #node_ymin.text = '358'
        node_ymin.text = obj_i['ymin']

        node_xmax = SubElement(node_bndbox, 'xmax')
        #node_xmax.text = '135'
        node_xmax.text = obj_i['xmax']

        node_ymax = SubElement(node_bndbox, 'ymax')
        #node_ymax.text = '375'
        node_ymax.text = obj_i['ymax']

    xml = tostring(node_root, pretty_print=True)  #格式化显示，该换行的换行
    dom = parseString(xml)
    #file_root = '/home/user/Downloads/caltech_data_set/data_train/'
    # file_root = '/home/user/Downloads/caltech_data_set/30stepsize1_train/'
    file_name = file_root;
    mkdir(file_name)
    fw = open(file_name+"/"+file_info[1].split('.')[0]+".xml", 'w')

    fw.write(xml)
    print "xml _ ok"
    fw.close()

    #for debug
    #print xml

def show_img(data_path):
    # data_path = "/home/unicoe/Desktop/train/MOT17-10"

    gt_path = os.path.join(data_path, "gt")
    img_path = os.path.join(data_path)

    print(gt_path, "\n", img_path)

    gt_info = open(os.path.join(gt_path,"gt.txt"), "r")

    gt_list = []

    for igt in gt_info.readlines():
        gt_list.append(igt)

    print(len(gt_list))

    """
    先遍历链表，对每一个框进行显示
    """
    im_bbox = {}

    for igt in gt_list:
        line_info = igt.strip("\n").split(",")
        if float(line_info[6]) in [1.0]  and float(line_info[7]) in [1.0,2.0] and float(line_info[8]) > 0.55:
            if line_info[0] in im_bbox:
                im_bbox[line_info[0]].append([line_info[2], line_info[3], line_info[4], line_info[5],])
            else:
                im_bbox[line_info[0]] = [[line_info[2], line_info[3], line_info[4], line_info[5],]]

    wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/anno/lst/MOT2017Det_6_24_05.txt", "aw")

    for i_im, i_bbox in im_bbox.items():
        #print(i_im, i_bbox)
        pre_zero = ""
        for izero in range(6 - len(i_im)):
            pre_zero += '0'

        im_name = pre_zero + i_im + '.jpg'

        #im = cv2.imread(os.path.join(img_path, im_name))
        im = plt.imread(os.path.join(img_path, im_name))
        img_h, img_w = im.shape[0:2]
        fileInfo=[]
        fileInfo.append(data_path.split("/")[-1])
        fileInfo.append(im_name)

        # 将一张图片中所有的框集合起来，然后再画出来
        obj = []
        for i in i_bbox:
            x1 = max(1,int(i[0]))
            y1 = max(1,int(i[1]))
            w  = min(int(i[2]),img_w)
            h  = min(int(i[3]),img_h)
            if h > 40:
                #print(w/(h+0.0))
                #cv2.rectangle(im, (x1, y1), (x1 + w, y1 + h), (255, 0, 0), 3)
                cor_dict = {}
                cor_dict["xmin"] = str(x1  )
                cor_dict["ymin"] = str(y1  )
                cor_dict["xmax"] = str(x1+w)
                cor_dict["ymax"] = str(y1+h)
                obj.append(cor_dict)

        if len(obj) != 0:
            target_path = os.path.join("/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/anno/19_6_24/",
                                       data_path.split("/")[-1])
            # mkdir(target_path)
            # generate_xml(target_path, fileInfo, obj, width=img_w, height=img_h)
            wf.write(data_path.split("/")[-1]+"/"+im_name.split(".")[0])
            wf.write('\n')
            with open('/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/train_h05.txt', 'aw') as f_h:
                f_h.write(str(h))
                f_h.write("\n")



if __name__ == "__main__":

    path_ls = [
        #"/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-02",
         #"/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-04",
         #"/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-09",
        #"/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-10",
        #"/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-11",
        #"/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-13",

        "/home/user/Disk1.8T/data_set/MOT17Det/train/MOT17-05",
    ]

    for i_p in path_ls:
        show_img(i_p)