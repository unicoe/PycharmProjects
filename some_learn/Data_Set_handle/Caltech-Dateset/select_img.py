# -*- coding: utf-8 -*-
"""
实现从几个有相同图片的文件夹中，取图片，到对应文件夹中

选取的图片的名字都是一样的
"""
import cv2

org_path_ls = [
# '/home/user/Disk1.8T/paper_img_result/paper_result/select/300',
# '/home/user/Disk1.8T/paper_img_result/paper_result/select/512',
# '/home/user/Disk1.8T/paper_img_result/paper_result/select/512_',
'/home/user/Disk1.8T/paper_img_result/paper_result/select/640_480',
'/home/user/Disk1.8T/paper_img_result/paper_result/select/960_720',
'/home/user/Disk1.8T/paper_img_result/paper_result/select/1280_960',
]

target_path_ls = [
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/300",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/512",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/512_",
"/home/user/Disk1.8T/paper_img_result/paper_result/compare/640_480",
"/home/user/Disk1.8T/paper_img_result/paper_result/compare/960_720",
"/home/user/Disk1.8T/paper_img_result/paper_result/compare/1280_960",
]

"""
org 和 target一一对应
"""

im_name_ls = [

'set06_V002_I00059',
'set06_V002_I01379',
'set06_V002_I01409',
'set06_V002_I01469',
'set06_V002_I01499',
'set06_V002_I01529',
'set06_V002_I01559',
'set06_V002_I01589',
'set06_V002_I01619',
'set06_V002_I01679',
'set06_V013_I01709',
'set06_V013_I01739',
'set06_V015_I00329',
'set07_V000_I01529',
'set07_V000_I01589',
'set07_V000_I01619',
'set07_V000_I01649',
'set07_V001_I00749',
'set07_V008_I01379',
'set07_V010_I01079',
'set07_V010_I01109',
'set09_V009_I00029',
'set09_V009_I00119',
'set09_V009_I00149',
'set10_V008_I00869',
'set10_V010_I00329',
'set10_V011_I00569',
'set10_V011_I00599',
'set10_V011_I00629',
'set10_V011_I00659',
'set10_V011_I01109',
'set10_V011_I01139',
'set10_V011_I01169',

]


for i in range(0,6):
    s_path = org_path_ls[i]
    t_path = target_path_ls[i]

    img_ls = []
    for idx_im in im_name_ls:
        tmp_path = s_path + "/VOC0712/JPEGImages/" +idx_im+".png"
        tmp_img = cv2.imread(tmp_path)
        # import pdb
        # pdb.set_trace()
        cv2.imwrite(t_path+"/"+idx_im+".png", tmp_img)

