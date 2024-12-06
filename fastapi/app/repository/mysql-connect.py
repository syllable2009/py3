import mysql.connector
from mysql.connector import errorcode


class Database:
    def __init__(self, host, user, password, database):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            print("Database connection successful")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def execute_query(self, query, data=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, data)
            self.connection.commit()
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

    def fetch_all(self, query, data=None):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, data)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")


# 示例使用
if __name__ == "__main__":
    db = Database(host="localhost", user="jiaxiaopeng", password="admin1234", database="my3")

    # 创建表
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE
    )
    """
    query = db.execute_query(create_table_query)
    print("create table result:{}".format(query))

    # 插入数据
    insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    user_data = ("John Doe", "john@example.com")
    db.execute_query(insert_query, user_data)

    # 查询数据
    select_query = "SELECT * FROM users"
    users = db.fetch_all(select_query)
    print(users)

    db.close()
