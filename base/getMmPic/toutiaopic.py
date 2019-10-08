import requests
import urllib.parse
from bs4 import BeautifulSoup
import json
import time;

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Cookie': '__tasessionId=e3twfdubn1570504339531; s_v_web_id=3b12eaa756919060f9683e82613ae4eb; tt_webid=6745265106295293453; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6745265106295293453',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
}

url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=40&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp='
def sendAjax(url):
    times = int(round(time.time() * 1000))

    response = requests.get(url+'{}'.format(times),headers=headers)
    html = response.text;
    # print(html)
    text = json.loads(html)
    list = text.get('data')
    # print(type(list))
    newList = [i for i in list if i.get('article_url') != None and i.get('article_url').startswith('http://toutiao.com') and i.get('has_video')==False]
    for j in newList:
        get = j.get('article_url')
        print(get)



if __name__ == '__main__':
    sendAjax(url)