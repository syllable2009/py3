from selenium import webdriver
import urllib
# browser = webdriver.Firefox(executable_path ="F:\GeckoDriver\geckodriver")
browser = '/Users/jiaxiaopeng/Downloads/chromedriver.3'

header = {
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
"host":"www.mzitu.com",
"cookie":"Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1552646036; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1552646036",
"authority":"www.mzitu.com",
"referer": "https://www.mzitu.com/171699/9",
"upgrade-insecure-requests":"1",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh,en;q=0.9,en-US;q=0.8,am;q=0.7,zh-CN;q=0.6",
"cache-control": "no-cache",
"pragma": "no-cache",
'Connection': 'keep - alive',

}

driver = webdriver.Chrome(executable_path=browser)

# get = driver.get("https://www.mzitu.com/all")

# print(get)
# print(driver.get_cookies())
url = 'https://i.meizitu.net/2019/01/29d09.jpg'
res = urllib.request.Request(url=url, headers=header)
response = urllib.request.urlopen(res)
data = response.read()
with open("/Users/jiaxiaopeng/mzitu-pictures/a.jpg", "wb") as f:
    f.write(data)
driver.get(url)
print(driver.page_source)
driver.close