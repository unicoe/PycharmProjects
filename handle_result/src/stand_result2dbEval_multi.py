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

file_path1 = "/home/user/PycharmProjects/handle_result/10_23/comp4_83769cde-202d-4f47-abf1-eaa9cb4609ec_det_test_person.txt"
save_path1 = "/home/user/PycharmProjects/handle_result/10_23/comp4_83769cde-202d-4f47-abf1-eaa9cb4609ec_det_test_person"
handle_result_for_eval(file_path1,save_path1)


file_path2 = "/home/user/PycharmProjects/handle_result/10_23/comp4_a2af19d5-45cc-499d-bbb6-7fce84eb0fa6_det_test_person.txt"
save_path2 = "/home/user/PycharmProjects/handle_result/10_23/comp4_a2af19d5-45cc-499d-bbb6-7fce84eb0fa6_det_test_person"
handle_result_for_eval(file_path2,save_path2)


file_path3 = "/home/user/PycharmProjects/handle_result/10_23/comp4_b67919a0-ade6-43f3-96e6-c7be425f5128_det_test_person.txt"
save_path3 = "/home/user/PycharmProjects/handle_result/10_23/comp4_b67919a0-ade6-43f3-96e6-c7be425f5128_det_test_person"
handle_result_for_eval(file_path3,save_path3)


file_path4 = "/home/user/PycharmProjects/handle_result/10_23/comp4_f61c1015-4e7c-4ade-b2ab-a8078fadc721_det_test_person.txt"
save_path4 = "/home/user/PycharmProjects/handle_result/10_23/comp4_f61c1015-4e7c-4ade-b2ab-a8078fadc721_det_test_person"
handle_result_for_eval(file_path4,save_path4)
