import numpy as np
a1=np.arange(10)
npArray= np.arange(0,12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)
for i in a1:
    print(i)

for i in npArray:
    print(i)


for i in a3:
    print(i)


for i in np.nditer(npArray):
    print(i)
for x in np.nditer(a3):
    print(x)