
from urllib import request


def downLoadPic(jpg_link,path):
    request.urlretrieve(jpg_link, path)  # path为路径加名字哦（如 ~/workjpg/111.jpg）！！！
    # 如果不需要路径，也要有个名字，如 111.jpg就直接保存在当前目录下

if __name__ == '__main__':
    print("download work")
    #<a href="http://downdb.51voa.com/201812/science-2018-gene-editing-private-space-travel-top-list.mp3" id="mp3"></a>
    downLoadPic("http://downdb.51voa.com/201812/science-2018-gene-editing-private-space-travel-top-list.mp3","/Users/jiaxiaopeng/py3test/science-2018-gene-editing-private-space-travel-top-list.mp3")