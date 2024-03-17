from data_base.data_base import DataBase
from aiogram.types import Message


class ResultTest(DataBase):

    def __init__(self, data):
        if isinstance(data, Message):
            self.tg_id = data.from_user.id
            self.task_1 = False
            self.task_2 = False
            self.task_3 = False
            self.task_4 = False
            self.task_5 = False
            self.task_6 = False
            self.task_7 = False
            self.task_8 = False
            self.task_9 = False
            self.task_10 = False
            self.total = 0
            self.create()
        if isinstance(data, int):
            self.tg_id = data
        ressult_test = self.load(tg_id=self.tg_id)
        self.tg_id, self.task_1, self.task_2, self.task_3, self.task_4, self.task_5, \
            self.task_6, self.task_7, self.task_8, self.task_9, self.task_10, self.total = ressult_test

    @staticmethod
    def great_table():
        sql = '''CREATE TABLE IF NOT EXISTS result_test
                 (tg_id INTEGER, task_1 INTEGER, task_2 INTEGER,
                  task_3 INTEGER, task_4 INTEGER,
                  task_5 INTEGER, task_6 INTEGER,
                  task_7 INTEGER, task_8 INTEGER,
                  task_9 INTEGER, task_10 INTEGER, total INTEGER)'''
        ResultTest.execute(sql, commit=True)

    def load(self, **kwargs):
        sql = """SELECT * FROM result_test WHERE """
        sql, parameters = self.extract_kwargs(sql, kwargs)
        result_test = self.execute(sql, parameters, fetchone=True)
        return result_test

    def save(self):
        sql = """UPDATE result_test SET """
        sql, parameters = self.extract_kwargs(sql, self.__dict__, _and=False)
        sql = sql + f" WHERE tg_id={self.tg_id}"
        self.execute(sql, parameters, commit=True)

    def create(self):
        sql = """SELECT * FROM result_test WHERE tg_id=?"""
        data = self.execute(sql, (self.tg_id,), fetchone=True)
        if data:
            print("Такой пользователь уже есть ) ")
        else:
            sql = """INSERT INTO result_test(tg_id,task_1,task_2,task_3 , task_4,
                    task_5, task_6,task_7,task_8,task_9,task_10)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?)"""
            self.execute(sql, (self.tg_id, self.task_1, self.task_2,
                               self.task_3, self.task_4, self.task_5,
                               self.task_6, self.task_7, self.task_8
                               , self.task_9, self.task_10), commit=True)
