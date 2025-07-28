



def myfun():
    a = 1 + 1
    return a
import sys


if __name__ == '__main__':
    a = myfun()
    b=a
    print(a)
    print(id(a))
    print(type(a))
    print(b)
    print(id(b))
    print(type(b))
    # is是用来判断两个引用所指的对象是否相同
    print(a is b)
    #查看对象的引用计数：
    print(sys.getrefcount(a))
    print(sys.getrefcount(100))
