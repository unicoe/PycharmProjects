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
    folder_name = "'/home/user/Downloads/amilan-motchallenge-devkit/res/MOT17Det/" + f_name[-2] + "',"
    folder_ls.add(folder_name)
    source_path = path
    mkdir("/home/user/Downloads/amilan-motchallenge-devkit/res/MOT17Det/" \
                + f_name[-2])
    dest_path = "/home/user/Downloads/amilan-motchallenge-devkit/res/MOT17Det/" \
                + f_name[-2] + "/" \
                + f_name[-1]
    shutil.move(source_path, dest_path)

    pass


res_ls = [
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_20_Tue_20_04_25/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_20_Tue_20_04_25/MOT17-11.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_20_Tue_21_24_13/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_20_Tue_21_24_13/MOT17-11.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_20_Tue_22_44_23/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_20_Tue_22_44_23/MOT17-11.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_00_04_43/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_00_04_43/MOT17-11.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_01_24_33/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_01_24_33/MOT17-11.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_02_44_48/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_02_44_48/MOT17-11.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_04_04_32/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_04_04_32/MOT17-11.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_05_24_36/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_05_24_36/MOT17-11.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_06_44_37/MOT17-10.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/2019_08_21_Wed_06_44_37/MOT17-11.txt',

]

for i_path in res_ls:
    sort_file(i_path)

for i in folder_ls:
    print i