#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a hello module'
__author__ = 'jxp'
__doc__='study and test'
# import mysql.connector
from www.com.jxp.note import test
#name = input('input your name:')
#print('welcome:',name)
n1=10

print(n1/3)
print(r'''hello,\n world''')

a = 'ABC'
b = a
a = 'XYZ'
print(b)

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

import sys
args = sys.argv
print(args)

test()
# 把所有的值放在内存中，它是实时地生成数据
mygenerator = [x*x for x in range(3)]
print(mygenerator)
# 返回的是个生成器,使用for进行迭代的时候才去执行
mygenerator = (x*x for x in range(3))
print(mygenerator)

import itertools


