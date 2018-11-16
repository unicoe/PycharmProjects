# -*- coding: utf-8 -*-
# @Time    : 18-11-15 下午6:57
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : height_hog.py
# @Software: PyCharm


from matplotlib import pyplot as plt
import numpy as np

rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/img_shape.txt", "r")

h_lst = []

content = rf.readline()

while content:
    im_w = int(content.strip("\n").split(" ")[2])
    im_h = int(content.strip("\n").split(" ")[1])

    min_size = min(im_w, im_h)
    max_size = max(im_w, im_h)

    """
    # Each scale is the pixel size of an image's shortest side
    __C.TEST.SCALES = (960,)

    # Max pixel size of the longest side of a scaled input image
    __C.TEST.MAX_SIZE = 1280
    """
    im_scale = float(960) / float(min_size)
    # Prevent the biggest axis from being more than MAX_SIZE
    if np.round(im_scale * max_size) > 1280:
        im_scale = float(1280) / float(max_size)

    sw = im_w * im_scale
    sh = im_h * im_scale

    h_lst.append(im_h)
    content = rf.readline()

height = np.array(h_lst)

plt.hist(height, bins = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050])

plt.title("histogram")
plt.show()

tmp_lst = []

for i in xrange(200,1100,50):
   tmp_lst.append(i)

print tmp_lst