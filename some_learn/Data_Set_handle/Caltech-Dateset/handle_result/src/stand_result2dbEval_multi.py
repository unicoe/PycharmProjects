def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok'
        return True
    else:

        print path + 'failed!'
        return False

def handle_result_for_eval(file_path, save_path):
    """
    :param file_path: "/home/user/PycharmProjects/handle_result/10_12/comp4_10_12_7_27_det_test_person.txt"
    :param save_path: "/home/user/PycharmProjects/handle_result/10_12/comp4_10_12_7_27_det_test_person/"
    :return: 
    """
    

    readfile = open(file_path)
    contx = readfile.readline()

    while contx:
        details = contx.replace("\n", "").split(" ")
        print details
        pathls = details[0].split('_')

        path_str = save_path

        mkdir(path_str +"/"+ pathls[0])
        wf = open(path_str +"/"+ pathls[0] +"/"+pathls[1]+".txt","aw")

        id = pathls[2][2:]
        id_int = int(id)
        if id_int - 1 != 0:
            wf.write(str(id_int + 1))
            wf.write(",")
            for i in range(2,6):
                if i < 4:
                    wf.write(str(details[i]))
                    wf.write(",")
                if i == 4:
                    wf.write(str(float(details[i])-float(details[2])))
                    wf.write(",")
                if i == 5:
                    print (details[i])
                    wf.write(str(float(details[i])-float(details[3])))
                    wf.write(",")
            wf.write(str(details[1]))
            wf.write("\n")
        contx = readfile.readline()

path_lst = [

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

for pth_idx in path_lst:
    save_path1 = pth_idx.split(".")[0]
    handle_result_for_eval(pth_idx, save_path1)


