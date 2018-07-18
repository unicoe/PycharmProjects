# -*- coding: utf-8 -*-
# @Time    : 18-6-20 下午4:05
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : reg_log.py
# @Software: PyCharm Community Edition

"""
I0704 21:44:17.368131 22667 solver.cpp:244]     Train net output #0: accuarcy = 0.914062
I0704 21:44:17.368135 22667 solver.cpp:244]     Train net output #1: head_accuarcy = 0.953125
I0704 21:44:17.368141 22667 solver.cpp:244]     Train net output #2: head_loss_bbox = 0.121259 (* 1 = 0.121259 loss)
I0704 21:44:17.368144 22667 solver.cpp:244]     Train net output #3: head_loss_cls = 0.173022 (* 1 = 0.173022 loss)
I0704 21:44:17.368147 22667 solver.cpp:244]     Train net output #4: loss_bbox = 0.120046 (* 1 = 0.120046 loss)
I0704 21:44:17.368150 22667 solver.cpp:244]     Train net output #5: loss_cls = 0.242736 (* 1 = 0.242736 loss)
I0704 21:44:17.368154 22667 solver.cpp:244]     Train net output #6: rpn_cls_loss = 0.0400376 (* 1 = 0.0400376 loss)
I0704 21:44:17.368156 22667 solver.cpp:244]     Train net output #7: rpn_head_cls_loss = 0.0151905 (* 1 = 0.0151905 loss)
I0704 21:44:17.368160 22667 solver.cpp:244]     Train net output #8: rpn_head_loss_bbox = 0.00887669 (* 1 = 0.00887669 loss)
I0704 21:44:17.368162 22667 solver.cpp:244]     Train net output #9: rpn_loss_bbox = 0.0281653 (* 1 = 0.0281653 loss)
"""

import re

rf = open("/home/user/PycharmProjects/draw_loss_curve/logs/rfcn_end2end_ResNet-50_.txt.2018-07-10_17-28-59")

content = rf.readline()

all_loss = []

cnt = 0

ls_all_loss         = []
ls_accuarcy      = []
ls_loss_bbox     = []
ls_loss_cls      = []
ls_rpn_cls_loss  = []
ls_rpn_loss_bbox = []

ls_head_accuarcy      = []
ls_head_loss_bbox     = []
ls_head_loss_cls      = []
ls_head_rpn_cls_loss  = []
ls_head_rpn_loss_bbox = []

while content:
    get_all_loss = re.findall(r", loss = \d.\d+", content)
    if get_all_loss:
        ls_all_loss.append(get_all_loss)
        content = rf.readline()
        continue

    get_accuarcy = re.findall(r"Train net output #\d: accuarcy = \d.\d+", content)
    if get_accuarcy:
        ls_accuarcy.append(get_accuarcy)
        content = rf.readline()
        continue

    get_loss_bbox = re.findall(r"Train net output #\d: loss_bbox = \d.\d+", content)
    if get_loss_bbox:
        ls_loss_bbox.append(get_loss_bbox)
        content = rf.readline()
        continue

    get_loss_cls = re.findall(r"Train net output #\d: loss_cls = \d.\d+", content)
    if get_loss_cls:
        ls_loss_cls.append(get_loss_cls)
        content = rf.readline()
        continue

    get_rpn_cls_loss = re.findall(r"Train net output #\d: rpn_cls_loss = \d.\d+", content)
    if get_rpn_cls_loss:
        ls_rpn_cls_loss.append(get_rpn_cls_loss)
        content = rf.readline()
        continue

    get_rpn_loss_bbox = re.findall(r"Train net output #\d: rpn_loss_bbox = \d.\d+", content)
    if get_rpn_loss_bbox:
        ls_rpn_loss_bbox.append(get_rpn_loss_bbox)
        content = rf.readline()
        continue


    get_head_accuarcy = re.findall(r"Train net output #\d: head_accuarcy = \d.\d+", content)
    if get_head_accuarcy:
        ls_head_accuarcy.append(get_head_accuarcy)
        content = rf.readline()
        continue

    get_head_loss_bbox = re.findall(r"Train net output #\d: head_loss_bbox = \d.\d+", content)
    if get_head_loss_bbox:
        ls_head_loss_bbox.append(get_head_loss_bbox)
        content = rf.readline()
        continue

    get_head_loss_cls = re.findall(r"Train net output #\d: head_loss_cls = \d.\d+", content)
    if get_head_loss_cls:
        ls_head_loss_cls.append(get_head_loss_cls)
        content = rf.readline()
        continue

    get_head_rpn_cls_loss = re.findall(r"Train net output #\d: rpn_head_cls_loss = \d.\d+", content)
    if get_head_rpn_cls_loss:
        ls_head_rpn_cls_loss.append(get_head_rpn_cls_loss)
        content = rf.readline()
        continue

    get_head_rpn_loss_bbox = re.findall(r"Train net output #\d: rpn_head_loss_bbox = \d.\d+", content)
    if get_head_rpn_loss_bbox:
        ls_head_rpn_loss_bbox.append(get_head_rpn_loss_bbox)
        content = rf.readline()
        continue

    content = rf.readline()

print ls_rpn_loss_bbox

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

mkdir("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/")
al_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_all_loss.txt", "w")
ac_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_accuarcy.txt", "w")
bl_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_loss_bbox.txt", "w")
cl_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_loss_cls.txt", "w")
rcl_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_rpn_cls_loss.txt", "w")
rbl_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_rpn_loss_bbox.txt", "w")
ac_head_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_head_accuarcy.txt", "w")
bl_head_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_head_loss_bbox.txt", "w")
cl_head_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_head_loss_cls.txt", "w")
rcl_head_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_head_rpn_cls_loss.txt", "w")
rbl_head_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/7_10/train_head_rpn_loss_bbox.txt", "w")



for idx_al in ls_all_loss:
    al_wf.write(str(idx_al[0]))
    al_wf.write("\n")
al_wf.close()

for idx_ac in ls_accuarcy:
    ac_wf.write(str(idx_ac[0]))
    ac_wf.write("\n")
ac_wf.close()

for idx_bl in ls_loss_bbox:
    bl_wf.write(str(idx_bl[0]))
    bl_wf.write("\n")
bl_wf.close()

for idx_cl in ls_loss_cls:
    cl_wf.write(str(idx_cl[0]))
    cl_wf.write("\n")
cl_wf.close()

for idx_rcl in ls_rpn_cls_loss:
    rcl_wf.write(str(idx_rcl[0]))
    rcl_wf.write("\n")
rcl_wf.close()


for idx_rbl in ls_rpn_loss_bbox:
    rbl_wf.write(str(idx_rbl[0]))
    rbl_wf.write("\n")
rbl_wf.close()

for idx_ac in ls_head_accuarcy:
    ac_head_wf.write(str(idx_ac[0]))
    ac_head_wf.write("\n")
ac_head_wf.close()

for idx_bl in ls_head_loss_bbox:
    bl_head_wf.write(str(idx_bl[0]))
    bl_head_wf.write("\n")
bl_head_wf.close()

for idx_cl in ls_head_loss_cls:
    cl_head_wf.write(str(idx_cl[0]))
    cl_head_wf.write("\n")
cl_head_wf.close()

for idx_rcl in ls_head_rpn_cls_loss:
    rcl_head_wf.write(str(idx_rcl[0]))
    rcl_head_wf.write("\n")
rcl_head_wf.close()


for idx_rbl in ls_head_rpn_loss_bbox:
    rbl_head_wf.write(str(idx_rbl[0]))
    rbl_head_wf.write("\n")
rbl_head_wf.close()