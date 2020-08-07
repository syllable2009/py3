python中有多种库可以用来处理http请求，比如：urllib包、requests类库
Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能,更好的方案是使用requests

python3中requests库和urllib包对比
1.1 基于urllib库的GET请求
import urllib.request
   req = urllib.request.urlopen('http://www.imooc.com/course/list?c=python')  #访问网页
   html=req.read().decode("utf-8") #读取该网页的html代码，同时将其转换为utf-8编码
1.2使用User-Agent伪装后请求网站
由于urllib.request.urlopen() 函数不接受headers参数，所以需要构建一个urllib.request.Request对象来实现请求头的设置
1.3 基于urllib库的POST请求，并用Cookie保持会话
1.4 基于urllib库使用代理请求

2.使用Requests
2.1 GET请求:
import requests
r = requests.get('https://www.douban.com/',params={'q': 'python', 'cat': '1001'}
,headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
, timeout=2.5) # 2.5秒后超时
r.url # 实际请求的URL
r.encoding #requests自动检测编码，可以使用encoding属性查看
r.status_code
r.text # 获取str文本
r.content # 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象content返回的是bytes，二级制型的数据。
r.json() # requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取
r.headers
r.headers['Content-Type']
2.2 POST请求
requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数
params = {
        'key1': 'value1',
        'key2': 'value2'
    }
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }    
r = requests.post(url, json=params,header=headers) # 内部自动序列化为JSON

类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)

把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie
r.cookies['ts']
要在请求中传入Cookie，只需准备一个dict传入cookies参数：
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)

headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
     'Content-Type': 'charset=UTF-8'
     }
data = {
     'identity':'irw27812@awsoo.com',
     'password':'test2018',
 }
url ='https://www.itjuzi.com/user/login?redirect=&flag=&radar_coupon='
session = requests.Session()
session.post(url,headers = headers,data = data)
# 登录后，我们需要获取另一个网页中的内容
response = session.get('http://radar.itjuzi.com/investevent',headers = headers)
