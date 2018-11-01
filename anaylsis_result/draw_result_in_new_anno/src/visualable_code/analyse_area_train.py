# -*- coding: utf-8 -*-
# @Time    : 18-10-18 下午3:53
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : analyse_area.py
# @Software: PyCharm Community Edition

import pdb
import matplotlib.pyplot as plt
import numpy as np

rf = open("/home/user/PycharmProjects/anaylsis_result/draw_result_in_new_anno/src/visualable_code/train_person_10_26_vis0.3_h20_w3.txt", "r")

content = rf.readline()

areas = []
index = []
i = 0
while content:

    res = content.strip('\n')
    res = int(res)
    areas.append(res)
    index.append(i)
    i = i + 1
    content = rf.readline()
    # pdb.set_trace()

np_areas = np.asarray(areas)

np_areas.sort()
area_list = []
for i in range(20,100,5):
    skip = (i*i) / 2.44
    res = np.sum(np_areas > skip)
    area_list.append(res)
    print str(skip) + " " + str(res)


tmp = []
for i in range(0,len(area_list)-1):
    tmp_num = area_list[i] - area_list[i+1]
    tmp.append(tmp_num)
    print "[" + str(20+i*5) + "-" + str(20+(i+1)*5) + "]" + " " + str(tmp_num)

print "tmp"
for i in range(1,len(tmp)):
    tmp[i] = tmp[i-1]+tmp[i]
    print "[" + str(20) + "-" + str(20+(i+1)*5) + "]" + " " + str(tmp[i])

"""
[20-25] 221
[25-30] 366
[30-35] 456
[35-40] 448


[40-45] 505
[45-50] 451
[50-55] 374
[55-60] 225   1555

[60-65] 196
[65-70] 201
[70-75] 142
[75-80] 117   656

[80-85] 87
[85-90] 87
[90-95] 56
[95   ] 495   725


tmp
[20-30] 587
[20-35] 1043
[20-40] 1491
[20-45] 1996
[20-50] 2447
[20-55] 2821
[20-60] 3046
[20-65] 3242
[20-70] 3443
[20-75] 3585
[20-80] 3702
[20-85] 3789
[20-90] 3876
[20-95] 3932

"""

# pdb.set_trace()


plt.plot(index, areas,  'ro')
plt.axis([0,3000,0,10000])
plt.plot((0,3000),(163,163),'g-')
plt.plot((0,3000),(1024,1024),'g-')
plt.plot((0,3000),(2000,2000),'g-')
plt.savefig("/home/user/PycharmProjects/anaylsis_result/draw_result_in_new_anno/src/visualable_code/check_train_set_area_10_26.png")
plt.show()