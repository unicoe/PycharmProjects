# -*- coding: utf-8 -*-
# @Time    : 18-11-5 下午9:47
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : generate_test_list.py
# @Software: PyCharm
import os

def generate_test_list():
    cur_path = "/home/user/Disk1.8T/data_set/cityspaces/leftImg8bit/test"
    dirList = []
    fileList = []
    files = os.listdir(cur_path)

    wf = open("/home/user/PycharmProjects/some_learn/CityPersons_handle/ann_code_src/test_list_citypersons.txt", "w")

    for f_idx in files:
        tmp_files = os.listdir(cur_path + "/" + f_idx)

        for img_idx in tmp_files:
            img = (f_idx + "/" + img_idx).split(".")[0]
            wf.write(img)
            wf.write("\n")

    wf.close()
    #print files

generate_test_list()