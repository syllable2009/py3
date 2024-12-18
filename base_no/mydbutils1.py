#
from DBUtils.PooledDB import PooledDB, SharedDBConnection
from DBUtils.PersistentDB import PersistentDB, PersistentDBError, NotSupportedError
import json
import pymysql

config = {
        'host': 'localhost',
        'port': 3306,
        'database': 'test',
        'user': 'root',
        'password': '123456',
        'charset': 'utf8mb4'
    }

def get_db_pool(is_mult_thread):
    if is_mult_thread:
        #这个用于多线程的
        poolDB = PooledDB(
            # 指定数据库连接驱动
            creator=pymysql,
            # 连接池允许的最大连接数,0和None表示没有限制
            maxconnections=3,
            # 初始化时,连接池至少创建的空闲连接,0表示不创建
            mincached=2,
            # 连接池中空闲的最多连接数,0和None表示没有限制
            maxcached=5,
            # 连接池中最多共享的连接数量,0和None表示全部共享(其实没什么卵用)
            maxshared=3,
            # 连接池中如果没有可用共享连接后,是否阻塞等待,True表示等等,
            # False表示不等待然后报错
            blocking=True,
            # 开始会话前执行的命令列表
            setsession=[],
            # ping Mysql服务器检查服务是否可用
            ping=0,
            **config
        )
    else:
        #PersistentDB这个用于单线程,如果你的程序只是在单个线程上进行频繁的数据库连接,最好使这个
        poolDB = PersistentDB(
            # 指定数据库连接驱动
            creator=pymysql,
            # 一个连接最大复用次数,0或者None表示没有限制,默认为0
            maxusage=None,
            **config
        )
    return poolDB


if __name__ == '__main__':
    db_pool = get_db_pool(True)
    # 从数据库连接池是取出一个数据库连接
    conn = db_pool.connection()
    cursor = conn.cursor()
    sql = 'select * from user_t'
    sql = '''select * from user_t \
      where id > %s ''' % (2)

    # 来查下吧
    cursor.execute(sql)
    # 取一条查询结果
    # result = cursor.fetchone()
    # 获取所有记录列表
    try:
        result = cursor.fetchall()
        for row in result:
            fname = row[0]
            lname = row[1]
            des = row[2]
            # 打印结果
            print("fname=%s,lname=%s,des=%s" % \
                  (fname, lname, des))
        print(json.dumps(result, indent=None))
    except:
        db_pool.rollback()
    # 关闭连接,其实不是关闭,只是把该连接返还给数据库连接池
    conn.close()
