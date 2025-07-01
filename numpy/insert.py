'''
np.insert(array, index , value, axis=none)
array-
index-
value-
axis= 0-rows wise
1-column wise
'''

# import numpy as np

# arr=np.array([1,2,3,4,5,6,7,8,])
# new_arr=np.insert(arr, 2 ,100)
# print(new_arr)

'''insertion in 2d'''

import numpy as np

arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d)
new_arr=np.insert(arr_2d, 1 ,[7,8,9], axis=None)
print(new_arr)