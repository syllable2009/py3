# lxml提供etree模块，专门用来解析html和xml
from lxml import etree


def parseByXpath(content: str, xpath: str):
    if content.strip() != '':
        # 指定解析器HTMLParser会修复html缺失的信息
        parser = etree.HTMLParser(encoding="utf-8")
        # tree = etree.fromstring(content, parser=parser)
        tree = etree.HTML(content, parser=parser)
        elements = tree.xpath(xpath)
        return elements
    else:
        print('parseByXpath input is blank')
        return None


if __name__ == "__main__":
    content = ''
    elements = parseByXpath(content, '//*[@id="markdownContent"]/p')
    if elements is None:
        pass
    else:
        print('共', len(elements), '个节点')
    for e in elements:
        if e is not None:
            # e.get('class')
            print(e.text)
            # print(e)
