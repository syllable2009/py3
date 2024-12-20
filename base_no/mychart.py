# import numpy as np
# import matplotlib.pyplot as plt
# x= np.linspace(0, 2, 100)
# # print(x)
# x2= np.linspace(1, 6, 100)
# x3= np.linspace(3, 5, 100)
# plt.plot(x, x, label='linear')
# plt.plot(x2, x2, label='quadratic')
# plt.plot(x3, x3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# # plt.show()
#
#
# import numpy as np
# import matplotlib.pyplot as plt
# size = 5
# a = np.random.random(size)
# b = np.random.random(size)
# c = np.random.random(size)
# x = np.arange(size)
# # 有多少个类型，只需更改n即可
# total_width, n = 0.8, 3
# width = total_width / n
# # 重新拟定x的坐标
# x = x - (total_width - width) / 2
# # 这里使用的是偏移
# plt.bar(x, a, width=width, label='a')
# plt.bar(x + width, b, width=width, label='b')
# plt.bar(x + 2 + width, c, width=width, label='c')
# plt.legend()
# # plt.show()

import matplotlib.pyplot as plt
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
# 设置分离的距离，0表示不分离
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
shadow=None, startangle=90)
# Equal aspect ratio 保证画出的图是正圆形
plt.axis('equal')
plt.show()