from code.crawlersavefile.fileutil.file import File
from code.crawlersavefile.crawsite.craw import Craw
from code.crawlersavefile.bs4util.bs import BS4
import time

def requestHtml(_url):
    craw = Craw(_url)
    return craw.sendGetRequest()

def handleUrl(_url):
    resp = requestHtml(_url)
    return BS4(resp)


if __name__ == '__main__':
    print("task start--->")
    inputurl = 'https://www.51voa.com/People_in_America_{}.html';
    i = 1;
    max = 1;
    url = inputurl.format(1);
    print('request:{} start'.format(url))
    bs4 = handleUrl(url)
    header = ['url', 'title', 'date']
    f = File()

    if i == 1:
        max = int(bs4.getVoaMaxPage())
        print('max page:{}'.format(max))
        # 处理请求
        bs4.handleVoaPage()
        data = bs4.handVoaArticle()
        f.writeCsvFileV('People in America.csv', 'a', header, _delimiter=',')
        f.writeCsvFileV('People in America.csv', 'a', data, _delimiter=',')
    while i < max:
        time.sleep(1)
        i = i + 1;
        url = inputurl.format(i);
        # print('request:{} start'.format(url))
        bs4 = handleUrl(url)
        bs4.handleVoaPage()
        data = bs4.handVoaArticle()
        f.writeCsvFileV('People in America.csv', 'a', data, _delimiter=',')
        # 处理请求
    print("task end--->")



