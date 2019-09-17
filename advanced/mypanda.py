import pandas as pd
from pandas import Series
from pandas import DataFrame
import logging

data = [1, 2, 3, 4, 5]
index = ['a', 'b', 'c', 'd', 'e']
s = Series(data=data, index=index)

data = [[1,2,3],
        [4,5,6]]
index = ['a','b']
columns = ['A','B','C']
df = pd.DataFrame(data=data, index=index, columns=columns)
print(data)