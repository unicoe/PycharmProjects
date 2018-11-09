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

'/home/user/PycharmProjects/handle_result/det_result/11_7/comp4_4ff291a1-ebd7-4003-9125-1d7e88ccf932_det_test_person.txt',
'/home/user/PycharmProjects/handle_result/det_result/11_7/comp4_9ca11107-ce28-4307-a24d-5b8302ec84e8_det_test_person.txt',
'/home/user/PycharmProjects/handle_result/det_result/11_7/comp4_703c00b0-cea8-4f0d-8a6a-a740aa3e8b99_det_test_person.txt',
'/home/user/PycharmProjects/handle_result/det_result/11_7/comp4_98936ab4-223e-493d-a5f4-e284cf1098cf_det_test_person.txt',
'/home/user/PycharmProjects/handle_result/det_result/11_7/comp4_c61ece65-dc68-4d48-b989-eebf381d00e9_det_test_person.txt',
'/home/user/PycharmProjects/handle_result/det_result/11_7/comp4_d1f13d52-30ef-4e18-9840-9699c925eb73_det_test_person.txt',
]


for file_idx in file_lst:
    save_path = file_idx.split(".")[0]
    generate_all_result(save_path)

"""

"""