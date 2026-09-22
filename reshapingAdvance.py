import numpy as np
a1=np.arange(10)
npArray= np.arange(0,12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)
#transpose
print(npArray.transpose())
print(a1.T)
#Ravel convert multi-dimensional array to 1D array
print(npArray.ravel())
print(a3.ravel())

