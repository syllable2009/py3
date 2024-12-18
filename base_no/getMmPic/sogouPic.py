import requests
from bs4 import BeautifulSoup

url='https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%E7%BE%8E%E5%A5%B3&tag=%E5%85%A8%E9%83%A8&start=45&len=15'
# url = 'https://pic.sogou.com/pics/recommend?category=%C3%C0%C5%AE&from=result#%E5%85%A8%E9%83%A8'


HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'https://pic.sogou.com/pics/recommend?category=%C3%C0%C5%AE&from=result',
    # 'Cookie': 'IPLOC=CN1100; SUV=00E341DD676BD8E75C94AD5FAFF06880; JSESSIONID=aaabp3EnXWTCR8qWtXKMw; tip_show_home_search=20190322; SUID=E7D86B671620940A000000005C94AD60; SNUID=FFC1727E191C9CB2BBA9C16F19C37D25; ld=syllllllll2tO3C0lllllVhUrQGlllllBLsYiZllll9lllllVklll5@@@@@@@@@@; tip_show=20190322; ABTEST=0|1553247689|v1',
    'Host': 'pic.sogou.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01'


}

url = 'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%E5%A3%81%E7%BA%B8&tag=%E5%85%A8%E9%83%A8&start=0&len=15 '
img_result = requests.get(url, headers=HEADERS, timeout=60)
soup = BeautifulSoup(img_result.content, 'lxml')
alist = soup.select('a img')
print(alist)

