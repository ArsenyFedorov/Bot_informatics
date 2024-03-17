from data_base.data_base import DataBase


class User(DataBase):

    def __init__(self, data):
        if isinstance(data, dict):
            self.tg_id = data["tg_id"]
            self.surname = data["surname"]
            self.name = data["name"]
            self.class_number = data["class_number"]
            self.points = 0
            self.create()
        if isinstance(data, int):
            self.tg_id = data
        user = self.load(tg_id=self.tg_id)
        self.tg_id, self.surname, self.name, self.class_number, self.points = user

    @staticmethod
    def great_table():
        sql = '''CREATE TABLE IF NOT EXISTS users
                 (tg_id INTEGER, surname TEXT, name TEXT,
                  class_number TEXT, points INTEGER)'''
        User.execute(sql, commit=True)

    def load(self, **kwargs):
        sql = """SELECT * FROM users WHERE """
        sql, parameters = self.extract_kwargs(sql, kwargs)
        user = self.execute(sql, parameters, fetchone=True)
        if user is None:
            return [1, 0, 2, 3, 4]
        else:
            return user

    def save(self):
        sql = """UPDATE users SET """
        sql, parameters = self.extract_kwargs(sql, self.__dict__, _and=False)
        sql = sql + f" WHERE tg_id={self.tg_id}"
        self.execute(sql, parameters, commit=True)

    def create(self):
        sql = """SELECT * FROM users WHERE tg_id=?"""
        data = self.execute(sql, (self.tg_id,), fetchone=True)
        if data:
            print("Такой пользователь уже есть ) ")
        else:
            sql = """INSERT INTO users(tg_id,surname,name,class_number,points) VALUES (?,?,?,?,?)"""
            self.execute(sql, (self.tg_id, self.surname, self.name,
                               self.class_number, self.points), commit=True)
