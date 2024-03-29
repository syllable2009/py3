import re


'''
str1 = 'Hello World!'
#第一个字符是 r，表示 raw string 原生字符，意在声明字符串中间的特殊字符不用转义

#re.match() 总是从字符串开头去匹配，并返回匹配的字符串的match对象
print(re.match(r'He',str1).group(0))
print(re.match(r'e',str1))
print('-------------')
#compile
pattern = re.compile(r'l', re.I) # re.I不区分大小写
print(type(pattern))
print('-------------')
# re.search()函数将对整个字符串进行搜索，并返回第一个匹配的字符串的match对象
search = re.search(r'l', str1)
print(type(search))
print(search.group(0))
print('-------------')
#re.findall()函数将返回一个所有匹配的字符串的字符串列表
findall = pattern.findall(str1) #re.search()或re.findall()可以查找字符串任意部分的出现位置
print(type(findall))
print(findall)
print('-------------')
#迭代方式返回匹配，可以使用 finditer() 方法来代替
finditer = re.finditer(r'l', str1)
for f in finditer:
    print(f.span())


常用的正则表达式符号:
1  '.'      # 默认匹配换行符(\n)之外的任意一个字符；flags=re.DOTALL(将换行符也匹配出来)
2  '^'      # 匹配字符串开头；flags=re.MULTILINE(如果开头为换行符或者其他特殊，可以从换行符后面开始匹配)
3  '$'      #匹配字符串结尾；flags=re.MULTILINE(如果字符串有换行符的话换行符前的字符也可以在行尾匹配)
4  '*'      #匹配*号前面的字符0次或者多次[0, +oo]
5  '+'      #匹配前一个字符1次或者多次[1, +oo]
6  '?'      #匹配前一个字符1次或者0次
7  '{m}'    #匹配前一个字符m次
8  '{n, m}' #匹配前一个字符n到m次
9  '|'      #匹配|左边或者|右边的字符
10 '(...)'  #匹配括号中的任意正则表达式
包含'\'的正则表达式特殊序列:
11 \d  #匹配任何十进制数：它相当于类[0-9]
12 \D  #匹配任何非数字字符：它相当于[^0-9]
13 \s  #匹配任何空白字符：它相当于类[ \t\n\r\f\v]
14 \S  #匹配任何非空白字符：它相当于类[^ \t\n\r\f\v]
15 \w  #匹配任何字母数字字符：它相当于类[a-zA-Z0-9]
16 \W  #匹配任何非数字字母字符：它相当于[^a-zA-Z0-9]
17 \b  #匹配一个单词边界，也就是指单词和空格间的位置
18 '[a-zA-Z0-9]' 匹配所有的大小写字母数字
'''

# 普通的内置方法代码查找，找不到有异常
def index(str,keyword):
    print(str.index(keyword) > -1)
    print(keyword in str)

# 这个例子只是方便我们理解正则表达式，这个正则表达式的写法是毫无意义的,正则表达式的灵魂在于规则，所以这样做意义不大
def find_all(keyword,str):
    findall = re.findall(keyword, str)
    if len(findall) > 0:
        print('str含有“两点水”这个字符串')
    else:
        print('str不含有“两点水”这个字符串')

#常用的语法
# import re #放在文件头以下省略
# def refindall():     #把所有匹配的字符以元素的形式放入列表，返回一个列表
#     print(re.findall('^a', '\nabc'))    #[]
#     print(re.findall('^a', '\nabc', flags=re.MULTILINE))   #['a']

# def research():      #查找字符串中于正则表达式匹配的第一个位置，返回相应的MatchObject实例,后缀 .group() 方法可以取得相应的str型值
#     print(re.search('a', '\nabdgc ddaad'))  #<re.Match object; span=(1, 2), match='a'>
#     print(re.search('a', '\nabdgc ddaad').group())  #a   #直接以字符出返回

# def resub():         #将匹配到的字符替换
#     print(re.sub('正则表达式', '用来替代的字符串', '字符串'))  #返回替换后的字符串


# def resplit():       #将匹配到的字符当做列表分隔符，将分隔开的元素放在列表中返回
#     print(re.split('abc', 'sldkleabcdklsabcd'))  #['sldkle', 'dkls', 'd']

# def rematch():       #只在字符串开头位置开始匹配，返回MatchObject实例,使用.group()获取值
#     print(re.match('abc', 'sldkleabcdklsabcd'))  #None  #匹配不到返回None
#     print(re.match('abc', 'abcabcsldkledklsabcd'))  #<re.Match object; span=(0, 3), match='abc'>
#     print(re.match('abc', 'abcabcsldkledklsabcd').group())  #abc


#*,+,?都是贪婪匹配，也就是尽可能的匹配 后面加？使其变成惰性匹配
import requests
if '__main__' == __name__:
    # 比如在一段字符串中寻找是否含有某个字符或某些字符，通常我们使用内置函数来实现，如下
    str = "两点水|twowater|liangdianshui|草根程序员|ReadingWithU"
    # index(str,"两点水")
    # re.findall('两点水', str) 该函数实现了在字符串中找到正则表达式所匹配的所有子串，并组成一个列表返回
    # find_all("两点水",str)
    re_findall = re.findall('[a-z]', str)
    print(re_findall)


    # str = 'https://box.bdimg.com/static/fisp_static/common/img/searchbox/logo_news_276_88_1f9876a.png,https://log.news.baidu.com/v.gif'
    # m = re.match(r'(https+://.+?(gif|png)$)', '')
    # print(m.groups())
    # get = requests.get('http://news.baidu.com/ent')
    # get.encoding = 'utf-8'
    # print(get.text)
    # # r'https://.*?(png|gif)'
    # r'https://.*?(png|gif)'
    # # re_compile = re.compile(r'^(http).+(.png|.jpg)$')
    # re_compile = re.compile(r'^(https?://)(.+?)(?:gif|png)$')
    # re_compile = re.compile('(.+?)(\.gif|\.jpeg|\.png|\.jpg|\.bmp)')
    # re_compile = re.compile('(https+.+?)(\.gif|\.jpeg|\.png|\.jpg|\.bmp)')
    # findall = re.findall(re_compile,get.text)
    # findall = set(findall)
    # for x in findall:
    #     print(''.join(x))





