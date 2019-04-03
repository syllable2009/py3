import re

#re.match() 总是从字符串“开头”去匹配，并返回匹配的字符串的match对象
str1 = 'Hello World!'
print(re.match(r'H',str1).group(0))
print(re.match(r'e',str1))

#re.search()或re.findall()可以查找字符串任意部分的出现位置
# re.search()函数将对整个字符串进行搜索，并返回第一个匹配的字符串的match对象
print(re.search(r'l', str1))

#re.findall()函数将返回一个所有匹配的字符串的字符串列表
print(re.findall(r'l',str1))

#迭代方式返回匹配，可以使用 finditer() 方法来代替
finditer = re.finditer(r'l', str1)
for f in finditer:
    print(f.span())

'''
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
'''

#常用的语法
import re #放在文件头以下省略
def refindall():     #把所有匹配的字符以元素的形式放入列表，返回一个列表
    print(re.findall('^a', '\nabc'))    #[]
    print(re.findall('^a', '\nabc', flags=re.MULTILINE))   #['a']
    print(re.findall('.', '\nabc'))    #['a', 'b', 'c']
    print(re.findall('.', '\nabc', flags=re.DOTALL))   #['\n', 'a', 'b', 'c']

def research():      #查找字符串中于正则表达式匹配的第一个位置，返回相应的MatchObject实例,后缀 .group() 方法可以取得相应的str型值
    print(re.search('a', '\nabdgc ddaad'))  #<re.Match object; span=(1, 2), match='a'>
    print(re.search('a', '\nabdgc ddaad').group())  #a   #直接以字符出返回

def resub():         #将匹配到的字符替换
    print(re.sub('正则表达式', '用来替代的字符串', '字符串'))  #返回替换后的字符串
    print(re.sub('.', 'a', '\nabdgc ddaad'))  #aaaaaaaaaaa

def resplit():       #将匹配到的字符当做列表分隔符，将分隔开的元素放在列表中返回
    print(re.split('abc', 'sldkleabcdklsabcd'))  #['sldkle', 'dkls', 'd']

def rematch():       #只在字符串开头位置开始匹配，返回MatchObject实例,使用.group()获取值
    print(re.match('abc', 'sldkleabcdklsabcd'))  #None  #匹配不到返回None
    print(re.match('abc', 'abcabcsldkledklsabcd'))  #<re.Match object; span=(0, 3), match='abc'>
    print(re.match('abc', 'abcabcsldkledklsabcd').group())  #abc


#*,+,?都是贪婪匹配，也就是尽可能的匹配 后面加？使其变成惰性匹配


