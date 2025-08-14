# 如果原函数需要参数，可以在装饰器的 wrapper 函数中传递参数
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        print(f"这里是在调用原始函数前添加的新功能,{args}, {kwargs}")
        result = original_function(*args, **kwargs)
        print("这里是在调用原始函数后添加的新功能")
        return result
    return wrapper


# 使用装饰器
@decorator_function
def target_function(arg1, arg2):
    print("原始函数的实现")
    print(f"Hello, {arg1}!, {arg2}")


# 装饰器本身也可以接受参数，此时需要额外定义一个外层函数
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper

    return decorator


@repeat(3)
def say_hello():
    print("Hello!")

# 类装饰器
def log_class(cls):
    """类装饰器，在调用方法前后打印日志"""
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)  # 实例化原始类

        def __getattr__(self, name):
            """拦截未定义的属性访问，转发给原始类"""
            return getattr(self.wrapped, name)

        def display(self):
            print(f"调用 {cls.__name__}.display() 前")
            self.wrapped.display()
            print(f"调用 {cls.__name__}.display() 后")

    return Wrapper  # 返回包装后的类

@log_class
class MyClass:
    def display(self):
        print("这是 MyClass 的 display 方法")


# 默认参数可以不传值
def func(a, b=0):
    return a + b
# 基础参数传递，1对应a，2对应b
func(1, 2)
# 显示参数传递
func(b=2, a=1)
# 可变参数*args
# 可变关键字参数（‌**kwargs）
# for k, v in kwargs.items():
#     print(f"{k}: {v}")

if __name__ == "__main__":
    print("main start")
    target_function("world", "你好")
    say_hello()
    obj = MyClass()
    obj.display()
