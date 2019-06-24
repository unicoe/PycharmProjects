#!/usr/bin/env python
# -*- conding:utf-8 -*-
__author__ = 'unicoe'
__date__ = '2019/4/29'
__time__ = '5:21'





ls = [1,2,3,1,2,4,1,2,3,1,2,4]
#ls = [1,1,2,2,3,4,2,3,4,4]
#ls = [3,4,2,1,3,4,1,2]
# ls = [1,2,1,2,3]
# ls = [1,1,2,2,3,2,3,4,4,4,4]
# ls = [1,1,2,2,3,2,3,4]



#ls = [1,1,2,2,3,2,3,4]

ls = [7,8,9,8,9,8,9,6,8,9,8,9,8,9]


s1 = []
s2 = []

s1_tmp = -1
flg = 0

for i in range(len(ls)):

    if len(s1) == 0:
        s1.append(ls[i])
    else:
        if flg == 0:
            clr_s = 0
            for s1_i in range(len(s1)):
                if ls[i] == s1[s1_i]:
                    s2.append(ls[i])
                    flg = 1
                    s1_tmp = s1_i
                    if s1_tmp+1 == len(s1):
                        while (len(s2)):
                            s2.pop()
                        s1_tmp = -1
                        flg = 0
                        clr_s = 1
                    break

            if flg == 0:
                if clr_s == 1:
                    continue
                s1.append(ls[i])
                flg = 0
                s1_tmp = -1
        else:

            if len(s1) == len(s2) or s1_tmp+1 == len(s1):
                while(len(s2)):
                    s2.pop()
                s1_tmp = -1
                flg = 0
                clr_s = 0
                for s1_i in range(len(s1)):
                    if ls[i] == s1[s1_i]:
                        s2.append(ls[i])
                        flg = 1
                        s1_tmp = s1_i
                        if s1_tmp + 1 == len(s1):
                            while (len(s2)):
                                s2.pop()
                            s1_tmp = -1
                            flg = 0
                            clr_s = 1
                        break
                if flg == 0:
                    if clr_s == 1:
                        continue
                    s1.append(ls[i])
                    flg = 0
                    s1_tmp = -1
                flg = 0
                s1_tmp = -1


            else:
                if s1[s1_tmp+1] == ls[i]:
                    s2.append(ls[i])
                    s1_tmp += 1
                    if len(s2) == len(s1):
                        while (len(s2)):
                            s2.pop()
                        s1_tmp = -1
                        flg = 0
                elif s1[s1_tmp+1] != ls[i]:
                    s2.append(ls[i])
                    s2.reverse()
                    while(len(s2)):
                        s1.append(s2.pop())
                    clr_s = 0
                    flg = 0
                    s1_tmp = -1


if s2 != None:
    print(s1+s2)
else:
    print(s1)