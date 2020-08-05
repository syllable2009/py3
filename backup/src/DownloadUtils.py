import os,urllib

from backup.src.PathUtils import PathUtils


def cbk(a,b,c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print('\r下载已完成{}%'.format(int(per)),end='')

class DownloadUtils(object):

    def __init__(self):
        pass


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


if __name__ == '__main__':
    url = "https://message.corp.kuaishou.com/api/file/preview/ccfb7c2c-a30e-4baa-b828-59e357a3b0a5?fileSuffix=png"
    # download = DownloadUtils(url)
    # DownloadUtils.downloadUrlFile()
    # dir = os.path.abspath('.')
    # file_path = os.path.join(dir, 'test2.gif')
    file_path = PathUtils.getPath('/Users/jiaxiaopeng', 'test2.png')
    # print(file_path)
    downloadUrlFile(url,file_path)




