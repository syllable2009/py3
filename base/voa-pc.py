import urllib.request
from bs4 import BeautifulSoup
import time
import os
import pymysql
# import sys
# import pprint
# sys.path.append("/Users/jiaxiaopeng/git/py3/mydbutils2.py")
# pprint.pprint(sys.path)
import mydbutils1

# url = 'http://www.51voa.com/Technology_Report_1.html'

# response = urllib.request.urlopen(url)


def insertDb(title=None,cn_tag=None,en_tag=None,href=None,content=None,date=None,create_time=None):
    pool = mydbutils1.get_db_pool(False)
    conn = pool.connection()
    cursor = conn.cursor()
    sql = "insert into special_voa(cat_cn,cat_en,title,content,date,href,create_time) " \
          "values(%s,%s,%s,%s,%s,%s,%s)"
    var = (cn_tag,en_tag,title,content,date,href,create_time)

    execute = cursor.execute(sql,var)
    conn.commit()
    # print("插入id：",execute.lastrowid)
    conn.close()




def getRequestList(url):
    soup = requestPage(url)
    lilist = soup.select("#list ul li")
    for li in lilist:
        a = li.a
        print(a.get('href').strip())
        print(a.get_text().strip())
        times = li.get_text().replace(a.get_text().strip(), '').strip()
        replace = times.replace('(', '20').replace(')','')

        # insertDb(title=a.get_text().strip(),en_tag='Technology Report',cn_tag='科技报道',date=replace,create_time=time.localtime())
        # print(replace)

def handleSinglePage(url):
    print(url)
    soup = requestPage(url)
    mp3 = soup.select_one('#mp3').get('href')
    content = soup.select_one('#content').get_text()
    print(content)
    print(mp3)
    local = os.path.join('/Users/jiaxiaopeng/VOA_Special_English/Technology Report', '1.mp3')
    # urlretrieve(url, [filename=None, [reporthook=None, [data=None]]])
    urllib.request.urlretrieve(mp3, local)
    # insertDb(href=mp3,content=content)


def requestPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    res = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(res)
    html = response.read().decode('utf-8')
    return BeautifulSoup(html, "lxml")

# url = urllib.request.urljoin(baseUrl, '/Technology_Report_1.html')
# handleSinglePage('http://www.51voa.com/VOA_Special_English/as-web-turns--creator-calls-for-big-changes-to-make-it-better-81612.html')
if __name__ == '__main__':
# def test():
    baseUrl = 'http://www.51voa.com/'
    for num in range(1, 2):
        nextPage = 'Technology_Report_%s.html' % num
        url = urllib.parse.urljoin(baseUrl, nextPage)
        print(url)
        soup = requestPage(url)
        lilist = soup.select("#list ul li")

        for li in lilist:
            a = li.a
            subUrl = a.get('href').strip()
            print("subUrl",subUrl)
            title = a.get_text().strip()
            print("title",title)
            times = li.get_text().replace(a.get_text().strip(), '').strip()
            replace = times.replace('(', '20').replace(')', '')
            print("date", replace)
            url = urllib.parse.urljoin(baseUrl, subUrl)
            soup = requestPage(url)
            mp3 = soup.select_one('#mp3').get('href')
            content = soup.select_one('#content').get_text()
            find = mp3.rfind('/')
            local = os.path.join('/Users/jiaxiaopeng/VOA_Special_English/Technology Report', mp3[find + 1:])
            urllib.request.urlretrieve(url, local)
            insertDb(en_tag='Technology Report',cn_tag='科技报道',title=title,href=mp3, content=content,date=replace,create_time=time.localtime())

