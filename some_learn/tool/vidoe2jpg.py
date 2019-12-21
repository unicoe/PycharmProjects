# -*- coding: utf-8 -*-
import os
import cv2
from PIL import Image

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + 'create done.')
        return True
    else:
        print(path + 'path already exists.')
        return False

def unlock_movie(path):

  save_path = path[:-4]
  mkdir(save_path)
  cap = cv2.VideoCapture(path)
  suc = cap.isOpened()  # 是否成功打开
  frame_count = 0
  while suc:
      frame_count += 1
      suc, frame = cap.read()
      params = []
      params.append(2)  # params.append(1)
      cv2.imwrite(save_path+'/%d.jpg' % frame_count, frame, params)

  cap.release()
  print('unlock movie: ', frame_count)


def  jpg_to_video(path, fps):
  """ 将图片合成视频. path: 视频路径，fps: 帧率 """
  fourcc = cv2.VideoWriter_fourcc(*"MJPG")
  images = os.listdir('frames')#os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
  image = Image.open('frames/' + images[0])
  vw = cv2.VideoWriter(path, fourcc, fps, image.size)

  os.chdir('frames')
  for i in range(len(images)):
    # Image.open(str(image)+'.jpg').convert("RGB").save(str(image)+'.jpg')
    jpgfile = str(i + 1) + '.jpg'
    try:
        new_frame = cv2.imread(jpgfile)
        vw.write(new_frame)
    except Exception as exc:
        print(jpgfile, exc)
  vw.release()
  print(path, 'Synthetic success!')


if __name__ == '__main__':

  path_ls = [
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/11/MOT17-02-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/11/MOT17-04-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/11/MOT17-05-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/11/MOT17-09-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/11/MOT17-10-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/11/MOT17-11-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/11/MOT17-13-SSD.avi',

      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/12/MOT17-02-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/12/MOT17-04-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/12/MOT17-05-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/12/MOT17-09-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/12/MOT17-10-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/12/MOT17-11-SSD.avi',
      '/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/12/MOT17-13-SSD.avi',
  ]
  PATH_TO_MOVIES = os.path.join('/home/user/Disk1.8T/end_ex/mot_pytorch_ssd_2_4/1', 'MOT17-02-SSD.avi')
  #PATH_TO_OUTCOME = os.path.join('detection_movies', 'beautiful_mind2_detection_1.avi')
  for i in path_ls:
    unlock_movie(i)  # 视频转图片
  #jpg_to_video(PATH_TO_OUTCOME, 24)  # 图片转视频