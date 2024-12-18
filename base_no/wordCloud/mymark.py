import os
root = "/Users/jiaxiaopeng/"

#1.准备字符串
total = ""

file_list = os.listdir(root)
for file in file_list:
# //处理md文件
    if os.path.splitext(file)[1] == ".md":
        path = os.path.join(root,file)
        text = open(path, encoding='utf-8').read()
        # //最终得到的字符串
        total = total + "\n" + text
    # print(os.path.splitext(file)[1])
    # print(os.path.join(root,file))

text = open("flow.md", encoding='utf-8').read()
total = total + "\n" + text

# print(total)

#2.生成词聘
import jieba
import re
# 正则只留下中文
rec = re.compile("[^\u4E00-\u9FA5]")
total = rec.sub("", total)
wordlist = jieba.cut(total, cut_all=True)
wl = " ".join(wordlist)
print(wl)

#3。最后就是生成词云，采用WordCloud的库
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wc = WordCloud(
    # 设置背景颜色
    background_color="white",
    # 设置最大显示的词云数
    max_words=200,
    # 这种字体都在电脑字体中，window在C:\Windows\Fonts\下，mac下的是/System/Library/Fonts/PingFang.ttc 字体
    font_path='/System/Library/Fonts/PingFang.ttc',
    height=2000,
    width=2000,
    collocations=False,
    # 设置字体最大值
    max_font_size=250,
    # 设置有多少种随机生成状态，即有多少种配色方案
    random_state=300
)
myword = wc.generate(wl)  # 生成词云
# 展示词云图
plt.imshow(myword)
plt.axis("off")
wc.to_file('blog.png')  # 保存图片
plt.ion()
plt.pause(5)
plt.close()  # 图片显示5s，之后关闭