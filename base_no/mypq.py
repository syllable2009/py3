from pyquery import PyQuery as pq
from lxml import etree

# 首先用 lxml 的 etree 处理一下代码，这样如果你的 HTML 代码出现一些不完整或者疏漏，都会自动转化为完整清晰结构的 HTML代码
# doc = pq(etree.fromstring("<html>"))
# pq 参数可以直接传入 HTML 代码
# 直接传URL=请求了一个网页一样，类似用 urllib2 来直接请求这个链接，得到 HTML 代码
# doc = pq('http://www.baidu.com')
# 直接传某个路径的文件名
# doc = pq(filename='hello.html')


doc = pq('<div id="d1"><ul><li class="class1" id="first">first item</li><li class="class2">second item</li>')
print(type(doc))
# print(doc.html())
li = doc('li')
print(type(li))
print(li.text())

print(doc.attr("id"))
print(doc.attr("id", "hello"))

print(doc.add_class('beauty'))
print(doc.remove_attr('id'))
print(doc('#test'))
