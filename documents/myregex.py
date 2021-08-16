import re

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

'''
[]:字符集一对方括号里面的字符关系是"或（OR）"关系,如果是连续的字母，数字可以使用-来代替,'u[abc]v' u[a-c]v'
^:对字符集取反,取反字符集必须要匹配一个字符,q[^u]
\d 相当于 [0-9] ,匹配所有数字字符
\D 相当于 [^0-9] ， 匹配所有非数字字符
\w 匹配包括下划线的任何单词字符，等价于 [A-Za-z0-9_]
{min,max} \b[1-9][0-9]{3}\b
?：告诉引擎匹配前导字符 0 次或 1 次 非贪婪模式[a-z]{4,7}?
+：告诉引擎匹配前导字符 1 次或多次
*：告诉引擎匹配前导字符 0 次或多次
'''

if '__main__' == __name__:
    # 比如在一段字符串中寻找是否含有某个字符或某些字符，通常我们使用内置函数来实现，如下
    str = "两点水|twowater|liangdianshui|草根程序员|ReadingWithU"
    # index(str,"两点水")
    # re.findall('两点水', str) 该函数实现了在字符串中找到正则表达式所匹配的所有子串，并组成一个列表返回
    # find_all("两点水",str)
    re_findall = re.findall('[a-z]', str)
    print(re_findall)