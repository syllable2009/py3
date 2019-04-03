import re
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
    reg = r'http://\w*?\.yinyuetai\.com/uploads/videos/common/.*?(?=&br)'
    pattern = re.compile(reg)
    findlist = re.findall(pattern, html)
    print(findlist)
    mvurl = findlist[-1]
    mp4 = mvurl.split('?')[0]
    mp4 = mp4[-4:]
    urllib.request.urlretrieve(mvurl, '1{}'.format(mp4))


if __name__ == '__main__':
    url = "http://v.yinyuetai.com/video/2895770"
    mv(url)
