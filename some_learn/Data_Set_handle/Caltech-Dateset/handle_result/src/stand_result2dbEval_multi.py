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

'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_20_Thu_21_01_26.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_20_Thu_21_29_16.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_20_Thu_21_57_08.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_20_Thu_22_24_32.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_20_Thu_22_51_12.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_20_Thu_23_17_45.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_20_Thu_23_44_27.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_21_Fri_00_11_36.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_21_Fri_00_38_18.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_21_Fri_01_04_55.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_21_Fri_01_32_45.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/det_result/6_24/2019_06_21_Fri_02_02_40.txt',

]

for pth_idx in path_lst:
    save_path1 = pth_idx.split(".")[0]
    handle_result_for_eval(pth_idx, save_path1)


