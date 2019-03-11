from goose3 import Goose
from goose3.text import StopWordsChinese

url  = 'http://news.china.com/socialgd/10000169/20180616/32537640_all.html'
g = Goose({'stopwords_class': StopWordsChinese})
article = g.extract(url=url)
print(article.cleaned_text[:150])