import os,urllib,requests
from contextlib import closing
from backup.src.PathUtils import PathUtils

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}


def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('\r下载已完成{}%'.format(round(per,2)), end='')

def cbk(a,b,c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0 * a * b / c
    if per>100:
        per=100
    print('\r下载已完成{}%'.format(int(per)),end='')

class DownloadUtils(object):

    def __init__(self):
        pass

# 使用urllib.request.urlretrieve(url, local, Schedule)下载文件
def downloadUrlFile(url,file_path,headers=[('User-agent', 'Mozilla/5.0')]):
    # 添加header
    opener = urllib.request.build_opener()
    headers.append(('Referer',url))
    parseResult = urllib.parse.urlparse(url)
    headers.append(('Host', parseResult.scheme + "://" + parseResult.netloc))
    opener.addheaders = headers
    urllib.request.install_opener(opener)
    print("开始下载：{}".format(os.path.basename(file_path)))
    urllib.request.urlretrieve(url, file_path,cbk)


def dowloadFile():
    url = 'http://downdb.51voa.com/201812/science-2018-gene-editing-private-space-travel-top-list.mp3'
    r = requests.get(url)
    # with语句时用于对try except finally 的优化，让代码更加美观
    with open("/Users/jiaxiaopeng/science-2018-gene-editing-private-space-travel-top-list.mp3", "wb") as code:
        code.write(r.content)

def download3():
    with closing(requests.get('http://downdb.51voa.com/201812/science-2018-gene-editing-private-space-travel-top-list.mp3', headers=headers, stream=True)) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 文件总大小
        data_count = 0 # 当前已传输的大小
        with open('Users/jiaxiaopeng/a', "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                done_block = int((data_count / content_size) * 50) #分成50份显示
                data_count = data_count + len(data)
                now_jd = (data_count / content_size) * 100
                print("\r %s：[%s%s] %d%% %d/%d" % ('Users/jiaxiaopeng/a', done_block * '█', ' ' * (50 - 1 - done_block), now_jd, now_photo_count, all_photo_count), end=" ")


if __name__ == '__main__':
    url = "https://message.corp.kuaishou.com/api/file/preview/ccfb7c2c-a30e-4baa-b828-59e357a3b0a5?fileSuffix=png"
    # download = DownloadUtils(url)
    # DownloadUtils.downloadUrlFile()
    # dir = os.path.abspath('.')
    # file_path = os.path.join(dir, 'test2.gif')
    file_path = PathUtils.getPath('/Users/jiaxiaopeng', 'test2.png')
    # print(file_path)
    # downloadUrlFile(url,file_path)
    # dowloadFile()
    print("%s：[%s%s] %d%% %d/%d" % (
        './Users/jiaixaopneg/test', 30 * '█', ' ' * (50 - 1 - 30), 66, 2, 100),
              end=" ")
    print("\n%s：[%s%s] %d%% %d/%d" % (
            './Users/jiaixaopneg/test', 50 * '█', ' ' * (50 - 1 - 50), 66, 2, 100),
              end=" ")



