import os
import matplotlib.pyplot as plt
import cv2

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + 'ok')
        return True
    else:
        print(path + 'failed!')
        return False

def get_result_dict(cur_path):
    cur_files = os.listdir(cur_path)
    res_dict_file = {}
    for i_file in ['MOT17-01.txt','MOT17-03.txt','MOT17-06.txt','MOT17-07.txt','MOT17-08.txt','MOT17-12.txt','MOT17-14.txt',]:
        read_info = open(os.path.join(cur_path,i_file))
        res_dict = {}
        for i_info in read_info.readlines():
            img_info = i_info.strip("\n").split(",")

            img_name = img_info[0]
            img_details = img_info[1:]

            if img_name in res_dict:
                res_dict[img_name].append(img_details)
            else:
                res_dict[img_name] = [img_details]
        res_dict_file[i_file] = res_dict
    return res_dict_file


def handle_result(res_dict, cur_path):

    cur_det_resutl = cur_path.strip("\n").split("/")[-1]

    for i_file, i_details in res_dict.items():
        # print(i_file, i_details)

        for i_img, i_info in i_details.items():

            pre_zero = ""
            for izero in range(6 - len(i_img)):
                pre_zero += '0'

            im_name = pre_zero + i_img + '.jpg'

            cur_img_path = os.path.join("/home/user/Disk1.8T/data_set/MOT17Det/test",
                                        i_file.split('.')[0],
                                        im_name)
            Debug = False
            if Debug:
                cur_img = plt.imread(cur_img_path)
                plt.imshow(cur_img)
                plt.show()

            cur_img = cv2.imread(cur_img_path)

            for i_bbox in i_info:
                x1 = int(float(i_bbox[1]))
                y1 = int(float(i_bbox[2]))
                x2 = int(float(i_bbox[1]) + float(i_bbox[3]))
                y2 = int(float(i_bbox[2]) + float(i_bbox[4]))

                score = float(i_bbox[5])

                cv2.rectangle(cur_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # cv2.rectangle(cur_img, (x1, y1), (x1 + 20, y1 - 10), (0, 255, 0), -1)
                cv2.putText(cur_img, str(score)[:4], (x1, y1), 0, 0.9, (255, 0, 0), 2)

            mkdir('/home/user/Disk1.8T/draw_result/MOT2017Det/'+cur_det_resutl+"/"+i_file.split('.')[0])
            cv2.imwrite('/home/user/Disk1.8T/draw_result/MOT2017Det/'+cur_det_resutl+"/"+i_file.split('.')[0]+"/"
                        +im_name, cur_img)
    pass


def handle_result1(cur_path):
    cur_files = os.listdir(cur_path)
    for i_file in ['MOT17-01.txt','MOT17-03.txt','MOT17-06.txt','MOT17-07.txt','MOT17-08.txt','MOT17-12.txt','MOT17-14.txt',]:
        read_info = open(os.path.join(cur_path,i_file))
        for i_info in read_info.readlines():
            """
            375,-1,1222,31.4,61,118.8,1
            1,-1,122.7,194.6,24.8,66,1
            """
            img_info = i_info.strip("\n").split(",")

            pre_zero = ""
            for izero in range(6 - len(img_info[0])):
                pre_zero += '0'

            im_name = pre_zero + img_info[0] + '.jpg'

            cur_img_path = os.path.join("/home/user/Disk1.8T/data_set/MOT17Det/test",
                                        i_file.split('.')[0],
                                        im_name)
            Debug = False
            if Debug:
                cur_img = plt.imread(cur_img_path)
                plt.imshow(cur_img)
                plt.show()

            cur_img = cv2.imread(cur_img_path)
            x1 = int(float(img_info[2]))
            y1 = int(float(img_info[3]))
            x2 = int(float(img_info[2])+float(img_info[4]))
            y2 = int(float(img_info[3])+float(img_info[5]))

            score = float(img_info[6])

            cv2.rectangle(cur_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            #cv2.rectangle(cur_img, (x1, y1), (x1 + 20, y1 - 10), (0, 255, 0), -1)
            cv2.putText(cur_img, str(score)[:4], (x1, y1), 0, 0.9, (255, 0, 0), 2)

        # if flag == 1:
        #     img_cnt = img_cnt + 1
        #
        #     mkdir('/home/user/Disk1.8T/draw_result/2019_01_18_Fri_00_54_51/' + folder_name + '/' + str(
        #         inDict[-3] + '/' + inDict[-2]))
        #     cv2.imwrite('/home/user/Disk1.8T/draw_result/2019_01_18_Fri_00_54_51/' + folder_name + '/' +
        #                 str(inDict[-3] + '/' + inDict[-2]) + '/' + bot + ".jpg",
        #                 im)

            plt.imshow(cur_img)
            plt.show()

            print i_info
            break
    pass

result_path = [
    '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/src/vis_MOT_benchmark/frcnn',
    '/home/user/PycharmProjects/some_learn/Data_Set_handle/MOT17Det/src/vis_MOT_benchmark/sdp'
]

for cur_path in result_path:
    res_dict = get_result_dict(cur_path)
    handle_result(res_dict, cur_path)




