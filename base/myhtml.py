
import requests
from bs4 import BeautifulSoup
# print(BeautifulSoup.__file__)


if __name__ == "__main__":

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