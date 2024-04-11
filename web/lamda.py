
# Lambda函数的基本语法形式是 lambda 参数: 表达式
add = lambda x, y: x + y
print(add(5, 3))  # 输出: 8
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)


z = 2 + 3j
print(type(z))
b = b"Hello"
print(type(b))

bytes_array = bytearray(b"Hello")
print(type(bytes_array)) # <class 'bytearray'>
range_ = range(5)
print(type(range_)) # <class 'range'>

tuple_ = (1, 2, 3)
print(type(tuple_)) # <class 'tuple'>

list_ = [1, 2, 3] # 列表是可变的，而元组和字符串是不可变的
print(type(list_)) # <class 'list'>

set_ = {1, 2, 3}
print(type(set_)) # <class 'set'>

frozenset_ = frozenset([1, 2, 3])
print(type(frozenset_)) # <class 'frozenset'>
# None类型
none_ = None

# Python的数据类型都是类（class）。这意味着，我们可以像处理对象一样处理这些数据，调用它们的方法，甚至给它们添加属性。

