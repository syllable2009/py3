import sys, re
from util import *

print('<html><head><meta charset="gbk"><title>doc.txt</title></head><body>')  # 添加HTML基本标签
blocks = blocks(sys.stdin)  # 获取系统标准输入
# blocks = blocks("doc.txt")
for block in blocks:  # 遍历文件内容
    block = re.sub('\*(.+)\*', '<strong>\\1</strong>', block)  # 替换内容块中两个星号间的内容为加重样式
    block = re.sub(r'\n *- *(.+)', '\n<li>\\1</li>', block)  # 替换内容块中以“-”开头的内容为列表项
    block = re.sub(r'([^:>])\n', '\\1<br/>\n', block)  # 替换内容块中换行符“\n”为换行标签
    if re.match(r'(^[A-Z][\w ]+[A-Za-z]$)', block):  # 匹配大写字母开头和以字母结尾的内容
        print('<h1>' + block + '</h1>')  # 添加一级标题标签
    elif '<li>' in block:  # 如果内容块包含列表项
        print('<ul>' + block + '</ul>')  # 添加项目列表标签
    else:
        print('<p>' + block + '</p>')  # 添加段落标签

print('</body></html>')  # 添加HTML结束标签