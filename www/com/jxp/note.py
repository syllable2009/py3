#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a module note'

__author__ = 'jiaxiaopeng'

from distutils.core import setup


import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('欢迎来到note项目!'+args[0])
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()