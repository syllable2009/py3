
import requests
import urllib.parse
from bs4 import BeautifulSoup
# print(BeautifulSoup.__file__)

def request_test():
    url = 'http://httpbin.org/get?a=b&c=d'
    response = requests.get(url)
    print(type(response.text), response.text)
    print(type(response.content), response.content)

def request_test2():
    base_url = 'http://httpbin.org/'
    params = {
        'key1': 'value1',
        'key2': 'value2'
    }
    full_url = base_url + urllib.parse.urlencode(params)

    print(full_url)

def request_test3():
    payload = {
        'key1': 'value1',
        'key2': 'value2'
    }
    response = requests.get('http://httpbin.org/get', params=payload)
    print(response.url)

def request_test4():
    url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LcN2z'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    data = {
        'username': 'StrivePy',
        'password': 'XXX'
    }
    response = requests.post(url=url, data=data, headers=headers)
    page_source = response.text
    print(response.status_code)
    print(page_source)

    url1 = 'http://bbs.chinaunix.net/thread-4263876-1-1.html'
    response1 = requests.get(url=url1, headers=headers)
    page_source1 = response1.text
    print(response1.status_code)
    print(page_source1)

def request_test5():
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

if __name__ == '__main__':
    proxy_test()

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