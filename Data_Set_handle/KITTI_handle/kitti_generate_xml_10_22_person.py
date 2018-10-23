#--coding:utf-8--
"""
生成kitti的标注
"""

import os

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
    node_width.text = '1224'

    node_height = SubElement(node_size, 'height')
    node_height.text = '370'

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
    mkdir(file_name)
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
            #print '-' * (int(dirList[0])), dl
            folder_struct((int(dirList[0]) + 1), path+'/'+dl)

    print fileList
    print dirList
    cnt = 0
    wf = open("/home/user/PycharmProjects/Data_Set_handle/kitti_data/person_10_22.txt", "w")
    print len(fileList)
    for fl in fileList:
        #todo 遍历txt文件，然后根据txt文件生成xml文件
        tmp = path + "/" + fl

        rtmp = open(tmp, "r")
        # wf.write(fl)
        # wf.write("----")
        # wf.write('\n')
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
                flag = 1

                cnt += 1
                cor_dict = {}
                tmpv = []
                tmpv = contx.split(" ")
                print tmpv
                if tmpv[0] in ['Pedestrian', 'Person_sitting']:
                    if tmpv[2] in ['0', '1']:
                        # bbox_info = str(float(data[4])) + " " + str(float(data[5])) + " " + str(float(data[6])) + " " + str(float(data[7]))
                        print "tmpv" + str(tmpv)
                        xmin = str(max(0,int(float(tmpv[4]))))
                        ymin = str(max(0,int(float(tmpv[5]))))
                        xmax = str(min(int(float(tmpv[4])) + int(float(tmpv[6])),1244))
                        ymax = str(min(int(float(tmpv[5])) + int(float(tmpv[7])), 370))

                        cor_dict["xmin"] = xmin
                        cor_dict["ymin"] = ymin
                        cor_dict["xmax"] = xmax
                        cor_dict["ymax"] = ymax

                        obj.append(cor_dict)
            else:
                if flag == 0:
                    fileInfo.append("VOC0712")
                    fileInfo.append(fl.split('.')[0]+'.jpg')
                flag = 1

        generate_xml("/home/user/PycharmProjects/Data_Set_handle/kitti_data/person_10_22/", fileInfo, obj)
        wf.write(fl.split('.')[0])
        wf.write('\n')
    print cnt
    #wf.write(cnt)
    pass
    wf.close()


#folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/caltechx10/train/annotations")
folder_struct(1, "/home/user/Disk1.8T/data_set/training/label_2/")
