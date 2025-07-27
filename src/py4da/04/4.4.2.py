import numpy as np

arr = np.arange(32).reshape(8, 4)
print(arr)

# 求和
print(np.sum(arr))
# 平均值
print(np.average(arr))
print(np.mean(arr))
# 标准差（方差开根号）
print(np.std(arr))
# 方差
print(np.var(arr))
# 最值
print(np.max(arr), np.argmax(arr))
print(np.min(arr), np.min(arr))
# 分位数
print(np.percentile(arr, 0))
print(np.percentile(arr, 25))
print(np.percentile(arr, 50))
print(np.percentile(arr, 100))
# 中位数
print(np.median(arr))
# 累计和
print(np.cumsum(arr))
# 累计积
print(np.cumprod(arr))
