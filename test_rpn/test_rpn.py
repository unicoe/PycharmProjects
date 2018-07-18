import sys

caffe_root="/home/user/unicoe_experiments/py-faster-rcnn/caffe-fast-rcnn"

sys.path.append(caffe_root+"python")

import caffe

caffe.set_mode_gpu()

from pylab import *

model_def = "deploy.prototxt"
model_weights = "/home/user/unicoe_experiments/py-faster-rcnn/output/VGG_RPN/model/voc_2007_trainval/vgg16_rpn_iter_20000.caffemodel"

net = caffe.Net(model_def, model_weights, caffe.TEST)

def convert_mean(binMean, npyMean):
     blob = caffe.proto.caffe_pb2.BlobProto()
     bin_mean = open(binMean, "rb").read()
     blob.ParseFromString(bin_mean)
     arr = np.array(caffe.io.blobproto_to_array(blob))
     npy_mean = arr[0]
     np.save(npyMean, npy_mean)

binMean = ""
npyMean = ""
convert_mean(binMean, npyMean)

