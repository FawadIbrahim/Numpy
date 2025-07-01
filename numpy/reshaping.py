'''
reshape(rows, columns) that specify new shape
you can only reshape when dimensions are match
'''

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,])
reshape_arr=arr.reshape(4,2)
print(reshape_arr)