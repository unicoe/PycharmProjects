% Copyright (c) 2016 The Regents of the University of California
% see mscnn/LICENSE for details
% Written by Zhaowei Cai [zwcai-at-ucsd.edu]
% Please email me if you find bugs, or have suggestions or questions!

% clear and close everything
clear all; close all;
root_dir = '/home/user/Disk1.8T/data_set/KITTI/';
addpath([root_dir 'devkit_object/matlab']);

data_set = 'val'; % or 'test'
if (strcmp(data_set,'test')) 
  is_gt_available = 0;
else
  is_gt_available = 1;
end
gt_dir = [root_dir '/training/label_2'];

% get the list for evaluation original code for val/test
%list_dir = ['../../data/kitti/ImageSets/' data_set '.txt'];
list_dir = ['/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/mscnn/ImageSets/val.txt'];
test_id = load(list_dir);
nimages = length(test_id);

%load detection results
% car_dets_path = '../kitti_car/detections/kitti_7 s_576_2x_25k_val_car.txt';
% if (exist(car_dets_path))
%   car_dets = load(car_dets_path);
% else
%   car_dets = zeros(0,6);
% end

fileID = fopen('result.txt','w');

str = {

'/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/nms_handle/det_result/12_1/2018_nms_6_2018_11_30_Fri_12_58_17_det_test_person.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/nms_handle/det_result/12_1/2018_nms_55_2018_11_30_Fri_12_58_17_det_test_person.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/nms_handle/det_result/12_1/2018_nms_56_2018_11_30_Fri_12_58_17_det_test_person.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/nms_handle/det_result/12_1/2018_nms_57_2018_11_30_Fri_12_58_17_det_test_person.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/nms_handle/det_result/12_1/2018_nms_58_2018_11_30_Fri_12_58_17_det_test_person.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/nms_handle/det_result/12_1/2018_nms_59_2018_11_30_Fri_12_58_17_det_test_person.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/nms_handle/det_result/12_1/2018_nms_61_2018_11_30_Fri_12_58_17_det_test_person.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/nms_handle/det_result/12_1/2018_nms_62_2018_11_30_Fri_12_58_17_det_test_person.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/nms_handle/det_result/12_1/2018_nms_63_2018_11_30_Fri_12_58_17_det_test_person.txt',
'/home/user/PycharmProjects/some_learn/Data_Set_handle/KITTI-Dataset/src/nms_handle/det_result/12_1/2018_nms_64_2018_11_30_Fri_12_58_17_det_test_person.txt',

}

det_paths = cell2struct(str',{'path'});

tic;%tic1
t1=clock;
tic ;%tic2
for i=1:100
    ped_path = det_paths(i).path;
    
    file_name = ped_path(105:142)
    
    ped_dets_path = ped_path;

    if (exist(ped_dets_path))
      ped_dets = load(ped_dets_path);
    else
      ped_dets = zeros(0,6);
    end
    % cyc_dets_path = '../kitti_ped_cyc/detections/kitti_7s_576_2x_25k_val_cyc.txt';
    % if (exist(cyc_dets_path))
    %   cyc_dets = load(cyc_dets_path);
    % else
    %   cyc_dets = zeros(0,6);
    % end

    score_scale = 1000; 
    comp_id = 'test_val';
    result_dir = [data_set '/' comp_id '/'];
    save_dir = [result_dir 'data/'];
    if (~exist(save_dir)), mkdir(save_dir); end

    for i = 1:nimages
        if (mod(i,100)==0), fprintf('idx: %i / %i\n',i,nimages); end
        objects=[]; num = 0;

        % car
    %     idx = find(car_dets(:,1)== test_id(i));
    %     bbs = car_dets(idx,2:6);
    %     bbs(:,3:4) = bbs(:,1:2)+bbs(:,3:4);
    %     for j = 1:size(bbs,1)
    %       num = num+1;
    %       objects(num).type = 'Car'; objects(num).score = bbs(j,5)*score_scale;
    %       objects(num).x1 = bbs(j,1); objects(num).y1 = bbs(j,2);
    %       objects(num).x2 = bbs(j,3); objects(num).y2 = bbs(j,4);
    %     end

        % pedestrian
        idx = find(ped_dets(:,1)==test_id(i));
        bbs = ped_dets(idx,2:6);
    %    bbs(:,4:5) = bbs(:,2:3)+bbs(:,4:5);
        for j = 1:size(bbs,1)
          num = num+1;
          objects(num).type = 'Pedestrian'; objects(num).score = bbs(j,1)*score_scale;
          objects(num).x1 = bbs(j,2); objects(num).y1 = bbs(j,3);
          objects(num).x2 = bbs(j,4); objects(num).y2 = bbs(j,5);
        end

        % cyclist
    %     idx = find(cyc_dets(:,1)==test_id(i));
    %     bbs = cyc_dets(idx,2:6);
    %     bbs(:,3:4) = bbs(:,1:2)+bbs(:,3:4);
    %     for j = 1:size(bbs,1)
    %       num = num+1;
    %       objects(num).type = 'Cyclist'; objects(num).score = bbs(j,5)*score_scale;
    %       objects(num).x1 = bbs(j,1); objects(num).y1 = bbs(j,2);
    %       objects(num).x2 = bbs(j,3); objects(num).y2 = bbs(j,4);
    %     end

        img_idx = test_id(i);
        writeLabels(objects,save_dir,img_idx);
    end
    
    if (is_gt_available)
      plot_dir = [result_dir 'plot/'];
      % input arguments [gt_dir, result_dir, list_dir];
      command_line = sprintf('eval/evaluate_object %s %s %s', gt_dir,result_dir,list_dir);
      system(command_line);
      plot_set = dir([plot_dir '*.txt']);
      for i = 1:length(plot_set)
        results = load([plot_dir plot_set(i).name]);
        x = results(:,1); 
        easy_legend = sprintf('%s %.02f','Easy',100*mean(results(1:4:41,2)));
        easy = 100*mean(results(1:4:41,2));
        
        moderate_legend = sprintf('%s %.02f','Moderate',100*mean(results(1:4:41,3)));
        moderate = 100*mean(results(1:4:41,3));
        
        hard_legend = sprintf('%s %.02f','Hard',100*mean(results(1:4:41,4)));
        hard  = 100*mean(results(1:4:41,4));
        
      end
      
      fprintf(fileID, file_name);
      fprintf(fileID, '\n');
      fprintf(fileID,easy_legend);
      fprintf(fileID, '\n');
      fprintf(fileID,moderate_legend);
      fprintf(fileID, '\n');
      fprintf(fileID,hard_legend);
      fprintf(fileID, '\n');
      fprintf(fileID, '\n');
      
    end
   
    disp(['toc计算第',num2str(i),'次循环运行时间：',num2str(toc)]);
end

fclose(fileID);

