import numpy as np
print("Array Creation : ")
a = np.arange(0,10).reshape(2,5)
b = np.arange(10,20).reshape(2,5)
print(a)
print(b)
c = np.zeros((2,5))
for i in range(a.shape[0]):
   for j in range(a.shape[1]):c[i,j]=a[i,j]*b[i,j];
print(c)