# -*- coding: utf-8 -*-
# @Time    : 18-8-11 下午2:52
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : learning_weight.py
# @Software: PyCharm Community Edition

from mxnet import autograd, nd
from mxnet import symbol
import mxnet as mx
import random


print mx.gpu()

num_examples = 4457

num_inputs = 1

w1 = nd.random.normal(scale=0.1, shape=(num_inputs, 1))

w2 = nd.random.normal(scale=0.1, shape=(num_inputs, 1))

b1 = nd.zeros(shape=(1,))

params = [w1, w2, b1]

print params

for param in params:
    param.attach_grad()

features1 = []
features2 = []

rf1 = open("/home/user/PycharmProjects/setting_weight_by_learn/basic_data/1_withgt_head.txt")
content1 = rf1.readline().strip("\n")
while content1:
    str1 = content1.split(" ")
    tmp1  = map(eval, str1[:])
    features1.append(tmp1)
    content1 = rf1.readline().strip("\n")

rf2 = open("/home/user/PycharmProjects/setting_weight_by_learn/basic_data/1_withgt_person.txt")
content2 = rf2.readline().strip("\n")
while content2:
    str2 = content2.split(" ")
    tmp2 = map(eval, str2[:])
    features2.append(tmp2)
    content2 = rf2.readline().strip("\n")

print features1, features2

data1 = nd.array(features1)
data2 = nd.array(features2)

labels = []

rf3 = open("/home/user/PycharmProjects/setting_weight_by_learn/basic_data/3_gt.txt")

content3 = rf3.readline().strip("\n")
while content3:
    str3 = content3.split(" ")
    tmp3 = map(eval, str3[:])
    labels.append(tmp3)
    content3 = rf3.readline().strip("\n")

gt = nd.array(labels)

batch_size = 4457

def data_iter(batch_size, features1, features2, labels):
    num_examples = len(features1)
    indices = list(range(num_examples))

    for i in range(0, num_examples, batch_size):
        j = nd.array(indices[i:min(i+batch_size, num_examples)])

        yield features1.take(j),features2.take(j), labels.take(j)


for X1, X2, y in data_iter(batch_size, data1, data2, gt):
    print (X1, X2, y)
    break


def linreg(X1,X2,w1,w2,b1):
    # print X1, X2, w1, w2, b1
    #
    # print "nd.dot output : "
    # print  w1*X1 + w2*X2 + b1
    return X1*w1 + X2*w2 + b1

def squared_loss(y_hat, y):
    return nd.sqrt(nd.mean(nd.abs(y_hat - y)))

def squared_loss1(y_hat, y):
    return nd.mean((y_hat-y)**2/2)



HUBER_DELTA = 0.5
def smoothL1(y_pred, y_true):
   x   = nd.abs(y_true - y_pred)
   if x < HUBER_DELTA:
       x = 0.5 * x ** 2
   else:
       x = HUBER_DELTA * (x - 0.5 * HUBER_DELTA)
   return  nd.sum(x)



def sgd(params, lr, batch_size):
    for param in params:
        param[:] = param - lr*param.grad / batch_size


lr = 0.05

num_epochs = 10000

net = linreg

loss = squared_loss


wf = open("/home/user/PycharmProjects/setting_weight_by_learn/src/loss.txt", "w")

for epoch in range(1, num_epochs+1):

    # if epoch % 50000 == 0:
    #     lr = 0.005

    for X1,X2,y in data_iter(batch_size, data1, data2, gt):

        with autograd.record():
            res = net(X1, X2, w1, w2, b1)
            l = loss(res, y)
            print l
        l.backward()

        sgd([w1,w2,b1], lr, batch_size)

    print("epoch %d, loss %f"
          % (epoch, loss(net(data1, data2, w1,w2, b1), gt).mean().asnumpy()))
    wf.write(str(epoch))
    wf.write("\n")
    wf.write(str(loss(net(data1, data2, w1,w2, b1), gt).mean().asnumpy()))
    wf.write("\n\n")

print params


"""
10w 
[
[[0.59744453]]
<NDArray 1x1 @cpu(0)>, 
[[0.39810976]]
<NDArray 1x1 @cpu(0)>, 
[-0.00324005]
<NDArray 1 @cpu(0)>]



epoch 100000, loss 2.453683
[
[[0.78413963]]
<NDArray 1x1 @cpu(0)>, 
[[0.21177217]]
<NDArray 1x1 @cpu(0)>, 
[-0.06293482]
<NDArray 1 @cpu(0)>]



epoch 999, loss 2.628376

[2.6283762]
<NDArray 1 @cpu(0)>
epoch 1000, loss 2.628367
[
[[0.5760476]]
<NDArray 1x1 @cpu(0)>, 
[[0.4194624]]
<NDArray 1x1 @cpu(0)>, 
[0.00023032]
<NDArray 1 @cpu(0)>]
"""

"""
当前通过学习，然后将结果整合，得到的结果不好，

loss是一直在下降，但是最后的参数却变化剧烈，

这里只是学习了将训练集的det学习，然后得到在训练集上的分布。



考虑怎么能将loss，使用smooth l1 loss

不同于物体检测，我现在做的是将检测框融合，这里不需要使用smooth l1 loss，
用简单的线性回归就可以将检测框做融合，

初始的参数是随机参数，通过学习之后，可以看到，这两个参数的加和趋于1（0.99）


但是，这样的参数在测试集上的效果并不好，mr=17%差直接做 nms太多了


"""


"""
epoch 10000, loss 8.956559
[
[[0.5731586]]
<NDArray 1x1 @cpu(0)>, 
[[0.42243934]]
<NDArray 1x1 @cpu(0)>, 
[0.00054808]
<NDArray 1 @cpu(0)>]



def squared_loss(y_hat, y):
    return nd.sqrt(nd.mean(nd.abs(y_hat - y)))

epoch 10000, loss 1.616827
[
[[0.5871187]]
<NDArray 1x1 @cpu(0)>, 
[[0.40840456]]
<NDArray 1x1 @cpu(0)>, 
[-0.00156271]
<NDArray 1 @cpu(0)>]
"""