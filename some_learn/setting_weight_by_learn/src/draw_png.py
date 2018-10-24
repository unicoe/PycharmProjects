# -*- coding: utf-8 -*-
# @Time    : 18-8-12 下午4:06
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : draw_png.py
# @Software: PyCharm Community Edition

from matplotlib import  pyplot as plt
import cv2


#cv2.rectangle(res, (414,179), (424, 209), (0,255,255), 2)


rf1 = open("/home/user/PycharmProjects/setting_weight_by_learn/basic_data/generate_data.txt")
rf2 = open("/home/user/PycharmProjects/setting_weight_by_learn/basic_data/3_gt.txt")
rf3 = open("/home/user/PycharmProjects/setting_weight_by_learn/basic_data/1_withgt_head.txt")
rf4 = open("/home/user/PycharmProjects/setting_weight_by_learn/basic_data/1_withgt_person.txt")

content1 = rf1.readline()
content2 = rf2.readline()
content3 = rf3.readline()
content4 = rf4.readline()


cur = 0
while content1 and content2:
    im = cv2.imread("/home/user/PycharmProjects/setting_weight_by_learn/img/test.jpg")

    res = cv2.resize(im, (640, 480), interpolation=cv2.INTER_CUBIC)

    tmp1 = content1.strip("\n").split(" ")
    tmp2 = content2.strip("\n").split(" ")
    tmp3 = content3.strip("\n").split(" ")
    tmp4 = content4.strip("\n").split(" ")

    tmp1 = map(eval, tmp1)
    tmp2 = map(eval, tmp2)
    tmp3 = map(eval, tmp3)
    tmp4 = map(eval, tmp4)

    content1 = rf1.readline()
    content2 = rf2.readline()
    content3 = rf3.readline()
    content4 = rf4.readline()

    cv2.rectangle(res, (int(tmp1[0]),int(tmp1[1])), (int(tmp1[2]), int(tmp1[3])), (0,0,255), 1)
    cv2.rectangle(res, (int(tmp2[0]),int(tmp2[1])), (int(tmp2[2]), int(tmp2[3])), (255,0,0), 1)
    cv2.rectangle(res, (int(tmp3[0]), int(tmp3[1])), (int(tmp3[2]), int(tmp3[3])), (255, 0, 255), 1)
    cv2.rectangle(res, (int(tmp4[0]), int(tmp4[1])), (int(tmp4[2]), int(tmp4[3])), (255, 255, 0), 1)

    #plt.imshow(res)
    #plt.show()
    cv2.imwrite("/home/user/Disk1.8T/tmp/img/" + str(cur)+".jpg", res)
    cur = cur + 1