# tell us dimesions of an array
# dtype helps us to create an array of specific data type
import numpy as np
n1=np.arange(6,dtype=int)
print(n1.ndim)
n2=np.arange(10, dtype=float).reshape(2,5)
print(n2.ndim)
n3=np.arange(12).reshape(2,3,2)
print(n3.ndim)
print( n3)
#shape attribute
print(n1.shape)
print(n2.shape)
print(n3.shape)
#size
print(n1.size)
#itemSize
print(n2.itemsize)
print(n1.itemsize)
#dtype
print(n1.dtype)
print(n2.dtype)