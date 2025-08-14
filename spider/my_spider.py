import my_request
import my_bs4
from lxml import etree

url = 'https://blog.51cto.com/ranking/hot/python'

body = my_request.stealth_crawl(url)
extract_body = my_bs4.extract_body(body)
if body is None:
    print("body is None")
else:
    # 转换DOM结构
    dom = etree.HTML(str(extract_body))
    xpath = dom.xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[1]/text()')
    print(xpath)