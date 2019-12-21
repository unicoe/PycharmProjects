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
# '/home/user/Disk1.8T/draw_result/paper_result/submit/2019_10_10_Thu_01_58_01',
# '/home/user/Disk1.8T/draw_result/paper_result/submit/2019_06_20_Thu_00_14_46',
# '/home/user/Disk1.8T/draw_result/paper_result/submit/2019_06_19_Wed_11_43_49',
"/home/user/Disk1.8T/paper_img_result/paper_result/AD-SSD",
"/home/user/Disk1.8T/paper_img_result/paper_result/SSD_SEG_VIS",
]

target_path_ls = [
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/300",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/512",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/512_",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/2019_10_10_Thu_01_58_01",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/2019_06_20_Thu_00_14_46",
# "/home/user/Disk1.8T/paper_img_result/paper_result/compare/2019_06_19_Wed_11_43_49",
"/home/user/Disk1.8T/paper_img_result/paper_result/compare/AD-SSD",
"/home/user/Disk1.8T/paper_img_result/paper_result/compare/SSD_SEG_VIS"
]
"""
org 和 target一一对应
"""

im_name_ls = [

"MOT17-10/000009",
"MOT17-10/000034",
"MOT17-10/000098",
"MOT17-10/000149",
"MOT17-10/000459",
"MOT17-10/000482",
"MOT17-10/000537",
"MOT17-10/000653",
"MOT17-11/000043",
"MOT17-11/000137",
"MOT17-11/000615",
"MOT17-11/000672",


"MOT17-14/000001",
"MOT17-14/000129",
"MOT17-14/000596",

"MOT17-12/000030",
"MOT17-12/000043",
"MOT17-12/000045",
"MOT17-12/000106",
"MOT17-12/000124",
"MOT17-12/000139",
"MOT17-12/000153",
"MOT17-12/000154",


"MOT17-06/000021",
"MOT17-06/000022",
"MOT17-06/000255",

"MOT17-07/000031",
"MOT17-07/000086",
"MOT17-07/000168",

"MOT17-08/000001",
"MOT17-08/000084",
"MOT17-08/000098",
"MOT17-08/000102",

"MOT17-10/000038",
"MOT17-10/000098",
"MOT17-10/000115",
"MOT17-10/000118",

"MOT17-11/000017",
"MOT17-11/000043",
"MOT17-11/000137",
"MOT17-11/000141",
"MOT17-11/000144",


"MOT17-01/000004",
"MOT17-01/000326",

"MOT17-03/000001",
"MOT17-03/000007",
"MOT17-03/000019",
"MOT17-03/001122",
"MOT17-03/001483",
]


for i in range(0,2):
    s_path = org_path_ls[i]
    t_path = target_path_ls[i]

    img_ls = []
    for idx_im in im_name_ls:
        tmp_path = s_path +"/"+ idx_im+".jpg"
        tmp_img = cv2.imread(tmp_path)
        print(tmp_path)
        print(tmp_img)
        # import pdb
        # pdb.set_trace()
        cv2.imwrite(t_path+"/"+idx_im+".png", tmp_img)

