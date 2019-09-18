import codecs
import os

a,b=0,1 #复合赋值
# print(a,b,end="\t\n")
a,b=b,a #复合赋值
# print(a,b,end="\t\n")

a = {'1','he','ok'}
a.add('ok')
# print(a)

c = set(['i'])
c.add('i')
# print(c)
# print(os.path)

# with codecs.open('/Users/jiaxiaopeng/1.txt', 'w',encoding='utf-8') as f:
#     # for line in f.readlines():
#     f.write("胜利的方法")

path = '/Users/jiaxiaopeng/1.txt'

# print(os.path.basename(path))    # 查询路径中包含的文件名
# print(os.path.dirname(path))     # 查询路径中包含的目录

info = os.path.split(path)       # 将路径分割成文件名和目录两个部分，放在一个表中返回
path2 = os.path.join('/', 'home', 'vamei', 'doc', 'file1.txt')  # 使用目录名和文件名构成一个路径字符串

p_list = [path, path2]
# print(os.path.commonprefix(p_list))

# print(os.path.abspath('./'))

def getAllFile(path):
    for parent, dirnames, filenames in os.walk(path): #os.walk返回是一个三元组
        file = open('explore.txt', 'a+', encoding='utf-8')
        file.write('\n'.join([parent, ",".join(str(x) for x in dirnames) , ",".join(str(x) for x in filenames) ]))
        file.write('\n' + '=' * 100 + '\n')
        file.close()
        #
        # for filename in filenames:
        #     print("parent is" + parent)
        #     print("filename is:" + filename)
        #     print("the full name of the file is:" + os.path.join(parent, filename))
# getAllFile('/Users/jiaxiaopeng/demo')

with open(file='explore.txt',mode='a+',encoding = 'utf-8') as file:
    pass

import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "王伟",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
dumps = json.dumps(data, indent=2,ensure_ascii=False)
print(dumps)
print(type(dumps))

import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])
    writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])

with open('data.csv', 'a') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10004', 'name': 'Durant', 'age': 29})