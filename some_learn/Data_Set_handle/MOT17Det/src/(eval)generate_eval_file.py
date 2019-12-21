#--coding:utf-8--
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
    flag_10 = 0
    for item in conxt:
        line_info = item.strip("\n").split(" ")

        name1 = line_info[0].split("/")[0]
        name2 = line_info[0].split("/")[1]

        # 生成临时文件
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
        if name1 == 'MOT17-10' and flag == 0:
            print("'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                            + save_file_name + "/" + name1 + ".txt',")
            flag += 1
            flag_10 = 1
        if name1 == 'MOT17-11' and flag_10 == 1 :
            print("'/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/eval_file/" \
                            + save_file_name + "/" + name1 + ".txt',")
            flag_10 +=1

    pass


res_ls = [
    '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_set/AD-SSD.txt',
    '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/det_result/val_set/SSD+SEG+VIS.txt',
]

for i_path in res_ls:
    generate_eval_file(i_path)
