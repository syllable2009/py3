from bs4 import BeautifulSoup
import requests
import urllib
import os


start_url="http://www.mzitu.com/"
path = '/Users/jiaxiaopeng/mzitu-pictures/{title}'

header = {
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
"host":"www.mzitu.com",
"cookie":"Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1552646036; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1552646036",
"authority":"www.mzitu.com",
"referer": "https://www.mzitu.com/171699/9",
"upgrade-insecure-requests":"1",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh,en;q=0.9,en-US;q=0.8,am;q=0.7,zh-CN;q=0.6",
"cache-control": "no-cache",
"pragma": "no-cache",
'Connection': 'keep - alive',

}

headers = {
    'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
    'Accept - Encoding': 'gzip, deflate',
    'Accept - Language': 'zh - CN, zh;q = 0.9',
    'Cache - Control': 'max - age = 0',
    'Host': 'www.mzitu.com',
    'Upgrade - Insecure - Requests': '1',
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 66.0.3359.117 Safari / 537.36'
}

def findStorePath(filePath):
    path_format = path.format(title=filePath)
    exists = os.path.exists(path_format)
    if not exists:
        os.mkdir(path_format)
    else:
        pass
    return path_format


def getRequest(url):
    web_data = requests.get(url)
    # print(web_data.status_code)
    return BeautifulSoup(web_data.text, 'lxml')

#获取妹子图首页热门专题的链接
def get_mei_channel(url):
    soup = getRequest(url)
    # print(soup)
    channel = soup.select('body ul#menu-nav li a')
    # print(channel)
    for list in channel:
        print(list.get('href'))

# get_mei_channel(start_url)

def get_mei_all(url):
    soup = getRequest(url)
    postlist = soup.select('body div.main-content div.postlist ul#pins li')[0]
    for post in postlist:
        alist = post.children #取标签下的.contents 和 .children，仅包含tag的直接子节点
        for a in alist:
            name = a.name
            if 'img'== name:
                pass
            elif 'a'== name:
                print(a.get('href'))
                print(a.string)
            else:
                print(a)

# get_mei_all(start_url)

def deal_per_post(href):
    href = href + "/"
    soup = getRequest(href)
    span = soup.select('body div.content div.pagenavi span')[-2]
    for i in range(47,int(span.string)+1):
        img_add = urllib.parse.urljoin(href, str(i))
        print("img_add",img_add)
        download_post(img_add)
        # # 取第一个图片
        # img = soup.select_one('body div.content div.main-image p a img')
        # download_post(img.get('src'), img.get('alt'))

def download_post(href):
    soup = getRequest(href)
    img = soup.select_one('body div.content div.main-image p a img')
    get = img.get('alt')
    # print(get)
    img_src = img.get('src')

    # store_path = findStorePath(img.get('alt'))
    # find = img_src.rfind('/')
    print("img_src",img_src)
    r = requests.get('https://i.meizitu.net/2019/01/29d09.jpg',headers = header)
    print(r.status_code)
    # find_ = store_path + img.get('alt')+'/'+ img_src[find + 1:]
    # findStorePath(find_)
    with open("/Users/jiaxiaopeng/mzitu-pictures/a.jpg", "wb") as f:
        f.write(r.content)

deal_per_post('https://www.mzitu.com/171699')

# url = 'https://i.meizitu.net/2019/01/29d06.jpg'
# url="https://www.mzitu.com/all/"
# r = requests.get(url, headers=headers)
# cookies = str(r.cookies.get_dict())
# print(cookies)


# print(r.status_code)
# find_ = '/Users/jiaxiaopeng/mzitu-pictures/a.jpg'
# with open(find_, "wb") as f:
#     f.write(r.content)



