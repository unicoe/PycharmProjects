# _*_ coding:utf-8 _*_
# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Test a Fast R-CNN network on an imdb (image database)."""

from fast_rcnn.config import cfg, get_output_dir
from fast_rcnn.bbox_transform import clip_boxes, bbox_transform_inv
import argparse
from utils.timer import Timer
import numpy as np
import cv2
import caffe
from fast_rcnn.nms_wrapper import nms
import cPickle
from utils.blob import im_list_to_blob
import os

#--测试适应不同尺寸的输入图片

######## 4444 ########
def _get_image_blob(im):
    """Converts an image into a network input.

    Arguments:
        im (ndarray): a color image in BGR order

    Returns:
        blob (ndarray): a data blob holding an image pyramid
        im_scale_factors (list): list of image scales (relative to im) used
            in the image pyramid
    """
    im_orig = im.astype(np.float32, copy=True)
    im_orig -= cfg.PIXEL_MEANS

    im_shape = im_orig.shape
    im_size_min = np.min(im_shape[0:2])
    im_size_max = np.max(im_shape[0:2])

    processed_ims = []
    im_scale_factors = []

    for target_size in cfg.TEST.SCALES:
        # im_scale1 = float(target_size) / float(im_size_min)
        #
        # # Prevent the biggest axis from being more than MAX_SIZE
        #
        # if np.round(im_scale1 * im_size_max) > cfg.TEST.MAX_SIZE:
        #    im_scale1 = float(cfg.TEST.MAX_SIZE) / float(im_size_max)

        # im = cv2.resize(im_orig, None, None, fx=im_scale, fy=im_scale,
        #                 interpolation=cv2.INTER_LINEAR)


        # --测试来适应不同尺寸的输入图片
        im_scale = []
        im_scale.append(float(target_size) / float(im_size_min))
        im_scale.append(float(cfg.TEST.MAX_SIZE) / float(im_size_max))

        # print type(im_scale[0])
        im = cv2.resize(im_orig, (2112, 640), interpolation=cv2.INTER_LINEAR)
        im_scale_factors.append(im_scale)
        processed_ims.append(im)

    # Create a blob to hold the input images
    blob = im_list_to_blob(processed_ims)

    return blob, np.array(im_scale_factors)

def _get_rois_blob(im_rois, im_scale_factors):
    """Converts RoIs into network inputs.

    Arguments:
        im_rois (ndarray): R x 4 matrix of RoIs in original image coordinates
        im_scale_factors (list): scale factors as returned by _get_image_blob

    Returns:
        blob (ndarray): R x 5 matrix of RoIs in the image pyramid
    """
    rois, levels = _project_im_rois(im_rois, im_scale_factors)
    rois_blob = np.hstack((levels, rois))
    return rois_blob.astype(np.float32, copy=False)

def _project_im_rois(im_rois, scales):
    """Project image RoIs into the image pyramid built by _get_image_blob.

    Arguments:
        im_rois (ndarray): R x 4 matrix of RoIs in original image coordinates
        scales (list): scale factors as returned by _get_image_blob

    Returns:
        rois (ndarray): R x 4 matrix of projected RoI coordinates
        levels (list): image pyramid levels used by each projected RoI
    """
    im_rois = im_rois.astype(np.float, copy=False)

    if len(scales) > 1:
        widths = im_rois[:, 2] - im_rois[:, 0] + 1
        heights = im_rois[:, 3] - im_rois[:, 1] + 1

        areas = widths * heights
        scaled_areas = areas[:, np.newaxis] * (scales[np.newaxis, :] ** 2)
        diff_areas = np.abs(scaled_areas - 224 * 224)
        levels = diff_areas.argmin(axis=1)[:, np.newaxis]
    else:
        levels = np.zeros((im_rois.shape[0], 1), dtype=np.int)

    rois = im_rois * scales[levels]

    return rois, levels

######## 3333 ########
def _get_blobs(im, rois): # rois = none
    """Convert an image and RoIs within that image into network inputs."""
    blobs = {'data' : None, 'rois' : None}
    blobs['data'], im_scale_factors = _get_image_blob(im)
    if not cfg.TEST.HAS_RPN: # pass
        blobs['rois'] = _get_rois_blob(rois, im_scale_factors)
    return blobs, im_scale_factors # blobs = im_info / im_scale_factors = resize_scale

######## 2222 ########
def im_detect(net, im, boxes=None):
    """Detect object classes in an image given object proposals.

    Arguments:
        net (caffe.Net): Fast R-CNN network to use
        im (ndarray): color image to test (in BGR order)
        boxes (ndarray): R x 4 array of object proposals or None (for RPN)

    Returns:
        scores (ndarray): R x K array of object class scores (K includes
            background as object category 0)
        boxes (ndarray): R x (4*K) array of predicted bounding boxes
    """
    blobs, im_scales = _get_blobs(im, boxes)
    im_s = im_scales[0][0]
    print im_scales
    # When mapping from image ROIs to feature map ROIs, there's some aliasing
    # (some distinct image ROIs get mapped to the same feature ROI).
    # Here, we identify duplicate feature ROIs, so we only compute features
    # on the unique subset.
    if cfg.DEDUP_BOXES > 0 and not cfg.TEST.HAS_RPN: #pass
        v = np.array([1, 1e3, 1e6, 1e9, 1e12])
        hashes = np.round(blobs['rois'] * cfg.DEDUP_BOXES).dot(v)
        _, index, inv_index = np.unique(hashes, return_index=True,
                                        return_inverse=True)
        blobs['rois'] = blobs['rois'][index, :]
        boxes = boxes[index, :]

    if cfg.TEST.HAS_RPN: #输入数据
        im_blob = blobs['data']
        # blobs['im_info'] = np.array(
        #     [[im_blob.shape[2], im_blob.shape[3], im_scales[0]]],
        #     dtype=np.float32)

        #--测试来适应不同尺寸的输入图片
        blobs['im_info'] = np.array(
                 [[im_blob.shape[2], im_blob.shape[3], im_s]],
                 dtype=np.float32)

    # reshape network inputs
    net.blobs['data'].reshape(*(blobs['data'].shape))
    if cfg.TEST.HAS_RPN:
        net.blobs['im_info'].reshape(*(blobs['im_info'].shape))
    else:
        net.blobs['rois'].reshape(*(blobs['rois'].shape))
#-----------------------------------

    # do forward
    forward_kwargs = {'data': blobs['data'].astype(np.float32, copy=False)}
    if cfg.TEST.HAS_RPN:
        forward_kwargs['im_info'] = blobs['im_info'].astype(np.float32, copy=False)
    else: # pass
        forward_kwargs['rois'] = blobs['rois'].astype(np.float32, copy=False)
    blobs_out = net.forward(**forward_kwargs)


    #### ************* ####
    if cfg.TEST.HAS_RPN:
        #assert len(im_scales) == 2, "Only single-image batch implemented"
	#--------------拷贝rois---------------------
        rois1 = net.blobs['rpn_rois_p2'].data.copy() 
        rois2 = net.blobs['rpn_rois_p3'].data.copy()
        # unscale back to raw image space

        # print im_scales[0][0],im_scales[0][1]

	#--------------boxes---------------------
        #--测试来适应不同尺寸的输入图片

        bx1 = rois1[:,1] / im_scales[0][1]
        by1 = rois1[:,2] / im_scales[0][0]
        bx2 = rois1[:,3] / im_scales[0][1]
        by2 = rois1[:,4] / im_scales[0][0]

        boxes1 = np.stack((bx1, by1, bx2, by2),axis=1)

        bx1 = rois2[:, 1] / im_scales[0][1]
        by1 = rois2[:, 2] / im_scales[0][0]
        bx2 = rois2[:, 3] / im_scales[0][1]
        by2 = rois2[:, 4] / im_scales[0][0]

        boxes2 = np.stack((bx1, by1, bx2, by2),axis=1)

        # boxes1 = rois1[:, 1:5] / im_scales[0]
        # boxes2 = rois2[:, 1:5] / im_scales[0]

    if cfg.TEST.SVM: # pass
        # use the raw scores before softmax under the assumption they
        # were trained as linear SVMs
        scores = net.blobs['cls_score'].data

    else: 
	#-------------prob----------------------
        # use softmax estimated probabilities
        scores1 = blobs_out['cls_prob_p2']  ## return ##
        scores2 = blobs_out['cls_prob_p3']  ## return ##


    if cfg.TEST.BBOX_REG: 
	#-------------deltas----------------------
        # Apply bounding-box regression deltas
        box_deltas1 = blobs_out['bbox_pred_p2']
        box_deltas2 = blobs_out['bbox_pred_p3']


	#-------------pred----------------------
        pred_boxes1 = bbox_transform_inv(boxes1, box_deltas1)
        pred_boxes1 = clip_boxes(pred_boxes1, im.shape)  ## return ##
        #pred_boxes1 = clip_boxes(pred_boxes1, (640,2112))  ## return ##

        pred_boxes2 = bbox_transform_inv(boxes2, box_deltas2)
        pred_boxes2 = clip_boxes(pred_boxes2, im.shape)  ## return ##
        #pred_boxes2 = clip_boxes(pred_boxes2, (640,2112))  ## return ##

    else: # pass
        # Simply repeat the boxes, once for each class
        pred_boxes = np.tile(boxes, (1, scores.shape[1]))


    if cfg.DEDUP_BOXES > 0 and not cfg.TEST.HAS_RPN: # pass
        # Map scores and predictions back to the original set of boxes
        scores = scores[inv_index, :]
        pred_boxes = pred_boxes[inv_index, :]

	
    scores = np.vstack((scores1,scores2))
    pred_boxes = np.vstack((pred_boxes1,pred_boxes2))
    return scores, pred_boxes

def vis_detections(im, class_name, dets, thresh=0.3):
    """Visual debugging of detections."""
    import matplotlib.pyplot as plt
    im = im[:, :, (2, 1, 0)]
    for i in xrange(np.minimum(10, dets.shape[0])):
        bbox = dets[i, :4]
        score = dets[i, -1]
        if score > thresh:
            plt.cla()
            plt.imshow(im)
            plt.gca().add_patch(
                plt.Rectangle((bbox[0], bbox[1]),
                              bbox[2] - bbox[0],
                              bbox[3] - bbox[1], fill=False,
                              edgecolor='g', linewidth=3)
                )
            plt.title('{}  {:.3f}'.format(class_name, score))
            plt.show()

def apply_nms(all_boxes, thresh):
    """Apply non-maximum suppression to all predicted boxes output by the
    test_net method.
    """
    num_classes = len(all_boxes)
    num_images = len(all_boxes[0])
    nms_boxes = [[[] for _ in xrange(num_images)]
                 for _ in xrange(num_classes)]
    for cls_ind in xrange(num_classes):
        for im_ind in xrange(num_images):
            dets = all_boxes[cls_ind][im_ind]
            if dets == []:
                continue
            # CPU NMS is much faster than GPU NMS when the number of boxes
            # is relative small (e.g., < 10k)
            # TODO(rbg): autotune NMS dispatch
            keep = nms(dets, thresh, force_cpu=True)
            if len(keep) == 0:
                continue
            nms_boxes[cls_ind][im_ind] = dets[keep, :].copy()
    return nms_boxes


######## 1111 ########
def test_net(net, imdb, max_per_image=400, thresh=-np.inf, vis=False):
    """Test a Fast R-CNN network on an image database."""

    num_images = len(imdb.image_index) # 测试图片数量 = 4024

    # all detections are collected into:
    #    all_boxes[cls][image] = N x 5 array of detections in
    #    (x1, y1, x2, y2, score)
    all_boxes = [[[] for _ in xrange(num_images)]
                 for _ in xrange(imdb.num_classes)]

    output_dir = get_output_dir(imdb, net)

    # timers
    _t = {'im_detect' : Timer(), 'misc' : Timer()}

    if not cfg.TEST.HAS_RPN: # 不使用RPN
        roidb = imdb.roidb

    for i in xrange(num_images): # 每张图
        # filter out any ground truth boxes
        if cfg.TEST.HAS_RPN: # 使用RPN
            box_proposals = None
        else: # pass
            # The roidb may contain ground-truth rois (for example, if the roidb
            # comes from the training or val split). We only want to evaluate
            # detection on the *non*-ground-truth rois. We select those the rois
            # that have the gt_classes field set to 0, which means there's no
            # ground truth.
            box_proposals = roidb[i]['boxes'][roidb[i]['gt_classes'] == 0]

        im = cv2.imread(imdb.image_path_at(i))
        _t['im_detect'].tic()
        scores, boxes = im_detect(net, im, box_proposals)  #box_proposals = none
        _t['im_detect'].toc()

        _t['misc'].tic()
        # skip j = 0, because it's the background class
        for j in xrange(1, imdb.num_classes):
            inds = np.where(scores[:, j] > thresh)[0]
            cls_scores = scores[inds, j]
            if cfg.TEST.AGNOSTIC:
                cls_boxes = boxes[inds, 4:8]
            else:
                cls_boxes = boxes[inds, j*4:(j+1)*4]
            cls_dets = np.hstack((cls_boxes, cls_scores[:, np.newaxis])) \
                .astype(np.float32, copy=False)

            keep = nms(cls_dets, cfg.TEST.NMS)
            cls_dets = cls_dets[keep, :]
            if vis:
                vis_detections(im, imdb.classes[j], cls_dets)
            all_boxes[j][i] = cls_dets

        # Limit to max_per_image detections *over all classes*
        # if max_per_image > 0:
        #     image_scores = np.hstack([all_boxes[j][i][:, -1]
        #                               for j in xrange(1, imdb.num_classes)])
        #     if len(image_scores) > max_per_image:
        #         image_thresh = np.sort(image_scores)[-max_per_image]
        #         for j in xrange(1, imdb.num_classes):
        #             keep = np.where(all_boxes[j][i][:, -1] >= image_thresh)[0]
        #             all_boxes[j][i] = all_boxes[j][i][keep, :]
        _t['misc'].toc()

        print 'im_detect: {:d}/{:d} {:.3f}s {:.3f}s' \
              .format(i + 1, num_images, _t['im_detect'].average_time,
                      _t['misc'].average_time)

    det_file = os.path.join(output_dir, 'detections.pkl')
    with open(det_file, 'wb') as f:
        cPickle.dump(all_boxes, f, cPickle.HIGHEST_PROTOCOL)

    print 'Evaluating detections'
    imdb.evaluate_detections(all_boxes, output_dir)