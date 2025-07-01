import numpy as np
arr=np.array([[1,2,4],[4,5,6]])
arr_2=np.array([1,2])
result=arr+arr_2.reshape(2,1)
print(result)