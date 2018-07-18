# -*- coding: utf-8 -*-
# @Time    : 18-6-12 下午9:55
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : 2.py
# @Software: PyCharm Community Edition
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1,6,5)
        self.conv2 = nn.Conv2d(6,16,5)

        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2,2))

        x = F.max_pool2d(F.relu(self.conv2(x)), 2)

        x = x.view(-1, self.num_flat_features(x))

        x = F.relu(self.fc1(x))

        x = F.relu(self.fc2(x))

        x = self.fc3(x)

        return x

    def num_flat_features(self,x):
        size = x.size()[1:]
        num_feautres = 1
        for s in size:
            num_feautres *= s
        return num_feautres

net = Net()
print(net)

print(len(list(net.parameters())))

input = Variable(torch.randn(1,1,32,32))

out = net(input)

print(out)

print(out.backward(torch.randn(1,10)))

lr = 0.01

for f in net.parameters():
    f.data.sub_(f.grad.data * lr)

import torch.optim as optim

optimizer = optim.SGD(net.parameters(), lr=0.01)

optimizer.zero_grad()

output = net(input)

loss = criterion(output,target)