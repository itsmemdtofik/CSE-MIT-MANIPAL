import numpy as np
b = np.array([[2,0],[3,4]])
print(b)
print('Column sum: ',b.sum(axis=0))
print('Row sum: ',b.sum(axis=1))