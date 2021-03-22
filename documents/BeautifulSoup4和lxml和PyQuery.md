lxml和BeautifulSoup4库是HTML/XML的解析器，主要的功能也是如何解析和提取 HTML/XML 数据
lxml 只会局部遍历，而Beautiful Soup 是基于HTML DOM（Document Object Model）的，会载入整个文档，解析整个DOM树，因此时间和内存开销都会大很多，所以性能要低于lxml
BeautifulSoup 用来解析 HTML 比较简单，API非常人性化，支持CSS选择器、Python标准库中的HTML解析器，也支持 lxml 的 XML解析器。

正则解析也是可行的办法，解析速度最快，但是使用难度最难

要解析文档内容之前，先要用BeautifulSoup实例一个对象。如下，它的类型为<class 'bs4.BeautifulSoup'>
soup = BeautifulSoup(html,"lxml") #使用lxml来进行解析
缩进格式
print(bs.prettify())

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
#四个常用的对象：
Tag
NavigatableString
BeautifulSoup
Comment 
 
1.Tag 通俗点讲就是 HTML 中的一个个标签。 它有两个重要的属性，分别是name和attrs
print soup.p 获取第一个符合条件的标签# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
print type(soup.p) # <class 'bs4.element.Tag'> 
print soup.head.name #soup 对象本身比较特殊，它的 name 即为 [document]，其他为为标签本身的名称
print soup.p.attrs #把 p 标签的所有属性打印输出了出来，得到的类型是一个字典 
print soup.p['class'] # soup.p.get('class') #获取某一个标签属性
2.NavigatableString
print soup.p.string #获取标签中的文字
print type(soup.p.string) #<class 'bs4.element.NavigableString'>
3.BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象,它支持 遍历文档树 和 搜索文档树 中描述的大部分的方法
因为 BeautifulSoup 对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性.但有时查看它的 .name 属性是很方便的,所以 BeautifulSoup 对象包含了一个值为 “[document]” 的特殊属性 .name
4.Comment 文档的注释部分,是一个特殊类型的 NavigableString 对象
comment = soup.b.string # <!--Hey, buddy. Want to buy a used parser?-->
type(comment) # <class 'bs4.element.Comment'>

# 遍历文档树：
1. contents和children：
head_tag = soup.head
print(head_tag.contents)# 返回所有子节点的列表
for child in head_tag.children: # 返回所有子节点的迭代器
    print(child)
2.strings 和 stripped_strings
如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取,使用 .stripped_strings 可以去除多余空白内容
for string in soup.stripped_strings:
    print(repr(string))

# 搜索文档树  
1. find和find_all方法： #第一个参数是标签的名字，要使用标签属性进行过滤，那么可以在这个方法中通过关键字参数的形式，
将属性的名字以及对应的值传进去。或者是使用attrs属性，将所有的属性以及对应的值放在一个字典中传给attrs属性 
soup.find_all("a",attrs={"id":"link2"}) 或者soup.find_all("a",id='link2')
2. select方法：结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容
有时候使用css选择器的方式可以更加的方便。使用css选择器的语法，应该使用select方法
print(soup.select('a')) #通过标签名查找
print(soup.select('.sister')) #通过类名，则应该在类的前面加一个.
print(soup.select("#link1")) #通过id查找，应该在id的名字前面加一个＃号
print(soup.select("p #link1")) #组合查找，二者需要用空格分开，表示子父关系
print(soup.select("head > title")) #直接子标签查找
print(soup.select('a[href="http://example.com/elsie"]')) #通过属性查找


def function(arg,*args,**kwargs):
    print(arg,args,kwargs)

function(6,7,8,9,a=1, b=2, c=3)

PyQuery 是 Python 仿照 jQuery 的严格实现。语法与 jQuery 几乎完全相同。
BeautifulSoup 用来解析 HTML 比较简单，API非常人性化，支持CSS选择器、Python标准库中的HTML解析器，也支持 lxml 的 XML解析器
lxml是python的一个解析库，支持HTML和XML的解析，支持XPath解析方式，而且解析效率非常高

1.BeautifulSoup
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:　Tag　　NavigableString　　BeautifulSoup　　Comment  。
Tag:  即我们在写网页时所使用的标签（如<a>超链接标签）
NavigableString：简单的说就是一种可以遍历的字符串

python的正则
正则表达式使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串。
import re

str1 = 'Hello World!'
#compile
pattern = re.compile(r'l', re.I) # #第一个字符是 r，表示 raw string 原生字符，意在声明字符串中间的特殊字符不用转义,re.I不区分大小写
findall = pattern.findall(str1) #re.findall()函数将返回一个所有匹配的字符串的字符串列表[]

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
18 '[a-zA-Z0-9]' 匹配所有的大小写字母数字
'''