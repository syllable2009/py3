from time import time, sleep

#将函数作为参数传递

def logger(msg=None):
    def run_time(func):
        def wrapper(*args, **kwargs):
            start = time()
            func()  # 函数在这里运行
            end = time()
            cost_time = end - start
            print("[{}] func three run time {}".format(msg, cost_time))

        return wrapper

    return run_time


@logger(msg="One")
def fun_one():
    sleep(1)
    print("*****1")


@logger(msg="Two")
def fun_two():
    sleep(1)
    print("*****2")


@logger(msg="Three")
def fun_three():
    sleep(1)
    print("*****3")





if __name__ == '__main__':
    print("----start----")
    fun_one()
    fun_two()
    fun_three()