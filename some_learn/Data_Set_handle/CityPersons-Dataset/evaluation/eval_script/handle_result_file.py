# -*- coding: utf-8 -*-
# @Time    : 18-11-1 上午10:11
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : handle_result_file.py
# @Software: PyCharm Community Edition

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/evaluation/eval_script/det_result.txt", "r")

content = rf.readline()

while content:

    print "'" + content.strip("\n") + "',"

    content = rf.readline()