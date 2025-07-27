import numpy as np

# 生成 0 - 1 之间的随机浮点数（均匀分布：概率相等）
arr = np.random.rand(2, 3)
print(arr)

# 生成制定范围区间的随机浮点数（均匀分布）
arr = np.random.uniform(low=-1, high=1, size=(2, 3))
print(arr)

# 生成制定范围区间的随机整数（均匀分布）
arr = np.random.randint(low=10, high=50, size=(2, 3))
print(arr)

# 生成随机数列（标准正态分布: 两边概率小，中间概率大，均值为 0，标准差为 1）
arr = np.random.randn(2, 3)
print(arr)

# 设置随机种子
np.random.seed(20)
arr = np.random.randint(low=10, high=50, size=(2, 3))
print(arr)

