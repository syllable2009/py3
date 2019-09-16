
from bs4 import BeautifulSoup
import re
import os
import requests
import urllib.request

#操作视频地址
operatorVedioUrl ='http://www.bjtth.org/Html/News/Columns/1091/3.html'

baseUrl = 'http://www.bjtth.org/'

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'www.bjtth.org'
}

addheaders = [
    ('X-Requested-With', 'XMLHttpRequest'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                      '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'),
    ('Referer', 'www.bjtth.org')
]

def downloadVedio(url,path):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    text = r.text
    search = re.search('/Sites(.*?).mp4', text).group()
    if search:
        search = search.replace('File','video')
        urljoin = urllib.request.urljoin(baseUrl, search)
        print(urljoin,path)
        r = requests.get(urljoin,headers=headers)
        with open(path, "wb") as code:
            code.write(r.content)

if __name__ == '__main__':

    url = "https://video.fjhps.com/share/lDqRroGeAZhFEllx"
    r = requests.get(url,headers=headers)
    with open("/Users/jiaxiaopeng/bjtth/1.mp4", "wb") as code:
        code.write(r.content)

    # r = requests.get(operatorVedioUrl,headers=headers)
    # r.encoding = 'utf-8'
    # soup = BeautifulSoup(r.text, 'lxml')
    # channel = soup.select('body #zoom a')
    # for list in channel:
    #     urljoin = urllib.request.urljoin(baseUrl, list.get('href'))
    #     downloadVedio(urljoin,'/Users/jiaxiaopeng/bjtth/'+list.get('title')+'.mp4')
