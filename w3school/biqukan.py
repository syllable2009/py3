# encoding: utf-8
#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import time

url = 'http://www.biqukan.com/1_1094/5403177.html'
headers = '';

def getUrlContext(url):
    resp = requests.get(url=url, headers=headers)
    resp.raise_for_status()
    resp.encoding = 'gb2312'
    # print(resp.text)
    # soup = BeautifulSoup(resp.text, "lxml")

def getUrlImages(url):
    resp = requests.get(url=url, headers=headers,verify=False)
    resp.raise_for_status()
    resp.encoding = 'utf-8'
    return BeautifulSoup(resp.text, "lxml")

if __name__  == '__main__':
    images = getUrlImages('http://unsplash.com/napi/feeds/home')
    time.sleep(1)
    find_all = images.find_all(name='img')
    print(find_all)
