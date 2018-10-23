import os
from unicoe_tool.mkdir import mkdir

readfile = open("/home/user/PycharmProjects/handle_result/10_17/comp4_0e007648-6c6f-423c-9e62-ab7e975065ab_det_test_person.txt")


contx = readfile.readline()
details = []

while contx:
    details = contx.replace("\n", "").split(" ")
    print(details)
    pathls = details[0].split('_')

    save_path = "/home/user/PycharmProjects/handle_result/10_17/comp4_0e007648-6c6f-423c-9e62-ab7e975065ab_det_test_person/"
    mkdir(save_path + pathls[0])
    wf = open(save_path + pathls[0] +"/"+pathls[1]+".txt","aw")

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



