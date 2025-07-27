import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(f"dimensions: {arr.ndim}") # 维度
print(f"shape: {arr.shape}")

arr = np.array([1, "hello"])
print(arr)

arr = np.array([1, 2.5])
print(arr)

# 等差数列 start end step
arr = np.arange(1, 10, 1)
print(arr)

arr = np.linspace(1, 10, 4)
print(arr)

arr = np.logspace(0, 3, num=4, base=10.0)
print(arr)

# 主对角线上的数字是 1，其他数字是 0
arr = np.eye(3) # 参数为矩阵形状
print(arr)

# 主对角线上是非 0 的数字，其他数字是 0
arr = np.diag([1, 2, 3])
print(arr)
