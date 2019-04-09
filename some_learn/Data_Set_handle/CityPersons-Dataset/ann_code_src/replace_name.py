rf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/ann_code_src/ann_file/out_val.txt")

name_ls = []

name_info = rf.readline()

while name_info:

    tmp_info = name_info.strip("\n")
    name_ls.append(tmp_info)

    name_info = rf.readline()


res_ls = [

#'/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_31_56_val_det.txt',
'/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_33_45_val_det.txt',
'/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_35_35_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_37_25_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_39_15_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_41_07_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_43_00_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_44_53_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_46_45_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_48_38_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_50_31_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_52_24_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_54_18_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_56_11_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_58_05_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_11_59_58_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_01_52_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_03_45_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_05_40_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_07_34_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_09_28_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_11_23_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_13_18_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_15_14_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_17_09_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_19_05_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_21_00_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_22_56_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_24_51_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_26_48_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_28_44_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_30_40_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_32_37_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_34_34_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_36_31_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_38_28_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_40_25_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_42_23_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_44_20_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_46_18_val_det.txt',
# '/home/user/Disk1.8T/unicoe/ALFNet/output/valresults/resnet50/1step/2019_04_08_Mon_12_48_16_val_det.txt',

]

for idx in res_ls:
    rf1 = open(idx)
    wf1 = open(idx+'.re', "w")
    context = rf1.readline()
    while context:
        info = context.strip("\n").split(" ")
        tmp_name = name_ls[int(float(info[0]))-1]
        wf1.write(tmp_name)
        wf1.write(" ")
        wf1.write(info[5])
        wf1.write(" ")
        wf1.write(info[1])
        wf1.write(" ")
        wf1.write(info[2])
        wf1.write(" ")
        wf1.write(str(float(info[1])+float(info[3])))
        wf1.write(" ")
        wf1.write(str(float(info[2])+float(info[4])))

        wf1.write("\n")

        context = rf1.readline()
    wf1.close()
    rf1.close()