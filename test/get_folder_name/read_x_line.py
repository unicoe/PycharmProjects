import linecache
import numpy as np
from matplotlib import pyplot as plt

fig,ax = plt.subplots(figsize=(12,12))


for i in xrange(1,42,10):
    str = linecache.getline('/home/user/Downloads/vot2015/bag/groundtruth.txt', i)
    str = str.replace('\n', '')
    l = str.split(',')
    x = []
    y = []
    indx = 0
    for j in xrange(0,8,2):
        x.append(float(l[0+j]))
        y.append(float(l[1+j]))
        T = np.arctan2(x[indx], y[indx])
        plt.scatter(x[indx], y[indx], c=T, s=25, alpha=0.4, marker='o')
        indx += 1
    #todo

    print x
    print y
    ax.add_patch(plt.Rectangle((min(x), min(y)), abs(max(x) - min(x)), abs(max(y) - min(y)),  fill=False,edgecolor='red', linewidth=2.5))
    plt.axis('off')
    plt.tight_layout()
    plt.draw()
plt.show()
    #print l
