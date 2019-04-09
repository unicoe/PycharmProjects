# -*- coding: utf-8 -*-
# @Time    : 18-11-4 下午3:45
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : generate_cityperons_json.py
# @Software: PyCharm Community Edition

"""
生成coco的检测结果格式

"""
import copy
import eval_demo


file_list = [
#'/home/user/PycharmProjects/some_learn/CityPersons_handle/evaluation/11_13/0/comp4_a7e8f78e-5da1-4f8b-9349-12bbf3b57148_det_test_person.txt',

#'/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_31_56_val_det.txt.re',
'/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_33_45_val_det.txt.re',
'/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_35_35_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_37_25_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_39_15_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_41_07_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_43_00_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_44_53_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_46_45_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_48_38_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_50_31_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_52_24_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_54_18_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_56_11_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_58_05_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_59_58_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_01_52_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_03_45_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_05_40_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_07_34_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_09_28_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_11_23_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_13_18_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_15_14_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_17_09_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_19_05_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_21_00_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_22_56_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_24_51_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_26_48_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_28_44_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_30_40_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_32_37_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_34_34_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_36_31_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_38_28_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_40_25_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_42_23_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_44_20_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_46_18_val_det.txt.re',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_48_16_val_det.txt.re',

]

def generate_json(file_name):
    rf = open(file_name, "r")

    # frankfurt/frankfurt_000000_000294_leftImg8bit 0.149 1214.6 359.7 1269.1 488.0
    # frankfurt/frankfurt_000000_000294_leftImg8bit 0.047 1153.1 370.8 1202.9 486.8

    content = rf.readline()

    img_list = []
    img_dir  = {}

    while content:
        result_info = content.strip("\n").split("/")[1]

        im_name  = result_info.split(" ")[0]
        info_str = result_info.split(" ")[1:]

        if im_name in img_dir:
            img_dir[im_name].append(info_str)
        else:
            img_list.append(im_name)

            img_dir[im_name] = []
            img_dir[im_name].append(info_str)



        content = rf.readline()

    print("paper dt_data done.")

    # val_gt.json中，"id":1，是框的id、"image_id":1，是图片的id

    # for i=1:length(dt)
    #     bbs=dt{i};
    #     for ibb=1:size(bbs,1)
    #         ndt=ndt+1;
    #         bb=bbs(ibb,:);
    #         dt_coco(ndt).image_id=i;
    #         dt_coco(ndt).category_id=1;
    #         dt_coco(ndt).bbox=bb(1:4);
    #         dt_coco(ndt).score=bb(5);
    #     end
    # end

    dt_coco = []

    cnt = 1
    for im_idx in img_list:
        if im_idx in img_dir:
            dt_info = {}
            dt_info["image_id"]    = int(cnt)
            dt_info["category_id"] = int(1)
            for dt_idx in img_dir[im_idx]:
                bbox_ls = dt_idx[1:5]
                for box_idx in range(len(bbox_ls)):
                    bbox_ls[box_idx]  = float(bbox_ls[box_idx])

                bbox_ls[2] = round(bbox_ls[2] - bbox_ls[0])
                bbox_ls[3] = round(bbox_ls[3] - bbox_ls[1])

                dt_info["bbox"] = (bbox_ls)

                dt_info["score"] = (float(dt_idx[0]))
                #--debug
                # if (float(dt_idx[0])) == 2.0:
                #     print(im_idx)
                dt_coco.append(copy.deepcopy(dt_info))

            cnt += 1

    import json

    jsObj = json.dumps(dt_coco)

    fileObject = open('/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/evaluation/val_dt.json', 'w')
    fileObject.write(jsObj)
    fileObject.close()



for file in file_list:
    generate_json(file)
    eval_demo.run_eval_demo()