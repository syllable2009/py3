import re, sys
import requests
import urllib.request


def getHtml(url):
    page = requests.get(url)
    html = page.text
    return html


def mv(url):
    mvid = url.split('/')[-1]
    url = 'http://www.yinyuetai.com/insite/get-video-info?flex=true&videoId={}'.format(mvid)
    html = getHtml(url)
    # print("html:{}".format(html))
    reg = r'http://\w*?\.yinyuetai\.com/uploads/videos/common/.*?(?=&br)'
    pattern = re.compile(reg)
    findlist = re.findall(pattern, html)
    print("findlist:{}".format(findlist))
    mvurl = findlist[-2]
    print("mvurl:{}".format(mvurl))
    mp4 = mvurl.split('?')[0]
    print("mp4:{}".format(mp4))
    ext = mp4[-4:]
    print("ext:{}".format(ext))
    urllib.request.urlretrieve(url=mvurl, filename='1{}'.format(ext), reporthook=Schedule)


def Schedule(a, b, c):
    '''回调函数
       @a: 已经下载的数据块
       @b: 数据块的大小
       @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    sys.stdout.write('下载进度：{0}%\r'.format(per))
    sys.stdout.write("" + "%.2f%% 已经下载的大小:%ld 文件大小:%ld" % (per, a * b, c) + '\r')
    sys.stdout.flush()


if __name__ == '__main__':
    url = "http://v.yinyuetai.com/video/2895770"
    mv(url)
