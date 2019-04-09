# -*- coding: utf-8 -*-
# @Time    : 18-6-6 下午8:03
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : handle_result.py
# @Software: PyCharm Community Edition

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/12_24/target/comp4_det_test_person.txt")
wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/12_24/target/replace_comp4_det_test_person.txt","w")

content = rf.readline()

while content:

    info = content.replace('/','_')
    # if (float(info[5]) - float(info[3]) < 50):
    #     content = rf.readline()
    #     continue


    wf.write(info)
    content = rf.readline()
