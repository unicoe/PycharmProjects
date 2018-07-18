def generate_result(resource_path, des_path):
    """
    :param path: 
    :return: 
    """
    des_path1 = "/home/user/PycharmProjects/MissRate_FPPI_plot/out1.txt"
    des_path2 = "/home/user/PycharmProjects/MissRate_FPPI_plot/out2.txt"

    rf = open(resource_path)

    content = rf.readline()
    cnt = 0
    tmp_dict = {}

    while content:
        #print content

        res = content.replace("\n", "").split(" ")

        cls  = str(res[0:1][0])
        bbox = res[1:6]

        if cls in tmp_dict:
            tmp_dict[cls].append(bbox)
        else:
            tmp_dict[cls] = [bbox]
            cnt += 1

        content = rf.readline()
    rf.close()

    wpath = resource_path.split("/")[-1]
    respath = wpath[-9:-4] + "/" + wpath[-4:]
    print wpath, respath
    wfname = open(des_path, "w")
    wfscr  = open(des_path1, "w")
    wfbbox = open(des_path2, "w")

    for key_ in tmp_dict:
        wfname.write(str(key_)+',')
        for detail in tmp_dict[key_]:
            for index in detail:
                if index == detail[0]:
                    wfscr.write(str(index))
                else:
                    if index is detail[1]:
                        tmpp1 = index
                        wfbbox.write(str(int(float(index))))
                    if index is detail[2]:
                        tmpp2 = index
                        wfbbox.write(str(int(float(index))))

                    if index is detail[3]:
                        wfbbox.write(str(int(float(index) - float(tmpp1))))
                    if index is detail[4]:
                        wfbbox.write(str(int(float(index) - float(tmpp2))))

                    if index is not detail[-1]:
                        wfbbox.write(",")
            if len(tmp_dict[key_]) > 1:
                if detail is not tmp_dict[key_][-1]:
                    wfscr.write(";")
                    wfbbox.write(";")
        wfname.write("\n")
        wfscr.write("\n")
        wfbbox.write("\n")

    wfname.close()
    wfscr.close()
    wfbbox.close()

generate_result("/home/user/PycharmProjects/MissRate_FPPI_plot/3_14_fasterrcnn_det_test_person.txt", "/home/user/PycharmProjects/MissRate_FPPI_plot/out.txt")

# def generate_all_result(path):
#     import os
#     dirList = []
#     fileList = []
#
#     files = os.listdir(path)
#
#     for f in files:
#         if(os.path.isdir(path + "/" + f)):
#             if f[0] != '.':
#                 dirList.append(f)
#         if(os.path.isfile(path + '/'+ f)):
#                 fileList.append(f)
#
#     for fl in fileList:
#         generate_result(path + fl, "/home/user/PycharmProjects/MissRate_FPPI_plot/out.txt")

#generate_all_result("/home/user/Downloads/caltech_data_set/data_test/")