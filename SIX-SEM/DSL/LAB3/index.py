import numpy as np
import random
print("Array Creation : \n\n")
A = np.array([2, 5, 10])
print(A.dtype)
B = np.array([2.4, 10.6, 5.2])
print(B.dtype)

print("\n\n")
print("Creating sequences of sequence will create 2 dimensional array : \n")
X = np.array([(3, 4, 5), (12, 6, 1)])
print(X)
Y = np.zeros((2, 4))
print(Y)
Z = np.ones((3, 3))
print(Z)

print("To create a sequence of data : \n\n")
S = np.arange(10, 30, 5)
print(S)
P = np.arange(0, 2, 0.3)
print(P)

print("\n\n")
print("Uses of Random Number function : \n")
print(random.choice([1, 2, 3, 4, 5]))
print(random.choice('python'))
print(random.randrange(25, 50))
print(random.randrange(25, 50, 2))
print(random.random())
print(random.uniform(5, 10))
print(random.shuffle([1, 2, 3, 4, 5]))
print(random.seed(10))

print("\n\n")
print("2-dimensional array (Matrix)")
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.size)
print(a.T)

print("\n\n")
print("3-dimensional array : \n")
c = np.arange(24).reshape(2, 3, 4)
print(c)
print(c.shape)
print(c[1, :, :])
print(c[:, :, 2])

print("\n\n")
print("Array operation : \n")
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)
c = a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a < 35)

print("\n\n")
print("Matrix operation : \n")
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A*B)
print(A.dot(B))
print(np.dot(A, B))
C = np.arange(12).reshape(3, 4)
print(C)
print(C.sum(axis=0))
print(C.sum(axis=1))

print("\n\n")
print("Indexing, Slicing Litrating array : \n")
x = np.arange(10)**3
print(x)
print(x[2:5])
print(x[0:6:2])
y = np.array([[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23],
             [30, 31, 32, 33], [40, 41, 42, 43]])
print(y[2, 3])
print(y[:5, 1])
print(y[-1, :])
print(y[:, -1])
for row in y:
    print(row)
for element in y.flat:
    print(element)

print("\n\n")
print("Creating the shape of the matrix : \n")
x = np.arange(10)**3
print(x)
print(x[2:5])
print(x[0:6:2])
y = np.array([[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23],
             [30, 31, 32, 33], [40, 41, 42, 43]])
print(y[2, 3])
print(y[:5, 1])
print(y[-1, :])
print(y[:, -1])
for row in y:
    print(row)
for element in y.flat:
    print(element)
    print(y.ravel())
B1 = y.reshape(4, 5)
print(B1)

print("\n\n")
print("Stacking together different array : \n")
A1 = np.array([(3, 4, 5), (12, 6, 1)])
A2 = np.array([(1, 2, 6), (-4, 3, 8)])
D1 = np.vstack((A1, A2))
D2 = np.hstack((A1, A2))
print(A1)
print(A2)
print(D1)
print(D2)

print("\n\n")
print("Stacking one D array into  2-D array : \n")
a = np.array([4., 2.])
b = np.array([3., 8.])
print(np.column_stack((a, b)))
print(np.hstack((a, b)))

print("\n\n")
print("Indexing with array of the indices : \n")
k = np.arange(12)**2
i = np.array([1, 1, 3, 8, 5])
j = np.array([[3, 4], [9, 7]])
print(k[i])
print(k[j])

print("\n\n")
print("Use of for loop (Mapping by value : \n")
x = np.array([(3, 2, 9), (1, 6, 7)])
s1 = 0
for row in x:
    for col in row:
        s1 += col
print(s1)

print("\n\n")
print("Use of for loop (Mapping by Index : \n")
y = np.array([(3, 2, 9), (1, 6, 7)])
s = 0
for p in range(y.shape[0]):
    for q in range(y.shape[1]):
        s += y[p, q]
print(s)
