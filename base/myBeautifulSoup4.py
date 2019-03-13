from bs4 import BeautifulSoup

html = """  
<html><head><title>The Dormouse's story</title></head>  
<body>  
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>  
<p class="story">Once upon a time there were three little sisters; and their names were  
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and  
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;  
and they lived at the bottom of a well.</p>  
</body>  
</html>  
"""
#要解析文档内容之前，先要用BeautifulSoup实例一个对象。如下，它的类型为<class 'bs4.BeautifulSoup'>
soup = BeautifulSoup(html, "lxml")
# print(soup, type(soup))
#获取标签Tag：soup.'标签名'，就可以匹配出第一个该标签，它将会把第一次出现的该标签完整的返回
print(soup.p)
print(type(soup.p))
print(soup.p['class'])   # 没有该属性会报错
print(soup.p.attrs)     # 输出标签的属性和值
print(soup.p.get('id'))    # 推荐使用get取属性,没有返回None

#字符串：soup.find_all('p')  获取所有的P标签，返回一个列表或空列表，soup.findl('p')只返回一个或者None，类型为'bs4.element.Tag'
#列表：find_all方法也能接受列表参数，BeautifulSoup会将与列表中任一元素匹配的内容返回

plist = soup.find_all(['p'],class_='story')
print(type(plist))
print(plist)

# 正则表达式：需要导入re，再用re.compile()根据包含的正则表达式的字符串创建模式对象
print("-----------")
import re
for i in soup.find_all(re.compile('a')):
    print(i.text) # 会将a标签内的所有文本内容返回
print("-----------")
#方法(调用函数体)：如果没有合适的过滤器,我们也可以自定义一个方法，方法只接受一个元素参数
def has_class_and_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
for tag in soup.find_all(has_class_and_no_id):
    print(tag)


#2.基于select获取：css选择器，写 CSS 时，标签名不加任何修饰，类名前加.，id名前加#；返回值是一个列表
# 标签名查找：soup.select('h3 a')取h3标签下的a标签；等价于soup.select('h3 > a')

print(soup.select('p')[0])
print(soup.select('.story'))
print(soup.select('#link3'))
print("-----------")
for i in soup.select('p a'):
    # text取内容时返回的是str字符串
    result_1 = i.text
    # get_text取内容时返回的是str字符串
    result_2 = i.get_text()
    # string返回的是NavigableString，没有内容，将返回None
    result_3 = i.string
    # strings返回的是generator  如果内容为空，将返回None
    result_4 = i.strings
    print(result_1, type(result_1))
    print(result_2, type(result_2))
    print(result_3, type(result_3))
    print(result_4, type(result_4))

# 组合查找可以分为两种，一种是在一个tag中进行两个条件的查找，一种是树状的查找一层一层之间的查找
print(soup.select('a#link2'))
print(soup.select('body p a#link2')) #层和层之间用空格分开