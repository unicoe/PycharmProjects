from __future__ import print_function
import torch as t
import torch.nn as nn

x = t.Tensor([[1,2],[4,5]])

print(x)

y = nn.Conv2d(1,1,kernel_size=3,padding=1,stride=2)

out = y(x)

print(out)