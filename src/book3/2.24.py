import numpy as np

A = np.array([[1], [2]])
B = np.array([[4], [3], [2]])
C = A @ B.T
print(C)
