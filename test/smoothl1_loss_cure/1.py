# -*- coding: utf-8 -*-
# @Time    : 18-7-23 下午10:08
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : 1.py
# @Software: PyCharm Community Edition
from pylab import *

x = linspace(-3,3)

cond1 = [True if (i>1 or i<-1) else False for i in x]
cond2 = [True if (i>=-1 and i<=1) else False for i in x]

y = 0.5*x*x*cond2  + (abs(x) - 0.5)*cond1
#y = (abs(x) -0.5)*cond1
print y
plot(x,y,'r')
savefig("/home/user/PycharmProjects/test/smoothl1_loss_cure/1.jpg")
show()
