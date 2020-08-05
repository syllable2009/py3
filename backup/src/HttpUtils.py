import requests
import urllib.parse

class HttpUtils(object):

    # __slots__ = ('url','headers','referer','host','timeout')

    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/84.0.4147.105 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9 ',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,am;q=0.6 '
    }
    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
    }

    html = None
    resp = None
    timeout = 20

    def __init__(self,url,method = 'get'):
        self.url = url
        self.method = method
        self.headers['Referer'] = url
        parseResult = urllib.parse.urlparse(url)
        self.headers['Host'] = parseResult.scheme + "://" + parseResult.netloc

    def sendRequest(self):
        if "get" == self.method.islower():
            self.resp = requests.get(self.url, self.headers,self.timeout)
        else:
            self.resp = requests.post(self.url, self.headers,self.timeout)
        self.resp.raise_for_status()
        self.resp.encoding = 'utf-8'
        self.html = self.resp.text

    def parseResult(self,func):
        return func()

    # def myParse(self):
    #     print("that's ok")

    @staticmethod
    def download(url,file_path):
        # HttpUtils.headers['Referer'] = url
        # parseResult = urllib.parse.urlparse(url)
        # HttpUtils.headers['Host'] = parseResult.scheme + "://" + parseResult.netloc
        r = requests.get(url, headers=HttpUtils.headers2)
        # print(HttpUtils.headers)
        with open(file_path, "wb") as code:
            code.write(r.content)


if __name__ == '__main__':
    http = HttpUtils("https://gif.sina.com.cn/user/test.html?a=4,5,6&b=56");
    # http.sendRequest()
    # print("{}".format(http.headers))
    # http.parseRequest()
    # print(http.headers)
    # http.parseResult(http.myParse)
    # HttpUtils.download("https://message.corp.kuaishou.com/api/file/preview/ccfb7c2c-a30e-4baa-b828-59e357a3b0a5?fileSuffix=png",
    #                    "/Users/jiaxiaopeng/d.png")
    url = 'https://message.corp.kuaishou.com/api/file/preview/ccfb7c2c-a30e-4baa-b828-59e357a3b0a5?fileSuffix=png';
    r = requests.get(url,headers=HttpUtils.headers2)
    with open("/Users/jiaxiaopeng/e.png", "wb") as code:
        code.write(r.content)

