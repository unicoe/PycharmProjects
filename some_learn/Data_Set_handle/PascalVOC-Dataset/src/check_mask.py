from matplotlib import pyplot as plt
import PIL
from PIL import Image, ImageDraw
import numpy as np

seglbl1 = PIL.Image.open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/000148.jpg")
seglbl = seglbl1.convert('P')
seglbl = np.array(seglbl, dtype=np.int32)

print seglbl > 0
print seglbl > 1
print seglbl > 2
print seglbl > 3
print seglbl > 4

seglbl[seglbl > 0 ] = 1

plt.imshow(seglbl)
plt.show()
