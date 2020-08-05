import tkinter as tk


# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('自动化测试')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上设定标签
# l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签
# l.pack()
# Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();

list = ['Python','C++','Java','Go']
v = 0
list2 = []
for i in list:
    c1 = tk.Checkbutton(window, text=i, onvalue=1, offvalue=0)    # 传值原理类似于radiobutton部件
    list2.insert(v,c1)
    v = v + 1
    c1.pack()
    # c2 = tk.Checkbutton(window, text='C++', onvalue=1, offvalue=0)
    # c2.pack()
for j in list2:
    print(j.select(),end=',')

# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，
# 如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，
# 有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
