# --------------------------------------------------------
# Faster R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick and Sean Bell
# --------------------------------------------------------

import numpy as np

# Verify that we compute the same anchors as Shaoqing's matlab implementation:
#
#    >> load output/rpn_cachedir/faster_rcnn_VOC2007_ZF_stage1_rpn/anchors.mat
#    >> anchors
#
#    anchors =
#
#       -83   -39   100    56
#      -175   -87   192   104
#      -359  -183   376   200
#       -55   -55    72    72
#      -119  -119   136   136
#      -247  -247   264   264
#       -35   -79    52    96
#       -79  -167    96   184
#      -167  -343   184   360

#array([[ -83.,  -39.,  100.,   56.],
#       [-175.,  -87.,  192.,  104.],
#       [-359., -183.,  376.,  200.],
#       [ -55.,  -55.,   72.,   72.],
#       [-119., -119.,  136.,  136.],
#       [-247., -247.,  264.,  264.],
#       [ -35.,  -79.,   52.,   96.],
#       [ -79., -167.,   96.,  184.],
#       [-167., -343.,  184.,  360.]])

#def generate_anchors(base_size=16, ratios=[0.5, 1, 2],
def generate_anchors(feat_stride=8, base_size=16, ratios=[2.44],
                     scales=2**np.arange(3, 6)):
    """
    Generate anchor (reference) windows by enumerating aspect ratios X
    scales wrt a reference (0, 0, 15, 15) wianchor_target_layer.py
generate_anchors.py
proposal_layer.py
proposal_target_layer.pyndow.
    """
    ratios=[2.44]

    #-- cityperons 40
    # if   feat_stride == 8:
    #     scales = np.array((2.5, 3.2, 4.1, 5.24, 6.71, 8.59, 10., 14.07, 18.01, 23.06, 29.51),dtype=float)*0.5
    # elif feat_stride == 16:
    #     scales = np.array((2.5, 3.2, 4.1, 5.24, 6.71, 8.59, 10., 14.07, 18.01, 23.06, 29.51),dtype=float)*0.5

    #-- citypersons 50
    # if   feat_stride == 8:
    #     scales = np.array((3.4, 4.25, 5.31, 6.64, 8.3, 10.38, 12.97, 16.21, 20.27, 25.33, 31.66),dtype=float)*0.5
    # elif feat_stride == 16:
    #     scales = np.array((3.4, 4.25, 5.31, 6.64, 8.3, 10.38, 12.97, 16.21, 20.27, 25.33, 31.66),dtype=float)*0.5

    base_anchor = np.array([1, 1, base_size, base_size]) - 1
    ratio_anchors = _ratio_enum(base_anchor, ratios)
    anchors = np.vstack([_scale_enum(ratio_anchors[i, :], scales)
                         for i in xrange(ratio_anchors.shape[0])])

    return anchors


#2.0, 2.7, 3.64, 4.92, 6.64, 8.97, 12.11, 16.34, 22.06, 29.79, 40.21



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
    import time
    t = time.time()
    a = generate_anchors()
    print(a[:,3] -a[:,1])
    # print time.time() - t
    # print a
    # from IPython import embed; embed()
