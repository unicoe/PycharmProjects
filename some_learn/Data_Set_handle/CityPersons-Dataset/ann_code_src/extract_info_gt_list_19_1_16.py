# -*- coding: utf-8 -*-

def extrat_info():

    rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/"
              "ann_code_src/ann_file/ann_train_aligned.txt", "r")
    wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/"
              "ann_code_src/ann_file/out_train_19_1_16.txt", "w")

    contx = rf.readline()
    ctx_str = ""

    ctx_dict ={}
    im_list = []
    cnt = 0
    cnt1 = 0
    while contx:
        ls = []
        if contx[0].isalpha():
            contx = contx.replace(" ","/")

            tmp = contx
            ctx_dict[tmp] = []
            im_list.append(tmp)
        elif contx[0].isalnum() and contx[0] > '0' and contx[0] <= '3':   #对类别进行筛选
        #elif contx[0].isalnum():                                          #不进行筛选
            contx = contx.strip("\n").strip(" ")
            cnt = cnt+1
            ctx_dict[tmp].append(contx)
        elif contx[0].isalnum() and contx[0]== '0':
            cnt1 += 1
        elif contx[0] == "\n":
            if len(ctx_dict[tmp]) > 0:  #  对没有标注的图片进行筛选
            #if len(ctx_dict[tmp])>=0:    #  不进行筛选
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
    return ctx_dict, im_list
gt_info,im_ls = extrat_info()


print gt_info, im_ls

def generate_gt_txt(gt_info, im_ls):

    wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/ann_code_src/train_gt_list_19_1_16.txt", "w")

    for im_idx in im_ls:
        wf.write(str(im_idx.strip("\n").split(".")[0]))
        if im_idx in gt_info:
            for dt_idx in gt_info[im_idx]:
                # dt_idx '3 892 445 21 53 24000 892 445 21 53'
                # dt_idx 参数意义: 类别 行人坐标 24000 可见部分坐标

                tmpv = dt_idx.split(" ")
                print tmpv
                xmin = str(max(1, int(tmpv[1])))
                ymin = str(max(1, int(tmpv[2])))
                xmax = str(min(2048, int(tmpv[1]) + int(tmpv[3])))
                ymax = str(min(1024, int(tmpv[2]) + int(tmpv[4])))

                v_xmin = str(max(1, int(tmpv[6])))
                v_ymin = str(max(1, int(tmpv[7])))
                v_xmax = str(min(2048, int(tmpv[6]) + int(tmpv[8])))
                v_ymax = str(min(1024, int(tmpv[7]) + int(tmpv[9])))

                orginal_size = (int(ymax) - int(ymin)) * (int(xmax) - int(xmin))
                v_size = (int(v_ymax) - int(v_ymin)) * (int(v_xmax) - int(v_xmin))

                ratio = v_size / (orginal_size + 0.0)

                if int(ymax) - int(ymin) >= 20 and ratio >= 0.3:

                    bbox_ls = dt_idx.split(" ")[1:5]
                    wf.write(" ")
                    for box_idx in range(len(bbox_ls)):
                        bbox_ls[box_idx] = float(bbox_ls[box_idx])
                        if box_idx == 0:
                            wf.write(str(int(bbox_ls[box_idx])))
                        else:
                            wf.write(",")
                            wf.write(str(int(bbox_ls[box_idx])))

                ratio = 0


            wf.write("\n")

    wf.close()

generate_gt_txt(gt_info, im_ls)



