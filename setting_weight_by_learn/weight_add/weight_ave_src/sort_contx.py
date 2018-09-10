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

fileList = generate_all_result("/home/user/PycharmProjects/handle_result/6_25(7_18)/weight_add/result/weight_handle_result1.0")

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