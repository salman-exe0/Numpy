import numpy as np
a1=np.arange(10)
npArray= np.arange(0,12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)
print(np.hsplit(npArray, 2))
print(np.vsplit(npArray, 3))