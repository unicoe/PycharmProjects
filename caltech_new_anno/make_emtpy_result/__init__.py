from unicoe_tool import mkdir
import os
cu_path = os.path.dirname(__file__)
print cu_path
for i in xrange(10, 20):
    path_txt = cu_path + '/res/V0' + str(i) + '.txt'
    mkdir.mkdir(cu_path + '/res/')
    fw  = open(path_txt, "w")

    fw.close()