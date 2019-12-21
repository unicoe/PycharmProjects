# -*- coding: utf-8 -*-
import os

path = "/home/user/Disk1.8T/lb_exp/add_data/"

num = 9000

for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, "00" + str(num)+'.jpg'))
    num += 1