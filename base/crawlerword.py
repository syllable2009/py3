# encoding: utf-8
#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'https://www.cnblogs.com/ityouknow/p/5662753.html'
    req = requests.get(url=target)
    # print(req.text)
    html = req.text
    bf = BeautifulSoup(html)
    # <div id="content", class="showtxt">
    texts = bf.find_all('div',id='mainContent')
    print(texts[0].text.replace('\xa0' * 8, '\n\n'))
    print(texts)

#爬虫的第一步，获取整个网页的HTML信息
#第二步，解析HTML信息，提取我们感兴趣的内容,提取的方法有很多，例如使用正则表达式、Xpath、Beautiful Soup等