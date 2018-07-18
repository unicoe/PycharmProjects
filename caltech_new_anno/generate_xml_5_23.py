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
            #print '-' * (int(dirList[0])), dl
            folder_struct((int(dirList[0]) + 1), path+'/'+dl)

    # print fileList
    # print dirList
    cnt = 0
    wf = open("/home/user/PycharmProjects/caltech_new_anno/test1x.txt", "w")
    print len(fileList)
    for fl in fileList:
        #todo 遍历txt文件，然后根据txt文件生成xml文件
        tmp = path + "/" + fl

        rtmp = open(tmp, "r")
        # wf.write(fl)
        # wf.write("----")
        # wf.write('\n')
        contx = rtmp.readline()

        fileInfo = []
        obj = []
        cor_dict = {}
        flag = 0

        while contx:
            contx = rtmp.readline()
            cur_path = "/home/user/draw_result/py_top_down_20000/gt4_test/"
            im_path = cur_path + fl.split('.')[0] + ".jpg"
            im = cv2.imread(im_path)
            if contx:

                if flag == 0:
                    fileInfo.append("VOC0712")
                    fileInfo.append(fl.split('.')[0]+'.jpg')
                flag = 1

                cnt += 1
                cor_dict = {}
                tmpv = []
                tmpv = contx.split(" ")

                if tmpv[0] == "person":

                    xmin = (max(1,int(tmpv[1])))
                    ymin = (max(1,int(tmpv[2])))
                    xmax = (min(int(tmpv[1]) + int(tmpv[3]),640))
                    ymax = (min(int(tmpv[2]) + int(tmpv[4]), 480))

                    x1 = (xmax + xmin)/2. - 0.6*((xmax - xmin)/2.)
                    x2 = (xmax + xmin)/2. + 0.6*((xmax - xmin)/2.)
                    y1 = (ymax + ymin)/2. - 1*((ymax - ymin)/2.)
                    y2 = (ymax + ymin)/2. + 0.8*((ymax - ymin)/2.)
                    cor_dict = {}
                    cor_dict["xmin"] = str(x1)
                    cor_dict["ymin"] = str(y1)
                    cor_dict["xmax"] = str(x2)
                    cor_dict["ymax"] = str(y2)
                    cv2.rectangle(im, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 1)
                    #mkdir('/home/user/draw_result/py_top_down_20000/gt4_test/')
                    cv2.imwrite('/home/user/draw_result/py_top_down_20000/gt4_test/' + str(fl.split('.')[0] + ".jpg"),
                                im)
                    obj.append(cor_dict)
                # wf.write(str(tmpv))
                # wf.write('\n')

            else:
                if flag == 0:
                    fileInfo.append("VOC0712")
                    fileInfo.append(fl.split('.')[0]+'.jpg')
                flag = 1


        #train
        if flag == 1:
            #generate_xml("/home/user/PycharmProjects/caltech_new_anno/annos/", fileInfo, obj)
            #print fl
            #wf.write(fl.split('.')[0])
            # wf.write('\n')
            pass
        #test
        generate_xml("/home/user/PycharmProjects/caltech_new_anno/5_23annoss/", fileInfo, obj)
        wf.write(fl.split('.')[0])
        wf.write('\n')
    print cnt
    #wf.write(cnt)
    pass
    wf.close()

"""
这里替换不同的数据集，从而生成不同的ｘｍｌ文件
２０１８年０５月０４日２２：２１：４３　　对坐标进行了限制，即最大值和最小值
"""
#folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/caltechx10/train/annotations")
folder_struct(1, "/home/user/Downloads/caltech_data_set/datasets/caltechx1/test/annotations")
