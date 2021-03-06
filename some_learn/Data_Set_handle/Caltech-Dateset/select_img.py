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
'/home/user/Disk1.8T/paper_img_result/paper_result/select/960_720',
# '/home/user/Disk1.8T/draw_result/paper_result/submit/2019_10_10_Thu_01_58_01',
# '/home/user/Disk1.8T/draw_result/paper_result/submit/2019_06_20_Thu_00_14_46',
# '/home/user/Disk1.8T/draw_result/paper_result/submit/2019_06_19_Wed_11_43_49',
]

target_path_ls = [
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/300",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/512",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/512_",
'/home/user/Disk1.8T/paper_img_result/paper_result/compare/960_720',
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/2019_10_10_Thu_01_58_01",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/2019_06_20_Thu_00_14_46",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/2019_06_19_Wed_11_43_49",
]

"""
org 和 target一一对应
"""

im_name_ls = [

'set06_V002_I00029',
'set06_V002_I00729',
'set06_V002_I00839',
'set06_V002_I01499',
'set06_V002_I01619',
'set06_V002_I01559',
'set06_V002_I01619',
'set06_V002_I01739',
'set06_V010_I01799',

'set06_V012_I00749',
'set06_V013_I00629',
'set06_V013_I01739',
'set06_V015_I00359',
'set06_V015_I00509',
'set06_V015_I00539',
'set06_V015_I00899',
'set06_V015_I01379',
'set06_V015_I01829',

'set06_V016_I00019',
'set06_V016_I00599',
'set06_V016_I00719',

'set06_V017_I01799',

'set07_V000_I00569',
'set07_V000_I00839',
'set07_V000_I00869',
'set07_V000_I00899',
'set07_V000_I01049',
'set07_V000_I01619',

'set07_V003_I00659',
'set07_V003_I01349',
'set07_V003_I01499',
'set07_V005_I01769',
'set07_V005_I01799',
'set07_V008_I00779',
'set07_V008_I01049',


'set10_V009_I00659',
'set10_V010_I00419',
'set10_V010_I01439',
'set10_V011_I00629',


]


for i in range(0,1):
    s_path = org_path_ls[i]
    t_path = target_path_ls[i]

    img_ls = []
    for idx_im in im_name_ls:
        tmp_path = s_path + "/VOC0712/JPEGImages/" +idx_im+".png"
        tmp_img = cv2.imread(tmp_path)
        # import pdb
        # pdb.set_trace()
        cv2.imwrite(t_path+"/"+idx_im+".png", tmp_img)

