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
    dest_path = "/home/user/Downloads/caltech_data_set/data-ETH/res/" + f_name
    #dest_path = "/home/user/Downloads/caltech_data_set/data-INRIA/res/" + f_name
    shutil.move(source_path, dest_path)


file_lst = [

'/home/user/PycharmProjects/some_learn/Data_Set_handle/ETH-Dataset/result/ETH-500-51.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/ETH-Dataset/result/ETH-500_50.txt',


]


for file_idx in file_lst:
    save_path = file_idx.split(".")[0]
    generate_all_result(save_path)

"""

"""