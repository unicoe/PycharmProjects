# -*- coding: utf-8 -*-
# @Time    : 18-11-22 上午11:24
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : test_handle.py
# @Software: PyCharm

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/submit/2018_12_07_Fri_16_15_09_det_test_person.txt")
wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/submit/handle_2018_12_07_Fri_16_15_09_det_test_person.txt", "w")

content = rf.readline()

while content:
    det_info = content.strip("\n").split(" ")

    im_name = det_info[0][5:]

    wf.write(im_name)
    wf.write(" ")
    wf.write(det_info[1])
    wf.write(" ")
    wf.write(det_info[2])
    wf.write(" ")
    wf.write(det_info[3])
    wf.write(" ")
    wf.write(det_info[4])
    wf.write(" ")
    wf.write(det_info[5])
    wf.write("\n")

    content = rf.readline()

wf.close()
rf.close()
