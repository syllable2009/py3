#!usr/bin/env/python
# encoding:UTF-8

import urllib
import requests
import json
import os
import re
import time

currentPage = 1

headers = {
    'User-Agent': r'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Connection': 'keep-alive'
}

def HexStr2Unicode(Hex_Str):
    Unicde_Str = ""
    for i in range(0,len(Hex_Str)//4):
        chr(int(Hex_Str[i*4:i*4+4], 16))
        Unicde_Str += chr(int(Hex_Str[i*4:i*4+4], 16))
    return Unicde_Str

root_url="https://v.taobao.com/v/content/live?catetype=704"

def getSiteSet(url):
    '''根据传入的roo_url获取到每个淘女郎的个人网址,以及每个淘女郎的名字'''
    page=urllib.request.urlopen(url)
    cont=page.read()
    cont=cont.decode(encoding="gbk")#很关键，原网页淘宝的是gbk编码
    # print(cont)
    pattern1=r'href=".{1,35}\.htm" target='#匹配个人网址的正则表达式
    pattern2=r'class="lady-name" href=".{1,100}<\/a>'#匹配个人名字的表达式
    # print(cont)
    SiteSet={}
    i=1
    try:
        while len(cont)>5:
            matchObj=re.search(pattern1,cont,re.M).group()
            nameObj=re.search(pattern2,cont,re.M).group()
            # print("------->",matchObj)
            if matchObj:
                site='https:'+(matchObj[6:-9])
                id1=nameObj.find(">")
                id2=nameObj.find("<")
                # print(name)
                name=nameObj[id1+1:id2]
                # print("网站地址%d: "%i,site)
                # print("淘女郎名字:",name)
                SiteSet[name]=site
                index=cont.find(nameObj)
                i+=1
            else:
                print("没有匹配上")

            cont=cont[index+2:]
    except:
        # import traceback
        # traceback.print_exc()
        print("*********Match error****************")
    return SiteSet

try:
    data = urllib.parse.urlencode({"page": currentPage,"type":0}).encode('utf-8')
    request = urllib.request.Request(root_url, data=data, headers=headers)
    cont = urllib.request.urlopen(request).read().decode('gbk')
    print(cont)

    pattern1=r'https://v.taobao.com/v/home/?userId="{1,350}"'#匹配个人网址的正则表达式
    pattern2=r'class="lady-name" href=".{1,100}<\/a>'#匹配个人名字的表达式
    # print(cont)
    SiteSet={}
    # i=1
    try:
        search = re.search('https://v.taobao.com/v/home', cont, re.M)
        if search != None:
            matchObj =search.group()
            print("------->", matchObj)
        else:
            print("------->", None)
    #     while len(cont)>5:
    #         matchObj=re.search(pattern1,cont,re.M).group()
    #         nameObj=re.search(pattern2,cont,re.M).group()
    #         # print("------->",matchObj)
    #         if matchObj:
    #             site='https:'+(matchObj[6:-9])
    #             id1=nameObj.find(">")
    #             id2=nameObj.find("<")
    #             # print(name)
    #             name=nameObj[id1+1:id2]
    #             # print("网站地址%d: "%i,site)
    #             # print("淘女郎名字:",name)
    #             SiteSet[name]=site
    #             index=cont.find(nameObj)
    #             i+=1
    #         else:
    #             print("没有匹配上")
    #
    #         cont=cont[index+2:]

    except BaseException as e:
        # import traceback
        # traceback.print_exc()
        print("*********Match error****************",e)
    print(SiteSet)
except urllib.error.URLError as e:
    if hasattr(e, "reason"):
        print("连接失败，错误原因：", e.reason)


