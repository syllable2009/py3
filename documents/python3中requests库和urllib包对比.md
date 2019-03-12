python3中requests库和urllib包对比

python中有多种库可以用来处理http请求，比如：urllib包、requests类库

1.1 基于urllib库的GET请求
import urllib.request
1.2使用User-Agent伪装后请求网站
由于urllib.request.urlopen() 函数不接受headers参数，所以需要构建一个urllib.request.Request对象来实现请求头的设置
1.3 基于urllib库的POST请求，并用Cookie保持会话
1.4 基于urllib库使用代理请求



2.使用Requests
2.1 在GET方法中传递参数的三种方式:
将字典形式的参数用urllib.parse.urlencode()函数编码成url参数
直接在urllib.request.get()函数中使用params参数
url直接包含参数
2.2 基于requests库的POST请求，并用session保持会话