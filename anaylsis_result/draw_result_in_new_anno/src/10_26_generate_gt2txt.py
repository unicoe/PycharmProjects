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
    wf = open("/home/user/PycharmProjects/anaylsis_result/draw_result_in_new_anno/gt_file/10_26_zss_1x_train_gt.txt", "w")
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

                # zss 新标注
                if tmpv[0] == "person":
                    xmin = str(int(float(tmpv[1])))
                    ymin = str(int(float(tmpv[2])))
                    xmax = str(int(float(tmpv[1])) + int(float(tmpv[3])))
                    ymax = str(int(float(tmpv[2])) + int(float(tmpv[4])))

                    if tmpv[5] == '1':
                        v_xmin = str(max(1,int(float(tmpv[6]))))
                        v_ymin = str(max(1,int(float(tmpv[7]))))
                        v_xmax = str(min(int(float(tmpv[6])) + int(float(tmpv[8])),640))
                        v_ymax = str(min(int(float(tmpv[7])) + int(float(tmpv[9])),480))

                        bbox_size = (int(xmax)-int(xmin))*(int(ymax)-int(ymin))
                        vis_bbox_size = (int(v_xmax)-int(v_xmin))*(int(v_ymax)-int(v_ymin))
                        if bbox_size != 0:
                            rate = vis_bbox_size / (bbox_size + 0.0)
                        else:
                            rate = 0

                    w = (int(xmax)-int(xmin))
                    h = (int(ymax)-int(ymin))

                    if tmpv[5] == '1' and (rate > 0.3):
                        if w >=3 and h >= 20:
                            cor_dict = {}
                            cor_dict["xmin"] = xmin
                            cor_dict["ymin"] = ymin
                            cor_dict["xmax"] = xmax
                            cor_dict["ymax"] = ymax
                            obj.append(cor_dict)
                            rate = 0

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

folder_struct(1, "/home/user/Downloads/caltech_data_set/anno_train_1xnew/")

# zss new
# folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/anno_test_1xnew")

#folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/head_5_28new1x")
