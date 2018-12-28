import requests
from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner
import urllib
import re
from w3lib.html import remove_tags


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return None

def getContent(url):
    html = getHTMLText(url)
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    title = soup.select("div.hd > h1")
    print(title[0].get_text())
    time = soup.select("div.a_Info > span.a_time")
    print(time[0].string)
    author = soup.select("div.qq_articleFt > div.qq_toolWrap > div.qq_editor")
    print(author[0].get_text())
    paras = soup.select("div.Cnt-Main-Article-QQ > p.text")
    for para in paras:
        if len(para) > 0:
            print(para.get_text())
            print()

if __name__ == '__main__':
    print("tx-news works ...")

def GetUrlFileSize(url):
    urlHandler = urllib.urlopen(url)
    headers = urlHandler.info().headers
    length = 0
    for header in headers:
        if header.find('Length') != -1:
            length = header.split(':')[-1].strip()
            length = int(length)
    return length

def SpliteBlocks(totalsize, blocknumber):
    blocksize = totalsize / blocknumber
    ranges = []
    for i in range(0, blocknumber -1):
        ranges.append((i * blocksize, i * blocksize + blocksize -1))
    ranges.append((blocksize * (blocknumber -1), totalsize -1))
    return ranges

def getContentId(url):
    html = getHTMLText(url)
    # print(html)html.parser
    soup = BeautifulSoup(html, "html.parser")
    sound = soup.find(id="mp3")
    print("sound",sound)
    print("attrs",html)
    content = soup.find(id="content")
    print("content",remove_tags(bytes(content), encoding = 'utf8'));
def main():
    print("main work")
    url = "http://www.51voa.com/VOA_Special_English/"
    getContentId(url)
    # size = GetUrlFileSize(url)
    # ranges = SpliteBlocks(size, blocks=6)
def clear_html_re(src_html):
    '''
    正则清除HTML标签
    :param src_html:原文本
    :return: 清除后的文本
    '''
    pat = re.compile('(?<=\>).*?(?=\<)')
    content =  ''.join( pat.findall(src_html))
    # content = re.sub(r"</?(.+?)>", "", src_html) # 去除标签
    # content = re.sub(r"&nbsp;", "", content)
    # dst_html = re.sub(r"\s+", "", content)  # 去除空白字符
    return content
#用了HTMLParser，有更简单的方式吗？正则？
def strip_tags(html):
    """
    Python中过滤HTML标签的函数
    hello
    """
    from HTMLParser import HTMLParser
    html = html.strip()
    html = html.strip("\n")
    result = []
    parser = HTMLParser()
    parser.handle_data = result.append
    parser.feed(html)
    parser.close()
    return ''.join(result)
main()


