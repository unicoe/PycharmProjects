import re
import shutil

def generate_all_result(path):
    import os
    dirList = []
    fileList = []

    files = os.listdir(path)

    for f in files:
        if(os.path.isdir(path + "/" + f)):
            if f[0] != '.':
                dirList.append(f)

        if(os.path.isfile(path + '/'+ f)):
                fileList.append(f)


    for f in dirList:
        tmp_path = path + "/" + f
        tmp = os.listdir(tmp_path)
        for idx in tmp:
            if (os.path.isfile(tmp_path + '/' + idx)):
                fileList.append(tmp_path+"/"+idx)
    #print dirList, fileList

    for idx in fileList:
        tmp = idx
        rf = open(idx)
        ls = []
        contx = rf.readline()
        while contx:
            ls.append(contx)
            contx = rf.readline()

        new = sorted(ls, key=lambda i: int(re.match(r'(\d+)', i).group()))
        rf.close()
        wf = open(tmp, "w")
        for itme in new:
            wf.write(str(itme))
        wf.close()

    f_name = path.split("/")[-1]
    print "'"+f_name+ "',            0, clrs(299,:),  '-'"
    source_path = path
    dest_path = "/home/user/Downloads/caltech_data_set/data-USA/res/" + f_name
    shutil.move(source_path, dest_path)


file_lst = [

'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_00_14_46.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_00_40_16.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_01_06_30.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_01_32_39.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_01_58_42.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_02_24_43.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_02_50_45.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_03_17_04.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_03_43_02.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_04_08_52.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_04_35_53.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/0/2019_06_20_Thu_05_03_38.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_21_10_45.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_21_23_36.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_21_35_40.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_21_47_44.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_21_59_30.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_22_11_22.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_22_23_03.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_22_35_09.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_22_46_43.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_22_57_57.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_23_13_24.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_20/1/2019_06_19_Wed_23_25_43.txt',

]


for file_idx in file_lst:
    save_path = file_idx.split(".")[0]
    generate_all_result(save_path)

"""
2019_05_27_Mon_10_35_11.txt
"""
