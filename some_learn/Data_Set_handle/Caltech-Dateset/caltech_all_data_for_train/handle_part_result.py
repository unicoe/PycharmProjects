rf = open("/home/user/PycharmProjects/caltech_new_anno/result/part_detection/6_11_test_det_test_upper.txt")
wf = open("/home/user/PycharmProjects/caltech_new_anno/result/part_detection/handled_6_11_1_det_test_upper.txt","w")

content = rf.readline()


while content:

    info = content.strip("\n").split(" ")
    # if (float(info[1])-0.01) < 0:
    #     content = rf.readline()
    #     continue
    info[5] = str(float(info[3]) + (float(info[5])-float(info[3]))/0.6)

    for idx in info:
        wf.write(str(idx))
        wf.write(" ")
    wf.write("\n")
    content = rf.readline()
