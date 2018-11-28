# -*- coding: utf-8 -*-
# @Time    : 18-11-13 上午11:16
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : anchor_compute.py
# @Software: PyCharm
import numpy as np

scale = [3.5, 4.41, 5.56, 7.0, 8.82, 11.12, 14.01, 17.65, 22.23, 28.02, 35.3]

# for i in range(len(scale)-1):
#     print scale[i+1] / scale[i]

base = 0.7

scale_lst = []

for i in range(11):
    scale_lst.append(round(base, 2))
    base = base * 1.32
    #print round(base, 2)

print "anchor scale:"
print np.array(scale_lst)*1.7
print scale_lst
print "\n"



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
kitti
*1
anchor scale:
[ 0.8   1.05  1.37  1.8   2.36  3.09  4.04  5.3   6.94  9.09 11.91]


h:
[ 18.2   24.2   31.88  42.2   55.64  73.16  95.96 126.2  165.56 217.16
 284.84]





*1.7
anchor scale:
[ 1.36   1.785  2.329  3.06   4.012  5.253  6.868  9.01  11.798 15.453
 20.247]


h:
[ 31.64   41.84   54.896  72.44   95.288 125.072 163.832 215.24  282.152
 369.872 484.928]
 

 h >= 16
 [0.67, 0.88, 1.17, 1.54, 2.03, 2.69, 3.54, 4.68, 6.18, 8.15, 10.76]


h:
[ 15.08  20.12  27.08  35.96  47.72  63.56  83.96 111.32 147.32 194.6
 257.24]
 
"""