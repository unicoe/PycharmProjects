# -*- coding: utf-8 -*-
import os
import cv2
import cPickle
import numpy as np
from utils.bbox import box_op
from scipy import io as scio
import matplotlib.pyplot as plt
import PIL
from PIL import Image, ImageDraw


def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok'
        return True
    else:

        print path + 'failed!'
        return False

root_dir = '/home/user/Disk1.8T/unicoe/ALFNet/data/cityperson_org'
all_img_path = os.path.join(root_dir, 'images')
all_anno_path = os.path.join(root_dir, 'annotations')
types = ['train']
rows, cols = 1024, 2048
for type in types:
	anno_path = os.path.join(all_anno_path, 'anno_'+type+'.mat')
	#res_path = os.path.join('data/cache/cityperson', type)
	image_data = []
	annos = scio.loadmat(anno_path)  # 导入mat文件
	index = 'anno_'+type+'_aligned'
	valid_count = 0
	iggt_count = 0
	rea_count = 0
	box_count = 0
	for l in range(len(annos[index][0])):
		anno = annos[index][0][l]
		cityname = anno[0][0][0][0].encode()
		imgname = anno[0][0][1][0].encode()
		gts = anno[0][0][2]
		img_path = os.path.join(all_img_path, type + '/'+ cityname+'/'+imgname)
		boxes = []
		ig_boxes = []
		vis_boxes = []
		if len(gts)==0:
			continue
		for i in range(len(gts)):
			label, x1, y1, w, h = gts[i, :5]
			x1, y1 = max(int(x1), 0), max(int(y1), 0)
			w, h = min(int(w), cols - x1 -1), min(int(h), rows - y1 -1)
			xv1, yv1, wv, hv = gts[i, 6:]
			xv1, yv1 = max(int(xv1), 0), max(int(yv1), 0)
			wv, hv = min(int(wv), cols - xv1 - 1), min(int(hv), rows - yv1 - 1)
			# here we only choose height>50 optionally
			if label == 1 and h>=50:
				rea_count += 1
				box = np.array([int(x1), int(y1), int(x1)+int(w), int(y1)+int(h)])
				boxes.append(box)
				vis_box = np.array([int(xv1), int(yv1), int(xv1)+int(wv), int(yv1)+int(hv)])
				vis_boxes.append(vis_box)
			else:
				ig_box = np.array([int(x1), int(y1), int(x1)+int(w), int(y1)+int(h)])
				ig_boxes.append(ig_box)

		boxes = np.array(boxes)
		vis_boxes = np.array(vis_boxes)
		ig_boxes = np.array(ig_boxes)
		if len(boxes)==0:
			continue
		valid_count += 1

		#img = cv2.imread(img_path)

		# for i in range(len(vis_boxes)):
		# 	#(x1, y1, x2, y2) = boxes[i, :]
		# 	(x1, y1, x2, y2) = vis_boxes[i, :]
		# 	if y2-y1>50:
		# 		cv2.rectangle(img, (x1, y1), (x2, y2),(255,0,0), 2)
				# y3 = int(y1+(y2-y1)/3.0)
				# cv2.rectangle(img, (x1, y1), (x2, y3), (0, 255, 0), 2)
				# cv2.putText(img, str(boxes[i, 0]), (x1 - 2, y1 - 2), cv2.FONT_HERSHEY_DUPLEX, 1,colors[label], 1)

		# plt.imshow(img, interpolation='bicubic')
 		# print(img_path)
		# annotation = {}
		# annotation['filepath'] = img_path
		if len(ig_boxes) > 0 and len(boxes) > 0:
			boxig_overlap = box_op(np.ascontiguousarray(boxes, dtype=np.float),
								   np.ascontiguousarray(ig_boxes, dtype=np.float))
			ignore_sum = np.sum(boxig_overlap, axis=1)
			oriboxes = np.copy(boxes)
			boxes = oriboxes[ignore_sum < 0.5, :]
			vis_boxes = vis_boxes[ignore_sum < 0.5, :]

			if ignore_sum.max()>=0.5:
				iggt_count += len(ignore_sum)-len(boxes)
				ig_boxes = np.concatenate([ig_boxes, oriboxes[ignore_sum >= 0.5, :]], axis=-0)
		box_count += len(boxes)

		## 生成弱语义分割标注

		img = PIL.Image.new("P", (2048, 1024), color=0)

		draw2 = ImageDraw.Draw(img)

		for i in range(len(boxes)):
			# (x1, y1, x2, y2) = boxes[i, :]
			(x11, y11, x22, y22) = boxes[i, :]

			# draw2.rectangle((0, 0, 2048, 1024), fill=(0))
			# draw2.rectangle((x1 - 3, y1 - 3, x2 + 3, y2 + 3), fill=(224, 224, 192))
			draw2.rectangle((x11 - 3, y11 - 3, x22 + 3, y22 + 3), fill=(255))
			print((x11, y11, x22, y22))
		# img = img[:,:,(2,1,0)]
		# debug 2018-12-06 22:12:56
		# plt.imshow(img)
		# plt.show()
		# cv2.imwrite("/home/user/Disk1.8T/data_set/seglabel_png1/" + i_im + ".png", img)
		i_folder = img_path.split(".")[1].split('/')[-2]
		i_im = img_path.split('.')[1].split('/')[-1]
		mkdir("/home/user/Disk1.8T/data_set/city_seglabel_png_5_6/" + i_folder + '/')

		img.save("/home/user/Disk1.8T/data_set/city_seglabel_png_5_6/" + i_folder + '/' + i_im + ".png", 'png')

	# annotation['bboxes'] = boxes
		# annotation['vis_bboxes'] = vis_boxes
		# annotation['ignoreareas'] = ig_boxes
		# image_data.append(annotation)
	# with open(res_path, 'wb') as fid:
	# 	cPickle.dump(image_data, fid, cPickle.HIGHEST_PROTOCOL)
	print '{} has {} images and {} valid images, {} valid gt and {} ignored gt'.format(type, len(annos[index][0]), valid_count, box_count, iggt_count)