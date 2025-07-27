import numpy as np

# 一维数组
arr = np.random.randint(low=10, high=50, size=20)
print(arr)
print(arr[3])
print(arr[:]) # 全部数据
print(arr[3:5])
print(arr[arr>20]) # 布尔索引

arr = np.random.randint(low=10, high=50, size=(4, 8))
print(arr)
print(arr[1, 3])
print(arr[1][3])

print(arr[:][3])
print(arr[:,3]) # 获取列
