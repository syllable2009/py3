# 多进程 多进程可以实现真正的并行
import multiprocessing
# 多线程 尽管Python的多线程因为全局解释器锁（GIL）的存在，并不能实现真正的并行，但是它们在I/O密集型任务中仍然很有用
import threading


def print_numbers():
    for i in range(10):
        print(i)


def print_letters():
    for letter in 'abcdefghij':
        print(letter)


# 创建进程
p1 = multiprocessing.Process(target=print_numbers)
p2 = multiprocessing.Process(target=print_letters)
# 创建线程
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# 线程池
import concurrent.futures

if __name__ == '__main__':
    # 使用线程池
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(print_numbers)
        future2 = executor.submit(print_letters)
        for future in concurrent.futures.as_completed([future1, future2]):
            pass
    print('-------------')
    # 使用进程池
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future1 = executor.submit(print_numbers)
        future2 = executor.submit(print_letters)
        for future in concurrent.futures.as_completed([future1, future2]):
            pass


    # # 启动进程
    # p1.start()
    # p2.start()
    # # 等待进程结束
    # p1.join()
    # p2.join()
    # # 启动线程
    # t1.start()
    # t2.start()
    # # 等待线程结束
    # t1.join()
    # t2.join()
