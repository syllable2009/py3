import time
def decorator(func):
    def punch():
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        func()
    return punch
def punch():
    print('昵称：两点水  部门：做鸭事业部 上班打卡成功')
f = decorator(punch)
f()
