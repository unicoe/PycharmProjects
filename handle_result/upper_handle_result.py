rf = open("/home/user/PycharmProjects/handle_result/check_point_6_13/611_det_test_upper.txt")
wf = open("/home/user/PycharmProjects/handle_result/check_point_6_13/check_eval/handle_611_det_test_upper.txt","w")

content = rf.readline()


while content:

    info = content.strip("\n").split(" ")

    info[5] = str(float(info[3]) + (float(info[5])-float(info[3]))/0.6)

    for idx in info:
        wf.write(str(idx))
        wf.write(" ")
    wf.write("\n")
    content = rf.readline()
