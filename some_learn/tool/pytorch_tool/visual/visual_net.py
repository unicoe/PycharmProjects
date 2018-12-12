# -*- coding: utf-8 -*-
# @Time    : 18-12-11 下午4:12
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : visual_net.py
# @Software: PyCharm


from torch.autograd import Variable
from examples.voc.visual.visualize import  make_dot
from torchfcn.models import *
import torch

"""
计算图可视化
"""

# vgg ssd
# ssd_net = build_ssd('train', 300, 2)
# net = ssd_net
#
# x = Variable(torch.randn(1,3,300,300))
#
# y = net(x)
# print(net)
#
# dot = make_dot(y, params=dict(net.named_parameters()))
# print(dot)
# dot.view()


# resnet
#
# from layers.resnet import *
#
# resnet = resnet101()
# net = resnet
#
# x = Variable(torch.randn(1,3,300,300))
#
# y = net(x)
# print(net)
#
# dot = make_dot(y, params=dict(net.named_parameters()))
# print(dot)
# dot.view()

# FCN8s
model = FCN8sAtOnce(n_class=21)
net = model

x = Variable(torch.randn(1,3,300,300))

y = net(x)
print(net)

dot = make_dot(y, params=dict(net.named_parameters()))
print(dot)
dot.view()