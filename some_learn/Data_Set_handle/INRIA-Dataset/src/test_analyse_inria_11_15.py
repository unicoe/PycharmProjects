#--coding:utf-8--
import os

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + 'ok')
        return True
    else:
        print(path + 'failed!')
        return False


def folder_struct(level, path):
    global allFileNum

    dirList = []
    fileList = []
    files = os.listdir(path)
    dirList.append(str(level))

    # get img shape info
    rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/img_shape.txt", "r")
    shape_dict = {}
    content = rf.readline()
    while content:
        im_info = content.strip("\n").split(" ")
        shape_dict[im_info[0]] = [int(im_info[1]), int(im_info[2])]  # h w
        content = rf.readline()

    #
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            if f[0] != '.':
                dirList.append(f)
        if (os.path.isfile(path + '/' + f)):
            fileList.append(f)

    i_dl = 0
    for dl in dirList:
        if i_dl == 0:
            i_dl = i_dl + 1
        else:
            #print '-' * (int(dirList[0])), dl
            folder_struct((int(dirList[0]) + 1), path+'/'+dl)

    cnt = 0
    #wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/train_lst_11_15.txt", "w")
    # save ratio
    #wf1 = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/h_w_lst.txt","w")

    #save h
    #wf2 = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/h_lst.txt","w")

    # save img w/h
    wf3 = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/lst/test_img_w_h_lst.txt","w")
    print len(fileList)
    for fl in fileList:
        #todo 遍历txt文件，然后根据txt文件生成xml文件
        tmp = path + "/" + fl

        rtmp = open(tmp, "r")
        contx = rtmp.readline()

        fileInfo = []
        obj = []
        cor_dict = {}
        flag = 0

        img_w = 0
        img_h = 0

        while contx:
            contx = rtmp.readline()
            if contx:

                if flag == 0:
                    fileInfo.append("VOC0712")
                    fileInfo.append(fl.split('.')[0]+'.png')
                    img_h = shape_dict[fl.split('.')[0]][0]
                    img_w = shape_dict[fl.split('.')[0]][1]

                    wf3.write(str(img_w/(img_h+0.0)))

                    wf3.write("\n")
                flag = 1

                cnt += 1
                tmpv = contx.split(" ")

                if tmpv[0] == "person":
                    for idx in range(1,5):
                        tmpv[idx] = int(float(tmpv[idx]))
                        tmpv[idx+5] = int(float(tmpv[idx+5]))

                    xmin = str(tmpv[1])
                    ymin = str(tmpv[2])
                    xmax = str(tmpv[1] + tmpv[3])
                    ymax = str(tmpv[2] + tmpv[4])

                    if tmpv[5] == '0':
                        cor_dict = {}
                        cor_dict["xmin"] = xmin
                        cor_dict["ymin"] = ymin
                        cor_dict["xmax"] = xmax
                        cor_dict["ymax"] = ymax

                        # wf1.write(str(tmpv[3] / (tmpv[4] + 0.0)))
                        # wf1.write("\n")
                        #
                        # wf2.write(str(tmpv[4]))
                        # wf2.write("\n")
                        obj.append(cor_dict)

            else:
                if flag == 0:
                    fileInfo.append("VOC0712")
                    fileInfo.append(fl.split('.')[0]+'.png')
                flag = 1

        if len(obj) != 0:
            # generate_xml("/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/anno_11_15/",
            #              fileInfo, obj, width=img_w, height=img_h)
            # wf.write(fl.split('.')[0])
            # wf.write('\n')


            pass
    print cnt
    pass
    # wf.close()
    # wf1.close()
    # wf2.close()
    wf3.close()


#folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/caltechx10/train/annotations")
folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/inria_test/images/set01/V000_copy")
