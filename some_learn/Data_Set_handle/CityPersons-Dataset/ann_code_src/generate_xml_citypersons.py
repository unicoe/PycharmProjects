# -*- coding: utf-8 -*-
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
    node_width.text = '2048'

    node_height = SubElement(node_size, 'height')
    node_height.text = '1024'

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


def extrat_info():
    rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/ann_code_src/ann_file/ann_train_aligned.txt", "r")
    # wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/ann_code_src/ann_file/trainval_lst" \
    #           "/train_3_11_40_0.6.txt", "w")
    contx = rf.readline()
    ctx_str = ""

    ctx_dict ={}
    im_list = []
    cnt = 0
    cnt1 = 0
    while contx:

        if contx[0].isalpha():
            contx = contx.replace(" ","/")

            tmp = contx
            ctx_dict[tmp] = []
            im_list.append(tmp)
        elif contx[0].isalnum() and contx[0] > '0' and contx[0] <= '3':   #对类别进行筛选
        #elif contx[0].isalnum():                                          #不进行筛选
            contx = contx.strip("\n").strip(" ")
            cnt = cnt+1
            ctx_dict[tmp].append(contx)
        elif contx[0].isalnum() and contx[0]== '0':
            cnt1 += 1
        elif contx[0] == "\n":
            if len(ctx_dict[tmp]) > 0:  #  对没有标注的图片进行筛选
            #if len(ctx_dict[tmp])>=0:    #  不进行筛选
                pass
                # wf.write(tmp.split('.')[0])
                # wf.write("\n")
        contx = rf.readline()

    rf.close()
    # wf.close()
    return ctx_dict

ctx_dict = extrat_info()

wf = open(
    "/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/ann_code_src/ann_file/trainval_lst" \
    "/train_3_11_40_0.6.txt", "w")

for k,v in ctx_dict.items():
    folderName,fileName = k.split("/")



    # 保存标注的文件
    mkdir("/home/user/PycharmProjects/some_learn/CityPersons_handle/ann_code_src/ann_file/anno_3_11_40_0.6/")
    root_file = "/home/user/PycharmProjects/some_learn/CityPersons_handle/ann_code_src/ann_file/anno_3_11_40_0.6/"

    fileInfo=[]
    obj = []
    cor_dict = {}

    fileInfo.append(folderName)
    fileInfo.append(fileName)

    img_root = "/home/user/Disk1.8T/py-R-FCN/data/VOCdevkit0712(citypersons)/VOC0712/JPEGImages"
    im_path = img_root + "/" + folderName + "/" + fileName.split("\n")[0]
    print(fileName.split("\n")[0])
    if v:
        for v_i in v:
            tmpv = v_i.split(" ")
            print tmpv
            xmin = str(max(1,int(tmpv[1])))
            ymin = str(max(1,int(tmpv[2])))
            xmax = str(min(2048,int(tmpv[1])+int (tmpv[3])))
            ymax = str(min(1024,int(tmpv[2])+int (tmpv[4])))

            v_xmin = str(max(1, int(tmpv[6])))
            v_ymin = str(max(1, int(tmpv[7])))
            v_xmax = str(min(2048, int(tmpv[6]) + int(tmpv[8])))
            v_ymax = str(min(1024, int(tmpv[7]) + int(tmpv[9])))

            orginal_size = (int(ymax)-int(ymin))*(int(xmax)-int(xmin))
            v_size = (int(v_ymax)-int(v_ymin))*(int(v_xmax)-int(v_xmin))

            ratio = v_size / (orginal_size+0.0)

            if int(ymax) - int(ymin) >= 40  and ratio >= 0.6:
                cor_dict = {}
                cor_dict["xmin"] = xmin
                cor_dict["ymin"] = ymin
                cor_dict["xmax"] = xmax
                cor_dict["ymax"] = ymax
                obj.append(cor_dict)

        if len(obj) > 0:
            generate_xml(root_file, fileInfo, obj)
            wf.write(folderName + "/" + fileName.split("\n")[0].split(".")[0])
            wf.write("\n")
wf.close()