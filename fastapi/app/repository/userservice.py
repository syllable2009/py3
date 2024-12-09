from models import User, new_session, engine
from sqlalchemy import delete, select, update, text
from sqlalchemy.orm import DeclarativeBase, relationship, Session, Mapped, mapped_column


class UserService:
    # SELECT * FROM users
    def select_all(self):
        with new_session() as s:
            stmt = select(User)
            execute = s.execute(stmt)
            return execute.all()

    # SELECT * FROM users WHERE name='nick'
    def select_by_name(name: str):
        with new_session() as s:
            stmt = select(User).filter(User.name == name)
            return s.execute(stmt).first()

    # 查询用户信息的函数
    def select_user_by_id(user_id):
        with new_session() as s:
            # 查询用户
            return s.get(User, user_id)

    # 创建用户添加对象直接使用 session.add 方法
    # session.add(user)
    # session.add_all([user1, user2, group1])
    def create_user(name):
        with new_session() as session:
            new_user = User(name=name, fullname='test')
            new_user.description = ''
            add = session.add(new_user)
            session.commit()
            print("add:{},result:{}".format(new_user, add))

    # 更新用户
    def update_user(user_id, name=None):
        with new_session() as session:
            stmt = update(User).where(User.id == user_id).values(name=name).execution_options(
                synchronize_session="fetch")
            execute = session.execute(stmt)
            session.commit()
            print("update:{}".format(execute))

    # 删除用户
    def delete_user(user_id):
        with new_session() as session:
            # user = session.get(User, user_id)
            # session.delete(user)
            stmt = delete(User).where(User.id == user_id)
            execute = session.execute(stmt)
            session.commit()


# Core 层 -- 直接使用 SQL
def origin_sql():
    with engine.connect() as conn:
        result = conn.execute(text("select * from users"))
        print("select * 查询结果：{}".format(result.all()))
        result = conn.execute(text("select * from users"))
        # result 可以遍历，每一个行结果是一个 Row 对象
        for row in result:
            # row 对象三种访问方式都支持
            print(row.id, row.name)
            print(row[0], row[1])
        # where条件查询与传值
        result = conn.execute(
            text("SELECT id, name FROM users WHERE id = :y"),
            {"y": 3}
        )
        print("where id= 查询结果：{}".format(result.all()))
        # 也可以预先编译好参数
        stmt = text("SELECT id, name FROM users WHERE id = :y ORDER BY id desc").bindparams(y=6)
        # 插入时，可以直接插入多条
        # conn.execute(text("INSERT INTO users (id, name) VALUES (:x, :y)"),
        #              [{"x": 11, "y": 12}, {"x": 13, "y": 14}])

# 事务与 commit
def transaction_commit():
    # 半自动 autocommit不建议使用
    # 半自动 commit
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    # 手工 commit
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
        )
        conn.commit()  # 注意这里的 commit

def orm_mapping():
    foo = User(name='jxp', email='123@test.qq.com')
    with Session(engine) as session:
        session.add(foo)
        session.commit()

def orm_mapping2():
    with new_session() as session:
        pass

if __name__ == "__main__":
    pass
    # stmt = select(User).where(User.name == "john").order_by(User.id)
    # result = new_session().execute(stmt)
    # print(result.all())
    # print(select_by_name('jxp'))
    # print(select_user_by_id(1))
    # create_user('lisi')
    # delete_user(7)
    # update_user(4,'李四')