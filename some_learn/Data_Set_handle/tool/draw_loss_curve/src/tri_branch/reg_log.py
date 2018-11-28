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

file_path = "/home/user/PycharmProjects/draw_loss_curve/logs/10_14_mutli/train_rfcn_end2end_ResNet-50_.txt.2018-10-12_21-59-36"

rf = open(file_path)

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

    get_accuarcy = re.findall(r"Train net output #\d+: accuarcy_res5c = \d.\d+", content)
    if get_accuarcy:
        ls_accuarcy.append(get_accuarcy)
        content = rf.readline()
        continue

    get_loss_bbox = re.findall(r"Train net output #\d+: loss_bbox_res5c = \d.\d+", content)
    if get_loss_bbox:
        ls_loss_bbox.append(get_loss_bbox)
        content = rf.readline()
        continue

    get_loss_cls = re.findall(r"Train net output #\d+: loss_cls_res5c = \d.\d+", content)
    if get_loss_cls:
        ls_loss_cls.append(get_loss_cls)
        content = rf.readline()
        continue

    get_rpn_cls_loss = re.findall(r"Train net output #\d+: rpn_cls_loss_res5c = \d.\d+", content)
    if get_rpn_cls_loss:
        ls_rpn_cls_loss.append(get_rpn_cls_loss)
        content = rf.readline()
        continue

    get_rpn_loss_bbox = re.findall(r"Train net output #\d+: rpn_loss_bbox_res5c = \d.\d+", content)
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

mkdir("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/")
al_wf_res5c = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_all_loss_res5c.txt", "w")
ac_wf_res5c = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_accuarcy_res5c.txt", "w")
bl_wf_res5c = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_loss_bbox_res5c.txt", "w")
cl_wf_res5c = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_loss_cls_res5c.txt", "w")
rcl_wf_res5c = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_rpn_cls_loss_res5c.txt", "w")
rbl_wf_res5c = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_rpn_loss_bbox_res5c.txt", "w")



for idx_al in ls_all_loss:
    al_wf_res5c.write(str(idx_al[0]))
    al_wf_res5c.write("\n")
al_wf_res5c.close()

for idx_ac in ls_accuarcy:
    ac_wf_res5c.write(str(idx_ac[0]))
    ac_wf_res5c.write("\n")
ac_wf_res5c.close()

for idx_bl in ls_loss_bbox:
    bl_wf_res5c.write(str(idx_bl[0]))
    bl_wf_res5c.write("\n")
bl_wf_res5c.close()

for idx_cl in ls_loss_cls:
    cl_wf_res5c.write(str(idx_cl[0]))
    cl_wf_res5c.write("\n")
cl_wf_res5c.close()

for idx_rcl in ls_rpn_cls_loss:
    rcl_wf_res5c.write(str(idx_rcl[0]))
    rcl_wf_res5c.write("\n")
rcl_wf_res5c.close()


for idx_rbl in ls_rpn_loss_bbox:
    rbl_wf_res5c.write(str(idx_rbl[0]))
    rbl_wf_res5c.write("\n")
rbl_wf_res5c.close()


#--res3d
rf = open(file_path)
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

    get_accuarcy = re.findall(r"Train net output #\d+: accuarcy_res3d = \d.\d+", content)
    if get_accuarcy:
        ls_accuarcy.append(get_accuarcy)
        content = rf.readline()
        continue

    get_loss_bbox = re.findall(r"Train net output #\d+: loss_bbox_res3d = \d.\d+", content)
    if get_loss_bbox:
        ls_loss_bbox.append(get_loss_bbox)
        content = rf.readline()
        continue

    get_loss_cls = re.findall(r"Train net output #\d+: loss_cls_res3d = \d.\d+", content)
    if get_loss_cls:
        ls_loss_cls.append(get_loss_cls)
        content = rf.readline()
        continue

    get_rpn_cls_loss = re.findall(r"Train net output #\d+: rpn_cls_loss_res3d = \d.\d+", content)
    if get_rpn_cls_loss:
        ls_rpn_cls_loss.append(get_rpn_cls_loss)
        content = rf.readline()
        continue

    get_rpn_loss_bbox = re.findall(r"Train net output #\d+: rpn_loss_bbox_res3d = \d.\d+", content)
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

mkdir("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/")
al_wf_res3d = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_all_loss_res3d.txt", "w")
ac_wf_res3d = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_accuarcy_res3d.txt", "w")
bl_wf_res3d = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_loss_bbox_res3d.txt", "w")
cl_wf_res3d = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_loss_cls_res3d.txt", "w")
rcl_wf_res3d = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_rpn_cls_loss_res3d.txt", "w")
rbl_wf_res3d = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_rpn_loss_bbox_res3d.txt", "w")



for idx_al in ls_all_loss:
    al_wf_res3d.write(str(idx_al[0]))
    al_wf_res3d.write("\n")
al_wf_res3d.close()

for idx_ac in ls_accuarcy:
    ac_wf_res3d.write(str(idx_ac[0]))
    ac_wf_res3d.write("\n")
ac_wf_res3d.close()

for idx_bl in ls_loss_bbox:
    bl_wf_res3d.write(str(idx_bl[0]))
    bl_wf_res3d.write("\n")
bl_wf_res3d.close()

for idx_cl in ls_loss_cls:
    cl_wf_res3d.write(str(idx_cl[0]))
    cl_wf_res3d.write("\n")
cl_wf_res3d.close()

for idx_rcl in ls_rpn_cls_loss:
    rcl_wf_res3d.write(str(idx_rcl[0]))
    rcl_wf_res3d.write("\n")
rcl_wf_res3d.close()


for idx_rbl in ls_rpn_loss_bbox:
    rbl_wf_res3d.write(str(idx_rbl[0]))
    rbl_wf_res3d.write("\n")
rbl_wf_res3d.close()



#--res4f
rf = open(file_path)
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

    get_accuarcy = re.findall(r"Train net output #\d+: accuarcy_res4f = \d.\d+", content)
    if get_accuarcy:
        ls_accuarcy.append(get_accuarcy)
        content = rf.readline()
        continue

    get_loss_bbox = re.findall(r"Train net output #\d+: loss_bbox_res4f = \d.\d+", content)
    if get_loss_bbox:
        ls_loss_bbox.append(get_loss_bbox)
        content = rf.readline()
        continue

    get_loss_cls = re.findall(r"Train net output #\d+: loss_cls_res4f = \d.\d+", content)
    if get_loss_cls:
        ls_loss_cls.append(get_loss_cls)
        content = rf.readline()
        continue

    get_rpn_cls_loss = re.findall(r"Train net output #\d+: rpn_cls_loss_res4f = \d.\d+", content)
    if get_rpn_cls_loss:
        ls_rpn_cls_loss.append(get_rpn_cls_loss)
        content = rf.readline()
        continue

    get_rpn_loss_bbox = re.findall(r"Train net output #\d+: rpn_loss_bbox_res4f = \d.\d+", content)
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

mkdir("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/")
al_wf_res4f = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_all_loss_res4f.txt", "w")
ac_wf_res4f = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_accuarcy_res4f.txt", "w")
bl_wf_res4f = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_loss_bbox_res4f.txt", "w")
cl_wf_res4f = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_loss_cls_res4f.txt", "w")
rcl_wf_res4f = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_rpn_cls_loss_res4f.txt", "w")
rbl_wf_res4f = open("/home/user/PycharmProjects/draw_loss_curve/logs/10_14/train_rpn_loss_bbox_res4f.txt", "w")



for idx_al in ls_all_loss:
    al_wf_res4f.write(str(idx_al[0]))
    al_wf_res4f.write("\n")
al_wf_res4f.close()

for idx_ac in ls_accuarcy:
    ac_wf_res4f.write(str(idx_ac[0]))
    ac_wf_res4f.write("\n")
ac_wf_res4f.close()

for idx_bl in ls_loss_bbox:
    bl_wf_res4f.write(str(idx_bl[0]))
    bl_wf_res4f.write("\n")
bl_wf_res4f.close()

for idx_cl in ls_loss_cls:
    cl_wf_res4f.write(str(idx_cl[0]))
    cl_wf_res4f.write("\n")
cl_wf_res4f.close()

for idx_rcl in ls_rpn_cls_loss:
    rcl_wf_res4f.write(str(idx_rcl[0]))
    rcl_wf_res4f.write("\n")
rcl_wf_res4f.close()


for idx_rbl in ls_rpn_loss_bbox:
    rbl_wf_res4f.write(str(idx_rbl[0]))
    rbl_wf_res4f.write("\n")
rbl_wf_res4f.close()