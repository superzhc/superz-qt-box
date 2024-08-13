import pymysql

from source.db.db_source import DBSource

DEFAULT_PORT = 3306
DEFAULT_USER = "root"


class MysqlSource(DBSource):

    def __init__(self,
                 *,
                 port: int = DEFAULT_PORT,
                 username: str = DEFAULT_USER,
                 **kwargs,
                 ):
        super().__init__(port=port, username=username, **kwargs)

    def create_conn(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            database=self.database,
            charset=self.options.get("charset") if "charset" in self.options else "utf8",
            **self.options
        )


if __name__ == "__main__":
    source = MysqlSource(host="localhost", password="123456", database="employees")
    conn = source.get_connect()
    with conn.cursor() as cursor:
        cursor.execute("select * from dept_manager")
        print(cursor.fetchall())

    conn.close()
