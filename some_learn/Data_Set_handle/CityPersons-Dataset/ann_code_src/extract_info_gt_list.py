# -*- coding: utf-8 -*-

def extrat_info():
    rf = open("/home/user/PycharmProjects/some_learn/CityPersons_handle/ann_train_aligned.txt", "r")
    wf = open("/home/user/PycharmProjects/some_learn/CityPersons_handle/out_train_19_1_16.txt", "w")
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

    wf = open("/home/user/PycharmProjects/some_learn/CityPersons_handle/ann_code_src/train_gt_list.txt", "w")

    for im_idx in im_ls:
        wf.write(str(im_idx.strip("\n").split(".")[0]))
        if im_idx in gt_info:
            for dt_idx in gt_info[im_idx]:
                bbox_ls = dt_idx.split(" ")[1:5]
                wf.write(",")
                for box_idx in range(len(bbox_ls)):
                    bbox_ls[box_idx] = float(bbox_ls[box_idx])
                    if box_idx == 0:
                        wf.write(str(int(bbox_ls[box_idx])))
                    else:
                        wf.write(" ")
                        wf.write(str(int(bbox_ls[box_idx])))
            wf.write("\n")

    wf.close()

generate_gt_txt(gt_info, im_ls)



