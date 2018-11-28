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
                        if float(idx_bbox[0]) > 0.3:
                            cv2.putText(im, idx_bbox[0], (int(x1), int(y1 - 6)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,
                                        (255, 255, 0))
                    elif  w >= 0 and h>=0:
                        if float(idx_bbox[0]) > 0.3:
                            cv2.putText(im, idx_bbox[0], (int(x1), int(y1 + 15)), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                        0.8, (255, 255, 0))
                elif WRITE_TXT:
                    wtxt.write(str(inDict[-3] + '/' + inDict[-2]) + '/' + bot + ".png "+ str(idx_bbox))
                    wtxt.write("\n")
                        # plt.axis('off')
                    # plt.tight_layout()
                    # plt.imshow(im)
                    # plt.show()
            mkdir('/home/user/Disk1.8T/draw_result/inria/11_16_2/' + str(inDict[-3] + '/' + inDict[-2]))
            if DRAW_IMG:
                cv2.imwrite(
                            '/home/user/Disk1.8T/draw_result/inria/11_16_2/' + str(inDict[-3] + '/' + inDict[-2]) + '/' + bot + ".jpg",
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