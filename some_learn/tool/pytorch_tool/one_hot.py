
import torch


def one_hot_embedding(labels, num_classes):
    '''Embedding labels to one-hot.

    Args:
      labels: (LongTensor) class labels, sized [N,].
      num_classes: (int) number of classes.

    Returns:
      (tensor) encoded labels, sized [N,#classes].
    '''
    y = torch.eye(num_classes, device='cpu')  # [D,D]
    return y[labels]  # [N,D]

if __name__=='__main__':
    labels= [1,2,3,4,4,5,6,7,5,4,5,3,3,4,2,2,2,3,3,4,2,1,3,4,]
    num_classes=10
    one_hot_vector=one_hot_embedding(labels,num_classes)
    print(one_hot_vector)
    #tensor([0., 0., 1., 0., 0., 0., 0., 0., 0., 0.])