# -*- coding: utf-8 -*-
# @Time    : 18-10-18 下午8:34
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : 10_18.py
# @Software: PyCharm Community Edition

import numpy as np
import pdb

a = np.array([1,2,3], ndmin=2).reshape(3,1)
print a
print a.ndim
print a.itemsize
print a.flags

a = np.array([[1],[2]])
print a
a.shape = (1,2)
print a.shape
print a

a = np.array([1,2,3], ndmin=2, dtype=complex)
print a


print type(a)


dt = np.dtype(np.int32)
print dt

dt = np.dtype([('age', np.int8)])
print dt

a = np.array([(1,),(2,)], dtype=dt)
print a
print a['age']

student = np.dtype([('name','S20'),('age', 'i1')])

print student

stu_np = np.array([('unicoe',23),('harper',23)])
print stu_np



x = np.empty([3,2], dtype=int)
print x

x = np.zeros([2,2,3],dtype=float)
print x

y = np.ones([1,2]).reshape(2)
print y
print y.ndim

x = [1,2,3,4]
y = (3,2,1)
y = [(1,2),(2,1)]
a = np.asarray(y, dtype='float16')
print a
print a.dtype

s = 'string!'
a = np.frombuffer(s, dtype='S1')
print a

ls = range(5)
it = iter(ls)
x = np.fromiter(it, dtype=float)
print x

x = np.arange(5)
print x

x = np.arange(10,20,2)
print  x

x = np.linspace(10,14,5)
print x

a = np.arange(10)
s = slice(2,7,2)
print a[s]
print a[2:7:2]
print a[:7:2]
print a[::3]
print a[2::]
print a[:5:]

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print a[1:]
print a[:2:]
print a[::2]

print a[...,1]
print a[1,...]
print a[...,1:]

"""
如果一个 ndarray 是非元组序列，数据类型为整数或布尔值的 ndarray ，或者
至少一个元素为序列对象的元组，我们就能够用它来索引 ndarray 。高级索引始
终返回数据的副本。 与此相反，切片只提供了一个视图。

"""


x = np.array([[1, 2], [3, 4], [5, 6]])

y = x[[0,1,2],[0,1,0]]
#该结果包括数组中 (0,0) ， (1,1) 和 (2,0) 位置处的元素。
print y


x = np.array([[ 0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 10, 11]])
print '我们的数组是：'
print x
print '\n'

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
# 行索引是 [0,0] 和 [3,3] ，
# 而列索引是 [0,2] 和 [0,2] 。
y = x[rows,cols]
print y

"""
高级和基本索引可以通过使用切片 : 或省略号 ... 与索引数组组合。 以下示例
使用 slice 作为列索引和高级索引。 当切片用于两者时，结果是相同的。 但高级
索引会导致复制，并且可能有不同的内存布局。
"""

z = x[1:4:2,1:3]
print z

z = x[1:4,[1,2]]
print z

#这个例子中，大于 5 的元素会作为布尔索引的结果返回。
print x[x > 5]


a = np.array([np.nan, 1,2,3,np.nan])

print a[~np.isnan(a)]



a = np.array([[1,2,3],[4,5,6]])
b = np.array([100,200,300])

c = a+b
print c



a = np.arange(0,60,5)
a = a.reshape(3,4)
print a
for i in np.nditer(a):
    print i,
print ""
for i in np.nditer(a):
        print i

b = a.T
print b
for i in np.nditer(b):
    print i,
print ""
a = np.arange(8).reshape(2,4)

print a



c = a.flatten()
print c
print a

d = a.ravel()
print d


a = np.arange(12).reshape(2,2,3)

print a


print np.rollaxis(a,2)


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print np.concatenate((a,b))
print np.concatenate((a,b), axis=1)

print np.stack((a,b))
print np.stack((a,b),0)
print np.stack((a,b),1)


print np.hstack((a,b))
print np.vstack((a,b))


a = np.arange(12)

b = np.split(a,3)

a = np.arange(16).reshape(4,4)

b = np.hsplit(a,2)



#pdb.set_trace()