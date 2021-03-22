
import requests
from requests.packages import urllib3
urllib3.disable_warnings()    # 就这一句就可以解决verify=False时的警告信息
import urllib.parse
from bs4 import BeautifulSoup
# print(BeautifulSoup.__file__)
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}
parameter = {
    "key1":"value1",
    "key2":"value2"
}
def request_test():
    #timeout 仅对连接过程有效，与响应体的下载无关。 timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，将会引发一个异常（更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时
    url = 'http://httpbin.org/get?a=b&c=d'
    response = requests.get(url,params = parameter,headers = headers,timeout = 300,allow_redirects=True, verify=True)
    print(response.url)
    print(type(response))
    print(response.status_code)
    print(response.encoding)
    #改变编码
    # response.encoding = 'ISO-8859-1'
    print(response.request.headers)
    print(response.headers['content-type'])
    print(type(response.text))
    print(type(response.content))
    print(response.json())
    print(type(response.cookies),response.cookies)
    print(type(response.headers),response.headers)
    print(type(response.history),response.history)

url = 'http://httpbin.org/post'
def request_test2():
    file = {"file":open('1.py', 'rb')}
    response = requests.post(url,files = file)
    print(response.json())
    # with open('massive-body') as f:
    #     requests.post('http://some.url/streamed', data=f)

def request_test3():
    #Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用。还可以把 Cookie Jar 传到 Requests 中
    jar = requests.cookies.RequestsCookieJar()
    jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
    url = 'http://httpbin.org/cookies'
    response = requests.get(url, cookies=jar)
    print(response.cookies)
    for key,value in response.cookies.items():
        print(key+"="+value)

def request_test4():
    url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LcN2z'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    data = {
    'username': 'StrivePy',
    'password': 'XXX'
    }
    session = requests.session()
    response = session.post(url=url, data=data, headers=headers)
    page_source = response.text
    print(response.status_code)
    print(page_source)

    url1 = 'http://bbs.chinaunix.net/thread-4263876-1-1.html'
    response1 = session.get(url=url1, headers=headers)
    page_source1 = response1.text
    print(response1.status_code)
    print(page_source1)

def proxy_test():
    url = 'http://myip.kkcha.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    proxy = {
        'https': '127.0.0.1:8899'
    }
    response = requests.get(url=url, headers=headers, proxies=proxy)
    print(response.text)


def request_test6():
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'
    headers['Accept-Encoding'] = 'gzip, deflate'
    headers['Content-Type'] = 'text/html; charset=utf-8'
    print(headers)
    print("handle start...")
    r = requests.get("http://www.51voa.com/VOA_Special_English/the-law-of-life-by-jack-london-part-one-81124.html", timeout=10)
    r.raise_for_status()
    r.encoding = 'utf-8'
    print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    informationlist = []
    for tr in soup.find('tbody').children:
        # 出现/n情况，/n在soup中被认为是子节点之一
        if (tr != '\n'):
            tds = tr('td')
            informationlist.append([tds[0].string, tds[1].string, tds[8].string])
    for i in range(len(informationlist)):
        information = informationlist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(information[0], information[1], information[2]))

# 利用request上传文件
def postfile():
    files = {'file': open('1.py', 'rb')}
    r = requests.post("http://httpbin.org/post", files=files)
    print(r.text)

# 利用request保持cookies
def getCookies():
    r = requests.get("https://www.baidu.com")
    print(r.cookies)
    for key, value in r.cookies.items():
        print(key + '=' + value)
def zhihuCookie():
    headers = {
        'Cookie': 'tgw_l7_route=e9ff3200fd05d0af15498c125aecf1a1; _zap=8965f710-bb58-4f90-b493-1f05b6403be3; _xsrf=CNYc6XGlPqIV0tuS2ZO1Wl9reugEhXKu; d_c0="AEAhgza4DxCPToqL_WDnYMMWIRN4Bgrda-M=|1568712830"; capsion_ticket="2|1:0|10:1568712835|14:capsion_ticket|44:MzE0OWZkNzFhNGJmNDMxYWE4MGI2YjlkZTg0MTdhODg=|2b4736ee3208971bb46c5d2f4fa7cb1a306c297209514a6e21b9fd1026ef0687"; z_c0="2|1:0|10:1568712849|4:z_c0|92:Mi4xMHA2OUFnQUFBQUFBUUNHRE5yZ1BFQ1lBQUFCZ0FsVk5rZlp0WGdBMS1XaW1sSnkwbjJ1bGZsS1NwOTcxMGJYOHVB|f25419803ff69811490f8766ca765787af94ce320a58d987e622cffeb7097e56"; tst=r',
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    }
    r = requests.get('https://www.zhihu.com', headers=headers)
    print(r.text)

def zhihuCookie2():
    cookies = 'tgw_l7_route=e9ff3200fd05d0af15498c125aecf1a1; _zap=8965f710-bb58-4f90-b493-1f05b6403be3; _xsrf=CNYc6XGlPqIV0tuS2ZO1Wl9reugEhXKu; d_c0="AEAhgza4DxCPToqL_WDnYMMWIRN4Bgrda-M=|1568712830"; capsion_ticket="2|1:0|10:1568712835|14:capsion_ticket|44:MzE0OWZkNzFhNGJmNDMxYWE4MGI2YjlkZTg0MTdhODg=|2b4736ee3208971bb46c5d2f4fa7cb1a306c297209514a6e21b9fd1026ef0687"; z_c0="2|1:0|10:1568712849|4:z_c0|92:Mi4xMHA2OUFnQUFBQUFBUUNHRE5yZ1BFQ1lBQUFCZ0FsVk5rZlp0WGdBMS1XaW1sSnkwbjJ1bGZsS1NwOTcxMGJYOHVB|f25419803ff69811490f8766ca765787af94ce320a58d987e622cffeb7097e56"; tst=r'
    jar = requests.cookies.RequestsCookieJar()
    headers = {
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }
    for cookie in cookies.split(';'):
        key, value = cookie.split('=', 1)
        jar.set(key, value)
    r = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
    # session = requests.Session()
    # r = session.get("http://www.zhihu.com",headers = headers)
    print(r.text)

#利用session维持会话
def session():
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)
if __name__ == '__main__':
    # zhihuCookie2()
    request_test3()