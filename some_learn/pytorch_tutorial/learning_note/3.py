# -*- coding: utf-8 -*-
# @Time    : 18-9-18 下午4:40
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : 3.py
# @Software: PyCharm Community Edition

import torch
import torch.nn as nn
import torch.nn.functional as F

class Test(nn.Module):
    def __init__(self):
        super(Test, self).__init__()
        self.conv1 = nn.Conv2d(1,1,kernel_size=5, stride=2, padding=1)
        self.conv2 = nn.Conv2d(1,1,kernel_size=3, stride=1, padding=1)



    def forward(self,x):
        out = self.conv1(x)
        print(out.shape)
        out = F.max_pool2d(out,kernel_size=3, padding=0, stride=1)
        print(out.shape)
        out = self.conv2(out)
        print(out.shape)
        return out


def print_model_parm_nums():
    model = Test()
    total = sum([param.nelement() for param in model.parameters()])
    print('  + Number of params: %.2fM' % (total / 1e6))

# 作者：Big Fish
# 链接：https://zhuanlan.zhihu.com/p/33992733
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

input_randn = torch.randn(1,1,200,200)

net = Test()
out = net(input_randn)

print_model_parm_nums()
