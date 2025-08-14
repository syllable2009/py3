import requests
from fake_useragent import UserAgent
import time
import random

# 初始化伪装组件
ua = UserAgent()
headers1 = {
    'User-Agent': ua.chrome,
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'text/html,application/xhtml+xml',
    'Referer': 'https://www.google.com/',
    'Accept-Encoding': 'gzip, deflate, br'
}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'text/html,application/xhtml+xml',
    'Referer': 'https://www.google.com/',
    'Accept-Encoding': 'gzip, deflate, br'
}

session = requests.Session()

def stealth_crawl(url):
    try:
        with requests.Session() as s:
            s.headers.update(headers2)
            # 随机延迟1-3秒
            time.sleep(random.uniform(1, 3))
            resp = s.get(url, timeout=10)
            resp.raise_for_status()
            return resp
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
    except Exception as e:
        print(f"抓取失败: {str(e)}")
    return None

if __name__ == '__main__':
    url = 'https://blog.51cto.com/ranking/hot/python'
    html = stealth_crawl(url)
    print(html[:500])  # 打印前500字符
