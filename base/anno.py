def check_args(func):
    def wapper(*args: int, **kwargs: int):
        for arg in args:
            print(args)
        for arg in kwargs.values():
            print(arg)
        return func(*args, **kwargs)
    return wapper

@check_args
def add(x, y):
    return x + y


def add2(x: int, y: int) -> int:
    return x + y


print(add.__annotations__)

print(add2.__annotations__)

print(add(1,2))

# 定义支持多值参数的函数
def demo(s,*args,**kwargs):
    print(s)
    print(args)
    print(kwargs)
    # 无论传递的参数类型是 可变 还是 不可变，在函数内部针对参数使用 赋值语句，不会影响调用函数时传递的实参变量。
    # 如果传递的参数是 可变类型，在函数内部，使用 方法 修改了参数，外部实参同样会改变。

demo('zhangsan', 'go', '1', 2, a='d', c='e')

import os
print(dir(super))
# print(dir(super()))


class Cat:
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        pass


print(Cat.mro())

def log(x):
    x = 1
    print(x)

e = 100
log(e)
print(e)




