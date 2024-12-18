# import sys
# sys.path.append("/Users/jiaxiaopeng/git/py3/base")
# import mymodule
import mydbutils1


# Call function
# mymodule.world()

config = {
    # "creator": "pymysql",
    "host": "127.0.0.1",
    "user": "root",
    "password": "123456",
    "database": "test",
    "port": 3306,
    "charset": 'utf8'
}
db_pool = mydbutils1.get_db_pool(True)
# 从数据库连接池是取出一个数据库连接
conn = db_pool.connection()
cursor = conn.cursor()
SQL = "select * from user_t"
r = cursor.execute(SQL)
r = cursor.fetchall()
for row in r:
    id = row[0]
    name = row[1]
    description = row[2]
    print(id, name, description)
conn.close()

mp3 = 'http://downdb.51voa.com/201903/as-web-turns-30-creator-calls-for-big-changes-to-make-it-better.mp3';
find = mp3.rfind('/')
print(mp3[find+1:])

import threading
threading.start_new
