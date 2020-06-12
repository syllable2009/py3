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