# -*- coding: utf-8 -*-
# @Time    : 18-11-13 上午11:16
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : anchor_compute.py
# @Software: PyCharm

scale = [3.5, 4.41, 5.56, 7.0, 8.82, 11.12, 14.01, 17.65, 22.23, 28.02, 35.3]

# for i in range(len(scale)-1):
#     print scale[i+1] / scale[i]

base = 2

scale_lst = []

for i in range(11):
    scale_lst.append(round(base, 2))
    base = base * 1.31
    #print round(base, 2)

print "anchor scale:"
print scale_lst
print "\n"

import numpy as np

def generate_anchors(base_size=16, scales=np.array(scale_lst)):

    ratios=[2.44]

    #-- citypersons 40 50
    # if   feat_stride == 8:
    #     scales = np.array((1.5, 2.03, 2.74, 3.71, 5.01, 6.78, 9.16, 12.39, 16.75, 22.64, 30.61),dtype=float)
    # elif feat_stride == 16:
    #     scales = np.array((1.8, 2.39, 3.18, 4.23, 5.63, 7.49, 9.96, 13.25, 17.62, 23.44, 31.17),dtype=float)

    base_anchor = np.array([1, 1, base_size, base_size]) - 1
    ratio_anchors = _ratio_enum(base_anchor, ratios)
    anchors = np.vstack([_scale_enum(ratio_anchors[i, :], scales)
                         for i in xrange(ratio_anchors.shape[0])])

    return anchors


def _whctrs(anchor):
    """
    Return width, height, x center, and y center for an anchor (window).
    """

    w = anchor[2] - anchor[0] + 1
    h = anchor[3] - anchor[1] + 1
    x_ctr = anchor[0] + 0.5 * (w - 1)
    y_ctr = anchor[1] + 0.5 * (h - 1)
    return w, h, x_ctr, y_ctr

def _mkanchors(ws, hs, x_ctr, y_ctr):
    """
    Given a vector of widths (ws) and heights (hs) around a center
    (x_ctr, y_ctr), output a set of anchors (windows).
    """

    ws = ws[:, np.newaxis]
    hs = hs[:, np.newaxis]
    anchors = np.hstack((x_ctr - 0.5 * (ws - 1),
                         y_ctr - 0.5 * (hs - 1),
                         x_ctr + 0.5 * (ws - 1),
                         y_ctr + 0.5 * (hs - 1)))
    return anchors

def _ratio_enum(anchor, ratios):
    """
    Enumerate a set of anchors for each aspect ratio wrt an anchor.
    """

    w, h, x_ctr, y_ctr = _whctrs(anchor)
    size = w * h
    size_ratios = size / ratios
    ws = np.round(np.sqrt(size_ratios))
    hs = np.round(ws * ratios)
    anchors = _mkanchors(ws, hs, x_ctr, y_ctr)
    return anchors

def _scale_enum(anchor, scales):
    """
    Enumerate a set of anchors for each scale wrt an anchor.
    """

    w, h, x_ctr, y_ctr = _whctrs(anchor)
    ws = w * scales
    hs = h * scales
    anchors = _mkanchors(ws, hs, x_ctr, y_ctr)
    return anchors

if __name__ == '__main__':
    a = generate_anchors()
    print "h:"
    print(a[:,3] -a[:,1])


"""
INRIA

anchor scale:
[2.3, 2.99, 3.89, 5.05, 6.57, 8.54, 11.1, 14.43, 18.76, 24.39, 31.71]


h:
[ 54.2   70.76  92.36 120.2  156.68 203.96 265.4  345.32 449.24 584.36
 760.04]
 
 
 anchor scale:
[2.0, 2.6, 3.38, 4.39, 5.71, 7.43, 9.65, 12.55, 16.31, 21.21, 27.57]


h:
[ 47.    61.4   80.12 104.36 136.04 177.32 230.6  300.2  390.44 508.04
 660.68]
"""