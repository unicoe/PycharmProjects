#!/usr/bin/env python
# coding:utf-8

#from xml.etree.ElementTree import Element, SubElement, tostring
from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString
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

def generate_xml(file_info, obj):
    node_root = Element('annotation')

    node_folder = SubElement(node_root, 'folder')
    node_folder.text = file_info[0]

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
    file_root = '/home/user/Downloads/caltech_data_set/data_reasonable_3_19/'
    file_name = file_root + file_info[0];
    mkdir (file_name)
    fw = open(file_name+"/"+file_info[1].split('.')[0]+".xml", 'a+')

    fw.write(xml)
    print "xml _ ok"
    fw.close()

    #for debug
    #print xml

def printPath(level, path):
    global allFileNum
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if(f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):
            # 添加文件
            fileList.append(f)
    # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if(i_dl == 0):
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            print '-' * (int(dirList[0])), dl
            # 打印目录下的所有文件夹和文件，目录级别+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    print fileList
    for fl in fileList:
        # 打印文件
        #print '-' * (int(dirList[0])), fl
        # 随便计算一下有多少个文件
        #allFileNum = allFileNum + 1
        """
        操作文件进行读写
        """
        print fl[12:17],fl[17:21]
        file_info = []
        file_info.append(fl[12:17]+'/'+fl[17:21])

        print file_info
        print path
        file_name = path+"/"+fl
        fw = open(file_name, 'r');
        line_content = fw.readlines()
        fw.close()
        print line_content


        tmp = -1
        obj = []
        con_len = len(line_content)
        try:
            string = line_content[0].split(" ")
            tmp = int(string[0])
        except Exception:
            continue
        file_info.append(str(tmp) + '.jpg')
        xmin = str(int(float(string[1])))
        ymin = str(int(float(string[2])))
        xmax = str(int(float(string[1]) + float(string[3])))
        ymax = str(int(float(string[2]) + float(string[4])))
        dict1 = {}
        dict1["xmin"] = xmin
        dict1["ymin"] = ymin
        dict1["xmax"] = xmax
        dict1["ymax"] = ymax
        obj.append(dict1)

        for con_i in xrange(1, con_len):
            string = line_content[con_i].split(" ")
            tmp1 = int(string[0])
            if tmp == tmp1:
                xmin = str(int(float(string[1])))
                ymin = str(int(float(string[2])))
                xmax = str(int(float(string[1]) + float(string[3])))
                ymax = str(int(float(string[2]) + float(string[4])))
                dict1 = {}
                dict1["xmin"] = xmin
                dict1["ymin"] = ymin
                dict1["xmax"] = xmax
                dict1["ymax"] = ymax
                obj.append(dict1)
            elif tmp1 > 0:
                generate_xml(file_info, obj)
                obj = []
                tmp = tmp1
                file_info[1] = str(tmp1) + ".jpg"
                xmin = str(int(float(string[1])))
                ymin = str(int(float(string[2])))
                xmax = str(int(float(string[1]) + float(string[3])))
                ymax = str(int(float(string[2]) + float(string[4])))
                dict1 = {}
                dict1["xmin"] = xmin
                dict1["ymin"] = ymin
                dict1["xmax"] = xmax
                dict1["ymax"] = ymax
                obj.append(dict1)
        continue

def read_annotations_generate_fileinfo_obj(file_path):
    pass

if __name__=="__main__":

    #
    # file_info = ['set00/V000', '1.jpg']
    #
    # obj = []
    # obj1 = {"xmin":"1", "ymin":"1", "xmax":"5", "ymax":"5"}
    # obj2 = {"xmin":"2", "ymin":"2", "xmax":"6", "ymax":"6"}
    # obj.append(obj1)
    # obj.append(obj2)
    #
    # generate_xml(file_info, obj)
    #

    printPath(1, "/home/user/Downloads/caltech_data_set/data_reasonable_3_19")
    #printPath(1, "/home/user/Downloads/caltech_data_set/data_reasonable_train")