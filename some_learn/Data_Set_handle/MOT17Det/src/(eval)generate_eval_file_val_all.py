"""
MOT17-11/000479 0.1943 1198.38 -64.15 1456.84 516.38
MOT17-11/000479 0.1932 1058.7 249.71 1169.88 663.98
"""
def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        # print path + 'ok'
        return True
    else:

        # print path + 'failed!'
        return False

def generate_eval_file(path):

    result_file = open(path, "r")
    conxt = result_file.readlines()

    save_file_name = path.split("/")[-1].split(".")[0]

    flag = 0
    flag_02 = 0
    flag_04 = 0
    flag_05 = 0
    flag_09 = 0
    flag_10 = 0
    flag_11 = 0
    flag_13 = 0


    for item in conxt:
        line_info = item.strip("\n").split(" ")

        name1 = line_info[0].split("/")[0]
        name2 = line_info[0].split("/")[1]

        mkdir( "/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                    + save_file_name)
        save_path = "/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                    + save_file_name + "/" + name1 + ".txt"

        """
        1,-1,1716.5,364.89,128.96,388.88,2.0587,-1,-1,-1
        1,-1,1286.3,461.78,59.629,180.89,0.43718,-1,-1,-1
        """
        with open(save_path, "aw") as save_w:
            save_w.write(str(int(name2)))
            save_w.write(",-1")
            save_w.write(","+str(line_info[2]))
            save_w.write(","+str(line_info[3]))
            save_w.write(","+str(float(line_info[4]) - float(line_info[2])))
            save_w.write(","+str(float(line_info[5]) - float(line_info[3])))
            save_w.write(","+str(line_info[1]))
            save_w.write(",-1")
            save_w.write(",-1")
            save_w.write(",-1")
            save_w.write("\n")
        if name1 == 'MOT17-02' and flag_02 == 0:
            print("'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                  + save_file_name + "/" + name1 + ".txt',")

            flag_02 += 1
        if name1 == 'MOT17-04' and flag_04 == 0:
            print("'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                  + save_file_name + "/" + name1 + ".txt',")
            flag_04 += 1
        if name1 == 'MOT17-05' and flag_05 == 0:
            print("'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                  + save_file_name + "/" + name1 + ".txt',")
            flag_05 += 1

        if name1 == 'MOT17-09' and flag_09 == 0:
            print("'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                  + save_file_name + "/" + name1 + ".txt',")

            flag_09 += 1
        if name1 == 'MOT17-10' and flag_10 == 0:
            print("'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                  + save_file_name + "/" + name1 + ".txt',")
            flag_10 += 1
        if name1 == 'MOT17-11' and flag_11 == 0:
            print("'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                  + save_file_name + "/" + name1 + ".txt',")
            flag_11 += 1
        if name1 == 'MOT17-13' and flag_13 == 0:
            print("'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                  + save_file_name + "/" + name1 + ".txt',")
            flag_13 += 1
        pass


res_ls = [

# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_2_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_3_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_4_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_5_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_15_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_16_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_17_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_18_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_19_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_21_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_22_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_23_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_24_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_25_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_26_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_27_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_28_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_29_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_31_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_32_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_33_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_34_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_35_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_36_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_37_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_38_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_39_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_41_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_42_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_43_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_44_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_45_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_46_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_47_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_48_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_04nms_49_AD-SSD_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_2_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_3_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_4_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_5_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_15_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_16_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_17_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_18_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_19_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_21_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_22_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_23_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_24_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_25_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_26_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_27_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_28_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_29_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_31_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_32_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_33_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_34_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_35_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_36_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_37_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_38_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_39_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_41_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_42_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_43_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_44_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_45_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_46_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_47_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_48_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0213nms_49_AD-SSD_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_2_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_3_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_4_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_5_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_15_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_16_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_17_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_18_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_19_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_21_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_22_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_23_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_24_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_25_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_26_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_27_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_28_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_29_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_31_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_32_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_33_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_34_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_35_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_36_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_37_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_38_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_39_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_41_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_42_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_43_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_44_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_45_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_46_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_47_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_48_AD-SSD_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_0509nms_49_AD-SSD_0509.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_2_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_3_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_4_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_5_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_15_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_16_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_17_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_18_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_19_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_21_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_22_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_23_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_24_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_25_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_26_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_27_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_28_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_29_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_31_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_32_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_33_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_34_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_35_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_36_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_37_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_38_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_39_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_41_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_42_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_43_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_44_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_45_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_46_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_47_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_48_AD-SSD_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/1/AD-SSD_1011nms_49_AD-SSD_1011.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_2_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_3_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_4_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_5_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_15_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_16_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_17_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_18_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_19_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_21_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_22_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_23_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_24_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_25_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_26_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_27_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_28_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_29_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_31_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_32_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_33_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_34_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_35_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_36_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_37_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_38_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_39_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_41_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_42_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_43_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_44_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_45_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_46_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_47_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_48_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_04nms_49_SSD_SEG_VIS_04.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_2_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_3_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_4_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_5_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_15_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_16_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_17_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_18_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_19_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_21_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_22_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_23_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_24_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_25_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_26_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_27_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_28_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_29_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_31_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_32_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_33_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_34_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_35_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_36_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_37_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_38_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_39_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_41_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_42_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_43_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_44_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_45_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_46_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_47_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_48_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0213nms_49_SSD_SEG_VIS_0213.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_2_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_3_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_4_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_5_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_15_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_16_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_17_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_18_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_19_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_21_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_22_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_23_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_24_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_25_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_26_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_27_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_28_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_29_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_31_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_32_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_33_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_34_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_35_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_36_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_37_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_38_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_39_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_41_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_42_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_43_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_44_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_45_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_46_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_47_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_48_SSD_SEG_VIS_0509.txt',
# '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_0509nms_49_SSD_SEG_VIS_0509.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_2_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_3_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_4_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_5_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_15_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_16_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_17_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_18_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_19_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_21_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_22_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_23_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_24_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_25_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_26_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_27_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_28_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_29_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_31_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_32_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_33_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_34_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_35_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_36_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_37_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_38_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_39_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_41_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_42_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_43_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_44_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_45_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_46_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_47_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_48_SSD_SEG_VIS_1011.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_det/2/SSD_SEG_VIS_1011nms_49_SSD_SEG_VIS_1011.txt',

]

for i_path in res_ls:
    generate_eval_file(i_path)
