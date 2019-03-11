#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from peewee import Model # peewee提供的基础类，一个Model就对应一个数据库
from peewee import MySQLDatabase # peewee支持常见的SqliteDatabase,MySQL、PostgreSQL等等多种数据库
from peewee import BooleanField    # 几种常见的数据类型，还有PrimaryField自己可以看看用法

from peewee import CharField
from peewee import FloatField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import TextField
from peewee import *
import datetime
import peewee

# 指定database的路径为同该.py文件目录下的test.db数据库
# 而且便于后边其他脚本的导入（主要是为了db.atomic()的使用）
# dbpath = os.path.join(
#     os.path.dirname(os.path.abspath(__file__)),
#     'test.db'
# )

db = MySQLDatabase("test", host="127.0.0.1", port=3306, user="root", passwd="123456")
# db.({'primary_key': 'BIGINT AUTOINCREMENT'})
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    id = IntegerField(20,primary_key=True) # peewee默认已经为我们加上这个id
    user = CharField(unique=False,max_length=50,null=False)
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

if __name__ == "__main__":
    # Tweet.create_table()  # 创建Tweet表
    Tweet.create(user='NO1927', message='this is word')
    Tweet.insert_many(('')).execute()