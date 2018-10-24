def generate_result(resource_path, des_path):
    """
    :param path: 
    :return: 
    """
    supname = resource_path[-9:-4] + "/" + resource_path[-4:] + "/"
    print supname
    rf = open(resource_path)

    content = rf.readline()
    cnt = 0
    tmp_dict = {}

    while content:
        #print content
        res = content.replace("\n", "").split(" ")

        cls  = supname + str(res[0:1][0])
        bbox = res[1:5]

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
    wfname = open(des_path, "a+")

    cnt = 0
    for key_ in tmp_dict:
        wfname.write(str(key_)+',')
        for detail in tmp_dict[key_]:
            cnt += 1
            for index in detail:

                    if index is detail[0]:
                        tmpp1 = index
                        wfname.write(str(int(float(index))))
                    if index is detail[1]:
                        tmpp2 = index
                        wfname.write(str(int(float(index))))
                    if index is detail[2]:
                        wfname.write(str(int(float(index))))
                    if index is detail[3]:
                        wfname.write(str(int(float(index))))
                    if index is not detail[-1]:
                        wfname.write(" ")
            if len(tmp_dict[key_]) > 1:
                if detail is not tmp_dict[key_][-1]:
                    wfname.write(",")
        wfname.write("\n")
    wfname.close()
    return cnt


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
    cnt = 0
    for fl in fileList:
        cnt += generate_result(path + fl, "/home/user/PycharmProjects/MissRate_FPPI_plot/reasonable_30_ground_truth.txt")
    return cnt
cnt = generate_all_result("/home/user/Downloads/caltech_data_set/data_reasonable_30stepsize1_test/")
print cnt