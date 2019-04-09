# -*- coding: utf-8 -*-
def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok'
        return True
    else:
        print path + 'failed!'
        return False

def extrat_info():
    rf = open("/home/user/PycharmProjects/some_learn/CityPersons_handle/ann_code_src/ann_file/ann_train_aligned.txt", "r")
    wf = open("/home/user/PycharmProjects/some_learn/CityPersons_handle/ann_code_src/ann_file/trainval_lst"
              "/anno_19_1_16_20_0.3.txt", "w")
    contx = rf.readline()
    ctx_str = ""

    ctx_dict ={}
    im_list = []
    cnt = 0
    cnt1 = 0
    while contx:

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

                wf.write(tmp.split('.')[0])
                wf.write("\n")
        contx = rf.readline()

    rf.close()
    wf.close()
    return ctx_dict

ctx_dict = extrat_info()

for k,v in ctx_dict.items():
    folderName,fileName = k.split("/")

    # 保存标注的文件
    mkdir("/home/user/PycharmProjects/some_learn/CityPersons_handle/ann_code_src/ann_file/anno_19_1_16_20_0.3/")
    root_file = "/home/user/PycharmProjects/some_learn/CityPersons_handle/ann_code_src/ann_file/anno_19_1_16_20_0.3/"

    fileInfo=[]
    obj = []
    cor_dict = {}

    fileInfo.append(folderName)
    fileInfo.append(fileName)

    img_root = "/home/user/Disk1.8T/py-R-FCN/data/VOCdevkit0712(citypersons)/VOC0712/JPEGImages"
    im_path = img_root + "/" + folderName + "/" + fileName.split("\n")[0]

    if v:
        for v_i in v:
            tmpv = v_i.split(" ")
            print tmpv
            xmin = str(max(1,int(tmpv[1])))
            ymin = str(max(1,int(tmpv[2])))
            xmax = str(min(2048,int(tmpv[1])+int (tmpv[3])))
            ymax = str(min(1024,int(tmpv[2])+int (tmpv[4])))

            v_xmin = str(max(1, int(tmpv[6])))
            v_ymin = str(max(1, int(tmpv[7])))
            v_xmax = str(min(2048, int(tmpv[6]) + int(tmpv[8])))
            v_ymax = str(min(1024, int(tmpv[7]) + int(tmpv[9])))

            orginal_size = (int(ymax)-int(ymin))*(int(xmax)-int(xmin))
            v_size = (int(v_ymax)-int(v_ymin))*(int(v_xmax)-int(v_xmin))

            ratio = v_size / (orginal_size+0.0)

            if int(ymax) - int(ymin) >= 20  and ratio >= 0.3:
                cor_dict = {}
                cor_dict["xmin"] = xmin
                cor_dict["ymin"] = ymin
                cor_dict["xmax"] = xmax
                cor_dict["ymax"] = ymax
                obj.append(cor_dict)

