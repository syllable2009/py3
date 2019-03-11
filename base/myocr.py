import pytesseract
from PIL import Image

# open image
image = Image.open('/Users/jiaxiaopeng/validCode.png')
code = pytesseract.image_to_string(image, lang='chi_sim+eng')
print(code)

#print(''.join([''.join([('sergiojune'[(x-y)%10]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

# itertools中的函数大多是返回各种迭代器对象
import itertools
x = itertools.accumulate(range(10))
print(list(x))


import plotly.plotly as py
import numpy as np
data = [dict(
    visible=False,
    line=dict(color='#00CED1', width=6), # 配置线宽和颜色
    name='𝜈 = ' + str(step),
    x=np.arange(0, 10, 0.01), # x 轴参数
    y=np.sin(step * np.arange(0, 10, 0.01))) for step in np.arange(0, 5, 0.1)] # y 轴参数
data[10]['visible'] = True
py.offline.plot(data, filename='Single Sine Wave')
