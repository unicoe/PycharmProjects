fr = open("/home/user/PycharmProjects/caltech_new_anno/SSD_pictures_list/result_focal_loss120000.txt")
fw = open("/home/user/PycharmProjects/caltech_new_anno/SSD_pictures_list/handle_result_focal_loss120000.txt", "w")
get_content = fr.readline()

while get_content:
    content = get_content.split(" ")
    id = content[0][-21:-4]
    fw.write(id+" ")
    fw.write(content[2]+" ")
    fw.write(content[3] + " ")
    fw.write(content[4] + " ")
    fw.write(content[5] + " ")
    fw.write(content[6])
    get_content = fr.readline()