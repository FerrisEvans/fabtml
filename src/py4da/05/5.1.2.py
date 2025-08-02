import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([1, 2, 3, 4, 5])
s2 = Series([6, 7, 8, 9, 10])

df = DataFrame({
    "第一列": s1,
    "第二列": s2
})
print(df)

df = DataFrame({
    'name': ['Tom', 'Jerry', 'Jack', 'Rose'],
    'age': [15, 16, 17, 18],
    'score': [80.1, 84.5, 89, 92.3]
}, index=[1, 2, 3, 4], columns=['name', 'score', 'age'])
print(df)

""" 学生成绩分析
1. 计算每位学生的总分和班级平均分
2. 找出数学成绩高于90分或英语成绩高于85分的学生
3. 按总分从高到低排序，并输出前3名学生
"""
df = DataFrame({
    'math': np.random.randint(low=60, high=100, size=10),
    'english': np.random.randint(low=60, high=100, size=10),
}, index=[i + 1 for i in range(10)])
df['total'] = df[['math', 'english']].sum(axis=1)
df['avg'] = df[['math', 'english']].mean(axis=1)
print(df)
print(df[(df.math > 80) | (df.english > 85)])
print(df.sort_values('total', ascending=False).head(3))
