import numpy
import os,jieba
from os import path
from PIL import Image
# 将所有文件夹名转换为 str 类型
folder_name = " ".join(os.listdir(r"/Users/jiaxiaopeng/git/mzitu"))
# print(folder_name)

# jieba 分词
# jieba.load_userdict(r".\data\jieba.txt")
jieba.load_userdict(r"/Users/jiaxiaopeng/git/mzitu/data/jieba.txt")
seg_list = jieba.lcut(folder_name, cut_all=False)
# print(seg_list)

# 利用字典统计词频
counter = dict()
for seg in seg_list:
    counter[seg] = counter.get(seg, 1) + 1
# print(counter)

# 根据词频排序字典
counter_sort = sorted(
    counter.items(), key=lambda value: value[1], reverse=True
)
# print(counter_sort)

