 from coco import COCO
from eval_MR_multisetup import COCOeval
import time
def run_eval_demo():
    annType = 'bbox'      #specify type here
    print 'Running demo for *%s* results.'%(annType)

    #initialize COCO ground truth api
    annFile = '/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/evaluation/val_gt.json'
    # initialize COCO detections api
    resFile = '/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/evaluation/val_dt.json'

    time_tup = time.localtime(time.time())
    format_time = '%Y_%m_%d_%a_%H_%M_%S'
    cur_time = time.strftime(format_time, time_tup)
    ## running evaluation
    res_file = open("/home/user/PycharmProjects/some_learn/Data_Set_handle/CityPersons-Dataset/evaluation/results" +str(cur_time)+".txt", "w")
    for id_setup in range(0,4):
        cocoGt = COCO(annFile)
        cocoDt = cocoGt.loadRes(resFile)
        imgIds = sorted(cocoGt.getImgIds())
        cocoEval = COCOeval(cocoGt,cocoDt,annType)
        cocoEval.params.imgIds  = imgIds
        cocoEval.evaluate(id_setup)
        cocoEval.accumulate()
        cocoEval.summarize(id_setup,res_file)

    res_file.close()

