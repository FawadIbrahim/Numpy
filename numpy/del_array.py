# import numpy as np

# arr=np.array([1,2,3,4,5,6,7,8,])
# new_arr=np.delete(arr,2)
# print(new_arr)

'''for 2d array'''
import numpy as np

arr_2d=np.array([[1,2,3],[4,5,6]])
# print(arr_2d)
new_arr=np.delete(arr_2d,0, axis=1)
print(new_arr)