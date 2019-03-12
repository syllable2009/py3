import urllib.request
import urllib.parse
import http.cookiejar

def get_page():
    url = 'http://www.baidu.com/'
    res = urllib.request.urlopen(url=url)
    page_source = res.read().decode('utf-8')
    print(page_source)

def get_page2():
    url = 'http://www.baidu.com'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(request)
    page_source = res.read().decode('utf-8')
    print(page_source)

def get_page3():
    url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LcN2z'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    data = {
    'username': 'StrivePy',
    'password': 'XXX'
    }
    postdata = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url=url, data=postdata, headers=headers)
    # 创建CookieJar对象
    # cjar = http.cookiejar.CookieJar()
    filename = 'cookies.txt'
    cjar = http.cookiejar.MozillaCookieJar(filename)
    # 以CookieJar对象为参数创建Cookie
    cookie = urllib.request.HTTPCookieProcessor(cjar)
    # 以Cookie对象为参数创建Opener对象
    opener = urllib.request.build_opener(cookie)
    # 将Opener安装位全局，覆盖urlopen函数，也可以临时使用opener.open()函数
    urllib.request.install_opener(opener)
    # 临时使用opener来请求
    opener.open(req)
    # 将cookie保存为文件
    cjar.save(ignore_discard=True, ignore_expires=True)
    res = urllib.request.urlopen(req)
    page_source = res.read().decode('gbk')
    print(page_source)

    url1 = 'http://bbs.chinaunix.net/thread-4263876-1-1.html'
    res1 = urllib.request.urlopen(url=url1)
    page_source1 = res1.read().decode('gbk')
    print(page_source1)

def get_page4():
    url1 = 'http://bbs.chinaunix.net/thread-4263876-1-1.html'
    filename = 'cookies.txt'
    cjar = http.cookiejar.MozillaCookieJar(filename)
    cjar.load(ignore_discard=True, ignore_expires=True)
    cookie = urllib.request.HTTPCookieProcessor(cjar)
    opener = urllib.request.build_opener(cookie)
    res1 = opener.open(url1)
    page_source1 = res1.read().decode('gbk')
    print(page_source1)

def proxy_test():
    url = 'http://myip.kkcha.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    proxy = {
        'http': '127.0.0.1:8899'
    }
    # 创建代理Handler对象
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 以Handler对象为参数创建Opener对象
    opener = urllib.request.build_opener(proxy_handler)
    # 将Opener安装为全局
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(request)
    page_source = response.read().decode('utf-8')
    print(page_source)

if __name__ == '__main__':
    proxy_test()
