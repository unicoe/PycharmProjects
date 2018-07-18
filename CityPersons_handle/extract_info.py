def extrat_info():
    rf = open("/home/user/PycharmProjects/CityPersons_handle/ann_train_aligned.txt", "r")
    wf = open("/home/user/PycharmProjects/CityPersons_handle/out1_2.txt", "w")
    contx = rf.readline()
    ctx_str = ""

    ctx_dict ={}

    cnt = 0
    cnt1 = 0
    while contx:
        ls = []
        if contx[0].isalpha():
            contx = contx.replace(" ","/")

            tmp = contx
            ctx_dict[tmp] = []
        elif contx[0].isalnum() and contx[0] > '0' and contx[0] < '3':
            contx = contx.strip("\n").strip(" ")
            cnt = cnt+1
            ctx_dict[tmp].append(contx)
        elif contx[0].isalnum() and contx[0]== '0':
            cnt1 += 1
        elif contx[0] == "\n":
            if len(ctx_dict[tmp])>0:
                #print tmp," ",ctx_dict[tmp]
                wf.write(tmp.split('.')[0])
                # wf.write(" ")
                # wf.write(str(ctx_dict[tmp]))
                wf.write("\n")
        contx = rf.readline()

    rf.close()
    wf.close()
    # print ctx_dict
    # print cnt,cnt1
    return ctx_dict
extrat_info()