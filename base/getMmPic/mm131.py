import requests
import re
from bs4 import BeautifulSoup
import time
import os

max_page_reg=re.compile(u'<div class="content-page"><span class="page-ch">.*?(\d+).*?</span>')
root_dir = '/Users/jiaxiaopeng/mm131/xinggan/'
host='http://www.mm131.com'
headers={
    'Referer':'http://www.mm131.com/'
    ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
parent='mm131'
list_pattern={
        u'性感美女':{'page1':'/xinggan/','page':'/xinggan/list_6_{page}.html','slug':'xinggan'}
        # ,u'清纯美女':{'page1':'/qingchun/','page':'/qingchun/list_1_{page}.html','slug':'qingchun'}
        # ,u'大学校花':{'page1':'/xiaohua/','page':'/xiaohua/list_2_{page}.html','slug':'xiaohua'}
        # ,u'性感车模':{'page1':'/chemo/','page':'/chemo/list_3_{page}.html','slug':'chemo'}
        # ,u'明星写真':{'page1':'/mingxing/','page':'/mingxing/list_5_{page}.html','slug':'mingxing'},
        # u'旗袍美女':{'page1':'/qipao/','page':'/qipao/list_4_{page}.html','slug':'qipao'}
        }
cate_dict={}


def make_dir(folder_name):
    """
    新建文件夹并切换到该目录下
    """
    path = os.path.join(root_dir, folder_name)
    # 如果目录已经存在就不用再次爬取了，去重，提高效率。存在返回 False，否则反之
    if not os.path.exists(path):
        os.makedirs(path)
        # print(path)
        # os.chdir(path)
    return True

def get_max_page(url):
    r=requests.get(url, headers=headers)
    pages=re.findall('''<a href='list_\d+_(\d+)\.html' class="page-en">''',r.text)
    pages=map(int,pages)
    max_page=max(pages)
    return max_page

def get_max_subid(url):
    try:
        r=requests.get(url,headers=headers)
        max_page=int(max_page_reg.findall(r.content.decode('gbk'))[0])
        return max_page
    except Exception as e:
        print(e)
        return False





def get_page_list(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    # aList = soup.find_all("dl",class_=["list-left public-box"])
    aList = soup.select('div.main dl dd a')
    print(len(aList))
    for per in aList:
        # print(per.string)
        if(per.string == None):
            try:
                handle_page(per.get('href'),per.contents[0].get('alt'))
            except:
                continue

            # print(per.get('href'),per.contents[0].get('alt'))
        else:
            break


# img_base='http://img1.mm131.me/pic/{pid}/{subid}.jpg'

# r=requests.get(url,headers=headers)
# get_page_list('http://www.mm131.com/xinggan/list_6_3.html')

def get_real_jpg_url(url):
    res = requests.get(url, headers=headers)
    # print(res.content)
    soup = BeautifulSoup(res.content.decode('gbk'), 'lxml')
    jpg = soup.select_one('body div.content div.content-pic a img')
    return jpg.get('src')


def save_pic(pic_src,dir_name,pic_no):
    """
    保存图片到本地
    """
    try:
        time.sleep(0.25)
        make_dir(dir_name)
        img = get_real_jpg_url(pic_src)
        r = requests.get(img, headers=headers)
        img_name = root_dir+dir_name+"/{}_{}.jpg".format(dir_name,pic_no)
        with open(img_name, 'ab') as f:
            f.write(r.content)
            print(img_name)
    except Exception as e:
        print(e)

def handle_page(url,alt):
    save_pic(url, alt, 1)
    max_subid = get_max_subid(url)
    rfind = url[: url.rfind('.')]
    # print("max_subid:",max_subid)
    for i in range(2,max_subid+1):
        next_pic_url = rfind + "_" + str(i) + ".html";
        # print(next_pic_url)
        save_pic(next_pic_url,alt,i)
    # r = requests.get(url, headers=headers)
    # soup = BeautifulSoup(r.content, 'lxml')

if __name__ == '__main__':
    for key in list_pattern:
        # print("key",key)
        # cate_dict[list_pattern[key]['slug']]=key
        index_page = host+list_pattern[key]['page1']
        # get_page_list(index_page)
        print("index",index_page)
        max_page = get_max_page(index_page)
        for page in range(86,max_page+1):
            page_list = host+list_pattern[key]['page'].format(page=page)
            get_page_list(page_list)




# get_page_list('http://www.mm131.com/xinggan/list_6_150.html')
# handle_page('http://www.mm131.com/xinggan/1731.html','xinli')
# URL = 'http://www.mm131.com/xinggan/1731.html'
# save_pic('http://www.mm131.com/xinggan/1731.html','xinli', 1)
# print(get_real_jpg_url('http://www.mm131.com/xinggan/1731.html'))

