#!/usr/bin/env python
# coding:utf-8


from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString
import os

def generate_xml(floder, file_name , save_path , bboxs):

    node_root = Element('annotation')

    node_folder = SubElement(node_root, 'folder')
    node_folder.text = floder

    node_filename = SubElement(node_root, 'filename')
    node_filename.text = file_name

    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = '640'

    node_height = SubElement(node_size, 'height')
    node_height.text = '480'

    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '3'

    for bbox in bboxs:

        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = bbox['class']

        node_name = SubElement(node_object, 'difficult')
        node_name.text = '0'

        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = bbox['xmin']

        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = bbox['ymin']

        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = bbox['xmax']

        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = bbox['ymax']

    xml = tostring(node_root, pretty_print=True)  #格式化显示，该换行的换行
    dom = parseString(xml)
    #file_root = '/home/user/Downloads/caltech_data_set/data_train/'
    # file_root = '/home/user/Downloads/caltech_data_set/30stepsize1_train/'

    fw = open(save_path, 'w')

    fw.write(xml)
    #print "xml _ ok"
    fw.close()

    #for debug
    #print xml