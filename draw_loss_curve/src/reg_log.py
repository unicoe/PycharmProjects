# -*- coding: utf-8 -*-
# @Time    : 18-6-20 下午4:05
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : reg_log.py
# @Software: PyCharm Community Edition

"""
Iteration 19320, loss = 0.332942
I0615 02:07:01.529966 15760 solver.cpp:244]     Train net output #0: accuarcy = 0.960938
I0615 02:07:01.529973 15760 solver.cpp:244]     Train net output #1: loss_bbox = 0.0748922 (* 1 = 0.0748922 loss)
I0615 02:07:01.529976 15760 solver.cpp:244]     Train net output #2: loss_cls = 0.0991373 (* 1 = 0.0991373 loss)
I0615 02:07:01.529980 15760 solver.cpp:244]     Train net output #3: rpn_cls_loss = 0.00157587 (* 1 = 0.00157587 loss)
I0615 02:07:01.529983 15760 solver.cpp:244]     Train net output #4: rpn_loss_bbox = 0.00667848 (* 1 = 0.00667848 loss)
"""

import re

rf = open("/home/user/PycharmProjects/draw_loss_curve/logs/train_rfcn_end2end_ResNet-50_.txt.2018-09-29_21-31-06")

content = rf.readline()

all_loss = []

cnt = 0

ls_all_loss         = []
ls_accuarcy      = []
ls_loss_bbox     = []
ls_loss_cls      = []
ls_rpn_cls_loss  = []
ls_rpn_loss_bbox = []

while content:
    get_all_loss = re.findall(r", loss = \d.\d+", content)
    if get_all_loss:
        ls_all_loss.append(get_all_loss)
        content = rf.readline()
        continue

    get_accuarcy = re.findall(r"Train net output #\d: accuarcy_res5c = \d.\d+", content)
    if get_accuarcy:
        ls_accuarcy.append(get_accuarcy)
        content = rf.readline()
        continue

    get_loss_bbox = re.findall(r"Train net output #\d: loss_bbox_res5c = \d.\d+", content)
    if get_loss_bbox:
        ls_loss_bbox.append(get_loss_bbox)
        content = rf.readline()
        continue

    get_loss_cls = re.findall(r"Train net output #\d: loss_cls_res5c = \d.\d+", content)
    if get_loss_cls:
        ls_loss_cls.append(get_loss_cls)
        content = rf.readline()
        continue

    get_rpn_cls_loss = re.findall(r"Train net output #\d: rpn_cls_loss_res4f = \d.\d+", content)
    if get_rpn_cls_loss:
        ls_rpn_cls_loss.append(get_rpn_cls_loss)
        content = rf.readline()
        continue

    get_rpn_loss_bbox = re.findall(r"Train net output #\d: rpn_loss_bbox_res4f = \d.\d+", content)
    if get_rpn_loss_bbox:
        ls_rpn_loss_bbox.append(get_rpn_loss_bbox)
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

mkdir("/home/user/PycharmProjects/draw_loss_curve/logs/10_9/")
al_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_9/train_all_loss.txt", "w")
ac_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_9/train_accuarcy.txt", "w")
bl_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_9/train_loss_bbox.txt", "w")
cl_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_9/train_loss_cls.txt", "w")
rcl_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_9/train_rpn_cls_loss.txt", "w")
rbl_wf = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_9/train_rpn_loss_bbox.txt", "w")



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