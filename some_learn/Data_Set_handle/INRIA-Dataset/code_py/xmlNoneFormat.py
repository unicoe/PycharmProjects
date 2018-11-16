#!/usr/bin/env python
# coding:utf-8


from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString
import os

def generate_xml(floder, file_name , save_path):

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