# -*- coding: utf-8 -*-
# @Time    : 18-7-18 上午9:49
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : extract_score.py
# @Software: PyCharm Community Edition


"""
/home/user/PycharmProjects/handle_result/6_25/handle_result/nms_handle_alone_det_test_head.txt

/home/user/PycharmProjects/handle_result/6_25/handle_result/5_29_960_1280_det_test_person.txt
"""
rf = open("/home/user/PycharmProjects/handle_result/6_25/handle_result/5_29_960_1280_det_test_person.txt")
wf = open("/home/user/PycharmProjects/handle_result/6_25/src_draw/score2.txt", "w")

content = rf.readline()

while content:

    tmp = content.strip().split(" ")[1]


    wf.write(str(tmp))
    wf.write("\n")


    content = rf.readline()

wf.close()
rf.close()

