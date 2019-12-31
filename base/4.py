import time
for i in range(10):
    print('\r距离退出还剩{}秒'.format(9-i),end='')
    time.sleep(1)