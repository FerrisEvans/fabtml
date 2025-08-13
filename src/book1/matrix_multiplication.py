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

A = np.array([[2, 1, 4, 0],
              [1, -1, 3, 4]])
B = np.array([[1, 3, 1],
              [0, -1, 2],
              [1, -3, 1],
              [4, 0, -2]])
C = A @ B
print(C)

A = np.array([[3, 5],
              [-1, 1]])
B = np.array([[-2, 2, 3],
             [3, 5, -2]])
C = A @ B
print(C)

A = np.array([[8, 8, 6]])
B = np.array([[5, 2], [1, 3], [6, 5]])
C = A @ B
print(C)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = A @ B
print(C)

A = np.array([[4, 5], [1, 2]])
B = np.array([[2, -1, 3], [1, 0, 4]])
C = np.array([[1, -1], [2, 3], [-1, 2]])
D = A @ B @ C
print(D)

A = np.array([[-2, 4],
              [1, -2]])
B = np.array([[2, 4],
              [-3, -6]])
C = A @ B
print(C)
