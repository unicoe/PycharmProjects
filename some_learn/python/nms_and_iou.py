# -*- coding: utf-8 -*-
import numpy as np
def IOU1(A,B):
    #左上右下坐标(x1,y1,x2,y2)
    w=max(0,min(A[2],B[2])-max(A[0],B[0]))
    h=max(0,min(A[3],B[3])-max(A[1],B[1]))
    areaA=(A[2]-A[0]+1)*(A[3]-A[1]+1)
    areaB=(B[2]-B[0]+1)*(B[3]-B[1]+1)
    inter=w*h
    union=areaA+areaB-inter
    return inter/union
def nms(dets, thresh):
    """Pure Python NMS baseline."""
    #x1、y1、x2、y2、以及score赋值
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:#还有数据
        i = order[0]
        keep.append(i)
        # np.maximum：(X, Y, out=None)
        # X与Y逐位比较取其大者,最少接收两个参数
        #计算当前概率最大矩形框与其他矩形框的相交框的坐标
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        #计算相交框的面积
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        #计算重叠度IOU：重叠面积/（面积1+面积2-重叠面积）
        IOU = inter / (areas[i] + areas[order[1:]] - inter)
        #找到重叠度不高于阈值的矩形框索引
        left_index = np.where(IOU <= thresh)[0]
        #将order序列更新，由于前面得到的矩形框索引要比矩形框在原order序列中的索引小1，所以要把这个1加回来
        order = order[left_index + 1]
    print(keep)
if __name__ == '__main__':
     dets=[[0,0,100,101,0.9],[5,6,90,110,0.7],[17,19,80,120,0.8],[10,8,115,105,0.5]]
     dets=np.array(dets)
     nms(dets,0.5)
     print IOU1(dets[0],dets[2])