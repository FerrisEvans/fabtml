import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s = Series([1, 2, 3, 4, 5])
print(s)

s = Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='series')
print(s)

s = Series({
    'a': 1,
    'b': 2,
    'c': 3
})
print(s)

s1 = Series(s, ['a', 'c'])
print(s1)

s = Series([1, 2, np.nan, 3, 4, None, 5], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'], name='data')
print(f"默认取前 5 行数据\n {s.head(3)}")
print(f"默认取后 5 行数据\n {s.tail(2)}")
print(f"查看所有描述性信息\n {s.describe()}")
