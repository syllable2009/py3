


# from fastapi import FastAPI
# app = FastAPI()

# 使用时只需要app目录下内容
# from seed.app.db.user import User
# u = User()
# print(u)

# 自动注册函数
registered_functions = []

# 装饰器将函数注册到一个列表中
def register_decorator(func_list):
    def decorator(func):
        func_list.append(func)
        return func
    return decorator

@register_decorator(registered_functions)
def message_decorator(before_message, after_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(before_message)
            result = func(*args, **kwargs)
            print(after_message)
            return result
        return wrapper
    return decorator

@message_decorator("Start", "End")
def hello_world():
    print("Hello, world!")


import functools
# 装饰器的实现？
def decorator(func):
    @functools.wraps(func) #默认情况下，装饰器会“掩盖”掉原函数的名字和文档字符串。这是因为在装饰器内部，我们返回了一个全新的函数。我们可以使用 functools.wraps 来解决这个问题
    def wrapper():
        print('Before function execution')
        func()
        print('After function execution')
    return wrapper

def hello_world2():
    "Prints 'Hello, world!'"
    print('Hello, world2!')

decorated_hello = decorator(hello_world2)
# decorated_hello()
#
# print(decorated_hello.__name__)
# print(decorated_hello.__doc__)

# if __name__ == '__main__':
#     hello_world()

import logging

def log_decorator(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f'Running "{func.__name__}" with arguments {args} and kwargs {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Finished "{func.__name__}" with result {result}')
        return result
    return wrapper

import time
from functools import wraps
def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function "{func.__name__}" took {end_time - start_time} seconds to run.')
        return result

    return wrapper


@log_decorator
@timer_decorator
def add(x, y):
    return x + y

add(1,2)

print(registered_functions)