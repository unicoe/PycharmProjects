import os
import random

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
    print dirList
    # print fileList
    # print dirList
    for fl in fileList:
        #print fl[12:17], fl[17:21]
        file_info = (fl[12:17] + '/' + fl[17:21])
        print file_info
        generate_txt(file_info)
    pass


def generate_txt(xml_folder):
    trainval_percent = 0
    train_percent = 0
    folder_root = '/home/user/Desktop/VOC/'
    xmlfilepath = folder_root + 'Annotations/'+xml_folder
    txtsavepath = folder_root + 'ImageSets/Main'
    try:
        total_xml = os.listdir(xmlfilepath)
        print total_xml

        num = len(total_xml)

        print num
        list = range(num)
        tv = int(num * trainval_percent)
        tr = int(tv * train_percent)
        trainval = random.sample(list, tv)
        train = random.sample(trainval, tr)

        ftrainval = open(folder_root + 'ImageSets/Main/trainval.txt', 'aw')
        ftest     = open(folder_root + 'ImageSets/Main/test.txt'    , 'aw')
        ftrain    = open(folder_root + 'ImageSets/Main/train.txt'   , 'aw')
        fval      = open(folder_root + 'ImageSets/Main/val.txt'     , 'aw')

        folder_name = xmlfilepath[-10:] + '/'

        print folder_name
        for i in list:
            name = folder_name + total_xml[i][:-4] + '\n'
            if i in trainval:
                ftrainval.write(name)
                if i in train:
                    ftrain.write(name)
                else:
                    fval.write(name)
            else:
                ftest.write(name)

        ftrainval.close()
        ftrain.close()
        fval.close()
        ftest.close()
    except Exception:
        pass

# these folders's file is annotations-set00V000,use these file name to generate foldernam
folder_struct(1, "/home/user/Downloads/caltech_data_set/data_reasonable_3_19")
#folder_struct(1, "/home/user/Downloads/caltech_data_set/data_reasonable_30stepsize1_test")