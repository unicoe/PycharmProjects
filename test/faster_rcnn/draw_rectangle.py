
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import os, sys, cv2
import argparse
import linecache

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

def demo(folder_name, image_name):
    """Detect object classes in an image using pre-computed object proposals."""

    # Load the demo image
    folder_path = '/home/user/Downloads/vot2015/' + folder_name
    im_file = os.path.join('/home/user/Downloads','vot2015',folder_name, image_name)
    #print("%s", im_file)

    iima_name = image_name.split('.')[0]
    #print iima_name
    iima_num = int(iima_name)

    #print iima_num
    ground_path = folder_path + '/groundtruth.txt'
    str1 = linecache.getline(ground_path, iima_num)
    #print str1
    str1 = str1.replace('\n', '')
    #print str1
    l = str1.split(',')
    #print l
    im = cv2.imread(im_file)
    im = im[:,:,(2,1,0)]
    fig,ax = plt.subplots(figsize=(12,12))
    ax.imshow(im, aspect='equal')

    x = []
    y = []
    indx = 0
    for j in xrange(0, 8, 2):
        x.append(float(l[0 + j]))
        y.append(float(l[1 + j]))
        T = np.arctan2(x[indx], y[indx])
        plt.scatter(x[indx], y[indx], c=T, s=25, alpha=0.4, marker='o')
        ax.add_patch(
            plt.Rectangle((min(x), min(y)),
                          max(x) - min(x),
                          max(y) - min(y),
                          fill=False,
                          edgecolor='red', linewidth=3.5)
        )
        indx += 1
        plt.axis('off')
        plt.tight_layout()
        plt.draw()
        mkdir('/home/user/tmp7/' + folder_name)

        plt.savefig('/home/user/tmp7/' +folder_name+ '/' +image_name)


lfile = []

file = open('/home/user/Downloads/save_file.txt')
# file1 = open('')
while 1:
    line = file.readline()
    if line != '\n':
        lfile.append(line.replace("\n", ""))
    if not line:
        break

print lfile

im_names = ['00000001.jpg', '00000011.jpg', '00000021.jpg',
            '00000031.jpg', '00000041.jpg']

for litme in lfile :
    file_log = open('/home/user/out_tmp/file_log.txt','a')
    file_log.write(litme)
    file_log.write('\n')
    file_log.close()
    print litme
    for im_name in im_names:
        #im_path = str(litme) + '/' + str(im_name)
        #print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        #print 'Demo for data/demo/{}'.format(im_name)
        # try:
        demo(str(litme), im_name)
        # except Exception:
        #     print 'ERROR'
#plt.show()