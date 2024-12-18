# encoding: utf-8
#!/usr/bin/python

import pymysql

# 打开数据库连接


# 打开数据库连接
conn = pymysql.connect(host="localhost", user="root",
                     password="123456", db="test", port=3306)

print(conn)
# 使用cursor()方法获取操作游标
cur = conn.cursor()

sql = "select * from user_t"
try:
    cur.execute(sql)  # 执行sql语句

    results = cur.fetchall()  # 获取查询的所有记录
    print("id", "name", "description")
    # 遍历结果
    for row in results:
        id = row[0]
        name = row[1]
        description = row[2]
        print(id, name, description)
except Exception as e:
    raise e
finally:
    conn.close()



