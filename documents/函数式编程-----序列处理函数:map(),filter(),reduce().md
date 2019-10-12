# map
map函数的原型是map(function, iterable, …)，它的返回结果是一个列表。
参数function传的是一个函数名，可以是python内置的，也可以是自定义的。
参数iterable传的是一个或多个可以迭代的对象，例如列表，元组，字符串这样的。

a=(1,2,3,4,5)
b=[1,2,3,4,5]
c="zhangkang"

la=map(str,a)
lb=map(str,b)
lc=map(str,c)

print(la)
print(lb)
print(lc)

['1', '2', '3', '4', '5']
['1', '2', '3', '4', '5']
['z', 'h', 'a', 'n', 'g', 'k', 'a', 'n', 'g']

str()是python的内置函数，自定义如下
def mul(x):
    return x*x

la=map(mul,a)
print(la)
输出：[1, 4, 9, 16, 25]   

def add(x,y,z):
    return x,y,z

list1 = [1,2,3]
list2 = [1,2,3,4]
list3 = [1,2,3,4,5]
res = map(add, list1, list2, list3)
print(res)

输出：
[(1, 1, 1), (2, 2, 2), (3, 3, 3), (None, 4, 4), (None, None, 5)]

可以看到不足的iterable参数会用None填补，除非参数function支持None的运算，否则根本没意义。

# reduce()
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def fn(x, y):
    return x * 10 + y
reduce(add, [1, 3, 5, 7, 9])
13579


# filter()
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
结果: [1, 5, 9, 15]

把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
结果: ['A', 'B', 'C']

# sorted()
默认情况下，对字符串排序，是按照ASCII的大小比较的
sorted([36, 5, -12, 9, -21], key=abs)


# enumerate
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

