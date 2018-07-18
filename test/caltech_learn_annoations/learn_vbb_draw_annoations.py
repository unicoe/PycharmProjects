from matplotlib import  pyplot as plt
import cv2
im = cv2.imread("/home/user/PycharmProjects/test/caltech_learn_annoations/set06_V002_I01499.jpg")

#
# /home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages/set10_V009_I01589.jpg 1 0.654737 358 109 524 461
# /home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages/set10_V009_I01589.jpg 1 0.566443 247 125 404 441
# /home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages/set10_V009_I01589.jpg 1 0.294481 192 15 449 455
# /home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages/set10_V009_I01589.jpg 1 0.240995 33 165 55 216
# /home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages/set10_V009_I01589.jpg 1 0.233527 379 168 416 258
# /home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages/set10_V009_I01589.jpg 1 0.228287 547 194 563 234
# /home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages/set10_V009_I01589.jpg 1 0.227012 25 174 57 257
# /home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages/set10_V009_I01589.jpg 1 0.225171 220 206 240 261
# # [452.380659429031,167.729915560917,47.0928829915561,52.4969843184559]
# [375.544632086852,172.740631992242,22.3884197828709,49.0229191797346]
# [498.576650563607,109.758615136876,61.8666666666667,253.866666666667]
# [134.138107416880,184.547267216065,23.3853935777211,35.2269015818888]
#877 383 14 26
#1844 436 44 106
#3 892 445 21 53 24000 892 445 21 53', '3 901 443 34 55 24001 901 443 34 55'


# ['414 179 424 209', '439 181 451 209', '425 181 435 209', '397 182 406 204'] 503 140 565 321

cv2.rectangle(im, (414,179), (424, 209), (0,255,0), 1)
cv2.rectangle(im, (439,181), (451, 209), (0,255,0), 1)
cv2.rectangle(im, (425,181), (435, 209), (0,255,0), 1)
cv2.rectangle(im, (397,182), (406, 204), (0,255,0), 1)
cv2.rectangle(im, (503,140), (565, 321), (0,255,0), 1)
#cv2.rectangle(im, (134,184), (134+23, 184+25), (0,255,0), 2)
plt.imshow(im)
plt.show()