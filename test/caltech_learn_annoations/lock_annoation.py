#18	[489.426367509247,142.926493006612,18.9472151204275,45.9412942528890]	true	1	[489.426367509247,142.926493006612,12.2535234905872,15.9078169143348]
#18	[471.323909531502,148.398673100121,17.6296489727196,44.7992267383284]	true	1	[473.513268998794,148.398673100121,11.3092536636053,13.0419269309319]
from matplotlib import pyplot as plt
import cv2
#im = cv2.imread("/home/user/PycharmProjects/test/caltech_learn_annoations/532.jpg")
im = cv2.imread("/home/user/PycharmProjects/test/caltech_learn_annoations/set06_V001_I00029.jpg")
# [452.380659429031,167.729915560917,47.0928829915561,52.4969843184559]
# [375.544632086852,172.740631992242,22.3884197828709,49.0229191797346]
# 611 179 636 241,462 180 480 224
cv2.rectangle(im, (611,179), (636, 241), (255,255,0), 2)
cv2.rectangle(im, (462,180), (480, 224), (255,255,0), 2)
cv2.imwrite("/home/user/PycharmProjects/test/caltech_learn_annoations/set06_V001_I000291.jpg",im)