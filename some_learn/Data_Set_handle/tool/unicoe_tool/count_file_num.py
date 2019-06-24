#!/bin/bash
#--coding:utf-8--
import os
path = os.getcwd()    #获取当前路径
count = 0
for root,dirs,files in os.walk(path):    #遍历统计
      for each in files:
             count += 1   #统计文件夹下文件个数
print count          
