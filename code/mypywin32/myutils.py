import time,random
from PIL import Image, ImageGrab

# print(random.randint(1, 10))  # 产生 1 到 10 的一个整数型随机数
# print(random.random())  # 产生 0 到 1 之间的随机浮点数
# print(random.uniform(1.1, 5.4))  # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
# print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数
# print(random.sample([1, 3, 5, 6, 7], 3))  # 从list中随机获取3个元素，作为一个片断返回

# 获取一个区间内随机的时间，采用浮点数更加逼真,并保留一定位的小数
def getRandomTimeSec(_left = 1.1,_right = 5.4, _round = 3):
    return round(random.uniform(_left, _right),_round)


# 线程休眠一定时间，如果不传值，将自动生成默认休眠时间
def waitSleep(_times = None):
    if _times is None:
        _times = getRandomTimeSec()
    # print('thred sleep {} second'.format(_times))
    time.sleep(_times)

def printScreen(_lx = None,_ly = None,_rx = None,_ry = None):
    # 1、用grab函数截图，参数为左上角和右下角左标
    _xy = (_lx, _ly, _rx, _ry)
    if any(e is None for e in _xy):
        image = ImageGrab.grab()
    else:
        image = ImageGrab.grab(_xy)
    # print('size:{}'.format(image.size))
    image.save("picture.png")
    image.close()

if __name__ == '__main__':
    # waitSleep()
    # waitSleep(3)
    printScreen()
    printScreen(100, 200, 300, None)
    printScreen(100,200,300,400)


