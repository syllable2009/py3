import pymysql
import random

# 操作数据库
def operateDB():
    # 加载驱动
    # 获取一个MySQL连接对象
    conn = pymysql.connect(host='localhost',user='root', password='123456', port=3306)
    # cursor方法获得MySQL的操作游标
    cursor = conn.cursor()
    # 用execute()方法执行即可
    cursor.execute('SELECT VERSION()')
    # 获取执行结果
    data = cursor.fetchone()
    print('Database version:', data)
    # cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4")
    # 关闭链接
    conn.close()

id = random.randint(1,2147483647)
name = random.sample('zyxwvutsrqponmlkjihgfedcba0123456789',5)
name = ''.join(str(x) for x in name)
age = random.randint(0,99)

# 操作数据表，id可以不传
def operateTable():
    conn = pymysql.connect(host='localhost',db='spiders', user='root', password='123456', port=3306)
    cursor = conn.cursor()
    # sql = 'CREATE TABLE IF NOT EXISTS students (id bigint(20) auto_increment, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
    sql = 'INSERT INTO students(id,name, age) values(%s,%s, %s)'
    try:
        cursor.execute(sql, (id,name, age))
        conn.commit()
        print('Successful')
    except:
        conn.rollback()
        conn.rollback()
    conn.close()


data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 20
}

# 优化改造
def remake():
    table = 'students'
    keys = keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    print(sql)
    print(tuple(data.values()))
    # cursor.execute(sql, tuple(data.values()))

def updateOrInsert():
    table = 'students'
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
    update = ','.join([" {key} = %s".format(key=key) for key in data])
    sql += update
    print(sql)
    # cursor.execute(sql, tuple(data.values())*2)

def query():
    conn = pymysql.connect(host='localhost',user='root',db='spiders', password='123456', port=3306)
    sql = 'SELECT * FROM students WHERE age >= 20'
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        print('Count:', cursor.rowcount)
        row = cursor.fetchone()
        # print('One:', row)
        while row:
            print('Row:', row)
            row = cursor.fetchone()
        # fetchallfetchall()会将结果以元组形式全部返回，如果数据量很大，那么占用的开销会非常高,不建议使用此方法
        # results = cursor.fetchall()
        # print('Results:', results)
        # print('Results Type:', type(results))
        # for row in results:
        #     print(row)
    except:
        print('Error')
    conn.close

def delete():
    table = 'students'
    condition = 'age > 20'
    sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
    print(sql)

if __name__ == '__main__':
    updateOrInsert()