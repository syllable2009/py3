
from pyquery import PyQuery as pq
from lxml import etree

url = 'http://www.51voa.com/VOA_Special_English/';

doc = pq(url,encoding="utf-8")

# formatdoc = pq(etree.fromstring(doc.html()))

lilist = doc('div').filter('#list').html()

lis = pq(lilist).children('li')

for l in lis:
    la = pq(l).children('a')
    print(la.attr('href'),la.text())