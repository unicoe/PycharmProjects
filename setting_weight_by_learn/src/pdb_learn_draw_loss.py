# -*- coding: utf-8 -*-
# @Time    : 18-8-11 下午6:54
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : draw_loss.py
# @Software: PyCharm Community Edition

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdb

rf = open("/home/user/PycharmProjects/setting_weight_by_learn/src/loss.txt")

content = rf.readline()

result = []

while content:
    res = re.findall("\[\d.\d+\]",content)

    if len(res) != 0:
        tmp = res[0][1:-2]
        result.append(float(tmp))
    content = rf.readline()

draw_train_all_loss = pd.Series(result, index = range(0,len(result),1))

#draw
fig = plt.figure()
w = 25
h = 10
fig.set_size_inches(w,h)

plt.plot(draw_train_all_loss,'r')
plt.title(u"all loss")
#plt.legend((u'accuracy'),loc='best')
plt.xlabel(u"iter")
plt.ylabel(u"loss")


plt.savefig("/home/user/PycharmProjects/setting_weight_by_learn/img/loss_add_wegiht_08_11.png")
#save format maybe : format="eps"  or "pdf"


plt.show()
