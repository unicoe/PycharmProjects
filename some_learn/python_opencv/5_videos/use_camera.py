# -*- coding: utf-8 -*-
# @Time    : 18-6-6 上午11:32
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : use_camera.py
# @Software: PyCharm Community Edition

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", gray)
    if cv2.waitKey(0):
        break

cap.release()
cv2.destroyAllWindows()