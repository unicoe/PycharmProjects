cnt = 0
for i in range(380,480,5):
    cnt += 1
print(cnt)

print (4800*12 + 1200*12 + 300*20 + 80*20 + 48*20 + 24*20 + 8*20)

print (4800*3 + 1200*3 + 300*5 + 80*5 + 48*5 + 24*5 + 8*5)


size = [[90, 120], [45, 60], [23, 30], [12, 15], [10, 13], [8, 11], [6, 9]]
ls = []
for i in size:
    ls.append([960/i[1],720/i[0]])
print(ls)


ls = [38, 19, 10, 5, 3, 1]
ls1 = []
for i in ls:
    ls1.append(i*i)

l1 = [6, 6, 10, 10, 10, 10]  # number of boxes per feature map location
l2 = [6, 6, 10, 10, 10, 20, 20]

cnt = 0
for i in range(0,6):
    cnt += ls[i]*l1[i]
print(cnt)

import time
import cv2
_imgpath = "/home/user/Disk1.8T/end_ex/test/set08_V003_I00689.jpg"
img = cv2.imread(_imgpath)
cv2.imshow("1", img)
cv2.waitKey(10990)
time.sleep(100000)