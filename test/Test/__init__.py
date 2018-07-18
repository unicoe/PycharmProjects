# import numpy as np
# print 'test'
#
# ans = 0
# test = np.array([1,2,3,4,5])
# ans =ans + sum(~test)
#
# print ans


str = {"1_test":"123","2_test":"234","3":"123"}
test = [k for k in str.keys() if "_test" in k]
print test


for t in test:
    print t.replace('_test', '')
    print t
print test