import win32api
import win32con
win32api.MessageBox(None,"Hello,pywin32!","pywin32",win32con.MB_OK)

import win32gui,win32ui,win32con

def get_windows(windowsname,filename):
    # 获取窗口句柄
    handle = win32gui.FindWindow(None,windowsname)
    # 将窗口放在前台，并激活该窗口（窗口不能最小化）
    win32gui.SetForegroundWindow(handle)
    # 获取窗口DC
    hdDC = win32gui.GetWindowDC(handle)
    # 根据句柄创建一个DC
    newhdDC = win32ui.CreateDCFromHandle(hdDC)
    # 创建一个兼容设备内存的DC
    saveDC = newhdDC.CreateCompatibleDC()
    # 创建bitmap保存图片
    saveBitmap = win32ui.CreateBitmap()

    # 获取窗口的位置信息
    left, top, right, bottom = win32gui.GetWindowRect(handle)
    # 窗口长宽
    width = right - left
    height = bottom - top
    # bitmap初始化
    saveBitmap.CreateCompatibleBitmap(newhdDC, width, height)
    saveDC.SelectObject(saveBitmap)
    saveDC.BitBlt((0, 0), (width, height), newhdDC, (0, 0), win32con.SRCCOPY)
    saveBitmap.SaveBitmapFile(saveDC, filename)

get_windows("PyWin32","截图.png")

import time
import win32gui, win32ui, win32con, win32api


def window_capture(filename):
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)

    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)

    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()

    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()

    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]

    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)

    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


if __name__ == "__main__":
    beg = time.time()
    for i in range(1):
        image_name = "haha%s.jpg" % i
        window_capture(image_name)
    end = time.time()
    print(end - beg)
