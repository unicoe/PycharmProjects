#--coding:utf-8--
import os
import cv2
from unicoe_tool.generate_xml import generate_xml

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
    wf = open("/home/user/PycharmProjects/caltech_new_anno/zss_train1x_11_11_1x_0.4_40_10.txt", "w")

    cur_path = "/home/user/py-R-FCN/data/VOCdevkit0712/VOC0712/JPEGImages/"

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

        while contx:
            contx = rtmp.readline()
            if contx:

                if flag == 0:
                    fileInfo.append("VOC0712")
                    fileInfo.append(fl.split('.')[0]+'.jpg')
                    im_path = cur_path + fl.split('.')[0]+'.jpg'
                    im = cv2.imread(im_path)
                flag = 1

                cnt += 1
                cor_dict = {}
                tmpv = []
                tmpv = contx.split(" ")

                if tmpv[0] == "person":
                    for idx in range(1,5):
                        tmpv[idx] = int(float(tmpv[idx]))
                        tmpv[idx+5] = int(float(tmpv[idx+5]))

                    xmin = str(max(1,tmpv[1]))
                    ymin = str(max(1,tmpv[2]))
                    xmax = str(min(tmpv[1] + tmpv[3],640))
                    ymax = str(min(tmpv[2] + tmpv[4], 480))

                    if tmpv[5] == '1':
                        v_xmin = str(max(1, tmpv[6]))
                        v_ymin = str(max(1, tmpv[7]))
                        v_xmax = str(min(tmpv[6] + tmpv[8], 640))
                        v_ymax = str(min(tmpv[7] + tmpv[9], 480))

                        bbox_size = (int(xmax) - int(xmin)) * (int(ymax) - int(ymin))
                        vis_bbox_size = (int(v_xmax) - int(v_xmin)) * (int(v_ymax) - int(v_ymin))

                        rate = vis_bbox_size / (bbox_size + 0.0)

                    w = int(xmax) - int(xmin)
                    h = int(ymax) - int(ymin)

                    if tmpv[5] == '0' or rate >= 0.4:
                        if h >= 40 and w >= 10:
                            cor_dict = {}
                            cor_dict["xmin"] = xmin
                            cor_dict["ymin"] = ymin
                            cor_dict["xmax"] = xmax
                            cor_dict["ymax"] = ymax

                            cv2.rectangle(im, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (225, 255, 0), 1)
                            mkdir('/home/user/Disk1.8T/draw_train_and_test/11_11/')
                            cv2.imwrite('/home/user/Disk1.8T/draw_train_and_test/11_11/' + str(fl.split('.')[0]+'.jpg'), im)

                            obj.append(cor_dict)
                        rate = 0

            else:
                if flag == 0:
                    fileInfo.append("VOC0712")
                    fileInfo.append(fl.split('.')[0]+'.jpg')
                flag = 1

        if len(obj) != 0:
            generate_xml("/home/user/PycharmProjects/caltech_new_anno/zss_train1x_11_11_1x_0.4_40_10/", fileInfo, obj)
            wf.write(fl.split('.')[0])
            wf.write('\n')
    print cnt
    pass
    wf.close()

folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/anno_train_1xnew")
