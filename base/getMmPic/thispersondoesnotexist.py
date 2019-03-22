import requests
import time

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
}
root_dir = '/Users/jiaxiaopeng/ai-photo/'
pic_src = 'https://thispersondoesnotexist.com/image'
i = 4427
while True:
    i += 1
    img = requests.get(pic_src, headers=HEADERS, timeout=60)
    img_name = root_dir + str(i) + '.jpg'
    with open(img_name, 'ab') as f:
        f.write(img.content)
        print("save:"+img_name)
    time.sleep(0.25)
