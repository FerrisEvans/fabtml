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
print(f"获取元素个数，忽略缺失值 {s.count()}")
print(f"获取索引两种方式 {s.keys()} - {s.index}")
print(f"判断元素的缺失值\n {s.isna()}")
print(f"判断元素是否在另一个集合中\n {s.isin([4, 5, 6])}")
print(f"平均数 {s.mean()} 标准差 {s.std():.2f} 方差 {s.var()} 最小值 {s.min()} 最大值 {s.max()} 总和 {s.sum()} 中位数 {s.median()}")
print(f"按索引排序\n {s.sort_index()} \n 按值排序\n {s.sort_values()}")
print(f"分位数 {s.quantile(0.25)} {s.quantile(0.75)}")
print(f"每个元素的计数\n {s.value_counts()}")
print(f"元素去重\n {s.drop_duplicates()} \n {s.unique()} \n 去重之后的元素个数 {s.nunique()}")
