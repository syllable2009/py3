from model import get_session, Test
from sqlmodel import Field, Session, SQLModel, create_engine, select,text


class TestService:

    def get_all(self):
        with get_session() as s:
            return s.exec(select(Test)).all()

    def get_by_id(self, id: int):
        with get_session() as s:
            return s.get(Test, id)

    def get_by_uid(self, uid: str):
        with get_session() as s:
            sql = text("SELECT * FROM test WHERE uid = :uid limit 1")
            param = {"uid": uid}
            result = s.execute(sql, param)
            # 自定义返回的sqlalchemy.engine.row.Row或者list[Row]需要自己遍历fetchall()
            return result.fetchone()

    def get_by_name(self, name: str):
        with get_session() as s:
            statement = select(Test).where(Test.uid == name).limit(1)
            return s.exec(statement).one()

    def add_one(self, test: Test):
        with get_session() as s:
            s.add(test)
            s.commit()
            return True

    def add_all(self, data: list[Test]):
        with get_session() as s:
            s.add_all(data)
            s.commit()
            return True

    def update_one(self, id: int, uid: str):
        # 更新 SQLModel 对象就像更新其他 Python 对象一样。🐍
        # 只需记住将它们 add 到 会话 中，然后 commit 它。如果需要，请 refresh 它们。
        with get_session() as s:
            db = s.get(Test, id)
            print("query:{}".format(db.uid))
            db.uid = uid
            print("==:{}".format(db.uid))
            s.add(db)
            print("add:{}".format(db.uid))
            s.commit()
            print("commit:{}".format(db.uid))
            s.refresh(db)
            print("refresh:{}".format(db.uid))
            return True

    def delete_by_aid(self, aid: int):
        with get_session() as s:
            # test = Test(aid=aid) 一定要是会话中查询的对象
            test = s.get(Test, aid)
            s.delete(test)
            s.commit()
            print("delete:{}".format(test))
            return True
