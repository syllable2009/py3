from pypinyin import pinyin, lazy_pinyin, Style


print('-'.join(lazy_pinyin(u'厦门')))
# 带音标的转换方式
print(pinyin(u'厦门'))
#多音词的转换
print(pinyin(u'厦', heteronym=True))
print(pinyin(u'中心', heteronym=True))

