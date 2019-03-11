import codecs
import os

a,b=0,1 #复合赋值
print(a,b,end="\t\n")
a,b=b,a #复合赋值
print(a,b,end="\t\n")

a = {'1','he','ok'}
a.add('ok')
print(a)

c = set(['i'])
c.add('i')
print(c)
print(os.path)

# with codecs.open('/Users/jiaxiaopeng/1.txt', 'w',encoding='utf-8') as f:
#     # for line in f.readlines():
#     f.write("胜利的方法")

path = '/Users/jiaxiaopeng/1.txt'

print(os.path.basename(path))    # 查询路径中包含的文件名
print(os.path.dirname(path))     # 查询路径中包含的目录

info = os.path.split(path)       # 将路径分割成文件名和目录两个部分，放在一个表中返回
path2 = os.path.join('/', 'home', 'vamei', 'doc', 'file1.txt')  # 使用目录名和文件名构成一个路径字符串

p_list = [path, path2]
print(os.path.commonprefix(p_list))

print(os.path.abspath('./'))

def getAllFile(path):
    for parent, dirnames, filenames in os.walk(path): #os.walk返回是一个三元组
        for filename in filenames:
            print("parent is" + parent)
            print("filename is:" + filename)
            print("the full name of the file is:" + os.path.join(parent, filename))
getAllFile('/Users/jiaxiaopeng/demo')