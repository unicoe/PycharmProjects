# -*- coding: utf-8 -*-
# @Time    : 18-12-6 下午9:16
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : check_img.py
# @Software: PyCharm

import matplotlib.pyplot as plt

print 255*0.753
print 255*0.502

im = plt.imread("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/mask_img/2007_000129.png")
plt.interactive(False)

plt.figure()
plt.imshow(im)
plt.show()

print 1

