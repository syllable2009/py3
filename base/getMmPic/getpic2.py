import re
import os
import time
import threading
from multiprocessing import Pool, cpu_count

import requests
from bs4 import BeautifulSoup

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
}

# 下载图片保存路径
DIR_PATH = r"/Users/jiaxiaopeng/mzitu"


def get_urls():
    """
    获取 mzitu 网站下所有套图的 url
    """
    page_urls = ['http://www.mzitu.com/page/{cnt}'.format(cnt=cnt)
                 for cnt in range(1, 2)]
    print("Please wait for second ...")
    print(page_urls)
    img_urls = []
    for page_url in page_urls:
        try:
            bs = BeautifulSoup(
                requests.get(page_url, headers=HEADERS, timeout=10).text,
                'lxml').find('ul', id="pins")
            result = re.findall(r"(?<=href=)\S+", str(bs))      # 匹配所有 urls
            img_url = [url.replace('"', "") for url in result]

            img_urls.extend(img_url)
        except Exception as e:
            print(e)
    return set(img_urls)    # 利用 set 去重 urls


# lock = threading.Lock()     # 全局资源锁
# urls = get_urls()
# print(urls)

def save_pic(pic_src, pic_cnt):
    """
    保存图片到本地
    """
    try:
        time.sleep(0.10)
        img = requests.get(pic_src, headers=HEADERS, timeout=10)
        img_name = "pic_cnt_{}.jpg".format(pic_cnt + 1)
        with open(img_name, 'ab') as f:
            f.write(img.content)
            print(img_name)
    except Exception as e:
        print(e)

save_pic('https://i.meizitu.net/2019/01/29d09.jpg',1000000)