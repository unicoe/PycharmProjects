#--coding:utf-8--
import os
from unicoe_tool.generate_xml import generate_xml

def folder_struct(level, path):
    global allFileNum

    dirList = []
    fileList = []
    files = os.listdir(path)
    dirList.append(str(level))

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
            folder_struct((int(dirList[0]) + 1), path+'/'+dl)

    cnt = 0
    wf = open("/home/user/PycharmProjects/caltech_new_anno/train1xnew_gt.txt", "w")
    print len(fileList)
    for fl in fileList:
        tmp = path + "/" + fl

        rtmp = open(tmp, "r")
        # wf.write(fl)
        # wf.write("----")
        # wf.write('\n')
        contx = rtmp.readline()

        obj = []
        cor_dict = {}
        flag = 0

        while contx:
            contx = rtmp.readline()
            if contx:
                flag = 1
                cnt += 1
                cor_dict = {}
                tmpv = []
                tmpv = contx.split(" ")

                if tmpv[0] == "person":
                    xmin = str(max(1,int(float(tmpv[1]))))
                    ymin = str(max(1,int(float(tmpv[2]))))
                    xmax = str(min(640,int(float(tmpv[1])) + int(float(tmpv[3]))))
                    ymax = str(min(480,int(float(tmpv[2])) + int(float(tmpv[4]))))
                    cor_dict = {}

                    cor_dict["xmin"] = xmin
                    cor_dict["ymin"] = ymin
                    cor_dict["xmax"] = xmax
                    cor_dict["ymax"] = ymax
                    obj.append(cor_dict)
                # wf.write(str(tmpv))
                # wf.write('\n')
            else:
                if flag == 1 and len(obj):
                    wf.write(fl.split('.')[0])
                    wf.write(',')
                    print fl.split('.')[0] + ","
                    for idx_o in obj:
                        if idx_o is not obj[-1]:
                            wf.write(idx_o["xmin"]+" ")
                            wf.write(idx_o["ymin"]+" ")
                            wf.write(idx_o["xmax"]+" ")
                            wf.write(idx_o["ymax"]+",")
                        else:
                            wf.write(idx_o["xmin"] + " ")
                            wf.write(idx_o["ymin"] + " ")
                            wf.write(idx_o["xmax"] + " ")
                            wf.write(idx_o["ymax"])
                    wf.write('\n')
                break


    print cnt
    #wf.write(cnt)
    pass
    wf.close()

#folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/caltechx1/train/annotations")
folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/anno_train_1xnew")
