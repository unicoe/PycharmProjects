# -*- coding: utf-8 -*-
# @Time    : 19-3-4 下午8:31
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : copy_param.py
# @Software: PyCharm

source_ls = []
target_ls = []

for source_i in open("/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/param_copy/source.txt"):
    source_ls.append(source_i.strip("\n"))

for target_i in open("/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/param_copy/source.txt"):
    target_ls.append(target_i.strip("\n"))


print(source_ls)
print(target_ls)


for i in range(len(source_ls)):
    print("""if k == '"""+source_ls[i] +"""'  :\n\tpretrained_dict1['"""+target_ls[i]+"""'] = v""")