from code.crawlersavefile.crawsite.craw import Craw
from code.crawlersavefile.fileutil.file import File
from code.crawlersavefile.bs4util.bs import BS4


if '__main__' == __name__:
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset={}'
    i = 20 * 0
    url = url.format(i)
    print(url)
    craw = Craw(url)
    html = craw.sendGetRequest()
    if None == html:
        print("request url: {} fail".format(url))
    # print(html)

    bs4 = BS4(html)
    # matches = bs4.getRegularMatches(r'https.*?jpg') #https.*?jpg
    bs4.getTag()
    # if len(matches):
    #     for m in matches:
    #         print(m.replace("\\",""))
    #         print("-----------------------------")
    # else:
    #     print("result no match pattern")
    # file = File('./json.txt','a',2)
    # file.saveLine('4')





