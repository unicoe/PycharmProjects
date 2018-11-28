#_*_ coding:utf-8 _*_

import os

import cv2

from gttTestVisualization import drawGtBoxByinfo

result_path = '/home/peiyuyang/data/caltech/results/caltech/R-FCN/66_34-lamr=4.51.txt'
jpg_path = '/home/peiyuyang/data/caltech/JPEGImages'
save_path = '/home/peiyuyang/data/visualization'



def judgeDir(path): #判断路径存在，不存在则创建
    if (os.path.exists(path)):
        pass
    else:
        os.mkdir(path)



def drawBboxs(result_path,jpg_path,save_path):

    result_map_dict = {}
    result_file = open(result_path)
    result_lines = result_file.readlines()

    for result_line in result_lines:
        result_line = result_line[:-1]
        result_line = result_line.split(' ')
        file_name = result_line[0]
        result_line.pop(0)
        if not result_map_dict.has_key(file_name):
            result_map_dict[file_name] = []
            result_map_dict[file_name].append(result_line)

        else:
            result_map_dict[file_name].append(result_line)

    key_list = result_map_dict.keys()

    for file_name in key_list:  #遍历name


        ##################
        sset_path = file_name.split('/')[0]
        v_path = file_name.split('/')[1]
        frame_name = file_name.split('/')[2]
        # sset_path = file_name.split('_')[0]
        # v_path = file_name.split('_')[1]
        # frame_name = str(int(file_name.split('_')[2][1:]))


        set_path = os.path.join(save_path,sset_path)


        judgeDir(set_path)
        boxes = result_map_dict[file_name]

        #open source jpg
        img = os.path.join(os.path.join(jpg_path,sset_path,v_path,frame_name+'.jpg'))
        im = cv2.imread(img)
        jpg_save_path = os.path.join(set_path,v_path +'_'+ frame_name +'.jpg')
        mark = 0
        for box in boxes:
            score = float(box[0])
            xmin = int(float(box[1]))
            ymin = int(float(box[2]))
            xmax = int(float(box[3]))
            ymax = int(float(box[4]))
            if score >= 0.1:
                mark = 1
                cv2.rectangle(im, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)
                cv2.rectangle(im,(xmin,ymin),(xmin+20,ymin-10),(0,255,0),-1)
                cv2.putText(im, str(score)[:4], (xmin, ymin), 0, 0.3, (0, 0, 0), 1)
        #the score fall in reasonable threshold. draw results and gtbb
        if mark:
            cv2.imwrite(jpg_save_path,im)

            drawGtBoxByinfo(sset_path,v_path,frame_name,jpg_save_path)
        #the score out of reasonable threshold. draw gtbb
        else:
            drawGtBoxByinfo(sset_path,v_path,frame_name,img)


if __name__ == '__main__':
        drawBboxs(result_path,jpg_path,save_path)