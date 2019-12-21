#--coding:utf-8--
import re
import shutil

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        #print path + 'ok'
        return True
    else:

        #print path + 'failed!'
        return False

folder_ls = set()
def sort_file(path):
    file_info = open(path,"r")


    ls = []
    contx = file_info.readline()
    while contx:
        ls.append(contx)
        contx = file_info.readline()

    new = sorted(ls, key=lambda i: int(re.match(r'(\d+)', i).group()))
    file_info.close()
    wf = open(path, "w")
    for itme in new:
        wf.write(str(itme))
    wf.close()

    f_name = path.split("/")
    # 测评结果存放的地方
    folder_name = "'/home/user/Downloads/amilan-motchallenge-devkit/res/MOT17Det/" + f_name[-2] + "',"
    folder_ls.add(folder_name)
    source_path = path
    # 将测评结果放在对应的目录下
    mkdir("/home/user/Downloads/amilan-motchallenge-devkit/res/MOT17Det/" \
                + f_name[-2])
    dest_path = "/home/user/Downloads/amilan-motchallenge-devkit/res/MOT17Det/" \
                + f_name[-2] + "/" \
                + f_name[-1]
    shutil.move(source_path, dest_path)

    pass


res_ls = [

'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/AD-SSD/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/AD-SSD/MOT17-11.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/SSD+SEG+VIS/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/SSD+SEG+VIS/MOT17-11.txt',

]

for i_path in res_ls:
    sort_file(i_path)

for i in folder_ls:
    print i