#!/usr/bin/env python3 # 告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*- # 告诉Python解释器，边解释边执行，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# 有些实现（如 PyPy）可以编译成字节码，提高性能。
# 单行注释
'''多行注释'''
# 使用缩进来表示代码块，不需要使用大括号 {}，缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
# 空行\n，书写时不插入空行，Python 解释器运行也不会出错。在同一行中使用多条语句，语句之间使用分号 ; 分割
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束
# 一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句。在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
# 区分大小写
total = 1 + \
        2 + \
        3
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

# 标准输入
user_input = input("\n请输入一些文字:(回车键结束)\n")
print(user_input)
# 标准输出，print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
print(r'Newlines are indicated by \n')  # 在字符串前面加上r或者R=原始字符串
print('name:%s,age:%d' % ('张三', 100))  # 格式化
# format + 转义序列
print('What\'s your name? \n{0} was {1} years old when he wrote this book'.format('jxp', 33))
print('god', end=" ")
print(1, 2, 3, sep='@')

# import 与 from...import 导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
# 模块与引用
# 搜索路径是在 Python 编译或安装的时候确定的，安装新的库应该也会修改。
import sys  # 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。

print(sys.argv)
print(sys.path)
# 当我们在命令行运行某个模块文件时，Python解释器把一个特殊变量__name__置为__main__
if __name__ == '__main__':
    print('__main__')

# Python动态类型语言，变量类型在运行时确定，变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 内置的 type() 函数可以用来查询变量所指的对象类型。还可以用 isinstance 来判断。isinstance(a, int)
# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
# 基本数据类型：数值（Numbers）、字符串（String）、列表（List）、元组（Tuple）、字典（Dictionary）、集合（Set）
# 数值：int (整数)、bool (布尔)、float (浮点数)和complex (复数)，复数由实部和虚部组成，形式为 a + bj，其中 a 是实部，b 是虚部，j 表示虚数单位。如
# 1 + 2j、 1.1 + 2.2j

# 字符串
# Python 中单引号 ' 和双引号 " 使用完全相同。
# 使用三引号(''' 或 """)可以指定一个多行字符串。
# 转义符 \。
# 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
# 按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python 中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
# 字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
print(ord('中'))  # 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符串
print(chr(20013))
print('ABC'.encode('ascii'))  # 以Unicode表示的str通过encode()方法可以编码为指定的bytes
x = b'ABC'  # 纯英文的str可以用ASCII编码为bytes
print(len(x))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode(
    'utf-8'))  # 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(
    "中文".encode('utf-8'))  # 字符在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes

# bytes 类型，bytes 类型中的元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符
x = bytes("hello", encoding="utf-8")
x = b"hello"

# 列表（List）可变
list = ['abcd', 786, 2.23, 'runoob', 70.2]
# 元组（Tuple）不可变
t = ('Michael', 'Bob', 'Tracy')
# 集合 可变
c = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
# Set（集合）可变
s = set([1, 1, 2, 2, 3, 3])
# dictionary字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 类型转换
str(1)

# 推导式 [表达式 for 变量 in 列表 if 条件]
# 列表推导式
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)
# 字典推导式
newdict = {key: len(key) for key in names}
print(newdict)
# 集合推导式 { expression for item in Sequence if conditional }
# 元组推导式 (expression for item in Sequence if conditional )

# Python3 迭代器与生成器
# 迭代器有两个基本的方法：iter() 和 next()
it = iter(names)
for x in it:
    print(x, end=" ")
# while True:
#     try:
#         print (next(it), end=" ")
#     except StopIteration:
#         sys.exit()

# 条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
# 循环
for name in c:
    print(name)
else:
    print(name)

while age < 5:
    age += 1
else:
    age += 1


# 函数
# 在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
def my_abs(x=10):
    if x >= 0:
        return x, x
    else:
        return -x, x


x, y = my_abs(-1)
print(x, y)


# 参数：必需参数，关键字参数，默认参数，不定长参数
# 加了一个星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。加了两个星号 ** 的参数会以字典的形式导入。
def show(a, *x, **y):
    print(a)
    print(x)
    print(y)


show(1, 2, 3, x=4, y=5)

# 高级函数：返回函数，匿名函数，装饰器，偏函数
# 匿名函数:lambda [arg1 [,arg2,.....argn]]:expression
add = lambda arg1, arg2: arg1 + arg2
# lambda 函数通常与内置函数如 map()、filter() 和 reduce() sorted() 一起使用，以便在集合上执行操作。
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# squared = list(map(lambda x: x**2, numbers))
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# product = reduce(lambda x, y: x * y, numbers)

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


# 装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。
# 装饰器允许在不修改原有函数代码的基础上，动态地增加或修改函数的功能，装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象。
# 装饰器的语法使用 @decorator_name 来应用在函数或方法上。
# Python 还提供了一些内置的装饰器，比如 @staticmethod 和 @classmethod，用于定义静态方法和类方法。
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 这里是在调用原始函数前添加的新功能
        before_call_code()

        result = original_function(*args, **kwargs)

        # 这里是在调用原始函数后添加的新功能
        after_call_code()

        return result

    return wrapper


# 使用装饰器，当我们使用 @decorator_function 前缀在 target_function 定义前，Python会自动将 target_function 作为参数传递给 decorator_function，
# 然后将返回的 wrapper 函数替换掉原来的 target_function。等同于target_function = decorator_function(target_function)
# 装饰器函数也可以接受参数
@decorator_function
def target_function(arg1, arg2):
    print('target_function')
    pass  # 原始函数的实现


def before_call_code():
    print('before_call_code')


def after_call_code():
    print('after_call_code')


target_function(1, 2)

# 类装饰器
# 除了函数装饰器，Python 还支持类装饰器。类装饰器是包含 __call__ 方法的类，它接受一个函数作为参数，并返回一个新的函数。





# 作用域：__xxx__这样的变量是特殊变量，可以被直接引用，以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的,__xxx这样的函数或变量就是非公开的（private），不应该被直接引用。
# 面向对象编程
class Student(object):
    def __init__(self, name,
                 score):  # __init__方法的第一个参数永远是self，表示创建的实例本身，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传
        self.name = name
        self.__score = score

    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
    def print_score(self):
        print('%s: %s' % (self.name, self.__score))


bart = Student('Bart Simpson', 59)
bart.print_score()


class Teacher(Student):
    pass


print(type(bart))  # 使用type()来判断类型，可配合types模块使用
print(isinstance(bart, Student))  # isinstance()来判断继承关系
print(dir(123))  # dir()函数获得一个对象的所有属性和方法，它返回一个包含字符串的list
hasattr(bart, 'id')
getattr(bart, '__name')
# 高级动态语言 Python的file-like object
bart.id = 'bart'  # 给实例动态绑定属性
bart.lazy_sum = lazy_sum  # 给实例动态绑定函数
from types import MethodType

bart.lazy_sum = MethodType(lazy_sum, bart)  # 给实例动态绑定函数
Teacher.lazy_sum = lazy_sum  # 给class动态绑定函数


class Student(object):
    __slots__ = ('name', 'age')  # __slots__限制用tuple定义允许绑定的属性名称


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
    logging.info('n = %d' % n)  # 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
    assert n != 0, 'n is zero!'  # 断言失败，assert语句本身就会抛出AssertionError
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
        print(line.strip())  # 把末尾的'\n'删掉
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

print(os.name)  # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.uname())
os.path.abspath('.')  # 看当前目录的绝对路径
os.path.join('/Users/michael', 'testdir')  # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir('/Users/michael/testdir')  # 然后创建一个目录
os.rmdir('/Users/michael/testdir')  # 删掉一个目录
os.path.split('/Users/michael/testdir/file.txt')  # 拆分路径
os.path.splitext('/path/to/file.txt')  # 你得到文件扩展名

os.rename('test.txt', 'test.py')  # 对文件重命名
os.remove('test.py')  # 删掉文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

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
