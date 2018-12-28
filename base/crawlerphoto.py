# encoding: utf-8
#!/usr/bin/python



import requests,json


if __name__ == '__main__':
    target = 'http://unsplash.com/napi/feeds/home'
    headers = {'authority': 'images.unsplash.com'}
    req = requests.get(url=target, headers=headers,verify=True)
    # print(req.text)
    html = json.loads(req.text)
    next_page = html['next_page']
    print('下一页地址:', next_page)
    for each in html['photos']:
        print('图片ID:', each['id'])