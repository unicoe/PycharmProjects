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

file_list = os.listdir("/home/user/Disk1.8T/vitual_machine/share/instance")

print file_list

for fidx in file_list:
    fname = fidx.split('.')[0]
    pictures_list = os.listdir("/home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages")
    for pidx in pictures_list:
        if fname == pidx.split(".")[0]:
            im = cv2.imread("/home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages/" + pidx)
            mkdir('/home/user/Disk1.8T/mask_dadta/')
            cv2.imwrite('/home/user/Disk1.8T/mask_dadta/' + str(pidx), im)

"""
search same name file from one file to others.


"""
