import numpy as np
import math
arr1 = np.array(
    [4.0,3.0,2.0,1.0,0.0,-1.0,-2.0,-3.0,-4.0]
)

arr2 = np.array(
    [4.5,1.5,-2.5,3.5,0.0,-3.5,2.5,-1.5,-4.5]
)

print ([bi for bi in arr1])
print(arr1, arr2)

print(arr1.reshape(9,1).dot(arr2.reshape(1,9)))

after = arr1.reshape(9,1).dot(arr2.reshape(1,9))

s = []

cnt = 0
for j in arr1:
    for i in arr2:
        tmp_sum = 0.0
        for ti in arr2:
            tmp_sum += math.exp(j*ti)

        cnt += 1
        s.append(math.exp(i*j)/tmp_sum)

        if cnt % 9 == 0:
            print(s)
            s = []


import torch
import torch.nn.functional as F

x1 = torch.Tensor([[ 18. ,   6. , -10. ,  14. ,   0.,  -14. ,  10. ,  -6.  ,-18. ],
                     [ 13.5 ,  4.5,  -7.5,  10.5,   0.,  -10.5,   7.5,  -4.5, -13.5],
                     [  9.  ,  3. ,  -5. ,   7. ,   0.,   -7. ,   5. ,  -3. ,  -9. ],
                     [  4.5 ,  1.5,  -2.5,   3.5,   0.,   -3.5,   2.5,  -1.5,  -4.5],
                     [  0.  ,  0. ,   0. ,   0. ,   0.,    0. ,   0. ,   0. ,   0. ],
                     [ -4.5 , -1.5,   2.5,  -3.5,   0.,    3.5,  -2.5,   1.5,   4.5],
                     [ -9.  , -3. ,   5. ,  -7. ,   0.,    7. ,  -5. ,   3. ,   9. ],
                     [-13.5 , -4.5,   7.5, -10.5,   0.,   10.5,  -7.5,   4.5,  13.5],
                     [-18.  , -6. ,  10. , -14. ,   0.,   14. , -10. ,   6. ,  18. ],])

# print(x1)

print(F.softmax(x1, dim=-1))

ans = F.softmax(x1, dim=-1)

print(torch.sum(ans[3][0]))
