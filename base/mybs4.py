from bs4 import BeautifulSoup
import re

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

soup = BeautifulSoup(html, "lxml")
# select('p') 返回了 所有标签名为p的tag数组
# 在进行过滤时类名前加点，id名前加 #
# print(soup.select('p')[0])
# print(soup.select('.story'))
# print(soup.select('#link3'))

# 组合查找可以分为两种，一种是在一个tag中进行两个条件的查找，一种是树状的查找一层一层之间的查找
print(soup.select('a#link2'))
print(soup.select('body p a#link2')) #层和层之间用空格分开