
import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.51voa.com/Technology_Report_1.html'
# response = urllib.request.urlopen(url)


num = 1

for num in range(1,20):
    nextPage = 'Technology_Report_%s.html' % num
    combineUrl = urllib.parse.urljoin(url,nextPage)
    print(combineUrl)


