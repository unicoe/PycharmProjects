# -*- coding: utf-8 -*-
# @Time    : 18-10-18 下午3:53
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : analyse_area.py
# @Software: PyCharm Community Edition

import pdb
import matplotlib.pyplot as plt
import numpy as np

rf = open("/home/user/PycharmProjects/caltech_new_anno/src/visualable_code/txt_person_10_11_vis0.3.txt", "r")

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
gt areas

[20-25] 290
[25-30] 386
[30-35] 370
[35-40] 295
[40-45] 290
[45-50] 232

[50-55] 215
[55-60] 126
[60-65] 127
[65-70] 107

[70-75] 81
[75-80] 60
[80-85] 39
[85-90] 52
[90-95] 29
[95-  ] 208

[20-30] 676
[20-35] 1046
[20-40] 1341
[20-45] 1631
[20-50] 1863     1863

[20-55] 2078
[20-60] 2204
[20-65] 2331
[20-70] 2438     575

[20-75] 2519
[20-80] 2579
[20-85] 2618
[20-90] 2670
[20-95] 2699
[20-  ] 2907     388
"""

pdb.set_trace()



plt.plot(index, areas,  'ro')
plt.axis([0,3000,0,10000])
plt.plot((0,3000),(163,163),'g-')
plt.plot((0,3000),(1024,1024),'g-')
plt.plot((0,3000),(2666,2666),'g-')
plt.savefig("/home/user/PycharmProjects/caltech_new_anno/src/visualable_code/check_test_set_area_10_18.png")
plt.show()