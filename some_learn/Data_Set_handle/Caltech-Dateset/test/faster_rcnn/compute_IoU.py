#--coding:utf-8--
"""
这两个函数都是正确的，经过了验证，还在笔记本上做了记录
需要的参数是，(x1,y1,x2,y2)

l1 和　l2的相对位置也考虑过了
"""
def compute_IoU(l1, l2):
    '''
    #the coordinate of this funcation is (x1,y1,x2,y2)
    :param l1: first rectangle coordinate 
    :param l2: second rectangle coordinate
    :return: yes or no IoU > 0.5(or x) 
    '''
    if(l1[0] > l2[0] + abs(l2[2]-l2[0])):
        return False
    if(l1[1] > l2[1] + abs(l2[3]-l2[1])):
        return False
    if(l1[0] + l1[2]-l1[0] < l2[0]):
        return False
    if(l1[1] + l1[3]-l1[1] < l2[1]):
        return False

    colInt = min(l1[0]+l1[2]-l1[0] , l2[0]+l2[2]-l2[0]) - max(l1[0], l2[0])
    rowInt = min(l1[1]+l1[3]-l1[1] , l2[1]+l2[3]-l2[1]) - max(l1[1], l2[1])

    intersection = colInt * rowInt
    area1 = (l1[2]-l1[0])*(l1[3]-l1[1])
    area2 = (l2[2]-l2[0])*(l2[3]-l2[1])

    intersectionPercent = intersection/(area1+area2-intersection + 0.0)
    print "IoU = " + str(intersectionPercent)
    if intersectionPercent < 0.5:
        return False
    else:
        return True


def compute_IoU1(l1, l2):
    '''
    #the coordinate of this funcation is (x1,y1,w,h)
    :param l1: first rectangle coordinate 
    :param l2: second rectangle coordinate
    :return: yes or no IoU > 0.5(or x) 
    '''
    if len(l1) < 4 or len(l2) < 4:
        return False

    w1 = l1[2] - l1[0]
    w2 = l2[2] - l2[0]
    ws = min(l1[0], l2[0])
    we = max(l1[2], l2[2])

    h1 = l1[3] - l1[1]
    h2 = l2[3] - l2[1]
    hs = min(l1[1], l2[1])
    he = max(l1[3], l2[3])

    weight = w1 + w2 - (we - ws)
    height = h1 + h2 - (he - hs)
    print weight,height
    if weight <= 0 or height <= 0:
        return False

    area = weight * height
    a1 = w1 * h1
    a2 = w2 * h2

    ratio = area * 1.0 / (a1 + a2 - area)
    print ratio
    if ratio >= 0.5:
        return True
    else:
        return False

    tl1 = []
    tl2 = []
    for i in xrange(0, 2):
        tl1.append(l1[i])
        tl1.append(l1[i + 2])
        tl2.append(l2[i])
        tl2.append(l2[i + 2])

l1 = [4,4,6,6]
l2 = [7,9,0,3]
import time
print time.time()
print compute_IoU(l1,l2)
print compute_IoU1(l1,l2)