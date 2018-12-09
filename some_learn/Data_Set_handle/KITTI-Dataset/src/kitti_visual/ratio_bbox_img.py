# -*- coding: utf-8 -*-
# @Time    : 18-12-8 上午10:55
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : ratio_bbox_img.py
# @Software: PyCharm

bboxes = [5845,5993,6036,5880,5880,5879,6298,6351,6354,6515]

img    = [1963,2007,2020,1975,1975,1951,2030,2093,2119,2069]

for i in range(len(bboxes)):
    print bboxes[i]/(img[i]+0.0)