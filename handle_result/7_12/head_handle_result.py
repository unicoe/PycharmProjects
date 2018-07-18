rf = open("/home/user/PycharmProjects/handle_result/7_12/result/7_12_det_test_head.txt")
wf = open("/home/user/PycharmProjects/handle_result/7_12/result/handle_7_12_det_test_head.txt","w")

content = rf.readline()


while content:

    info = content.strip("\n").split(" ")

    info[5] = str(float(info[3]) + (float(info[5])-float(info[3]))/0.35)

    for idx in info:
        wf.write(str(idx))
        wf.write(" ")
    wf.write("\n")
    content = rf.readline()
