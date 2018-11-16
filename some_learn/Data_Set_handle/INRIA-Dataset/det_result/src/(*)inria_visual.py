#--coding:utf-8--
import os
import cv2

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

def generate_gt_dict(resource_path):
    """
    :param path: 
    :return: image dict
    """

    rf = open(resource_path)

    content = rf.readline()
    cnt = 0
    tmp_dict = {}

    while content:
        #print content
        res = content.replace("\n", "").split(",")

        cls  = str(res[0:1][0])
        bbox = res[1:]

        if cls in tmp_dict:
            tmp_dict[cls].append(bbox)
        else:
            tmp_dict[cls] = [bbox]
            cnt += 1
        content = rf.readline()
    rf.close()

    return tmp_dict

def draw_gt(tmp_dict, tmp_dict1):

    cur_path = "/home/user/t1_data_reason_data_set"
    dirList = []
    fileList = []
    files = os.listdir(cur_path)

    for file in files:
        tmp_path = cur_path+"/"+file
        if(os.path.isdir(tmp_path)):
            if file[0] != '.':
                tmp = os.listdir(tmp_path)
                for tt in tmp:
                    tt_path = tmp_path + "/" + tt
                    if (os.path.isdir(tt_path)):
                        if file[0] != '.':
                            dirList.append(tt_path)


    for dir_ in dirList:
        if(os.path.isdir(dir_)):
            tfile = os.listdir(dir_)
            for idx_im in tfile:
                all_str = dir_+"/"+idx_im
                inDict = all_str.split("/")
                bot = inDict[-1][:-4]
                inDict_name = str(inDict[-3] + '/' + inDict[-2] + '/'+ bot)

                if inDict_name in tmp_dict:
                    gtList = tmp_dict[inDict_name]
                    im = cv2.imread(all_str)
                    # im = im[:, :, (2, 1, 0)]
                    # fig, ax = plt.subplots(figsize=(1, 1))
                    # ax.imshow(im, aspect='equal')

                    for idx_gt in gtList:
                        # [452.380659429031,167.729915560917,47.0928829915561,52.4969843184559]
                        # [375.544632086852,172.740631992242,22.3884197828709,49.0229191797346]
                        if float(idx_gt[0]) > 0.7:
                            x1 = int(float(idx_gt[1]))
                            y1 = int(float(idx_gt[2]))
                            w = int(float(idx_gt[3]))
                            h = int(float(idx_gt[4]))
                            cv2.rectangle(im,(x1,y1),(w, h) , (0, 0, 255), 1)
                            # plt.axis('off')
                            # plt.tight_layout()
                            # plt.imshow(im)
                            #plt.show()
                    mkdir('/home/user/det_result_/' + str(inDict[-3] + '/' + inDict[-2]))
                    cv2.imwrite('/home/user/det_result_/' + str(inDict[-3] + '/' + inDict[-2]) + '/' + bot+".jpg",im)
        pass

def draw_gt1andresult(tmp_dict):
    cur_path = "/home/user/draw_train_and_test/new6_9_test/"
    dirList = []
    fileList = []
    files = os.listdir(cur_path)

    for file in files:
        tmp_path = file.split('.')[0]
        dirList.append(tmp_path)

    for dir_ in dirList:
        if dir_ in tmp_dict:
            gtList = tmp_dict[dir_]
            im_path = cur_path+dir_+".jpg"
            im = cv2.imread(im_path)
            # im = im[:, :, (2, 1, 0)]
            # fig, ax = plt.subplots(figsize=(1, 1))
            # ax.imshow(im, aspect='equal')

            for idx_gt in gtList:

                    # [452.380659429031,167.729915560917,47.0928829915561,52.4969843184559]
                    # [375.544632086852,172.740631992242,22.3884197828709,49.0229191797346]
                    #'475 172 488 225'
                #if  float(idx_gt[0]) > 0.001:
                    print idx_gt[0]
                    x1 = int(float(idx_gt[1]))
                    y1 = int(float(idx_gt[2]))
                    x2 = int(float(float(idx_gt[3])))
                    y2 = int(float(float(idx_gt[4])))

                    #这里还是有问题，画出结果不对
                    cv2.rectangle(im,(x1,y1),(x2, y2) , (0, 255, 255), 1)

                    cv2.putText(im, idx_gt[0], (int(x1), int(y1 - 6)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,
                                    (0, 255, 255))
                    # plt.axis('off')
                    # plt.tight_layout()
                    # plt.imshow(im)
                    #plt.show()
            mkdir('/home/user/draw_result/handle_6_11_nms_upper_person_all_det_test/test/')
            cv2.imwrite('/home/user/draw_result/handle_6_11_nms_upper_person_all_det_test/test/' + str(dir_ + ".jpg"),im)

def compute_IoU(l1, l2):
    '''
    #the coordinate of this funcation is (x1,y1,x2,y2)
    :param l1: first rectangle coordinate 
    :param l2: second rectangle coordinate
    :return: yes or no IoU > 0.5(or x) 
    '''
    if(l1[0] > l2[0] + abs(l2[2]-l2[0])):
        return False
    if(l1[1] > l2[1] + abs(l2[3]-l2[1])):
        return False
    if(l1[0] + l1[2]-l1[0] < l2[0]):
        return False
    if(l1[1] + l1[3]-l1[1] < l2[1]):
        return False

    colInt = min(l1[0]+l1[2]-l1[0] , l2[0]+l2[2]-l2[0]) - max(l1[0], l2[0])
    rowInt = min(l1[1]+l1[3]-l1[1] , l2[1]+l2[3]-l2[1]) - max(l1[1], l2[1])

    intersection = colInt * rowInt
    area1 = (l1[2]-l1[0])*(l1[3]-l1[1])
    area2 = (l2[2]-l2[0])*(l2[3]-l2[1])

    intersectionPercent = intersection/(area1+area2-intersection + 0.0)
    print "IoU = " + str(intersectionPercent)
    if intersectionPercent < 0.5:
        return False
    else:
        return True

def draw_bbox(tmp_dict):

    cur_path = "/home/user/Downloads/caltech_data_set/datasets/inria_test/images/set01/test_image"
    dirList = []
    fileList = []
    files = os.listdir(cur_path)

    #获取文件列表
    for file in files:
        tmp_path = cur_path + "/" + file

        dirList.append(tmp_path)
    #便利文件列表


    #获取当前图片的绝对路径，然后进行处理
    for idx_im in dirList:
        all_str = idx_im
        inDict = all_str.split("/")
        bot = inDict[-1][:-4]
        inDict_name = bot

        if inDict_name in tmp_dict :
            bboxList = tmp_dict[inDict_name]

            if DRAW_IMG:
                im = cv2.imread(all_str)
            # im = im[:, :, (2, 1, 0)]
            # fig, ax = plt.subplots(figsize=(1, 1))
            # ax.imshow(im, aspect='equal')
            if WRITE_TXT:
                wtxt = open("/home/user/PycharmProjects/anaylsis_result/name_score.txt","w")
            for idx_bbox in bboxList:

                x1 = int(float(idx_bbox[1]))
                y1 = int(float(idx_bbox[2]))
                w = int(float(idx_bbox[3]))
                h = int(float(idx_bbox[4]))

                if DRAW_IMG and w >= 0 and h>=0:
                    if float(idx_bbox[0]) > 0.3:
                        cv2.rectangle(im, (x1, y1), (w, h), (0, 0, 255), 1)

                    if (y1 > 10)and w >= 0 and h>=0 :
                        if float(idx_bbox[0]) > 0.01:
                            cv2.putText(im, idx_bbox[0], (int(x1), int(y1 - 6)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,
                                        (255, 255, 0))
                    elif  w >= 0 and h>=0:
                        if float(idx_bbox[0]) > 0.01:
                            cv2.putText(im, idx_bbox[0], (int(x1), int(y1 + 15)), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                        0.8, (255, 255, 0))
                elif WRITE_TXT:
                    wtxt.write(str(inDict[-3] + '/' + inDict[-2]) + '/' + bot + ".png "+ str(idx_bbox))
                    wtxt.write("\n")
                        # plt.axis('off')
                    # plt.tight_layout()
                    # plt.imshow(im)
                    # plt.show()
            mkdir('/home/user/Disk1.8T/draw_result/inria/11_16_1/' + str(inDict[-3] + '/' + inDict[-2]))
            if DRAW_IMG:
                cv2.imwrite(
                            '/home/user/Disk1.8T/draw_result/inria/11_16_1/' + str(inDict[-3] + '/' + inDict[-2]) + '/' + bot + ".jpg",
                            im)
            elif WRITE_TXT:
                wtxt.close()

    pass

def str2float_in_list(str_list):
    """
    this funcation transform strlist to floatlist
    :param str_list: 
    :return:float_list 
    """
    import re
    float_reg = re.compile(r'^\d+\.\d+$')
    float_list = [float(f) for f in str_list if float_reg.match(f)]

    return float_list

#从生成的文本文档中，读取标注信息，然后用来生成字典，然后读取图片名，然后对比在字典中有无当前的图片名，有的话，生成检测结果
DRAW_IMG = 1
DRAW_IOU = 0
WRITE_TXT = 0
#new_anno_gt = generate_gt_dict("/home/user/PycharmProjects/anaylsis_result/draw_result_in_new_anno/test_gt.txt")

file_path = "/home/user/PycharmProjects/some_learn/Data_Set_handle/INRIA-Dataset/det_result/det/001-5.txt"
dec_result = generate_result(file_path)

draw_bbox(dec_result)