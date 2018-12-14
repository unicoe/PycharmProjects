# -*- coding: utf-8 -*-
# @Time    : 18-12-13 下午8:56
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : combine.py
# @Software: PyCharm


def get_dict(path):
    read_file = open(path)

    r_info = read_file.readline()

    info_dict = {}

    while r_info:
        tmp_info = r_info.strip("\n")
        tmp_info = tmp_info.split(" ")
        print tmp_info

        str_ls = tmp_info[3][1:-1].split(",")
        int_ls = [int(c) for c in str_ls]
        info_dict[tmp_info[0]] = int_ls
        r_info = read_file.readline()

    return info_dict


dict_a = get_dict("/home/user/PycharmProjects/some_learn/Data_Set_handle/tmp/tmp_file/a.txt")
dict_b = get_dict("/home/user/PycharmProjects/some_learn/Data_Set_handle/tmp/tmp_file/b.txt")

print dict_a
print dict_b

c_w = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/tmp/tmp_file/c.txt", "w")

comb_ls = []
for ia in dict_a:
    if ia in dict_b:
        print dict_a[ia]
        print dict_b[ia]
        comb_ls.append(list(dict_a[ia])+list(dict_b[ia]))
        c_w.write(ia)
        c_w.write("\t")
        c_w.write(str(list(dict_a[ia])+list(dict_b[ia])))
        c_w.write("\n")

c_w.close()
print comb_ls