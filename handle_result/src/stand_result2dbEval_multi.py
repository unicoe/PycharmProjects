def handle_result_for_eval(file_path, save_path):
    """
    :param file_path: "/home/user/PycharmProjects/handle_result/10_12/comp4_10_12_7_27_det_test_person.txt"
    :param save_path: "/home/user/PycharmProjects/handle_result/10_12/comp4_10_12_7_27_det_test_person/"
    :return: 
    """
    from unicoe_tool.mkdir import mkdir

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
'/home/user/PycharmProjects/handle_result/11_1/1/comp4_3798c70a-996a-478a-a620-3a15b875e166_det_test_person.txt',
'/home/user/PycharmProjects/handle_result/11_1/1/comp4_74501413-4641-4f04-923a-93d9bda870a7_det_test_person.txt',
'/home/user/PycharmProjects/handle_result/11_1/1/comp4_ec4357a2-3945-40fb-9195-47bc4946bcc0_det_test_person.txt',
'/home/user/PycharmProjects/handle_result/11_1/1/comp4_f0cbc086-9756-47e5-b635-4b7f58057196_det_test_person.txt',
]

for pth_idx in path_lst:
    save_path1 = pth_idx.split(".")[0]
    handle_result_for_eval(pth_idx, save_path1)


