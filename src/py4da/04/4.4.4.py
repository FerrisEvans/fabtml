import numpy as np

np.random.seed(0)
arr = np.random.randint(1, 100, 10)
print(arr)
print(np.sort(arr))
# 索引
print(np.argsort(arr))
# 去重
print(np.unique(arr))
# 拼接
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
print(np.concatenate((arr1, arr2)))
# 等分
print(np.split(arr, 2))
# 切分
print(np.split(arr, [2, 6]))

print(np.reshape(arr, [2, 5]))
