lfile = []

file = open('/home/user/Downloads/save_file.txt')

while 1:
    line = file.readline()
    if line != '\n':
        lfile.append(line.replace("\n", ""))
    if not line:
        break
im_names =['00000023.jpg','00000011.jpg','00000001.jpg']
    # im_names = ['00000001.jpg', '000000011.jpg', '00000021.jpg',
    #             '00000031.jpg', '00000041.jpg']

for litme in lfile :
    for im_name in im_names:
        im_path = str(litme) + '/' + str(im_name)
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        #print 'Demo for data/demo/{}'.format(im_name)
        print im_path