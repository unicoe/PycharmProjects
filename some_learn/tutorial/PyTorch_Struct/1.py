# -*- coding: utf-8 -*-
# @Time    : 18-9-14 上午11:36
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : 1.py
# @Software: PyCharm Community Edition

import torch
from torch.autograd import Variable
import torch.nn
from torch import nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 1 input image channel, 6 output channels, 5*5 square convolution
        # kernel

        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(400,80)
        self.fc2 = nn.Linear(80, 20)
        self.fc3 = nn.Linear(20, 10)

    def forward(self, x):
        # max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        print(x.shape)
        # If size is a square you can only specify a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        print(x.shape)
        x = x.view(-1, self.num_flat_features(x))
        print(x.shape)
        x = F.relu(self.fc1(x))
        print(x.shape)
        x = F.relu(self.fc2(x))
        print(x.shape)
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:] # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features
net = Net()
print(net)


tmp_x = torch.randn(1,1,32,32);
out = net(tmp_x)

"""
torch.nn只支持小批量输入，整个torch.nn包都只支持小批量，而不是单个样本

nn.Conv2d将接受一个４维的张量，batch*channel*h*w


"""
