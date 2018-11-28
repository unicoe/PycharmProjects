# -*- coding: utf-8 -*-
# @Time    : 18-6-20 下午4:05
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : reg_log.py
# @Software: PyCharm Community Edition

"""
I0511 04:03:02.676997 23939 solver.cpp:243] Iteration 119970, loss = 2.56674
I0511 04:03:02.677028 23939 solver.cpp:259]     Train net output #0: mbox_loss = 3.73246 (* 1 = 3.73246 loss)
"""

import re

rf = open("/home/user/PycharmProjects/draw_loss_curve/logs/VGG_SSD_test5_11.log")

content = rf.readline()

all_loss = []

cnt = 0

ls_all_loss         = []
ls_mbox_loss     = []

while content:
    get_all_loss = re.findall(r", loss = \d.\d+", content)
    if get_all_loss:
        ls_all_loss.append(get_all_loss)
        content = rf.readline()
        continue

    get_loss_bbox = re.findall(r"Train net output #\d: mbox_loss = \d.\d+", content)
    if get_loss_bbox:
        ls_mbox_loss.append(get_loss_bbox)
        content = rf.readline()
        continue

    content = rf.readline()

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

mkdir("/home/user/PycharmProjects/draw_loss_curve/logs/ssd_5_11/")
al_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/ssd_5_11/train_all_loss.txt", "w")
bl_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/ssd_5_11/train_mbox_loss.txt", "w")


for idx_al in ls_all_loss:
    al_wf.write(str(idx_al[0]))
    al_wf.write("\n")
al_wf.close()

for idx_bl in ls_mbox_loss:
    bl_wf.write(str(idx_bl[0]))
    bl_wf.write("\n")
bl_wf.close()
