# -*- coding: utf-8 -*-
# @Time    : 18-11-20 下午10:04
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : sort_result.py
# @Software: PyCharm

res_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/det_result/src/inria_result.txt")

result = {}

content = res_r.readline()

while content:
    res_info = content.strip("\n").split(" ")
    result[res_info[0]] = float(res_info[1])
    content  = res_r.readline()



res_lst = sorted(result.items(), key=lambda result: result[1])

for i in res_lst:
    print i[0]

"""
('PAMS-FCN(ours)', 0.059768)
('F-DNN', 0.067819)
('PCN', 0.068592)
('RPN+BF', 0.068778)
('SpatialPooling', 0.112171)
('SketchTokens', 0.133166)
('Roerei', 0.135329)
('Franken', 0.136951)
"""
