from matplotlib import pyplot as plt
import cv2

im = cv2.imread("/home/user/PycharmProjects/MissRate_FPPI_plot/000000.png")

#cv2.rectangle(im,(int(856),int(318)),(int(856+39),int(318+41)),(0,225,0),2)
im.save();
plt.imshow(im)

plt.show()

