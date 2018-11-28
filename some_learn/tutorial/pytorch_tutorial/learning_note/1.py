# -*- coding: utf-8 -*-
# @Time    : 18-6-12 下午9:43
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : 1.py
# @Software: PyCharm Community Edition
import torch

x = torch.Tensor(2,3,4)

print(x)

a = torch.rand(2,3,4)
b = torch.rand(2,3,4)

_ = torch.add(a,b,out=x)

print(x)

a.add_(b)

print(torch.cuda.is_available())

from torch.autograd import Variable

x = torch.rand(5)

x = Variable(x, requires_grad=True)

y = x*2

grads = torch.FloatTensor([1,2,3,4,5])

print(y.backward(grads))

print(x.grad)