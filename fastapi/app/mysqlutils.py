import mysql.connector
from mysql.connector import Error
from typing import List, Dict, Any, Optional

class MySQLClient:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """连接到 MySQL 数据库"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Successfully connected to the database")
        except Error as e:
            print(f"Error: {e}")
            self.connection = None

    def close(self):
        """关闭数据库连接"""
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query: str, params: Optional[tuple] = None):
        """执行 DML 语句（INSERT, UPDATE, DELETE）"""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error: {e}")
            return 0
        finally:
            cursor.close()

    def fetch_all(self, query: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
        """执行 SELECT 查询并返回所有结果"""
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()

    def fetch_one(self, query: str, params: Optional[tuple] = None) -> Optional[Dict[str, Any]]:
        """执行 SELECT 查询并返回单个结果"""
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            return cursor.fetchone()
        except Error as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()

# 使用示例
def main():
    # 创建 MySQL 客户端实例
    db_client = MySQLClient("localhost", "your_username", "your_password", "your_database")

    # 连接到数据库
    db_client.connect()

    # 创建表（示例）
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL
    )
    """
    db_client.execute_query(create_table_query)

    # 插入数据
    insert_query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    db_client.execute_query(insert_query, ("Alice", 30))
    db_client.execute_query(insert_query, ("Bob", 25))

    # 查询数据
    select_query = "SELECT * FROM users"
    users = db_client.fetch_all(select_query)
    print("Users:", users)

    # 查询单个用户
    select_one_query = "SELECT * FROM users WHERE name = %s"
    user = db_client.fetch_one(select_one_query, ("Alice",))
    print("User:", user)

    # 更新数据
    update_query = "UPDATE users SET age = %s WHERE name = %s"
    db_client.execute_query(update_query, (31, "Alice"))

    # 删除数据
    delete_query = "DELETE FROM users WHERE name = %s"
    db_client.execute_query(delete_query, ("Bob",))

    # 关闭数据库连接
    db_client.close()

if __name__ == "__main__":
    main()
