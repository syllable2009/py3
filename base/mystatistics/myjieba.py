import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy
import matplotlib.pyplot as plt
from os import path

str = "明明知识点都熟记于心，可是在考试的时候脑子一片空白，什么都想不起来了"
# 使用自定义字典
#自定义词典的格式：一个词占一行；每一行分三部分，一部分为词语，另一部分为词频，最后为词性（可省略），用空格隔开

# jieba.load_userdict('dict.txt')

ex_list1 = jieba.cut(str)
ex_list2 = jieba.cut(str, cut_all=True)
ex_list3 = jieba.cut_for_search(str)
print("精准模式:" + '/'.join(ex_list1))
print("全模式:" + '/'.join(ex_list2))
print("搜索引擎模式：" + '/'.join(ex_list3))
#可以看到全模式和搜索引擎模式下分词分得比精准模式更稀碎

# 定义绝对路径地址
__file__ = r"/Users/jiaxiaopeng/"
# 把路径地址字符串转换为文件路径
d = path.dirname(__file__)
# 调用包PIL中的open方法，读取图片文件，通过numpy中的array方法生成数组
backgroud_Image = numpy.array(Image.open(path.join(d, "111.jpg")))

# 绘制词云图
wc = WordCloud(
    background_color='white',  # 设置背景颜色，与图片的背景色相关
    mask=backgroud_Image,  # 设置背景图片
    font_path='./font/msyh.ttf',  # 显示中文，可以更换字体
    max_words=2000,  # 设置最大显示的字数
    stopwords={'企业'},  # 设置停用词，停用词则不再词云图中表示
    max_font_size=150,  # 设置字体最大值
    random_state=1,  # 设置有多少种随机生成状态，即有多少种配色方案
    scale=1  # 设置生成的词云图的大小
)
for i in range(0,num):#num为文件个数
 # path.join实现文件地址的链接
 text = open(path.join(d, str(i)+'.txt')).read()

chtext = ''
    with open(path.join(d, str(i)+'.txt'), 'r') as fin:
    for line in fin.readlines():
        line = line.strip('\n')
        chtext += ' '.join(jieba.cut(line))



# 传入需画词云图的文本
wc.generate(chtext)

image_colors = ImageColorGenerator(backgroud_Image)
plt.imshow(wc.recolor(color_func=image_colors))

def word_picture():


if __name__ == '__main__':
    word_picture()
