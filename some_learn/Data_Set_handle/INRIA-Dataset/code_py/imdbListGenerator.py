import os

train_lst_file_path = '/home/peiyuyang/data/INRIA/Train/pos.lst'
test_lst_file_path = '/home/peiyuyang/data/INRIA/Test/pos.lst'
save_path = '/home/peiyuyang/data/INRIA/List/imdb'

train_lst_file = open(train_lst_file_path)
train_lst = train_lst_file.readlines()
for lst in train_lst:
    content = lst.split('/')[2].split('.')[0]+'\n'
    lst_file = open(os.path.join(save_path,'inria_train.txt'),'a')
    lst_file.write(content)

test_lst_file = open(test_lst_file_path)
test_lst = test_lst_file.readlines()
for lst in test_lst:
    content = lst.split('/')[2].split('.')[0]+'\n'
    lst_file = open(os.path.join(save_path,'inria_test.txt'),'a')
    lst_file.write(content)
