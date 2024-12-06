# python3


# asyncio
asyncio是一种使用单线程单进程的的方式实现并发的工具。
asyncio提供的框架以事件循环(event loop)为中心，程序会把一些函数注册到事件循环上，程序开启一个无限的循环,事件循环会循环执行这些函数(但同时只能执行一个)。
当执行到某个函数时，如果它正在等待I/O返回，事件循环会暂停它的执行去执行其他的函数。当某个函数完成I/O后，会恢复下次循环到它的时候继续执行。

asyncio.run() 是 Python asyncio 模块中的一个函数，用于运行异步协程。它是最简单和推荐的方式来启动事件循环并执行异步代码。

协程Coroutine：使用 async def 定义的函数，它可以在执行时被挂起，以便其他协程可以运行。协程本质上是一个函数，特点是在代码块中可以将执行权交给其他协程。
事件循环event loop：负责调度和执行协程的机制。只有一个事件循环在任何给定的时间运行。

#单纯的执行await协程函数，顺序执行两个协程，并没有实现两个协程并发执行
await say_after(1, 'hello')
await say_after(2, 'world')

#将协程函数用Task封装，才可以并发执行
task1 = asyncio.create_task(say_after(1, 'hello'))
task2 = asyncio.create_task(say_after(2, 'world'))
await task1
await task2

#asyncio.gather也可以实现协程的并发执行，也是最通常的做法
await asyncio.gather(say_after(1, 'hello'), say_after(2, 'world'))

可等待对象await
可以在await语句中使用的对象，有三种，协程，Future和Task，只是通常情况下没有必要在应用代码中创建 Future 对象。不能在同步/普通函数里使用await，否则会出错。但是在协程中可以调用另外一个协程（使用await），也可以调用普通函数。

future是一个数据结构，表示还未完成的工作结果。事件循环可以监视Future对象是否完成。从而允许一个协程等待另一协程完成一些工作。
它是一个占位符，表示某个尚未完成的操作的结果。你可以通过 Future 对象检查操作是否完成、获取结果或处理异常。
import asyncio

async def compute():
    await asyncio.sleep(1)
    return 42

async def compute_task(future):
    result = await compute()
    # 设置 Future 的结果
    future.set_result(result)

async def main():
    #创建一个 Future 对象
    future = asyncio.Future()  
    loop = asyncio.get_event_loop()
    #将计算任务放入事件循环
    loop.create_task(compute_task(future))
    #等待 Future 完成
    result = await future
    print(f"Result: {result}")
asyncio.run(main())

Task 是 Future 的子类，表示一个被调度的协程。它用于将协程封装成可调度的对象，以便在事件循环中运行。
Task 会自动创建一个 Future，用于跟踪协程的执行状态和结果。
import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    #创建两个任务
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))
    # 等待所有任务完成，并发执行
    await task1
    await task2

asyncio.run(main())

任务Event：Event 是一个简单的线程间同步原语，用于在多个协程之间共享状态。它可以用于实现简单的信号机制，使得一个协程可以等待另一个协程的事件发生。
import asyncio

async def waiter(event):
    print("Waiting for the event to be set...")
    await event.wait()  # 等待事件被 set()
    print("Event is set!")

async def setter(event):
    await asyncio.sleep(2)
    event.set()  # 设置事件

async def main():
    event = asyncio.Event()  # 创建一个 Event 对象
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())

# injector 是一个轻量级的依赖注入框架，可以帮助您管理依赖关系。
class AppModule(Module):
    @provider
    @Named('database')
    def provide_database(self) -> Database:
        return Database()
    @provider
    @Named('userService')
    def provide_user_service(self, db: Database) -> UserService:
        return UserService(db)

class UserService:
    @inject
    def __init__(self, db: Database = Named('database')):  # 默认使用 SQLite
        self.db = db

# 设置依赖注入
# 创建 Injector 实例
injector = Injector([AppModule()])
# 获取 UserService 实例
user_service = injector.get(UserService, db=Named('userService'))


Python打包方法——Pyinstaller
pyinstaller -F -i /Users/jiaxiaopeng/App.ico hello.py

利用PyCharm+Python+wordcloud+jieba+docx生成中文词云和词频统计-补充完善的代码


每个py结尾的文件都是一个模块。
模块中国定义的类，全局变量，函数都是直接提供给外界使用的工具。
包是包含多个模块的特殊目录，目录下有一个__init__.py来指定对外界的模块列表


# py3常用工具模块集合
-利用 Python Faker 包来制作假数据：
-爬虫智能解析库 Readability 和 Newspaper 的用法,智能文本提取
-Python 日志 logging 模块详解及应用
-使用 Pathlib 模块代替os 模快进行文件操作
-Python 使用 attrs 和 cattrs 实现面向对象编程
-Python 中提供了汉字转拼音的库，名字叫做 PyPinyin，可以用于汉字注音、排序、检索等等场合
-glom模块 处理结构化数据
-Pandas易于使用的数据结构和数据分析工具
-解析库
-存储文件，TXT文件存储,JSON文件存储,CSV文件存储,MySQL存储



Python 内置的注解
@property
@staticmethod
@classmethod

自定义注解以 @ 符号开头，紧跟着一个函数或类的定义

    