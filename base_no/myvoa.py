
# from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import urllib.request

url = 'http://m.51voa.com/hollywood-stars-executives-charged-in-college-admission-plot-81613'
response = urllib.request.urlopen(url)
getcode = response.getcode()

if getcode == 200:
    print("request ok")
    pass
content = response.read().decode('utf-8')

#Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器
#lxml 解析器更加强大，速度更快，推荐安装
soup = BeautifulSoup(content, 'lxml')
category = soup.select('#nav a')[2].string
print("category",category)
title = soup.select_one('#title')
print("title:",title.string)
# content = soup.select_one("#ShowEN")
# print(content.get_text())
src = soup.select('div.test li div a')
next = src[0].get("href")
src = src[1].get("href")

print(next)
print(src)
baseUrl = 'http://m.51voa.com/'
urljoin = urllib.request.urljoin(baseUrl, next)
print(urljoin)
# print("next:",soup.select('script')[2])
# print("next:",soup.select('script')[2])


#1.获取名称
# 通过这种soup.标签名,如果文档中有多个这样的标签，返回的结果是第一个标签的内容
# 当我们通过soup.title.name的时候就可以获得该title标签的名称，即title
# print(soup.title.name)

#2.获取属性:两种方式都可以获取p标签的name属性值,没有该属性会报错
# print(soup.div.attrs['id'])
# print(soup.div['id'])

#3.获取内容
# print(soup.title.string)

#4.嵌套选择
# print(soup.body.div.div.a['href'])

#5.子节点和子孙节点：将p标签下的所有子标签存入到了一个列表中
# print(soup.p.contents)

#6.children
# print(soup.p.children)
# for i,child in enumerate(soup.p.children):
#     print(i,child)

#7.通过contents以及children都是获取子节点，如果想要获取子孙节点可以通过descendants
# print(soup.descendants)#同时这种获取的结果也是一个迭代器


#
# print(soup.find_all('ul')[0])
# for ul in soup.find_all('ul'):
#     print(ul.find_all('li'))
# print(soup, type(soup))

# print(soup.prettify())

# print(soup.title.name)


# print(soup.title.parent.name)



# print(soup.p.attrs['name'])
# print(soup.p['test'])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='ShowEN'))
# print(soup.select(".content")[0].get_text())
# print(soup.find(id='ShowEN'))
# .text

# print(soup.select('#nav a')[-1].get_text())

# nextPage = soup.select(".test a")[0]['href'];
# baseUrl = 'http://m.51voa.com/new-center-brings-technology-to-traditional-games-81169'
# combineUrl = urllib.parse.urljoin(baseUrl,nextPage)
# print(combineUrl)
# print(soup.select(".test a")[1]['href'])

