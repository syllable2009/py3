#!/usr/bin/env python3 # 告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*- # 告诉Python解释器，边解释边执行，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# 有些实现（如 PyPy）可以编译成字节码，提高性能。
# 单行注释
'''多行注释'''
# 使用缩进来表示代码块，不需要使用大括号 {}，缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
# 一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句。在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
total = 1 + \
        2 + \
        3
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

# Python动态类型语言，变量类型在运行时确定


print(r'Newlines are indicated by \n')  # 在字符串前面加上r或者R=原始字符串
print('name:%s,age:%d' % ('张三', 100))  # 格式化
print('What\'s your name? \n{0} was {1} years old when he wrote this book'.format('jxp', 33))  # format + 转义序列
# 标准输入输出
user_input = input("请输入一些文字:(回车键结束)")
print(user_input)
# 基本数据类型：数值（Numbers）、字符串（String）、列表（List）、元组（Tuple）、字典（Dictionary）、集合（Set）
# 字符串
print(ord('中'))  # 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(chr(20013))
print('ABC'.encode('ascii'))  # 以Unicode表示的str通过encode()方法可以编码为指定的bytes
x = b'ABC'  # 纯英文的str可以用ASCII编码为bytes
print(len(x))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print("中文".encode('utf-8'))  # 字符在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
# 列表（List
classmates = ['Michael', 'Bob', 'Tracy']
# 元组（Tuple）
classmates = ('Michael', 'Bob', 'Tracy')
# 字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 集合
s = set([1, 1, 2, 2, 3, 3])
# 条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
# 循环
for name in classmates:
    print(name)


# 函数
def my_abs(x=10):
    if x >= 0:
        return x, x
    else:
        return -x, x


x, y = my_abs(-1)
print(x, y)
# 高阶函数：map reduce filter sorted
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def add(x, y):
    return x + y


from functools import reduce

print(reduce(add, [1, 3, 5, 7, 9]))


# 高级函数：返回函数，匿名函数，装饰器，偏函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)  # 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
print(f)
print(f())  # 返回的函数并没有立刻执行，而是直到调用了f()才执行

# 模块与引用
import sys  # 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
print(sys.argv)
print(sys.path)
# 当我们在命令行运行某个模块文件时，Python解释器把一个特殊变量__name__置为__main__
if __name__ == '__main__':
    print('__main__')
# 作用域：__xxx__这样的变量是特殊变量，可以被直接引用，以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的,__xxx这样的函数或变量就是非公开的（private），不应该被直接引用。
# 面向对象编程
class Student(object):
    def __init__(self, name, score): # __init__方法的第一个参数永远是self，表示创建的实例本身，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传
        self.name = name
        self.__score = score
    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
    def print_score(self):
        print('%s: %s' % (self.name, self.__score))
bart = Student('Bart Simpson', 59)
bart.print_score()

class Teacher(Student):
    pass
print(type(bart)) # 使用type()来判断类型，可配合types模块使用
print(isinstance(bart, Student)) # isinstance()来判断继承关系
print(dir(123)) # dir()函数获得一个对象的所有属性和方法，它返回一个包含字符串的list
hasattr(bart, 'id')
getattr(bart, '__name')
# 高级动态语言 Python的file-like object
bart.id = 'bart' # 给实例动态绑定属性
bart.lazy_sum = lazy_sum # 给实例动态绑定函数
from types import MethodType
bart.lazy_sum = MethodType(lazy_sum, bart) # 给实例动态绑定函数
Teacher.lazy_sum = lazy_sum # 给class动态绑定函数

class Student(object):
    __slots__ = ('name', 'age') # __slots__限制用tuple定义允许绑定的属性名称

# @property装饰器就是负责把一个方法变成属性调用的
# 定制类
# 枚举类与元类

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

import logging
logging.basicConfig(level=logging.INFO)
def foo(s):
    n = int(s)
    logging.info('n = %d' % n) # 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
    assert n != 0, 'n is zero!' # 断言失败，assert语句本身就会抛出AssertionError
    return 10 / n

# IO编程
try:
    f = open('/path/to/file', 'rw')
    print(f.read())
finally:
    if f:
        f.close()
with open('/path/to/file', 'rw') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
# StringIO在内存中读写字符串，BytesIO操作二进制数据
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
f.write('hello')
print(f.getvalue())
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
f.write('中文'.encode('utf-8'))
# 操作文件和目录:os模块的某些函数是跟操作系统相关的
import os
print(os.name) #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.uname())
os.path.abspath('.') #看当前目录的绝对路径
os.path.join('/Users/michael', 'testdir') # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir('/Users/michael/testdir') # 然后创建一个目录
os.rmdir('/Users/michael/testdir') # 删掉一个目录
os.path.split('/Users/michael/testdir/file.txt') # 拆分路径
os.path.splitext('/path/to/file.txt') # 你得到文件扩展名

os.rename('test.txt', 'test.py')  # 对文件重命名
os.remove('test.py')  # 删掉文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

# 序列化，Python提供了pickle模块来实现序列化
import pickle
d = dict(name='Bob', age=20, score=88)
with open('/path/to/file', 'wb') as f:
    pickle.dump(d, f)
    d = pickle.load(f)

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json
json_str = json.dumps(d)
json.loads(json_str)
print(json.dumps(s, default=lambda obj: obj.__dict__))


y = 9
def showMsg(a, b=1):
    x = 5
    global y
    print(a * b)


showMsg('jxp', 5)


def total(a=5, *numbers, **phonebook):
    print('a', a)

    # 遍历元组中的所有项
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项
    for first_part, second_part in phonebook.items():
        print('double', first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

import os

print(os.getcwd())
print(dir(os))


# print(help(int))

class Person:
    def __init__(self, name):
        print('__init__')
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Swaroop')
p.say_hi()
