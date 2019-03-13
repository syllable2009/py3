
import urllib
import os
import requests


def downLoadPic(jpg_link,path):
    requests.urlretrieve(jpg_link, path)  # path为路径加名字哦（如 ~/workjpg/111.jpg）！！！
    # 如果不需要路径，也要有个名字，如 111.jpg就直接保存在当前目录下

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print(round(per,1),"%")

def downloadFile1():
    print("--downloadFile--")
    url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
    # local = url.split('/')[-1]
    local = os.path.join('/Users/jiaxiaopeng/software', 'Python-2.7.5.tar.bz2')
    #urlretrieve(url, [filename=None, [reporthook=None, [data=None]]])
    urllib.request.urlretrieve(url, local, Schedule)
    #参数 finename 指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
    # 参数 reporthook 是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
    # 参数 data 指 post 到服务器的数据，该方法返回一个包含两个元素的(filename, headers)元组，filename 表示保存到本地的路径，header 表示服务器的响应头

def dowload2():
    url = 'http://downdb.51voa.com/201812/science-2018-gene-editing-private-space-travel-top-list.mp3'
    r = requests.get(url)
    # with语句时用于对try except finally 的优化，让代码更加美观
    with open("/Users/jiaxiaopeng/software/science-2018-gene-editing-private-space-travel-top-list.mp3", "wb") as code:
        code.write(r.content)
    print("end download")

if __name__ == '__main__':
    print("download work")
    #<a href="http://downdb.51voa.com/201812/science-2018-gene-editing-private-space-travel-top-list.mp3" id="mp3"></a>
    # downLoadPic("http://downdb.51voa.com/201812/science-2018-gene-editing-private-space-travel-top-list.mp3","/Users/jiaxiaopeng/py3test/science-2018-gene-editing-private-space-travel-top-list.mp3")
    # downloadFile1()
    # downloadFile2()
    dowload2()



