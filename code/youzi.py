from bs4 import BeautifulSoup
from pathlib import Path
import csv
import os
import requests
import time

_headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
path = '/Users/jiaxiaopeng/youzi4'


def request(_url):
    r = requests.get(_url, headers=_headers,
                     timeout=2.5)
    if r.status_code != 200:
        print('request {} state is {}'.format(r.url, r.status_code))
        return None
    r.encoding = 'utf-8'
    return r.text


def listPage():
    pass


def firstPage(pic_num):
    detailUrl = 'https://www.youzi4.com/tgod/{}.html'.format(pic_num)
    html = request(detailUrl)
    if html is not None:
        soup = BeautifulSoup(html, "lxml")
        soup_a = soup.select('.page ul li a')[0]
        num = getTotalPageNum(soup_a.get_text())
        select = soup.select('#nextPageTagA img')[0]
        tag_name = select.get('alt')
        download(select.get('src'), tag_name)
        for i in range(2, num + 1):
            time.sleep(2)
            detailPage(pic_num + '_' + str(i), tag_name)


def detailPage(pic_num, tag_name):
    detailUrl = 'https://www.youzi4.com/tgod/{}.html'.format(pic_num)
    # print(detailUrl)
    html = request(detailUrl)
    if html is not None:
        soup = BeautifulSoup(html, "lxml")
        select = soup.select('#nextPageTagA img')[0]
        download(select.get('src'), tag_name)


def download(image_url, tag_name):
    try:
        exist = Path(path +'/'+ tag_name)
        if (not exist.exists()):
            exist.mkdir(exist_ok=True, parents=True)
        name = exist / Path(image_url).name
        with open(name.absolute(), 'wb') as f:
            img = requests.get(image_url, headers=_headers,
                     timeout=5).content
            f.write(img)
    except OSError as e:
        print('download failed,{}'.format(e))


def getTotalPageNum(string):
    iterator = filter(str.isdigit, string)
    return int(''.join(iterator))

def getFirsetCat(url):
    html = requests(url)

    if html is not None:
        soup = BeautifulSoup(html, "lxml")
        list = soup.select('#nextPageTagA img') #找出本页列表
        max_num = 0;
    pass


filename = Path("youzi4.txt")

if '__main__' == __name__:
    print('task start->')
    # exist = filename.exist() #判断文件
    # exist = filename.is_file()
    # if(not exist):
    #     filename.touch()
    # print("文件存在：{}".format(exist))
    # url = 'https://www.youzi4.com/tgod/2302.html';
    firstPage('2302')
    # data = [('ab','bc')]
    # with open(filename, 'a+') as csv_file:
    #     csv_writer = csv.writer(csv_file, dialect='excel',delimiter=',')
    #     for row in data:
    #         csv_writer.writerow(row)
    # exist = Path(path + '123' + '/')
    # image_url = '123/345/abc.jpg'
    # file_name = exist.absolute() + '/' + Path(image_url).name
    # print(exist / Path(image_url).name)
    # print(Path('https://www.youzi4.com/d/file/090818/1a69bc04-37b3-4182-bc97-4984855ecc2f.jpg').name)
