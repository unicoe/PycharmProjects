# -*- coding: utf-8 -*-
# @Time    : 18-6-22 下午10:04
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : gluon_softmax.py
# @Software: PyCharm Community Edition

import sys
sys.path.append("..")

import gluonbook as gb

from mxnet import autograd, nd
from mxnet.gluon import data as gdata

def transform(feature, label):
    return feature.astype('float32')/255, label.astype('float32')

mnist_train = gdata.vision.FashionMNIST(train=True, transform=transform)
mnist_test = gdata.vision.FashionMNIST(train=False, transform=transform)

feature, label = mnist_train[0]

def get_text_labels(labels):
    text_labels = [
        't-shirt', 'trouser', 'pullover', 'dress', 'coat',
        'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot'
    ]
    return [text_labels[int(i)] for i in labels]

def show_fashion_imgs(images):
    n = images.shape[0]
    _, figs = gb.plt.subplots(1,n,figsize=(15,15))
    for i in range(n):
        figs[i].imshow(images[i].reshape((28,28)).asnumpy())
        figs[i].axes.get_xaxis().set_visible(False)
        figs[i].axes.get_yaxis().set_visible(False)
    gb.plt.show()

# X, y = mnist_train[0:15]
#
# show_fashion_imgs(X)
# print(get_text_labels(y))

batch_size = 256
train_iter = gdata.DataLoader(mnist_train, batch_size, shuffle=True)
test_iter = gdata.DataLoader(mnist_test, batch_size, shuffle=False)

num_inputs = 28*28
num_output = 10

W = nd.random.normal(scale=0.01, shape=(num_inputs, num_output))
b = nd.zeros(num_output)

params = [W, b]

for param in params:
    param.attach_grad()

def softmax(X):
    exp = X.exp()
    partition = exp.sum(axis=1, keepdims=True)
    return exp/ partition

X = nd.random.normal(shape=(2,5))
X_prob = softmax(X)
print(X_prob, X_prob.sum(axis=1))

def net(X):
    return softmax(nd.dot(X.reshape((-1, num_inputs)) ,W) +b)


y_hat = nd.array([[0.1,0.2,0.3],[0.3,0.2,0.6]])

y = nd.array([0,2])
print(nd.pick(y_hat, y))

def cross_entropy(y_hat,y):
    return -nd.pick(y_hat.log(),y)

def accuracy(y_hat, y):
    return (y_hat.argmax(axis=1) == y).mean().asscalar()

print(accuracy(y_hat, y))

def eval_acc(data_iter, net):
    acc = 0
    for X,y in data_iter:
        acc += accuracy(net(X), y)
    return acc/len(data_iter)

print(eval_acc(test_iter, net))

num_epochs = 5
lr = 0.1
loss = cross_entropy

def train_cpu(net, train_iter, test_iter, loss, num_epochs, batch_size,
              params=None, lr=None, trainer=None):
    for epoch in range(1, num_epochs + 1):
        train_l_sum = 0
        train_acc_sum = 0
        for X, y in train_iter:
            with autograd.record():
                y_hat = net(X)
                l = loss(y_hat, y)
            l.backward()
            if trainer is None:
                gb.sgd(params, lr, batch_size)
            else:
                trainer.step(batch_size)
            train_l_sum += l.mean().asscalar()
            train_acc_sum += accuracy(y_hat, y)
        test_acc = eval_acc(test_iter, net)
        print("epoch %d, loss %.4f, train acc %.3f, test acc %.3f"
              % (epoch, train_l_sum / len(train_iter),
                 train_acc_sum / len(train_iter), test_acc))

train_cpu(net, train_iter, test_iter, loss, num_epochs, batch_size, params,
          lr)


data, label = mnist_test[0:9]
show_fashion_imgs(data)
print('labels:', get_text_labels(label))
predicted_labels = net(data).argmax(axis=1)
print('predictions:', get_text_labels(predicted_labels.asnumpy()))