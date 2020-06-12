# encoding: utf-8
# !/usr/bin/python
import requests


class Craw(object):
    _headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}

    def __init__(self, _url, _params=None, *args, **kwargs):
        self._url = _url
        self._params = _params


    def sendGetRequest(self):
        r = requests.get(self._url, self._params,
                         headers=self._headers,
                         timeout=2.5)
        if r.status_code != 200:
            print('request {} state is {}'.format(r.url,r.status_code))
            return None
        r.encoding = 'utf-8'
        return r.text