PyQuery 是 Python 仿照 jQuery 的严格实现。语法与 jQuery 几乎完全相同。
BeautifulSoup 用来解析 HTML 比较简单，API非常人性化，支持CSS选择器、Python标准库中的HTML解析器，也支持 lxml 的 XML解析器
lxml是python的一个解析库，支持HTML和XML的解析，支持XPath解析方式，而且解析效率非常高

1.BeautifulSoup
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:　Tag　　NavigableString　　BeautifulSoup　　Comment  。
Tag:  即我们在写网页时所使用的标签（如<a>超链接标签）
NavigableString：简单的说就是一种可以遍历的字符串