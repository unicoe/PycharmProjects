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
    print dirList, fileList
    return fileList


def handle_sort(file_path):
    """
    :param file_path: "/home/user/PycharmProjects/handle_result/10_12/comp4_10_12_7_27_det_test_person"
    :return: 
    """
    fileList = generate_all_result(file_path)

    import re

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

file_path1 = "/home/user/PycharmProjects/handle_result/10_23/comp4_83769cde-202d-4f47-abf1-eaa9cb4609ec_det_test_person"
handle_sort(file_path1)

file_path2 = "/home/user/PycharmProjects/handle_result/10_23/comp4_a2af19d5-45cc-499d-bbb6-7fce84eb0fa6_det_test_person"
handle_sort(file_path2)

file_path3 = "/home/user/PycharmProjects/handle_result/10_23/comp4_b67919a0-ade6-43f3-96e6-c7be425f5128_det_test_person"
handle_sort(file_path3)

file_path4 = "/home/user/PycharmProjects/handle_result/10_23/comp4_f61c1015-4e7c-4ade-b2ab-a8078fadc721_det_test_person"
handle_sort(file_path4)