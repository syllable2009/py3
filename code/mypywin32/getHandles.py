import win32gui


#一般句柄名称都是这个窗口的title。但很多时候我们不能准确的输入title，所以我们可以通过遍历所有窗口的句柄，然后找到自己想要的窗口句柄。
#参考https://www.cnblogs.com/chenjy1225/p/12174889.html
#https://www.sohu.com/a/349817428_120372431
hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t is not "":
        print(h, t)