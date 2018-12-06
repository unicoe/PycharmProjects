# -*- coding: utf-8 -*-
# @Time    : 18-11-7 下午7:58
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : check_gt_new.py
# @Software: PyCharm

import scipy.io as scio

dataFile = '/home/user/PycharmProjects/caltech_new_anno/src/check_gt_new/gt-new.mat'
data = scio.loadmat(dataFile)
gt_new_info = data.get('gt')

gt_new_ls = gt_new_info.tolist()

print type(gt_new_ls)

wf = open("/home/user/PycharmProjects/caltech_new_anno/src/check_gt_new/gt_new_info.txt", "w")

bbox_ls = []

for gt_i in gt_new_ls:
    for idx in gt_i[4250:8274]:
        for bbox_idx in idx:
            if len(bbox_idx) > 0:     # 滤掉bbox值为空的数组
                wf.write(str(bbox_idx.tolist()))
                bbox_ls.append(bbox_idx.tolist())
                wf.write("\n")
wf.close()


"""
通过这个数据，是不是可以说明，这里的gt，也不是reasonable的数据

怎么进行筛选
"""
cnt_0 = 0
cnt_10 = 0
cnt_20 = 0
cnt_30 = 0
cnt_40 = 0
cnt_50 = 0

for box_idx in bbox_ls:
    if box_idx[4] > 0.5:
        if box_idx[3] >= 50:
            cnt_50 += 1
        elif box_idx[3] >= 40:
            cnt_40 += 1
        elif box_idx[3] >= 30:
            cnt_30 += 1
        elif box_idx[3] >= 20:
            cnt_20 += 1
        elif box_idx[3] >= 10:
            cnt_10 += 1
        elif box_idx[3] > 0:
            cnt_0 += 1
print cnt_50, cnt_40, cnt_30, cnt_20, cnt_10, cnt_0


"""
标记为 1

681 961 1621 2109 1129 183
"""