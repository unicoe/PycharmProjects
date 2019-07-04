#--coding:utf-8--
import os
import cv2
import matplotlib.pyplot as plt

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok.'
        return True
    else:

        print path + ' path already exits.'
        return False

def generate_result(resource_path):
    """
    :param path:
    :return:
    """
    rf = open(resource_path)

    content = rf.readline()
    cnt = 0
    tmp_dict = {}

    while content:
        #print content

        res = content.replace("\n", "").split(" ")
        cls  = str(res[0:1][0])
        bbox = res[1:6]

        if cls in tmp_dict:
            tmp_dict[cls].append(bbox)
        else:
            tmp_dict[cls] = [bbox]
            cnt += 1

        content = rf.readline()
    rf.close()
    return tmp_dict

def draw_bbox(file_idx, tmp_dict):

    bbox_cnt = 0
    img_cnt = 0
    undet_img = []

    tgt_r = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/Caltech-Dateset/handle_result/res_ls/res_ls.txt", "r")
    tg_ls = []
    tg_info = tgt_r.readline()
    while tg_info:
        tg_tmp = tg_info.strip("\n")
        tg_ls.append(tg_tmp)
        tg_info = tgt_r.readline()

    folder_name = file_idx.strip("\n").split("/")[-1].split(".")[0]
    cur_path = "/home/user/Disk1.8T/data_set/MOT17Det/test"

    # sub det
    # cur_path ="/home/user/Disk1.8T/data_set/testing/image_2"
    dirList = []
    files = os.listdir(cur_path)

    for file in files:
        tmp_path = cur_path + "/" + file
        fs = os.listdir(tmp_path)
        for f in fs:
            dirList.append((file +"/"+f).split(".")[0])
            with open('/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/im_list/test1.txt', 'aw') as f1:
                f1.write((file +"/"+f))
                f1.write("\n")

    #获取当前图片的绝对路径，然后进行处理

    for idx_im in dirList:
        all_str = idx_im
        inDict = all_str.split("/")
        bot = inDict[-1][:]
        inDict_name = all_str

        if inDict_name in tmp_dict:

            bboxList = tmp_dict[inDict_name]
            im_path = "/home/user/Disk1.8T/data_set/MOT17Det/test/" +all_str+'.jpg'
            im = cv2.imread(im_path)
            #im = im[:, :, (2, 1, 0)]

            flag = 0

            for idx_bbox in bboxList:

                x1 = int(float(idx_bbox[1]))
                y1 = int(float(idx_bbox[2]))
                x2 = int(float(idx_bbox[3]))
                y2 = int(float(idx_bbox[4]))

                if float(idx_bbox[0]) >= 0.3:
                    flag = 1
                    bbox_cnt = bbox_cnt + 1
                    # cv2.rectangle(im, (x1, y1), (x2, y2), (0, 255, 0), 1)
                    # cv2.rectangle(im, (x1, y1), (x1 + 20, y1 - 10), (0, 255, 0), -1)
                    # cv2.putText(im, str(float(idx_bbox[0]))[:4], (x1, y1), 0, 0.3, (0, 0, 0), 1)

                    cv2.rectangle(im, (x1, y1), (x2, y2), (0, 255, 0), 1)
                    cv2.rectangle(im, (x1, y1), (x1 + 20, y1), (0, 255, 0), -1)
                    cv2.putText(im, str(float(idx_bbox[0]))[:4], (x1, y1), 0, 0.3, (0, 0, 0), 1)

            if flag == 1:
                img_cnt = img_cnt + 1

                mkdir('/home/user/Disk1.8T/draw_result/paper_result/' + folder_name + '/' + str(inDict[0]))
                cv2.imwrite('/home/user/Disk1.8T/draw_result/paper_result/' + folder_name + '/' +
                            str(inDict[0]) + '/' + bot + ".jpg",
                            im)
            #plt.show()

            else:
                undet_img.append(bot)

    #print str(undet_img)
    w_undet = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/paper_result/" + folder_name + ".txt", "w")

    for idx in undet_img:
        w_undet.write(idx)
        w_undet.write("\n")

    w_undet.write("un_det " + str(len(undet_img)))
    w_undet.write("bbox: " + str(bbox_cnt))
    w_undet.write("img " + str(img_cnt))
    w_undet.close()

    print "un_det " + str(len(undet_img))
    print "bbox: " + str(bbox_cnt)
    print "img " + str(img_cnt)


def str2float_in_list(str_list):
    import re
    float_reg = re.compile(r'^\d+\.\d+$')
    float_list = [float(f) for f in str_list if float_reg.match(f)]

    return float_list

file_lst = [

'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/2019_06_29_Sat_19_27_53.txt'

]

for file_idx in file_lst:

    dec_result = generate_result(file_idx)

    draw_bbox(file_idx,dec_result)