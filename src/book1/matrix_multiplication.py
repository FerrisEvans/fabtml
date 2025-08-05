import numpy as np

A = np.array([[1, 2, 10, 20],
          [3, 4, 30, 40],
          [5, 6, 50, 60]])
B = np.array([[4, 2],
              [3, 1],
              [40, 20],
              [30, 10]])
C = A @ B
print(C)

A = np.array([[4, 3, 1],
              [1, -2, 3],
              [5, 7, 0]])
B = np.array([[7],
              [2],
              [1]])
C = A @ B
print(C)
