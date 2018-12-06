#!/usr/bin/env python
# coding:utf-8

def generate_xml(file_root, file_info, obj):
    import mkdir
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
