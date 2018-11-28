def search_in_result(path1):
    sf = open(path1)

    content = sf.readline()
    tmp_list1 = []

    while content:
        cls = str(content[:-2])
        tmp_list1.append(cls)
        content = sf.readline()
    sf.close()
    return tmp_list1

def des_search(path):
    df = open(path)
    content1 = df.readline()
    tmp_dict2 = {}

    while content1:
        #print content1
        det = content1.replace("\n", "").split(",")
        cls1 = det[0]
        bbox = []
        for i in xrange(1, len(det), 1):
            if det[i] is not '':
                bbox.append(det[i].strip())

        if cls1 in tmp_dict2:
            tmp_dict2[cls1].append(bbox)
        else:
            tmp_dict2[cls1] = [bbox]

        #break

        content1 = df.readline()
    df.close()
    return tmp_dict2
    # for key_ in tmp_dict2:
    #     print key_,tmp_dict2[key_]


res_list = search_in_result("/home/user/PycharmProjects/MissRate_FPPI_plot/out.txt")

gt_dict = des_search("/home/user/PycharmProjects/MissRate_FPPI_plot/reasonable_ground_truth.txt")

fw = open("/home/user/PycharmProjects/MissRate_FPPI_plot/result_pair1.txt", "w")

# print res_list
# print gt_dict

import os
#os.remove("/home/user/PycharmProjects/MissRate_FPPI_plot/result_pair1.txt")

for res_index in res_list:
    if res_index in gt_dict:
        #print res_index
        fw.write(res_index)
        fw.write("-")
        for b_index in gt_dict[res_index]:
            #print b_index
            for bb_index in b_index:
                num  = bb_index.split(" ")
                for num_index in num:
                    tttmp = int(num_index.split(".")[0])
                    if tttmp == 0:
                        tttmp = 1
                    fw.write(str(tttmp))
                    if num_index is not num[-1]:
                        fw.write(",")
                if bb_index is not b_index[-1]:
                    fw.write(";")
            if b_index is not gt_dict[res_index][-1]:
                fw.write(",")
    fw.write("\n")

fw.close()
