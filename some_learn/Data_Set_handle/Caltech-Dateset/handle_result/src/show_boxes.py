# --------------------------------------------------------
# Fully Convolutional Instance-aware Semantic Segmentation
# Copyright (c) 2017 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Yi Li, Haochen Zhang
# --------------------------------------------------------

import matplotlib.pyplot as plt
from random import random as rand


def show_boxes(im, dets, classes, scale = 1.0):
    plt.cla()
    plt.axis("off")
    plt.imshow(im)
    for cls_idx, cls_name in enumerate(classes):
        cls_dets = dets[cls_idx]
        for det in cls_dets:
            bbox = det[:4] * scale
            color = '#66CDAA' #(1, 0, 0)
            rect = plt.Rectangle((bbox[1], bbox[2]),
                                  bbox[3] - bbox[1],
                                  bbox[4] - bbox[2], fill=False,
                                  edgecolor=color, linewidth=1.25)
            plt.gca().add_patch(rect)

            if cls_dets.shape[1] == 5:
                score = det[0]
                plt.gca().text(bbox[1], bbox[2],
                               '{:s} {:.3f}'.format(cls_name, score),
                               bbox=dict(facecolor=color, alpha=0.5), fontsize=9, color='white')
    plt.show()
    return im

