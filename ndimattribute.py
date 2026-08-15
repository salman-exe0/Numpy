# tell us dimesions of an array
# dtype helps us to create an array of specific data type
import numpy as np
n1=np.arange(6,dtype=int)
print(n1.ndim)
n2=np.arange(10).reshape(2,5)
print(n2.ndim)
n3=np.arange(12).reshape(2,3,2)
print(n3.ndim)