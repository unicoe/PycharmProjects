# -*- coding: utf-8 -*-
# @Time    : 18-6-22 下午6:40
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : test_resnet_50.py
# @Software: PyCharm Community Edition


from mxnet import nd
from mxnet import autograd

x = nd.zeros((2,3,4))
y = nd.ones((2,3,4))

print(x == y)

print(x > y)

print(x < y)


x = nd.arange(4).reshape((4,1))

print(x)

tmp = x.attach_grad()
print(tmp)

with autograd.record():
    y = 2 * nd.dot(x.T, x)

tmp = y.backward()
print(tmp)

print(x.grad, x.grad==4*x)



def f(a):
    b = a*2
    while b.norm().asscalar() < 1000:
        b = b*2
    if b.sum().asscalar() > 0:
        c = b
    else:
        c = 100*b
    return c

a = nd.random.normal(shape=(2,2))

a.attach_grad()

with autograd.record():
    c = f(a)
c.backward()

print(a.grad == c/a)

def f1(a):
    b = a*a*a
    return b
a = nd.random.normal(shape=1)
a.attach_grad()
with autograd.record():
    b = f1(a)
b.backward()

print(a)
print(a.grad == 3*a*a)
print(b)
print(a.grad)



a = nd.ones(shape=3)

b = 10

print(a+b)


