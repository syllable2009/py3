#!/usr/bin/evn python #　这是标识当前脚本指定用python来执行它，为了防止用户没有将python装在默认的/usr/bin路径里，系统执行时首先会到env设置里查找python的安装路径，再调用对应路径下的python程序来执行
# coding=utf-8

from bottle import default_app, get, run #　由于bottle框架自身并没有提供Session的支持，所以使用beaker中间件来实现。
from beaker.middleware import SessionMiddleware

# 设置session参数
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': '/tmp/sessions/simple',
    'session.auto': True
}
#　　第7到第13行，是创建一个session配置的字典，用来存储session的存储类型为文件类型，session过期时间为3600秒，session文件存放路径为/tmp/sessions/simple

@get('/index/')
def callback():
    return 'Hello World! jxp'

# 函数主入口
if __name__ == '__main__':
    app_argv = SessionMiddleware(default_app(), session_opts) #启动WSGI WEB程序，地址为本机地址，访问端口为909
    run(app=app_argv, host='0.0.0.0', port=9090, debug=True, reloader=True)
# Bottle框架，它是一个快速的，简单的，非常轻量级的 Python WSGI Web 框架