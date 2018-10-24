from PIL import Image
import numpy as np
import os

img = Image.open(os.path.join("/home/user/PycharmProjects/mask_handle/instance_handle/label1.png"))
img = Image.fromarray(np.uint8(img))

img.save(os.path.join("/home/user/PycharmProjects/mask_handle/instance_handle/12.png"))