'''
vertically
horizantally

vstack -> row wise
hstack -> column wise
'''


import numpy as np

arr_1=np.array([1,2,3,])
arr_2=np.array([5,6,7])
print(np.vstack((arr_1,arr_2)))
print(np.hstack((arr_1,arr_2)))