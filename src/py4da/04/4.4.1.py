import numpy as np

arr = np.arange(1, 10, 1)
print(np.greater(arr, 4))
print(np.less(arr, 4))
print(np.equal(arr, 4))

# 与或非
print(np.logical_and([1, 0], [1, 1]))
print(np.logical_or([0, 0], [1, 0]))
print(np.logical_not([1, 0]))
print(np.logical_xor([0, 0], [1, 0]))

print(np.any([0, 1, 2]))
print(np.all([0, 1, 2]))
# 自定义
print(np.where(arr > 4, arr ** 2, -1))
print(np.select([arr < 4, (arr >= 4) & (arr <= 7),arr > 7], ['c', 'b', 'a'], default='d'))
