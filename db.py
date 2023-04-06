import sqlite3
import os


from dataclasses import dataclass


@dataclass
class M3u8Data(object):
    id: int
    title: str
    url: str


class DB():

    def __init__(self, db_name):
        self.conn = sqlite3.connect(f'data/{db_name}')
        self.init_db(self.conn)

    def init_db(self, conn):
        try:
            cursor = conn.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS m3u8_data
                            (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title VARCHAR,
                                url VARCHAR
                            );""")
        except Exception as e:
            raise
        finally:
            cursor.close()

    def insert(self, data: M3u8Data):
        try:
            cursor = self.conn.cursor()
            sql = "insert into m3u8_data (`title`,`url`) values (?,?)"
            cursor.execute(sql, (data.title, data.url))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
        finally:
            cursor.close()


if __name__ == "__main__":
    db = DB("demo.sqlite")
    db.insert(M3u8Data(0, "demo", "demo"))
