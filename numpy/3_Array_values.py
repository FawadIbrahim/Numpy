"""#zeros"""
import numpy as np
# zero=np.zeros(3)
# print(zero)

"""#ones"""
# one=np.ones([2,3])
# print(one)

"""#default values"""

# default=np.full([4,3],5)
# print(default)

"""#sequence of numbers"""
# seq=np.arange(1,20,3)
# print(seq)

"""identity Matrices"""
# id_matric=np.eye(5)
# print(id_matric)

'''Shape of an array'''

# arr_2d=np.array([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]])
# print(arr_2d.shape)
# print(arr_2d.size)

'''No of dimensions'''


numpy_list2=np.array([1,2,3,4,5])
numpy_list=np.array([[1,2,3],[4,5,6]])
numpy_list3=np.array([[[1,2,3,],[4,5,6],[7,8,9]]])

#type conversion
num_ty= numpy_list3.astype(float)
print(numpy_list3)

print(num_ty.dtype)

# print(numpy_list2.ndim)
# print(numpy_list.ndim)
# print(numpy_list3.ndim)