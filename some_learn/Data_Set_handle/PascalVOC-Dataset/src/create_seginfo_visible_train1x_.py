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


def generate_xml(file_root, file_info, obj):
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
    node_width.text = '640'

    node_height = SubElement(node_size, 'height')
    node_height.text = '480'

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
    file_name = file_root + file_info[0];
    mkdir.mkdir(file_name)
    fw = open(file_name+"/"+file_info[1].split('.')[0]+".xml", 'w')

    fw.write(xml)
    print "xml _ ok"
    fw.close()

    #for debug
    #print xml



def folder_struct(level, path):
    global allFileNum

    dirList = []
    fileList = []
    files = os.listdir(path)
    dirList.append(str(level))

    for f in files:
        if(os.path.isdir(path + '/' + f)):
            if f[0] != '.':
                dirList.append(f)
        if (os.path.isfile(path + '/' + f)):
            fileList.append(f)

    i_dl = 0
    for dl in dirList:
        if i_dl == 0:
            i_dl = i_dl + 1
        else:
            folder_struct((int(dirList[0]) + 1), path+'/'+dl)

    cnt = 0

    gt_info = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/gt_info_visible_zss.txt", "w")
    cur_path = "/home/user/py-R-FCN/data/VOCdevkit0712/VOC0712/JPEGImages/"

    print len(fileList)
    for fl in fileList:
        #todo 遍历txt文件，然后根据txt文件生成xml文件
        tmp = path + "/" + fl

        rtmp = open(tmp, "r")
        contx = rtmp.readline()

        fileInfo = []
        obj = []
        cor_dict = {}
        flag = 0

        while contx:
            contx = rtmp.readline()
            if contx:

                if flag == 0:
                    fileInfo.append("VOC0712")
                    fileInfo.append(fl.split('.')[0]+'.jpg')
                    im_path = cur_path + fl.split('.')[0]+'.jpg'
                    gt_info.write("\n")
                    gt_info.write(fl.split('.')[0])
                    gt_info.write(" ")
                flag = 1

                cnt += 1
                cor_dict = {}
                tmpv = []
                tmpv = contx.split(" ")

                if tmpv[0] == "person":
                    for idx in range(1,5):
                        tmpv[idx] = int(float(tmpv[idx]))
                        tmpv[idx+5] = int(float(tmpv[idx+5]))

                    xmin = str(max(1,tmpv[1]))
                    ymin = str(max(1,tmpv[2]))
                    xmax = str(min(tmpv[1] + tmpv[3],640))
                    ymax = str(min(tmpv[2] + tmpv[4], 480))

                    if tmpv[5] == '1':
                        v_xmin = str(max(1, tmpv[6]))
                        v_ymin = str(max(1, tmpv[7]))
                        v_xmax = str(min(tmpv[6] + tmpv[8], 640))
                        v_ymax = str(min(tmpv[7] + tmpv[9], 480))

                        bbox_size = (int(xmax) - int(xmin)) * (int(ymax) - int(ymin))
                        vis_bbox_size = (int(v_xmax) - int(v_xmin)) * (int(v_ymax) - int(v_ymin))

                        rate = vis_bbox_size / (bbox_size + 0.0)

                    w = int(xmax) - int(xmin)
                    h = int(ymax) - int(ymin)

                    # if tmpv[5] == '0' or rate >= 0.3:
                    #     if h >= 20 and w >= 10:
                    #     cor_dict = {}
                    #     cor_dict["xmin"] = v_xmin
                    #     cor_dict["ymin"] = v_ymin
                    #     cor_dict["xmax"] = v_xmax
                    #     cor_dict["ymax"] = v_ymax
                    if tmpv[5] == '1':
                        gt_info.write(v_xmin)
                        gt_info.write(",")
                        gt_info.write(v_ymin)
                        gt_info.write(",")
                        gt_info.write(v_xmax)
                        gt_info.write(",")
                        gt_info.write(v_ymax)
                        gt_info.write(" ")
                        # rate = 0
                    else:
                        gt_info.write(xmin)
                        gt_info.write(",")
                        gt_info.write(ymin)
                        gt_info.write(",")
                        gt_info.write(xmax)
                        gt_info.write(",")
                        gt_info.write(ymax)
                        gt_info.write(" ")

            else:
                if flag == 0:
                    fileInfo.append("VOC0712")
                    fileInfo.append(fl.split('.')[0]+'.jpg')
                flag = 1


        if len(obj) != 0:

            pass
    print cnt
    pass
    gt_info.close()


folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/anno_train_1xnew")
