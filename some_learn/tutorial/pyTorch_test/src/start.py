from __future__ import print_function
import torch as t
import torch.nn as nn
import torch
# x = t.Tensor([[1,2],[4,5]])
#
# print(x)
#
# y = nn.Conv2d(1,1,kernel_size=3,padding=1,stride=2)
#
# out = y(x)
#
# print(out)

print(torch.__version__)

torch.random.manual_seed(7)
torch.cuda.random.manual_seed(7)

w = torch.Tensor(3,5)
nn.init.xavier_normal_(w)
print(w)