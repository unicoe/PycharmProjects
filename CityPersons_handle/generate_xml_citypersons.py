import unicoe_tool.mkdir as mk
import extract_info
import cv2
ctx_dict = extract_info.extrat_info()

from unicoe_tool.generate_xml import generate_xml


def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok'
        return True
    else:

        print path + 'failed!'
        return False



for k,v in ctx_dict.items():
    #print k,v
    folderName,fileName = k.split("/")
    #mk.mkdir("/home/user/PycharmProjects/CityPersons_handle/anno/" + folderName)
    #print folderName + "\n" + fileName
    root_file = "/home/user/PycharmProjects/CityPersons_handle/anno4/"

    fileInfo=[]
    obj = []
    cor_dict = {}

    fileInfo.append(folderName)
    fileInfo.append(fileName)

    #img_root = "/home/user/Disk1.8T/py-R-FCN/data/VOCdevkit0712--citypersons/VOC0712/JPEGImages"
    img_root = "/home/user/Disk1.8T/py-R-FCN/data/VOCdevkit0712(citypersons)/VOC0712/JPEGImages"
    im_path = img_root + "/" + folderName + "/" + fileName.split("\n")[0]

    #im = cv2.imread(im_path)
    if v:
        for v_i in v:
            tmpv = v_i.split(" ")
            print tmpv
            xmin = str(max(1,int(tmpv[1])))
            ymin = str(max(1,int(tmpv[2])))
            xmax = str(min(2048,int(tmpv[1])+int (tmpv[3])))
            ymax = str(min(1024,int(tmpv[2])+int (tmpv[4])))

            v_xmin = str(max(1, int(tmpv[6])))
            v_ymin = str(max(1, int(tmpv[7])))
            v_xmax = str(min(2048, int(tmpv[6]) + int(tmpv[8])))
            v_ymax = str(min(1024, int(tmpv[7]) + int(tmpv[9])))

            orginal_size = (int(ymax)-int(ymin))*(int(xmax)-int(xmin))
            v_size = (int(v_ymax)-int(v_ymin))*(int(v_xmax)-int(v_xmin))

            ratio = v_size / (orginal_size+0.0)


            if int(ymax) - int(ymin) > 50 and ratio > 0.6:
                cor_dict = {}
                cor_dict["xmin"] = xmin
                cor_dict["ymin"] = ymin
                cor_dict["xmax"] = xmax
                cor_dict["ymax"] = ymax
                obj.append(cor_dict)
                #cv2.rectangle(im, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), 1)
                #mkdir('/home/user/draw_result/citypersons/gt3/')
                #cv2.imwrite('/home/user/draw_result/citypersons/gt3/' + str(fileName.split("\n")[0]),
                #    im)
        #print obj
        generate_xml(root_file, fileInfo, obj)