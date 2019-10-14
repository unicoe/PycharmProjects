import cv2


img = cv2.imread("/home/user/PycharmProjects/some_learn/opencv/webwxgetmsgimg.jpg")
img = cv2.pyrDown(img)
print(img.shape)
img = img[0:540,0:540,]
cv2.imshow("me", img)
#cv2.waitKey(0)
cv2.imwrite("/home/user/PycharmProjects/some_learn/opencv/result.jpg", img)