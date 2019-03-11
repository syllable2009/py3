# encoding: utf-8
#!/usr/bin/python



import urllib.request
import re
import urllib.parse
from bs4 import BeautifulSoup


def crawling():
    req = urllib.request.urlopen('http://www.imooc.com/course/list?c=python')  #访问网页
    html=req.read().decode("utf-8") #读取该网页的html代码，同时将其转换为utf-8编码
    print(html)
    #html=req.read().decode("gbk")
    reg=r'src="(.+?\.jpg)"'  #正则表达式，匹配当前图片的字符
    imgre=re.compile(reg)    #创建正则表达式的例子
    imglist=imgre.findall(html)  #在html中找到匹配的项
    count=1

    for img in imglist:
        print(img)
        img_add=urllib.parse.urljoin("http:",img)  #通过解析该匹配项的绝对地址，因为提取到的项都是相对位置，需要进行转换
        #对于urljoin()，第一个参数是基础母站的url，第二个是需要拼接成绝对路径的url。即使后者完全没有前者的内容，也可以，如果后者为完整的则以后面为主
        print(img_add)
        f=open("/Users/jiaxiaopeng/py3test/"+str(count)+".jpg",'wb')
        img_html=urllib.request.urlopen(img_add)
        picture=img_html.read()
        # f.write(picture)
        f.close()
        count+=1

# crawling()

def crawling2():
        url = "http://www.qiushibaike.com/imgrank/"
        print(url)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        req = urllib.request.Request(url, headers={
            'User-Agent': user_agent
            })
        response = urllib.request.urlopen(req)
        content = response.read().decode('utf-8')
        # print(content)
        return content


import bs4
print(bs4.__file__)

content = crawling2()
url = "http://www.qiushibaike.com/imgrank/"
#原生的html.parser解析速度一般而且对中文支持不是很好
soup = BeautifulSoup(content, "lxml")


items1 = soup.select("div.author a img")
items2 = soup.select("a div.content span")
items3 = soup.select("div.thumb a img")
items = soup.select("#content-left")
print(items)

for item in items2:
    # print(item)
    # print(urllib.parse.urljoin(url,item['src']))
    pass
for item in items3:
    # print(urllib.parse.urljoin(url,item['src']))
    pass