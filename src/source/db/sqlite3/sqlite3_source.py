import sqlite3

from source.db.db_source import DBSource


class Sqlite3Source(DBSource):

    def __init__(self, database: str, **kwargs):
        super().__init__(database=database, **kwargs)

    def create_conn(self):
        return sqlite3.connect(database=self.database, **self.options)
