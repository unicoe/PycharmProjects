# -*- coding: utf-8 -*-
# @Time    : 18-6-22 下午8:21
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : line_reg.py
# @Software: PyCharm Community Edition

from matplotlib import pyplot as plt
from mxnet import autograd, nd
import random

num_inputs = 2
num_examples = 1000

true_w = [2, -3.4]
true_b = 4.2

features = nd.random.normal(scale=1, shape=(num_examples, num_inputs))
labels = true_w[0]* features[:,0] + true_w[1]*features[:,1] + true_b
labels += nd.random.normal(scale=0.01, shape=labels.shape)

print(features[0], labels[0])

# plt.rcParams['figure.figsize'] = (4,3)
# im = plt.scatter(features[:,1].asnumpy(), labels.asnumpy(), 1)
# plt.show()

batch_size = 10

def data_iter(batch_size, num_examples, features, labels):
    indices = list(range(num_examples))

    random.shuffle(indices)

    for i in range(0, num_examples, batch_size):
        j = nd.array(indices[i:min(i+batch_size, num_examples)])
        yield features.take(j), labels.take(j)

for X,y in data_iter(batch_size, num_examples, features, labels):
    print(X,y)
    break


w = nd.random.normal(scale=0.01, shape=(num_inputs, 1))
b = nd.zeros(shape=(1,))
params = [w,b]

for param in params:
    param.attach_grad()

def linreg(X,w,b):
    return nd.dot(X,w)+b

def squared_loss(y_hat, y):
    return (y_hat - y.reshape(y_hat.shape)) ** 2/2

def sgd(params, lr, batch_size):
    for param in params:
        param[:] = param - lr*param.grad / batch_size

lr = 0.09
num_epochs = 10

net = linreg
loss = squared_loss

for epoch in range(1, num_epochs+1):
    for X,y in data_iter(batch_size, num_examples, features, labels):
        with autograd.record():
            l = loss(net(X, w, b), y)
        l.backward()
        sgd([w,b], lr, batch_size)
    print("epoch %d, loss %f"
          % (epoch, loss(net(features, w, b), labels).mean().asnumpy()))

print(true_w, w)
print(true_b, b)