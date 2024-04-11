# 生成器是一种特殊的迭代器，它们的创建方式是在函数定义中包含yield关键字。当这个函数被调用时，它返回一个生成器对象，该对象可以使用next()函数或for循环来获取新的元素。
# 生成器的主要优势之一是它们的惰性求值特性。也就是说，生成器只在需要时才计算和产生元素。这使得生成器在处理大规模数据时，可以大大降低内存使用量。与传统的数据结构（如列表）相比，生成器不需要在内存中存储所有元素，而是在每次迭代时动态计算出新的元素。
def simple_generator():
    yield "Python"
    yield "is"
    yield "awesome"

#生成器表达式是创建生成器的一种更简洁的方式
gen_expr = (x**2 for x in range(1000000))
# 输出前10个元素
for i in range(10):
    print(next(gen_expr))

import itertools
sliced_seq = itertools.islice(gen_expr, 5, 10)
print(sliced_seq)
# 创建生成器
gen = simple_generator()
print(type(gen))
# 使用next函数获取元素
print(next(gen))  # 输出: Python
print(next(gen))  # 输出: is
print(next(gen))  # 输出: awesome

# 使用for循环获取元素
for word in simple_generator():
    print(word)

print(range(1,10))
