import numpy as np
import pandas as pd

# Numpy的核心就是n维array
a = np.array([1, 2, 3, 4.])
b = np.zeros(3, int)
b = np.zeros_like(a)
print(a * 2)
print(a.dtype) #如果list里面的值类型不相同，那么dtype就会返回”object“
print(a.shape)

# 导入CSV或者xlsx文件
# df = pd.DataFrame(pd.read_csv('name.csv',header=1))
# df = pd.DataFrame(pd.read_excel('name.xlsx'))

# 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。
a = [1, 2, 3,'hi']
myvar = pd.Series(a,index = ["x", "y", "z","w"])
print(myvar)
# print(myvar[1]) # 默认索引值就从 0 开始
print(myvar["y"])

# 也可以使用 key/value 对象，类似字典来创建 Series，字典的 key 变成了索引值
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites)
print(myvar[1])

# 如果我们只需要字典中的一部分数据，只需要指定需要数据的索引即可
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites, index = [1, 2])
print(myvar)

# Pandas 数据结构 - DataFrame - Pandas DataFrame 是一个二维的数组结构，类似二维数组。
# excel = Series1 + Series2 + ... + SeriesN
# pandas.DataFrame( data, index, columns, dtype, copy)

data = [['Google',10],['Runoob',12],['Wiki',13]]
df = pd.DataFrame(data,columns=['Site','Age'])
print(df)

data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print (df)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行
print(df.loc[0])
# 返回列数据
print(df["calories"])
if __name__ == '__main__':
    print("main start")