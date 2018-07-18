#--coding:utf-8--
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

        node_object1 = SubElement(node_root, 'object')
        node_name1 = SubElement(node_object1, 'name')
        node_name1.text = 'upper'
        node_name1 = SubElement(node_object1, 'difficult')
        # node_name.text = 'mouse'
        node_name1.text = '0'

        node_bndbox1 = SubElement(node_object1, 'bndbox')
        node_xmin1 = SubElement(node_bndbox1, 'xmin')
        # node_xmin.text = '99'
        node_xmin1.text = obj_i['upper_xmin']

        node_ymin1 = SubElement(node_bndbox1, 'ymin')
        # node_ymin.text = '358'
        node_ymin1.text = obj_i['upper_ymin']

        node_xmax1 = SubElement(node_bndbox1, 'xmax')
        # node_xmax.text = '135'
        node_xmax1.text = obj_i['upper_xmax']

        node_ymax1 = SubElement(node_bndbox1, 'ymax')
        # node_ymax.text = '375'
        node_ymax1.text = obj_i['upper_ymax']

        node_object2 = SubElement(node_root, 'object')
        node_name2 = SubElement(node_object2, 'name')
        node_name2.text = 'head'
        node_name2 = SubElement(node_object2, 'difficult')
        # node_name.text = 'mouse'
        node_name2.text = '0'

        node_bndbox2 = SubElement(node_object2, 'bndbox')
        node_xmin2 = SubElement(node_bndbox2, 'xmin')
        # node_xmin.text = '99'
        node_xmin2.text = obj_i['head_xmin']

        node_ymin2 = SubElement(node_bndbox2, 'ymin')
        # node_ymin.text = '358'
        node_ymin2.text = obj_i['head_ymin']

        node_xmax2 = SubElement(node_bndbox2, 'xmax')
        # node_xmax.text = '135'
        node_xmax2.text = obj_i['head_xmax']

        node_ymax2 = SubElement(node_bndbox2, 'ymax')
        # node_ymax.text = '375'
        node_ymax2.text = obj_i['head_ymax']

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
            #print '-' * (int(dirList[0])), dl
            folder_struct((int(dirList[0]) + 1), path+'/'+dl)

    # print fileList
    # print dirList
    cnt = 0
    wf = open("/home/user/PycharmProjects/caltech_new_anno/head_upper_full_newtrain1x.txt", "w")
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
                if tmpv[0] == "person":
                    xmin = str(max(1,int(float(tmpv[1]))))
                    ymin = str(max(1,int(float(tmpv[2]))))
                    xmax = str(min(int(float(tmpv[1])) + int(float(tmpv[3])),640))
                    ymax = str(min(int(float(tmpv[2])) + int(float(tmpv[4])), 480))

                    if tmpv[5] == '1':
                        v_xmin = str(max(1,int(float(tmpv[6]))))
                        v_ymin = str(max(1,int(float(tmpv[7]))))
                        v_xmax = str(min(int(float(tmpv[6])) + int(float(tmpv[8])),640))
                        v_ymax = str(min(int(float(tmpv[7])) + int(float(tmpv[9])),480))

                        bbox_size = (int(xmax)-int(xmin))*(int(ymax)-int(ymin))
                        vis_bbox_size = (int(v_xmax)-int(v_xmin))*(int(v_ymax)-int(v_ymin))

                        rate = vis_bbox_size / (bbox_size + 0.0)


                    # x1 = (xmax - xmin)/2. + 0.2*((xmax - xmin)/2.)
                    # x2 = (xmax - xmin)/2. + 0.8*((xmax - xmin)/2.)
                    # y1 = (ymax - ymin)/2. + 0.1*((ymax - ymin)/2.)
                    # y2 = (ymax - ymin)/2. + 0.9*((ymax - ymin)/2.)

                    if tmpv[5] == '0' or rate > 0.65:
                        cor_dict = {}
                        # 生成全身bbox
                        cor_dict["xmin"] = xmin
                        cor_dict["ymin"] = ymin
                        cor_dict["xmax"] = xmax
                        cor_dict["ymax"] = ymax

                        #生成上半身bbox
                        tmp_y = ymax
                        ymax = str(int(int(ymin) + 0.6 * (int(ymax) - int(ymin))))
                        cor_dict["upper_xmin"] = xmin
                        cor_dict["upper_ymin"] = ymin
                        cor_dict["upper_xmax"] = xmax
                        cor_dict["upper_ymax"] = ymax

                        #生成头肩bbox
                        ymax = str(int(int(ymin) + 0.35 * (int(tmp_y) - int(ymin))))
                        cor_dict["head_xmin"] = xmin
                        cor_dict["head_ymin"] = ymin
                        cor_dict["head_xmax"] = xmax
                        cor_dict["head_ymax"] = ymax
                        obj.append(cor_dict)
                        rate = 0
                # wf.write(str(tmpv))
                # wf.write('\n')
                        print cor_dict
            else:
                if flag == 0:
                    fileInfo.append("VOC0712")
                    fileInfo.append(fl.split('.')[0]+'.jpg')
                flag = 1
        #train
        if flag == 1:
            #generate_xml("/home/user/PycharmProjects/caltech_new_anno/annos/", fileInfo, obj)
            #print fl
            #wf.write(fl.split('.')[0])
            # wf.write('\n')
            pass
        #test
        generate_xml("/home/user/PycharmProjects/caltech_new_anno/head_vis_0.6_6_13_head_upper_full_new1x/", fileInfo, obj)
        wf.write(fl.split('.')[0])
        wf.write('\n')
    print cnt
    #wf.write(cnt)
    pass
    wf.close()

"""
生成头肩、上半身、全身的标注，用来训练，
"""
#folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/caltechx10/train/annotations")
folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/anno_train_1xnew")
