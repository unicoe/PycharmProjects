rf = open("/home/user/PycharmProjects/handle_result/6_16/6_16_det_test_upper.txt")
wf = open("/home/user/PycharmProjects/handle_result/6_16/handle_result/handle_6_16_det_test_upper.txt","w")

content = rf.readline()


while content:

    info = content.strip("\n").split(" ")

    info[5] = str(float(info[3]) + (float(info[5])-float(info[3]))/0.6)

    for idx in info:
        wf.write(str(idx))
        wf.write(" ")
    wf.write("\n")
    content = rf.readline()
