import util
from handlers import Handler

file = open('file.txt',encoding = 'utf-8')
g = util.blocks(file)
for i in g:
    print(i)
Handler.