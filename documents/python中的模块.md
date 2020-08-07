# Click
Click 是 Flask 的开发团队 Pallets 的另一款开源项目，它是用于快速创建命令行的第三方模块
Click 对argparse 的主要改进在易用性，使用Click 分为两个步骤：
使用 @click.command() 装饰一个函数，使之成为命令行接口；
使用 @click.option() 等装饰函数，为其添加命令行选项等。
import click
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)
        
# goose3
获取任何新闻文章或文章类型的网页，不仅提取文章的主体，而且还提取所有元数据和图片
from goose3 import Goose
from goose3.text import StopWordsChinese

url  = 'http://news.china.com/socialgd/10000169/20180616/32537640_all.html'
g = Goose({'stopwords_class': StopWordsChinese})
article = g.extract(url=url)
print(article.title)       
print(article.meta_description) 
print(article.cleaned_text[:150])
print(article.top_image)

# pytesseract
ocr文字图片识别
import pytesseract
from PIL import Image

image = Image.open('/Users/jiaxiaopeng/validCode.png')
code = pytesseract.image_to_string(image, lang='chi_sim+eng')
print(code)