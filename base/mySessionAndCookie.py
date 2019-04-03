import requests


# python2 和 python3的兼容代码
try:
    # python2 中
    import cookielib
    print(f"user cookielib in python2.")
except:
    # python3 中
    import http.cookiejar as cookielib
    print(f"user cookielib in python3.")

# session代表某一次连接
mafengwoSession = requests.session()
# 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
mafengwoSession.cookies = cookielib.LWPCookieJar(filename = "mafengwoCookies.txt")

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    # "origin": "https://passport.mafengwo.cn",
    "Referer": "https://passport.mafengwo.cn/",
    'User-Agent': userAgent,
}

def mafengwoLogin(account, password):
    # 马蜂窝模仿 登录
    print("开始模拟登录马蜂窝")

    postUrl = "https://passport.mafengwo.cn/login/"
    postData = {
        "passport": account,
        "password": password,
    }
    # 使用session直接post请求
    responseRes = mafengwoSession.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    # 登录成功之后，将cookie保存在本地文件中，好处是，以后再去获取马蜂窝首页的时候，就不需要再走mafengwoLogin的流程了，因为已经从文件中拿到cookie了
    mafengwoSession.cookies.save()

def isLoginStatus():
    # 通过访问个人中心页面的返回状态码来判断是否为登录状态

    routeUrl = "http://www.mafengwo.cn/plan/route.php"
    # 下面有两个关键点
        # 第一个是header，如果不设置，会返回500的错误
        # 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，
        # 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码
        # allow_redirects = False  就是不允许重定向
    responseRes = mafengwoSession.get(routeUrl, headers = header, allow_redirects = False)
    print(f"isLoginStatus = {responseRes.status_code}")
    if responseRes.status_code != 200:
        return False
    else:
        return True


if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    # mafengwoLogin("13261573576", "jxp3395943")
    mafengwoSession.cookies.load()
    isLogin = isLoginStatus()
    print(f"is login mafengwo = {isLogin}")