import requests
import eventlet
eventlet.monkey_patch()

try:
    with eventlet.Timeout(2):
        requests.get("http://ipv4.download.thinkbroadband.com/1GB.zip", verify=False)
        print('====')
except Exception as e:
    print('____')
    print(type(e))
    print('____')