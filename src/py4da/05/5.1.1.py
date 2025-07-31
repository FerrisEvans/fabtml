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
