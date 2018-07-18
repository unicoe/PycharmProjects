rf = open("/home/user/PycharmProjects/caltech_new_anno/result/head_handle_det_test_person.txt")
wf = open("/home/user/PycharmProjects/caltech_new_anno/result/handled6_4_head_handle_det_test_person.txt","w")

content = rf.readline()


while content:

    info = content.strip("\n").split(" ")

    info[5] = str(float(info[3]) + (float(info[5])-float(info[3]))/0.6)

    for idx in info:
        wf.write(str(idx))
        wf.write(" ")
    wf.write("\n")
    content = rf.readline()
