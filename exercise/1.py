import time
import threading
from threading import Thread

# IO密集型任务和计算密集型任务的区别
# IO指input output，IO密集型任务包括文件读写（磁盘IO）、网页请求（网络IO）等。这类任务计算量较小，有比较多的等待时间，用多线程可以较大提高运行效率
# 计算密集型任务是指CPU计算占据主要运行时间，这类任务使用python多线程无法提高效率

def myfun():
    time.sleep(1)
    a = 1 + 1
    print(a)

def circle():
    t = time.time()
    for _ in range(5): #TODO
        myfun()
    print(time.time() - t)

def circle2():
    print(threading.currentThread().name)
    t = time.time()
    this = []
    for _ in range(5):
        th = Thread(target = myfun,args=()) #TODO
        this.append(th) #TODO
        print(th.name)
        # print(threading.currentThread().name) 这里打印出的都是MainThread
        th.start()
    for th in this:
        th.join() #TODO
    print(time.time() - t)

# 创建多线程的第二种方式
class MyThread(threading.Thread):
    def __init__(self, i,name):
        threading.Thread.__init__(self)
        self.i = i
        self.name = name
    def run(self):
        time.sleep(1)
        a = self.i + 1
        # print(a)
        print(self.name)

# 使用类继承方式其实还有另一种形式。
# 之前是直接用run定义计算函数，如果已经有一个计算函数，也可以用传入的方式而不是改写成run

class MyThread2(threading.Thread):

    def __init__(self, target, **args):
        threading.Thread.__init__(self)
        self.target = target
        self.args = args

    def run(self):
        self.target(**self.args)

if __name__ == '__main__':
       # circle()
       # circle2()
       for i in range(5):
           MyThread(i,'thread {}'.format(i)).start()
