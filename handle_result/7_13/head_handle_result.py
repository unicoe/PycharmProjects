rf = open("/home/user/PycharmProjects/handle_result/7_13/2018_07_13_Fri_10_16_26_det_test_head.txt")
wf = open("/home/user/PycharmProjects/handle_result/7_13/handle_2018_07_13_Fri_10_16_26_det_test_head.txt","w")

content = rf.readline()


while content:

    info = content.strip("\n").split(" ")

    info[5] = str(float(info[3]) + (float(info[5])-float(info[3]))/0.35)

    for idx in info:
        wf.write(str(idx))
        wf.write(" ")
    wf.write("\n")
    content = rf.readline()
