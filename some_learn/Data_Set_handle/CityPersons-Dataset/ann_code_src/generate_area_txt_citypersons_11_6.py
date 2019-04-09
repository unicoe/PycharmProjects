import extract_info

ctx_dict = extract_info.extrat_info()

for k,v in ctx_dict.items():
    #print k,v
    folderName,fileName = k.split("/")

    fileInfo=[]
    obj = []
    cor_dict = {}

    fileInfo.append(folderName)
    fileInfo.append(fileName)

    area_file = "/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/ann_code_src/analyse_citypersons_data/h_list.txt"
    wf = open(area_file, "a+")

    if v:

        print(v)
        print("v info:")
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


            if int(ymax) - int(ymin) >= 20 and ratio >= 0.3:
                cor_dict = {}
                cor_dict["xmin"] = xmin
                cor_dict["ymin"] = ymin
                cor_dict["xmax"] = xmax
                cor_dict["ymax"] = ymax

                w = int(xmax)-int(xmin)
                h = int(ymax)-int(ymin)

                wf.write(str(h))
                wf.write('\n')

                rate = 0
