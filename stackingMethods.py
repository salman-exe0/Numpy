import numpy as np
a1=np.arange(10)
npArray= np.arange(0,12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)
#horizontal stacking
print(np.hstack((npArray, npArray)))
#vertical stacking
print(np.vstack((npArray, npArray)))
#depth-wise stacking
print(np.dstack((a3, a3)))