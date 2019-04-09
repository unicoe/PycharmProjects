# -*- coding: utf-8 -*-
# @Time    : 19-1-16 下午8:34
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : 遍历文件夹和文件.py
# @Software: PyCharm
import os


def fun(path):            #含子文件夹
    for (root, dirs, files) in os.walk(path):
        for filename in files:
             print(os.path.join(root,filename))
