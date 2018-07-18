fr = open("/home/user/PycharmProjects/caltech_new_anno/SSD_pictures_list/test_name_size.txt")
fw = open("/home/user/PycharmProjects/caltech_new_anno/SSD_pictures_list/test1.txt", "w")
get_content = fr.readline()



while get_content:
    content = get_content.split(" ")[0]

    fw.write("/home/user/unicoe_experiments/SSD/cp_SSD/data/VOCdevkit/VOC2007/JPEGImages/" +content + ".jpg\n")
    get_content = fr.readline()

print "done"