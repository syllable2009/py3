# encoding: utf-8
# !/usr/bin/python
from bs4 import BeautifulSoup
import re
import json

class BS4(object):


    def __init__(self, _html, *args, **kwargs):
        self._html = _html
        self._bs = BeautifulSoup(_html, "lxml")

    def getRegularMatches(self,pattern):
        pattern = re.compile(pattern)
        findall = pattern.findall(self._html, re.S)
        return findall

    def getTag(self):
        loads = json.loads(self._bs.p.string)
        data_ = loads['data']
        print(type(data_))
        for d in data_:
            print(d['vertical_src'])

