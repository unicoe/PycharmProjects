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

def draw_gt(tmp_dict):

    cur_path = "/home/user/Disk1.8T/all_set"
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
                        x1 = int(float(idx_gt[0]))
                        y1 = int(float(idx_gt[1]))
                        w = int(float(idx_gt[2]))
                        h = int(float(idx_gt[3]))
                        cv2.rectangle(im,(x1,y1),(x1+w, y1+h) , (0, 255, 0), 1)
                        # plt.axis('off')
                        # plt.tight_layout()
                        # plt.imshow(im)
                        #plt.show()
                        mkdir('/home/user/data_all_annoations/' + str(inDict[-3] + '/' + inDict[-2]))
                        cv2.imwrite('/home/user/data_all_annoations/' + str(inDict[-3] + '/' + inDict[-2]) + '/' + bot+".jpg",im)
    pass

def generate_result(resource_path):
    """
    :param path: 
    :return: image dict
    """
    supname = resource_path[-9:-4] + "/" + resource_path[-4:] + "/"
    print supname
    rf = open(resource_path)

    content = rf.readline()
    cnt = 0
    tmp_dict = {}

    while content:
        #print content
        res = content.replace("\n", "").split(" ")

        cls  = supname + str(res[0:1][0])
        bbox = res[1:5]

        if cls in tmp_dict:
            tmp_dict[cls].append(bbox)
        else:
            tmp_dict[cls] = [bbox]
            cnt += 1
        content = rf.readline()
    rf.close()

    return tmp_dict


def generate_all_result(path):
    import os
    dirList = []
    fileList = []

    files = os.listdir(path)

    for f in files:
        if(os.path.isdir(path + "/" + f)):
            if f[0] != '.':
                dirList.append(f)
        if(os.path.isfile(path + '/'+ f)):
                fileList.append(f)
    tmp1 = {}
    for fl in fileList:
        tmp1 = dict(tmp1, **generate_result(path + fl))
    return tmp1

#从生成的　annotations-set06/V000 这样的文本文档中，读取标注信息，然后用来生成字典，然后从图片目录中读取图片名，然后对比在字典中有无当前的图片名，有的话，去生成ground truth.
file_dict = generate_all_result("/home/user/Downloads/caltech_data_set/data_all/")


draw_gt(file_dict)