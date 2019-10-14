readfile = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/new10x_gt_info_20_zss_vis.txt", "r")

context = readfile.readlines()

wf = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/PascalVOC-Dataset/SegmentationClass/lst/new10x_gt_info_20_zss_vis_img_list.txt", "w")

for i_info in context:
    ilist = i_info.split(" ")[0]
    wf.write(ilist)
    wf.write("\n")

wf.close()
