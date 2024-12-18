#_*_coding:utf-8_*_
import unicodedata
import urllib.request
import re
import os
root_url="https://mm.taobao.com/json/request_top_list.htm?type=0&page="

def HexStr2Unicode(Hex_Str):
    Unicde_Str = ""
    for i in range(0,len(Hex_Str)//4):
        chr(int(Hex_Str[i*4:i*4+4], 16))
        Unicde_Str += chr(int(Hex_Str[i*4:i*4+4], 16))
    return Unicde_Str
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

# SiteSet=getSiteSet("https://mm.taobao.com/json/request_top_list.htm?type=0&page=0")


def getImgSet(site_url):
    '''根据某个具体的网址，获取该网址中所有图片的路径'''
    page=urllib.request.urlopen(site_url)
    cont=page.read().decode("gbk").encode("utf-8")
    cont=str(cont,encoding="utf-8")
    pattern=r'src=\"\/\/.{0,150}(.jpg|.png)\"'
    ImgSet=[]
    index=0
    i=1
    try:
        while len(cont)>100:

            matchObj=re.search(pattern,cont,re.M).group()
            # print("------->",matchObj)
            if matchObj:
                img='https:'+(matchObj[5:-1])
                # print("图片地址%d: "%i,img)
                ImgSet.append(img)
                index=cont.find(matchObj)
                i+=1
            else:
                print("没有匹配上")

            cont=cont[index+len(matchObj[5:-1]):]
    except:
        print("-----------------------")

    return ImgSet

# ImgSet=getImgSet("https://mm.taobao.com/434479822.htm")
# ImgSet=set(list(ImgSet))#集合元素去重

def getIconSet(url):
    '''根据roo_url，获取每个淘女郎的头像icon图片'''
    page=urllib.request.urlopen(url)
    cont=page.read()
    cont=str(cont)
    head="<img src="
    tail=".jpg"
    k=1
    IconSet=[]
    while k!=0:
        id1=cont.find(head)
        id2=cont.find(tail,id1)
        if id1==-1 or id2==-1:
            k=0
            break
        else:
            icon="https:"+cont[id1+len(head)+1:id2+len(tail)]
            cont=cont[id2:]
            IconSet.append(icon)
            print(icon)
    return IconSet
#我们可以使用自己定义的auto_down()来代替python的urllib.urlretrieve()函数，实现我们自动重新下载的目标。
#    tips:新下载的文件会覆盖原来下载不完全的文件。
def auto_down(url,filename):
    '''使用自定义的方法进行下载文件，如果下载失败，还可以继续下载覆盖原来的文件'''
    try:
        # 添加头部信息，模仿浏览器,但是淘宝对于爬虫的爬取，做了很多防爬的措施，因此，及时添加了header头部信息，效果也并不好
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=url, headers=headers)
        urllib.request.urlretrieve(url,filename)
    except urllib.request.ContentTooShortError:
        print('Network conditions is not good.Reloading.')
        auto_down(url,filename)



# urllib.request.urlopen(req).read()
base =r"/Users/jiaxiaopeng/TaobaoGirlImg/"
for i in range(1,6):
    url=root_url+str(i)
    SiteSet=getSiteSet(url)
    for site in SiteSet.keys():
        i=1
        filename=base+site
        os.mkdir(filename)# 创建文件夹
        print(filename)
        ImgSet=getImgSet(SiteSet[site])
        ImgSet=set(list(ImgSet))
        for imgurl in ImgSet:
            # print(imgurl)
            file_name=filename+"/"+str(i)+".jpg"
            auto_down(imgurl,file_name)
            i+=1

