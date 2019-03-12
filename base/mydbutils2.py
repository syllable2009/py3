#-*- coding: UTF-8 -*-
import pymysql
from DBUtils.PooledDB import PooledDB
import json, os, sys, time, pymysql, pprint

def get_time():
     '获取时间'
     return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class DBUtils(object):
    '''
    简单的数据库操作类
    '''
    def __init__(self,creator=pymysql, host="localhost",port=3306, user=None, password="",
                      database=None, charset="utf8"):
        if host is None: raise Exception("Parameter [host] is None.")
        if port is None: raise Exception("Parameter [port] is None.")
        if user is None: raise Exception("Parameter [user] is None.")
        if password is None: raise Exception("Parameter [password] is None.")
        if database is None: raise Exception("Parameter [database] is None.")

        print(get_time(), "数据库开始初始化。")
        # 数据库连接配置
        self.__config = dict({
        "creator": creator, "charset": charset, "host": host, "port": port,
        "user": user, "password": password, "database": database})

        self.__database = self.__config["database"]  # 用于存储查询数据库
        self.__tableName = None  # 用于临时存储当前查询表名

        # 初始化
        self.__init_connect()  # 初始化连接
        self.__init_params()  # 初始化参数
        print(get_time(), self.__database, "数据库初始化成功。")
        pass

    def __init_connect(self):
        self.__pool = PooledDB(**self.__config)
        self.conn = self.__pool.connection()

    def __init_params(self):
        '初始化参数'
        # self.__init_table_dict()
        # self.__init__table_column_dict_list()

if __name__ == "__main__":

     config = {
         # "creator": "pymysql",
         "host" : "127.0.0.1",
         "user" : "root",
         "password" : "123456",
         "database" : "test",
         "port" : 3306,
         "charset" : 'utf8'
     }
     DB = DBUtils(**config)

     cur = DB.conn.cursor()
     SQL = "select * from user_t"
     r = cur.execute(SQL)
     r = cur.fetchall()
     for row in r:
         id = row[0]
         name = row[1]
         description = row[2]
         print(id, name, description)
     cur.close()




